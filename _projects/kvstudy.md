---
title: KVStudy
order: 2
group: Inference and serving
kind: Inference study
repo: harsha-moparthy/kvstudy
description: >-
  A controlled study of KV-cache compression — quantization down to 2 bits, four eviction
  policies, and their combinations — establishing 4x memory reduction at no measured quality
  loss, and showing which metric detects the damage the others miss.
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

The inverse effect appears with quantization, where perplexity *overstates* the damage:

| configuration | perplexity | task accuracy |
|---|---|---|
| `fp32 + full` | 27.757 | 100% |
| `int4 + full` | **1767** (64x worse) | **89%** |

A metric that reports 64x degradation for an 11-point accuracy drop, and no degradation at all for
a 67-point drop, is not measuring what matters. That is the argument for the task suite, and it is
the most transferable result in the project.

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

The measurement path is built to be trustworthy on its own terms: quantization is applied *inside*
the forward pass (on write, after RoPE, exactly where a real engine puts it) so every arm shares one
code path, and peak *resident* occupancy is tracked separately from tokens ever written so the memory
column reflects what is actually held at once. A 25-test suite backs the harness.

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
the memory. This is the clear recommendation for any workload, and it is the study's headline
practical result.

**int8 is more accurate than fp8, and the study prices both correctly.** int8's relative error is
roughly half fp8's (0.0124 vs 0.0222), because per-(token, head) asymmetric scaling fits the actual
distribution better than fp8's fixed exponent split. It carries an fp16 scale and zero point per
group, so at head_dim 64 its true cost is **8.5 bits/value, not 8** — quoting int8 as "8-bit"
overstates the saving by 6%, which is why the table reports the loaded figure.

**int4 is workload-dependent, int2 is past the useful range.** int4 keeps 89% accuracy at 0.14x
memory. int2 drops to 11%, and its measured key relative error of 1.093 is above 1.0 — the
reconstruction error exceeds the magnitude of the signal it is meant to represent.

**Eviction at 50% is expensive on recall tasks across every policy tested.** Sliding window,
attention sink, heavy hitter, and *random* all land in a 22–33% band. The useful structure is not a
ranking between them but *which* task families each one preserves.

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

The complementary result is that the policies trade against *different* task families rather than one
dominating: the heavy-hitter variant preserves instruction-following (100%) and multi-turn (67%),
which the window policies do not, while the window policies preserve late-context needle recall. For
a serving decision that matters more than an aggregate score, because it says which policy to pick
from the shape of the workload.

**Quantization stacks cleanly onto eviction for memory.** `int8 + attention_sink` reaches **0.13x
memory** at the same 33% accuracy as eviction alone — the compression techniques compose on the
memory axis even though neither repairs the other's quality cost. That is the combination result
worth taking to a real system.

## Recommendations

| workload | recommendation |
|---|---|
| anything | **fp8 or int8, full cache.** 4x memory reduction, no measured quality loss. |
| memory-critical, short-range dependencies | int4 full cache (0.14x), accepting ~11% task loss. |
| long-context recall (RAG, long chat) | **do not evict at 50%.** Every policy tested loses two thirds of task accuracy. |
| streaming with no recall requirement | attention sink, combined with int8 for 0.13x memory. |
| validation | score cache compression on recall tasks, not perplexity alone. |

## Scope and next steps

Results are measured on one small model (Qwen2.5-0.5B, 2 KV heads with heavy GQA, 24 layers) over a
9-task suite, so the natural extensions are a 7B+ model, a larger suite for finer resolution between
policies, and a layer-aware importance score for the heavy-hitter policy. fp8 is emulated by mantissa
rounding because Apple silicon has no fp8 type: it reproduces fp8's error characteristics faithfully,
which is what the quality claim rests on, and no throughput claim is attached to it. Quantization here
reconstructs to fp32 rather than computing in low precision, so the gains reported are memory gains —
low-precision compute is the next measurement, not a claim made here.
