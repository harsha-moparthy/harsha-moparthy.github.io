---
title: KVStudy
order: 2
group: Inference and serving
kind: Inference study
repo: harsha-moparthy/kvstudy
description: >-
  A controlled study of KV-cache compression — quantization down to 2 bits, four eviction
  policies, and their combinations — measured on tasks where degradation is actually
  detectable, with the metric that fails to detect it reported alongside.
stack: [Python, PyTorch, Qwen2.5-0.5B, Apple M4 Pro]
highlights:
  - value: "0.25x"
    label: KV memory at no measured quality loss
  - value: "identical"
    label: perplexity while accuracy fell 67 points
  - value: "14"
    label: configurations in the matrix
  - value: "25"
    label: tests
---

## Why this project exists

The KV cache is the model's working memory during generation, and in long-context serving it is
the dominant cost: unlike weights, it grows linearly with every token of every concurrent request.
The three main levers for shrinking it — lower precision, evicting stale tokens, sharing common
prefixes — each trade quality for memory differently.

This needed to be a *study* rather than a benchmark because the failure modes are not symmetric:

- **Quantization** degrades every token slightly, and the error compounds — a perturbed key changes
  an attention score, which reweights every value, layer after layer and step after step.
- **Eviction** removes some tokens completely. If the model needed one later, no precision elsewhere
  recovers it.
- **The interactions are not additive**, so measuring each alone and adding the deltas gives the
  wrong answer.

## The headline finding: perplexity measures the wrong thing

Most cache-compression results are reported as perplexity. On this suite, perplexity **completely
fails to detect eviction damage**:

| configuration | perplexity | task accuracy |
|---|---|---|
| `fp32 + full` (control) | 27.757 | **100%** |
| `fp32 + sliding_window@50%` | **27.757** (identical) | **22%** |
| `fp32 + attention_sink@50%` | **27.757** (identical) | **33%** |

Perplexity does not move *at all* while task accuracy collapses by two thirds. The reason is
structural: perplexity is a single forward pass over a passage, so there is no decode loop for
eviction to act on, and it averages over every position, so losing one load-bearing token barely
registers even when it does apply.

The inverse failure appears with quantization, where perplexity *overstates* the damage:

| configuration | perplexity | task accuracy |
|---|---|---|
| `fp32 + full` | 27.757 | 100% |
| `int4 + full` | **1767** (64x worse) | **89%** |

A metric that reports 64x degradation for an 11-point accuracy drop, and no degradation at all for
a 67-point drop, is not measuring what matters. That is the argument for the task suite.

## Evaluation design

Four task families, all scored programmatically against a known answer, each built so a specific
token becomes load-bearing for a later prediction:

- **needle-in-haystack** at four depths (5%, 35%, 65%, 95%) — an access code buried in filler. The
  depth sweep is what turns "eviction hurts" into "eviction hurts *here*".
- **multi-turn consistency** — a constraint set in turn 1 that must survive six turns of chatter.
- **instruction following** — a system-prompt instruction at position zero, which is exactly what a
  sliding window discards first.
- **summarisation recall** — a distinctive early detail a faithful answer must retain.

Decoding is greedy with no penalties in every arm, so differences are attributable to the cache and
nothing else. `fp32 + full` is the control, verified by a test to reproduce plain unmanaged
generation exactly.

## Measured results

Apple M4 Pro (CPU, float32), `Qwen/Qwen2.5-0.5B-Instruct`, 9 tasks, eviction budget 50% of full
context.

| configuration | task accuracy | Δ vs control | KV memory | mem vs control |
|---|---|---|---|---|
| `fp32 + full` | 9/9 (100%) | — | 7416 KiB | 1.00x |
| `fp16 + full` | 9/9 (100%) | 0 | 3708 KiB | 0.50x |
| `fp8 + full` | 9/9 (100%) | 0 | 1854 KiB | **0.25x** |
| `int8 + full` | 9/9 (100%) | 0 | 1970 KiB | 0.27x |
| `int4 + full` | 8/9 (89%) | −11% | 1043 KiB | 0.14x |
| `int2 + full` | 1/9 (11%) | −89% | 579 KiB | 0.08x |
| `fp32 + sliding_window@50%` | 2/9 (22%) | −78% | 3720 KiB | 0.50x |
| `fp32 + attention_sink@50%` | 3/9 (33%) | −67% | 3720 KiB | 0.50x |
| `fp32 + heavy_hitter@50%` | 3/9 (33%) | −67% | 3720 KiB | 0.50x |
| `fp32 + random@50%` | 3/9 (33%) | −67% | 3720 KiB | 0.50x |
| `int8 + attention_sink@50%` | 3/9 (33%) | −67% | 988 KiB | **0.13x** |
| `int4 + heavy_hitter@50%` | 4/9 (44%) | −56% | 523 KiB | 0.07x |

### Quantizer reconstruction error, measured on real KV activations

| quantizer | bits/value | key relative error | value relative error |
|---|---|---|---|
| fp16 | 16.0 | 0.00018 | 0.00018 |
| fp8 (E4M3 sim) | 8.0 | 0.0222 | 0.0225 |
| int8 | **8.5** | **0.0124** | **0.0068** |
| int4 | 4.5 | 0.209 | 0.115 |
| int2 | 2.5 | 1.093 | 0.578 |

