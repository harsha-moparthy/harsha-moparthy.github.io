---
title: PageServe
order: 1
group: Inference and serving
kind: Inference engine
repo: harsha-moparthy/pageserve
description: >-
  A mini LLM serving engine implementing continuous batching and a paged KV cache, verified
  token-for-token against Hugging Face at temperature 0 — with benchmarks that include the
  baseline it loses to.
stack: [Python, PyTorch, Qwen2, Apple M4 Pro]
highlights:
  - value: "3.07x"
    label: capacity gain from paging on heavy-tailed load
  - value: "3.14x"
    label: throughput vs sequential baseline
  - value: "exact"
    label: token-for-token match vs Hugging Face
  - value: "5"
    label: scheduler bugs found by benchmarks
---

## Why this project exists

Serving an LLM efficiently has almost nothing in common with running one in a notebook. Requests
arrive continuously, with different prompt lengths and different generation lengths, and the two
phases of inference have opposite bottlenecks: prefill processes many tokens at once and is
compute-bound, while decode processes one token per sequence and is memory-bound, dominated by
streaming weights and cache.

Two techniques fix this, and both are borrowed from operating systems:

**Continuous batching.** Static batching runs a fixed group of requests to completion, so every
request is billed for the slowest member of its batch and finished slots sit idle. Continuous
batching rebuilds the running set every decode step — finished sequences leave immediately, waiting
ones join the same step.

**Paged KV cache.** A naive engine reserves a contiguous `prompt + max_new_tokens` slab per sequence,
because it cannot know in advance how long the sequence will actually run. With realistic length
variance most of that reservation is never written, so concurrency is bounded by the *longest
possible* generation rather than the actual one. Paging allocates fixed-size blocks with a
per-sequence block table, exactly like virtual memory.

## What is actually implemented

- A hand-written Qwen2 forward pass (RMSNorm, GQA attention, RoPE, SwiGLU MLP) so the engine owns the
  KV path rather than delegating it to the framework.
- A **paged KV cache**: one flat block pool, per-sequence block tables, refcounted blocks for prefix
  sharing, and fragmentation accounting.
- A **continuous batching scheduler**: per-step admission with a prefill token budget, decode-headroom
  reservation, backpressure when the pool is full, and preemption with re-queue under memory pressure.
- A **batched decode step**: all running sequences advance in a single forward pass, with right-padded
  KV and masking.
- **Prefix sharing** for common system prompts, block-granular and copy-free.
- Benchmarks against sequential and static-batched Hugging Face baselines, plus a capacity study.

## Correctness comes first

A serving engine that is fast but not equivalent to the reference is not a speedup, it is a different
model. Every optimisation here is gated by exact-match tests at temperature 0:

- my forward pass vs HF logits (max abs diff ~2e-5, identical argmax),
- incremental paged decode vs full recompute,
- engine output vs HF `generate`, single and batched,
- output invariant to block size (1, 3, 7, 32) and to batch size (1, 2, 4),
- prefix sharing produces byte-identical results to not sharing,
- a short sequence batched with a long one is unaffected by its neighbour.

That last one matters more than it looks: a padding or masking bug lets one sequence attend to
another's slots and still produce fluent text. It would never be caught by reading output.

### The reference was wrong before my engine was

The first comparison showed my engine "diverging" from HF on one of three prompts. It wasn't.
Qwen2.5-Instruct ships `generation_config.json` with `repetition_penalty=1.1`, and Hugging Face
applies it even under `do_sample=False`. My engine does pure greedy argmax with no penalties, so the
two were running different decoding rules.

Finding this took proving that my forward pass agreed with HF's *forward* while disagreeing with HF's
*generate* — the gap between those two was the entire clue. The honest comparison pins
`repetition_penalty=1.0`, and all four prompts then match exactly.

## Measured results

Apple M4 Pro (CPU, float32), `Qwen/Qwen2.5-0.5B-Instruct`, 24 requests, generation budgets varying
from 2 to 32 tokens.

### Throughput and latency

| configuration | tok/s | speedup | TTFT p50 | TTFT p99 | latency p99 |
|---|---|---|---|---|---|
| sequential (HF) | 47.0 | 1.00x | 0.036 s | 0.069 s | 0.69 s |
| **static batch (HF)** | **323.8** | **6.89x** | 1.71 s | 1.71 s | 1.71 s |
| continuous+paged, max_running=4 | 72.8 | 1.55x | 3.37 s | 6.95 s | 7.59 s |
| continuous+paged, max_running=8 | 108.3 | 2.31x | 1.93 s | 4.14 s | 5.10 s |
| continuous+paged, max_running=16 | 147.3 | 3.14x | 0.59 s | 2.28 s | 3.75 s |
| continuous+paged, no prefix sharing, max_running=16 | 167.3 | 3.56x | 0.43 s | 1.86 s | 3.30 s |

