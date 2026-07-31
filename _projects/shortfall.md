---
title: Shortfall
track: hft
order: 48
group: Execution and routing
kind: RL execution study
repo: harsha-moparthy/shortfall
description: >-
  RL for optimal execution, measured honestly: PPO beats tuned TWAP and Almgren-Chriss baselines by
  0.86 bps (9% of all-in cost, paired bootstrap CI) over 200,000 common-random-number episodes and
  captures 94% of an exact dynamic-programming oracle ceiling. Frozen-weight OOD stress includes
  the scenario where the edge is designed to vanish — and it does, degrading to TWAP, not blowing up.
stack: [Python, PyTorch, NumPy, pytest, uv]
highlights:
  - value: "0.86 bps"
    label: edge vs tuned TWAP and AC, CI clear of zero
  - value: "94%"
    label: of the exact-DP oracle ceiling captured
  - value: "200k"
    label: paired common-random-number episodes
  - value: "+0.03 bps"
    label: when the signal is flattened — fails safe to TWAP
---

## Why this project exists

Optimal execution is one of the few RL-in-production success stories in finance, and it is
personal-project-feasible because the environment is a simulator you must calibrate and defend, not
a data feed you cannot get. "RL beats TWAP" is unfalsifiable without a ceiling and worthless
without fair baselines — so the deliverable is the measurement design: an exactly solvable DP
oracle, tuned baselines that see the same signal, common random numbers, and paired bootstrap CIs.

## What it does

- Sell 500,000 shares (5% of ADV) in 50 child-order buckets; the price is a martingale by
  construction, so the agent can only manage cost, never earn alpha
- The one exploitable structure is stochastic liquidity: the temporary-impact coefficient follows a
  persistent lognormal AR(1) (regime half-life ~35 min), observed through a noisy proxy
- Minimal PPO (clipped surrogate, GAE, tanh-squashed Gaussian) against a vectorized simulator with
  an exact, test-pinned cost decomposition
- Baselines: tuned TWAP, Almgren-Chriss closed form (risk-neutral and risk-averse), a tuned
  adaptive heuristic that sees the same signal, and an exact backward-induction DP oracle
- A perfect control variate on the reward removes the martingale noise exactly during training,
  collapsing variance more than 20x so PPO converges in ~4 minutes on a laptop CPU; evaluation
  reports raw shortfall, noise and all
- OOD study with frozen weights under perturbed dynamics, including the scenario built to erase
  the edge entirely

## Measured results

| Evidence | Result |
|---|---|
| PPO vs tuned TWAP / risk-neutral AC, 200,000 CRN episodes | **-0.86 bps**, paired bootstrap 95% CI [-0.93, -0.78] — 9% of all-in cost |
| Share of the exact-DP oracle edge captured | **94%**; residual gap to the ceiling 0.05 bps |
| vs an adaptive heuristic seeing the same signal | -0.14 bps [-0.16, -0.11] — the residual is learned nonlinearity |
| OOD, liquidity variation x0.25 (signal has nothing to say) | **+0.03 bps [-0.02, +0.09]** — the edge vanishes as designed; the agent degrades to ~TWAP |
| OOD, signal noise x5 | -0.65 bps; PPO (8.90) now beats the frozen DP (8.95), which naively trusts the garbage signal |
| Policy interpretability | 2.15x vs 0.57x remaining-TWAP rate across the liquidity signal; flat in price returns, which is correct for a martingale |
| Per-episode win rate | **52%** — the edge is real in aggregate (CI 20x clear of zero) and invisible per order |
| Tests | **38**, including exact decomposition vs closed forms and the return-to-shortfall identity to 1e-4 bps |

Limitations, stated plainly: linear temporary impact and a single observable liquidity factor — no
order book, queues, or fill uncertainty. The point is a defensible testbed with a computable
optimum, not market realism, and sub-1-bps edges are real money at institutional scale but
invisible per order, which is why every claim is paired.

## Tech stack

- Python + PyTorch: minimal PPO implementation (clipped surrogate, GAE)
- Interpretability pass committed as plots: policy surface vs the DP optimum, signal shrinkage
  at the extremes the DP naively trusts
- Vectorized simulator with Almgren-Chriss impact and an exact cost decomposition pinned by tests
- Deterministic grid tuning for every baseline; disjoint seed namespaces for training, tuning,
  validation, evaluation, and OOD
- CI re-evaluates the committed model on a fresh seed namespace and fails the build if PPO stops
  beating tuned TWAP/AC significantly or captures less than 75% of the DP edge