## What the numbers say

**Quantization to 8 bits is close to free.** fp8 and int8 hold 100% task accuracy at a quarter of
the memory. This is the clear recommendation for any workload.

**int8 is more accurate than fp8 but uses *more* memory.** Its relative error is roughly half fp8's
(0.0124 vs 0.0222), because per-(token, head) asymmetric scaling fits the actual distribution better
than fp8's fixed exponent split. But it carries an fp16 scale and zero point per group, so at
head_dim 64 its true cost is **8.5 bits/value, not 8**. Quoting int8 as "8-bit" overstates the
saving by 6%, which is why the table reports the loaded figure.

**int4 is workload-dependent, int2 is unusable.** int4 keeps 89% accuracy at 0.14x memory. int2
collapses to 11%, with a key relative error above 1.0 — meaning the reconstruction is on average
wronger than the signal.

**Eviction at 50% is catastrophic on recall tasks, and no policy escapes it.** Sliding window,
attention sink, heavy hitter, and *random* all land within one task of each other (22–33%). With 9
tasks one task is 11 points, so **none of these differences is significant** — the honest conclusion
is that at this budget the policies are indistinguishable, not that one wins.

### The needle depth sweep shows exactly where eviction fails

This is the finding aggregate accuracy hides:

| configuration | d=5% | d=35% | d=65% | d=95% |
|---|---|---|---|---|
| `fp32 + full` | pass | pass | pass | pass |
| `int4 + full` | pass | pass | pass | pass |
| `int2 + full` | fail | fail | fail | fail |
| `sliding_window@50%` | **fail** | **fail** | pass | pass |
| `attention_sink@50%` | **fail** | **fail** | pass | pass |
| `heavy_hitter@50%` | fail | fail | **fail** | **fail** |
| `random@50%` | fail | fail | fail | fail |

Window-based policies fail precisely when the fact is early and pass when it is late — the predicted
asymmetry, and a clean demonstration that "50% of the cache" is not 50% of the information.

**My heavy-hitter implementation is no better than random, and worse than a sliding window on
recall.** It fails the needle at *every* depth while keeping instruction-following (100%) and
multi-turn (67%) that the window policies destroy. Two honest readings: the policies fail on
*different* task families rather than one dominating, and my H2O variant is likely mis-specified — it
averages attention across all 24 layers into one importance score, which plausibly washes out the
layer-specific signal H2O relies on. I am reporting it as implemented rather than tuning it until it
wins.

**Combining techniques is not additive, and the one apparent synergy is noise.**
`int4 + heavy_hitter` scores 44% versus 33% for `fp32 + heavy_hitter` — quantizing *more* appearing
to help. That is a one-task difference on a 9-task suite, i.e. within resolution. The defensible
combination result is the memory one: `int8 + attention_sink` reaches **0.13x memory** at the same
33% accuracy as eviction alone, so quantization stacks cleanly onto eviction for memory even though
neither repairs the other's quality loss.

## Recommendations

| workload | recommendation |
|---|---|
| anything | **fp8 or int8, full cache.** 4x memory reduction, no measured quality loss. |
| memory-critical, short-range dependencies | int4 full cache (0.14x), accepting ~11% task loss. |
| long-context recall (RAG, long chat) | **do not evict at 50%.** Every policy tested loses two thirds of task accuracy. |
| streaming with no recall requirement | attention sink, combined with int8 for 0.13x memory. |
| never | int2, or any eviction validated only by perplexity. |

## Measurement bugs found and fixed

Both of the first two produced plausible-looking numbers, which is what makes them worth recording.

1. **Perplexity was measured on a single token for quantized arms.** The first run reported
   perplexity of ~58,000,000 for fp16 against 27.8 for the control — an obviously broken number that
   would have invalidated every quality claim. A special-case branch scored only the final token when
   quantization was active. Quantization is now applied *inside* the forward pass (on write, after
   RoPE, exactly where a real engine puts it), so all arms share one code path.
2. **Eviction appeared to save no memory.** The first run showed 0.98x memory for policies discarding
   60% of the cache. Memory was computed from peak tokens *ever written* rather than peak tokens
   *resident*. Resident occupancy is now tracked separately, and eviction shows the expected 0.50x.
3. **Needle depths rendered as `d=500%`** — a cosmetic double-multiplication caught while reading the
   generated report.

## Known limits

- **9 tasks means 11-point resolution.** Differences of one or two tasks are noise and are labelled
  as such rather than ranked.
- **One small model.** Qwen2.5-0.5B has 2 KV heads (heavy GQA) and 24 layers; quantization tolerance
  and eviction sensitivity both plausibly differ at 7B+.
- **fp8 is emulated.** Apple silicon has no fp8 type, so E4M3 is simulated by mantissa rounding. It
  reproduces fp8's error characteristics, but no throughput claim is attached to it.
- **Latency is flat across arms and therefore uninformative.** Quantization here reconstructs to
  fp32 rather than computing in low precision, so it saves memory, not time.
- **Perplexity does not exercise eviction at all**, by construction. It is included as the negative
  control, not as a quality metric.
