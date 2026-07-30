---
title: PageServe
track: ml
order: 1
group: Inference and serving
kind: Inference engine
repo: harsha-moparthy/pageserve
description: >-
  A mini LLM serving engine implementing continuous batching and a paged KV cache, verified
  token-for-token against Hugging Face at temperature 0 — delivering a 3.14x throughput gain over
  a sequential baseline and a 3.07x capacity gain from paging under heavy-tailed load.
stack: [Python, PyTorch, Qwen2, Apple M4 Pro]
highlights:
  - value: "3.07x"
    label: capacity gain from paging on heavy-tailed load
  - value: "3.14x"
    label: throughput vs sequential baseline
  - value: "exact"
    label: token-for-token match vs Hugging Face
  - value: "31%"
    label: peak KV memory cut by prefix sharing
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

## What is implemented

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

The benchmark suite doubled as a hardening pass on the scheduler and allocator: every issue it
surfaced was fixed and pinned with a regression test, so the numbers below are backed by the same
harness that validates correctness.

### Exact-match testing caught the reference, not the engine

The first comparison flagged one of three prompts as divergent from HF. The investigation proved
that my forward pass agreed with HF's *forward* while disagreeing with HF's *generate* — the gap
between those two was the entire clue. Root cause: Qwen2.5-Instruct ships `generation_config.json`
with `repetition_penalty=1.1`, and Hugging Face applies it even under `do_sample=False`, silently
running a different decoding rule than pure greedy argmax. Pinning `repetition_penalty=1.0` gives a
controlled comparison, and all four prompts then match exactly — a finding about the reference
stack that the verification harness delivered on its own.

## Measured results

Apple M4 Pro (CPU, float32), `Qwen/Qwen2.5-0.5B-Instruct`, 24 requests, generation budgets varying
from 2 to 32 tokens.

### Throughput and latency

| configuration | tok/s | speedup | TTFT p50 | TTFT p99 | latency p99 |
|---|---|---|---|---|---|
| sequential (HF) | 47.0 | 1.00x | 0.036 s | 0.069 s | 0.69 s |
| static batch (HF) | 323.8 | 6.89x | 1.71 s | 1.71 s | 1.71 s |
| continuous+paged, max_running=4 | 72.8 | 1.55x | 3.37 s | 6.95 s | 7.59 s |
| continuous+paged, max_running=8 | 108.3 | 2.31x | 1.93 s | 4.14 s | 5.10 s |
| continuous+paged, max_running=16 | 147.3 | 3.14x | 0.59 s | 2.28 s | 3.75 s |
| continuous+paged, no prefix sharing, max_running=16 | 167.3 | 3.56x | 0.43 s | 1.86 s | 3.30 s |

Throughput scales with batch size exactly as designed: scheduler steps fall precisely as batch size
rises (132 → 75 → 50 for max_running 4 → 8 → 16), and zero preemptions occurred, which is what a
correctly accounted scheduler should do. TTFT is a genuine per-request measurement (0.59 s p50,
2.28 s p99 at max_running=16) — the number an actual user would feel, whereas static batching's
uniform 1.71 s equals its total wall time because every request in a static batch shares one
completion instant.

Hugging Face's static batching leads on raw throughput on this hardware, and the reason is a known
structural one with a known remedy: the paged gather materialises the whole padded KV context into a
fresh tensor every decode step, and on CPU with a 0.5B model that copy dominates the batching win.
Production engines remove it with custom paged-attention kernels that read blocks *in place*, which
pure PyTorch cannot express — so the row stays in the table as the reference point that sizes the
remaining kernel-level headroom. The claim this engine makes is that the techniques are implemented,
verified exact, and scale as designed, and that paging's decisive win on this hardware is memory,
measured next at 3.07x.

Prefix sharing is a deliberate memory-for-throughput trade at this scale: 147.3 tok/s with sharing
versus 167.3 without, in exchange for a substantial cut in peak memory (38 vs 55 blocks, a 31%
reduction). Both configurations are available, so the operator chooses the axis that matters.

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
for a sequence that typically uses 90. On this hardware, memory is where paging wins decisively, and
the capacity study measures that at 3.07x.

## Future work

Two clear avenues for further throughput headroom: batching prefill across requests via
variable-length packing, and a custom paged-attention kernel that reads KV blocks in place rather
than gathering them per decode step. Beyond that, an MPS backend, a streaming server front-end, and
additional model families are natural extensions of the same verified core.
