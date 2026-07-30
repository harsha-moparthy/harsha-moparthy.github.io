---
title: SpecDec
order: 3
group: Inference and serving
kind: Inference study
repo: harsha-moparthy/specdec
description: >-
  Speculative decoding with the exact rejection-sampling correction: verified token-for-token at
  temperature 0, verified distributionally above it, and benchmarked to a negative wall-clock result
  that the cost model explains quantitatively.
stack: [Python, PyTorch, Transformers, Qwen2.5, Apple M4 Pro]
highlights:
  - value: "4.92"
    label: tokens per target pass (code, k=8)
  - value: "90.9%"
    label: peak draft acceptance rate
  - value: "15 of 16"
    label: configs slower than baseline
  - value: "0.40"
    label: measured draft cost ratio
---

## Why this project exists

Autoregressive generation leaves hardware idle. Each token needs a full forward pass through the
target model, and that pass is memory-bound — it streams gigabytes of weights to produce a few
kilobytes of logits. Speculative decoding fixes the utilisation problem: a small draft model proposes
`k` tokens cheaply, and the target verifies all `k + 1` positions in a *single* pass.

The algorithm is only interesting if it is **exact**. A speculative decoder that changes the output
distribution is just a worse model with extra steps, so the rejection-sampling correction — accept
token `x` with probability `min(1, p(x)/q(x))`, and on rejection sample from the residual
`max(0, p − q)` renormalised — is the entire substance. Getting it subtly wrong produces output that
looks fine and is silently off-distribution.

## What is actually verified

Two claims, each tested rather than asserted:

1. **Token-for-token identity at temperature 0.** Greedy speculative output is byte-identical to
   greedy baseline output across every domain and every `k`. Any divergence is a bug, and the test
   suite treats it as one.
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

## The honest part: 15 of 16 configurations are slower

Wall-clock speedup is below 1.0x almost everywhere. Only `code @ k=8` clears it, at 1.05x. This is
not a correctness bug and not a tuning failure — the cost model explains the direction:

```
draft step:   0.0205 s        two-token catch-up:  0.0531 s
target step:  0.0512 s        draft cost ratio:      0.40
```

**The draft costs 40% of a target step, not the ~10% speculative decoding needs.** Qwen2.5-0.5B has
24 layers against the 1.5B's 28 — nearly the same depth — and on CPU at batch size 1 the per-layer
Python and kernel-launch overhead dominates the FLOP difference that is supposed to make the small
model cheap. A fully accepted block also leaves the final draft token plus target bonus pending,
making the next catch-up call 0.0531 s rather than one 0.0205 s step; the audited cost model charges
that work rather than hiding it.

So the technique is implemented correctly and still loses on this hardware, because the *depth ratio*
between the two models is wrong for CPU inference. That is a real conclusion about when speculative
decoding pays, and it only appears if you report wall-clock alongside the flattering algorithmic
metric.

A post-audit rerun reproduced every acceptance rate and tokens-per-target-pass value exactly, while
wall speedups ranged 0.20x–1.27x under varying local CPU load. The algorithmic work-reduction numbers
are deterministic; the latency cells are directional single-run measurements, not stable point
estimates, and are labelled as such.
