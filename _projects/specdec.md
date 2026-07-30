---
title: SpecDec
track: ml
order: 3
group: Inference and serving
kind: Inference study
repo: harsha-moparthy/specdec
description: >-
  Speculative decoding with the exact rejection-sampling correction: verified token-for-token at
  temperature 0, verified distributionally above it, and benchmarked against an audited cost model
  that identifies the draft-to-target depth ratio as the CPU latency ceiling.
stack: [Python, PyTorch, Transformers, Qwen2.5, Apple M4 Pro]
highlights:
  - value: "4.92"
    label: tokens per target pass (code, k=8)
  - value: "90.9%"
    label: peak draft acceptance rate
  - value: "1.05x"
    label: wall speedup, code at k=8
  - value: "0.40"
    label: measured draft cost ratio
---

## Why this project exists

Autoregressive generation leaves hardware idle. Each token needs a full forward pass through the
target model, and that pass is memory-bound — it streams gigabytes of weights to produce a few
kilobytes of logits. Speculative decoding fixes the utilisation problem: a small draft model proposes
`k` tokens cheaply, and the target verifies all `k + 1` positions in a *single* pass.

The algorithm is only interesting if it is **exact**. The entire substance is the rejection-sampling
correction — accept token `x` with probability `min(1, p(x)/q(x))`, and on rejection sample from the
residual `max(0, p − q)` renormalised — because an approximate correction shifts the output
distribution while leaving the text looking plausible. That property is what this project verifies
directly rather than assumes.

## What is actually verified

Two claims, each tested rather than asserted:

1. **Token-for-token identity at temperature 0.** Greedy speculative output is byte-identical to
   greedy baseline output across every domain and every `k`. The suite fails on any divergence.
2. **Distributional equivalence above temperature 0.** Identity is the wrong test when sampling, so
   the correction is checked by drawing many samples and comparing the empirical distribution against
   the target's — the property the algorithm actually promises.

## Measured results

Target `Qwen2.5-1.5B-Instruct` (28 layers), draft `Qwen2.5-0.5B-Instruct` (24 layers), Apple M4 Pro
CPU, float32, 32 new tokens, greedy.

| domain | k | acceptance | tokens / target pass | wall speedup |
|---|---|---|---|---|
| **code** | **8** | 73.1% | **4.92** | **1.05x** |
| code | 4 | 84.2% | 3.66 | 0.77x |
| code | 1 | 90.9% | 1.83 | 0.50x |
| factual | 8 | 40.6% | 3.46 | 0.80x |
| dialogue | 8 | 43.1% | 3.37 | 0.74x |
| prose | 8 | 23.7% | 2.51 | 0.53x |

**Acceptance rate tracks domain predictability exactly as theory says it should.** At `k = 4`: code
84%, dialogue 60%, factual 59%, prose 37%. Code is highly constrained — after `def fibonacci(n):`
both models agree on the indentation, the docstring shape, the `if n <= 1` guard — so a 0.5B draft
predicts a 1.5B target's continuations almost perfectly. Open-ended prose is where the distributions
diverge, and acceptance halves.

**The algorithmic win is real and large.** On code at `k = 8` the target model runs once per 4.92
emitted tokens: 80% of target forward passes eliminated, with byte-identical output. That is a
hardware-independent measure of avoided work.

## What the cost model establishes: depth ratio, not parameter count

Wall-clock speedup stays below 1.0x in 15 of the 16 configurations measured; code at `k = 8` is the
one that clears it, at 1.05x. The audited cost model explains the direction, from instrumented
per-step timings rather than estimates:

```
draft step:   0.0205 s        two-token catch-up:  0.0531 s
target step:  0.0512 s        draft cost ratio:      0.40
```

**The draft costs 40% of a target step, not the ~10% speculative decoding needs.** Qwen2.5-0.5B has
24 layers against the 1.5B's 28 — nearly the same depth — and on CPU at batch size 1 the per-layer
Python and kernel-launch overhead dominates the FLOP difference that is supposed to make the small
model cheap. A fully accepted block also leaves the final draft token plus target bonus pending,
making the next catch-up call 0.0531 s rather than one 0.0205 s step; the cost model charges that
work explicitly rather than hiding it.

This is the transferable result: on CPU at batch size 1, the *depth ratio* between draft and target —
not their parameter counts — sets the latency ceiling, and a draft with far fewer parameters but
nearly the same depth does not reach the cost ratio the technique requires. The measurement gives a
concrete selection criterion for draft models, and it only appears because wall-clock is reported
alongside the algorithmic metric.

## Scope and next steps

A verification rerun reproduced every acceptance rate and tokens-per-target-pass value exactly, so
the algorithmic work-reduction numbers are deterministic. Wall speedups ranged 0.20x–1.27x across
runs under varying local CPU load, so the latency cells are labelled as directional single-run
measurements rather than stable point estimates. The natural next step is a draft model with a much
shallower stack, to test whether the wall-clock result follows the algorithmic one.
