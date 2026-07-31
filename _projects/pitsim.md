---
title: PitSim
track: hft
order: 53
group: Market simulation
kind: Market simulator
repo: harsha-moparthy/pitsim
description: >-
  An agent-based adversarial market simulator whose baseline LOB population quantitatively
  reproduces five stylized facts of real markets (excess kurtosis 4.03, Hill index 4.49, volatility
  clustering), plus a bandit adversary that learns quote-matching erases a fixed-clock market
  maker's edge (-26 ticks/h paired) at +322/h profit while manipulation loses 100x what it
  extracts. The intuitive clock-jitter defense fails; faster refresh restores the baseline.
stack: [Go, Go stdlib only, Python, matplotlib]
highlights:
  - value: "5/5"
    label: stylized facts reproduced, 30 seeds x 4 hours
  - value: "+322/h"
    label: adversary profit from the learned quote-matching arm
  - value: "-26 ticks/h"
    label: victim edge erased, paired against same-seed baseline
  - value: "100x"
    label: momentum ignition costs more than it extracts
---

## Why this project exists

Backtests assume the market ignores you; reality adapts. Agent-based simulation is how researchers
study strategy robustness and flash-crash dynamics — but it is only credible if the baseline market
is quantitatively realistic and the adversary is honest about what exploitation actually works.
Both are measured here, in the ABIDES lineage: agents interact only through the matching engine,
everything emergent is measured rather than scripted, and the tactics that do not work are
reported instead of deleted.

## What it does

- A price-time-priority LOB (integer ticks, FIFO levels, lazy cancels) under a deterministic event
  heap keyed by (time, seq); every run is deterministic in its seed
- Agent population: 40 zero-intelligence noise traders, 12 fundamentalists anchoring to a latent
  jump-diffusion value, 15 chartists providing momentum feedback, 4 background market makers, and
  one victim market maker with a fixed 5 s refresh clock — the predictable pattern under attack
- The baseline market must pass five stylized-fact criteria over 30 seeds x 4 simulated hours
  before any adversarial result counts
- An epsilon-greedy bandit adversary picks one tactic per 60 s episode — idle, fade, undercut
  (Harris's quote matcher), or momentum ignition — with inventory flattened at episode boundaries
  so each arm pays its own risk
- Defenses tested one change at a time against the strength-4 adaptive adversary

## Measured results

| Evidence | Result |
|---|---|
| Stylized facts (30 seeds x 4 h) | **5/5 pass**: excess kurtosis 4.03 ± 0.14, Hill tail index 4.49 ± 0.66, volatility-clustering ACF 0.142/0.052, aggregational Gaussianity 4.03 → 0.53, volume-volatility corr 0.222 |
| Undercut (quote matching) played alone, strength 4 | victim **-26 ± 14 ticks/h** (entire baseline edge of +28 ± 10 erased); adversary **+322 ± 29/h** |
| Momentum ignition | victim -43 ± 75, adversary **-37,310 ± 257/h** — manipulation loses ~100x what it extracts; the bandit rejects it within ~40 episodes |
| Learning vs random tactics, same firepower | random adversary loses **20-60x more** and produces no reliable degradation below strength 8 |
| Defense: refresh every 2 s instead of 5 s | victim 29 ± 10/h — **baseline restored** |
| Defense: widen half-spread to 3 | victim 60 ± 11/h |
| Defense: jittered clock ±2.5 s | victim 10 ± 8/h — **no help**; the exploit keys on staleness and tightness, not clock phase |
| Scale | ~5M events per run; the full 30-seed x 4 h matrix (~250 simulated market-hours) runs in seconds on a laptop |

The exploit has capacity limits, and the bandit learns those too: undercut stops paying above
strength ~2, and its selection share falls from 86% at strength 1 to 25% at strength 8. Learning
also has tuition: the adaptive adversary at strength 4 loses -385/h overall while its converged
undercut arm makes +322/h — the difference is exploration cost, dominated by mandatory visits to
the catastrophic ignite arm.

## Tech stack

- Go, stdlib only — zero dependencies for the simulator, agents, bandit, and statistics
- Discrete-event kernel with exact cash/inventory conservation, tested under `go test -race`
- Epsilon-greedy bandit with optimistic initialization and a live epsilon floor
- Python + matplotlib for figures, the only non-Go step; a `selfcheck` CI gate re-asserts
  determinism, conservation, fat tails, and paired victim degradation on every run
- Property tests for the LOB (price-time priority, FIFO after mid-queue cancels) and kernel
  (deterministic ordering at equal timestamps, cross-run reproducibility)