Scheduler steps fall exactly as batch size rises (132 → 75 → 50 for max_running 4 → 8 → 16), and zero
preemptions occurred, which is what a correctly accounted scheduler should do.

### Capacity: paging versus contiguous reservation

Same slot budget for both allocators, offered load 20x the pool so both saturate.

| workload | naive contiguous | paged | gain |
|---|---|---|---|
| low variance (budget 32, mean actual 23) | 30 sequences | 36 sequences | **1.2x** |
| heavy tail (budget 256, mean actual 60) | 28 sequences | **86 sequences** | **3.07x** |

Internal waste with paging is 6.0–6.5%, and it is bounded by construction: at most one
partially-filled block per sequence, no matter how long the sequence could theoretically become.

The heavy-tailed row is the realistic one and the whole argument for paging. Most replies are short,
a few are long, and the budget must cover the longest — so a contiguous allocator reserves 286 slots
for a sequence that typically uses 90.

## What this engine does *not* beat, and why

**Hugging Face's static batching is 2.2x faster than my best configuration.** That row is in the table
above rather than omitted, because leaving it out would make this a demo instead of a measurement.

The reason is structural, not tuning. My paged gather materialises the whole padded KV context into a
fresh tensor every decode step. On CPU with a 0.5B model, that copy dominates the batching win.
Production engines avoid it with custom paged-attention kernels that read blocks *in place* — pure
PyTorch has no way to express that, so the gather is the price of paging here.

So the defensible claim is: the techniques are implemented, verified exact, and scale as designed. It
is not "faster than a production baseline". The honest place paging wins on this hardware is
**memory**, and the capacity study measures that at 3.07x.

Two more results worth stating plainly:

**Prefix sharing currently costs throughput.** 147.3 tok/s with it versus 167.3 without. It only
saves prefill work while adding block-table complexity to every gather, and prefill is not the
bottleneck at this scale. It does cut peak memory substantially (38 vs 55 blocks, a 31% reduction), so
it is a memory-for-speed trade, not a free win.

**Static batching has the best TTFT here, and that is an artifact.** Its p50 TTFT of 1.71 s equals its
total wall time, because every request in a static batch shares one completion instant — there is no
meaningful per-request first-token time. My engine's TTFT genuinely varies per request (0.59 s p50,
2.28 s p99 at max_running=16), which is the number an actual user would feel.

## Bugs found and fixed

Each was caught by a test or a benchmark rather than by inspection, and each is now pinned.

1. **Continuous batching without batching.** The first working version scheduled continuously but
   decoded in a Python loop, one `forward_sequence` call per request per step. Output was perfectly
   correct and throughput was flat at ~55 tok/s regardless of batch size — the headline technique was
   not actually implemented. Decode is memory-bound, so N separate passes stream the weights N times.
   Batching them into one pass is what produced the 1.55x → 3.14x scaling above.
2. **Prefix sharing on an identical prompt crashed.** When a later request's prompt was byte-identical
   to an earlier one, sharing covered the *entire* prompt, leaving zero new tokens to forward — and the
   engine needs a forward pass to produce logits. Sharing is now capped to leave at least one token to
   recompute.
3. **Admission double-counted free blocks.** The scheduler checked free blocks per request, but the
   pool is only drawn down later during prefill. Several requests were admitted in one step each
   believing the same blocks were available. Admission now tracks blocks committed within the step.
4. **Livelock on a prompt that exactly filled the pool.** Such a request was admitted, preempted on
   its first decode (no room to grow), re-queued at the front, and retried forever. Admission now
   requires headroom for the prompt *and* at least one generated token.
5. **The capacity study measured nothing.** It offered only as many sequences as trivially fit, so
   paging never got the chance to saturate memory, and it reported a "capacity gain" of 0.23x —
   implying paging was three times *worse*. It now offers 20x the pool and models per-sequence actual
   lengths, which is what turns the comparison into evidence.

## Known limits

- **CPU float32 only.** MPS is available on this machine but not used: the gather-heavy decode path is
  dominated by memory traffic, and I have not verified numerical parity on MPS.
- **No custom attention kernel**, so the paged gather cost is unavoidable in pure PyTorch. This is the
  single biggest gap versus a real engine.
- **Prefill is not batched across requests.** Batching prefill needs variable-length packing and is
  the obvious next step.
- **No streaming API or server.** The engine is a library plus CLI, so this measures the scheduler,
  not a service.
- **Greedy decoding only.** Temperature 0 is what makes token-for-token verification possible.
- **One model family.** The forward pass is hand-written for Qwen2.
