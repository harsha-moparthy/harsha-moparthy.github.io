---
title: TwinSim
track: fde
order: 75
group: Analysis copilots
kind: Digital twin
repo: harsha-moparthy/twinsim
description: >-
  A digital twin of a fulfilment operation that must pass a pre-registered backtest on sealed
  weeks before any what-if is trusted: shipped-throughput MAE 1.9% against a 5.4% budget, with
  90% predictive intervals covering the actual in 32/32 week-by-metric cells. A guarded, metered
  proposal agent then optimises against the twin — greedy confirms +3.28 pts on-time on fresh
  seeds vs +2.56 for equal-budget random, and the winner stays positive in 15/15 sensitivity rows.
stack: [Python, FastAPI, Typer, Rich, qwen3:8b, GitHub Actions]
highlights:
  - value: "1.9%"
    label: holdout MAE vs a 5.4% pre-registered budget
  - value: "32/32"
    label: predictive-interval coverage, week x metric
  - value: "+3.28 pts"
    label: confirmed on-time gain, fresh seeds, 90% CI [+0.83, +5.72]
  - value: "15/15"
    label: sensitivity rows positive; worst row +1.55
---

## Why this project exists

Before changing a staffing plan, operators want "what happens if" answered safely. The failure
mode of digital twins is not building them — it is trusting an unvalidated one, or pointing an
optimiser at one and mistaking oracle-gaming for improvement. This project builds the whole chain
the way a deployment would need it: seal the holdout, pre-register the error budget, backtest,
and only then let anyone — human or agent — ask what-if, with the agent behind guardrails that
are each named, enforced, and tested.

The epistemic setup is honest by construction: the "real" operation has physics the twin never
sees (within-shift fatigue, a site skill ramp, correlated absence, label jams, QC rework), so the
backtest measures a genuine gap between a model and a reality structurally richer than the model.

## What it does

- Splits 21 weeks of history into burn-in, fit, check, and 8 sealed holdout weeks;
  `Split.assert_unseen` raises at runtime if anything that fits parameters touches a sealed week
- Calibrates on training weeks only: coordinate descent over six bounded knobs with common random
  numbers, a dispersion term so the twin cannot buy mean-accuracy by going deterministic, and
  per-station utilisation in the loss — because the first fit passed the aggregate backtest with
  the wrong internal bottleneck
- Fixes the error budget from check weeks before any holdout week is read
  (budget = max(floor, 1.75 x check MAE)), with validation seeds disjoint from calibration seeds
- Scores every what-if through one paired oracle — same demand bootstraps and twin seeds as the
  baseline — so a delta is a paired estimate, not a difference of two noisy runs
- Runs a three-arm agent study (diagnostics-guided greedy, equal-budget random, a local-model arm
  via committed transcript) against identically-seeded metered oracles, re-estimating every arm's
  winner on fresh seeds it never searched
- Closes the classic ways to beat a simulator structurally — promise-date gaming, demand
  shedding, oracle-noise overfitting, unmetered search, unpriced spend, pushing bad orders past
  the measurement window — and `test_guardrails.py` fails if any named guard is removed

## Measured results

| Evidence | Result |
|---|---|
| Twin validation, 8 sealed weeks x 30 replications | throughput MAE 1.9% (budget 5.4%), on-time 16.4 pts (budget 52.7), cycle p50 22.7% (budget 67.4%), cycle p90 14.6% (budget 38.8%) — all PASS |
| 90% predictive-interval coverage | 32/32 week x metric cells |
| Greedy arm, confirmed on fresh seeds | +3.28 pts on-time, 90% CI [+0.83, +5.72], using 26 of 120 evaluations |
| Random arm, equal budget | +2.56 pts [+0.22, +4.89] — greedy reached a better confirmed result on 4.6x fewer evaluations |
| Local-model arm (qwen3:8b, replayed transcript) | +1.79 pts [+0.71, +2.87] on 12 evaluations |
| Winner's curse, made visible | ~2.4-pt search-vs-confirmed gap on the guided arms, reported instead of hidden |
| Sensitivity: six knobs both ways, demand +/-10% | positive in 15/15 rows; worst row demand x1.1 at +1.55 pts |
| The winning intervention | +1 picker on Mon/Tue/Wed evening and Fri day blocks — +32 of the 56 person-hours/week offered |

The table is read honestly in the repo: throughput is the tight claim, and on-time error is wide
because the world's bad weeks are driven by correlated absence — exactly the data a WMS extract
does not contain. The wide budget is that statement, quantified and pre-registered rather than
discovered after the fact.

## Tech stack

| Component | Choice |
|---|---|
| Simulator and twin | stdlib Python discrete-event engine; the twin sees only fitted distributions and scalars |
| Calibration | coordinate descent, common random numbers, utilisation-anchored loss |
| Oracle | paired, metered, guarded; `BudgetExhausted` is a hard stop |
| Agent arms | diagnostics-guided greedy, equal-budget random, qwen3:8b via committed transcript |
| UI and CLI | FastAPI what-if UI, Typer + Rich CLI (`build`, `calibrate`, `validate`, `whatif`, `propose`, `sensitivity`) |
| CI | GitHub Actions runs the full pipeline end-to-end, offline, including the LLM arm via transcript |
