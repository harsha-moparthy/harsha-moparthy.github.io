---
title: EvalGate
track: sde
order: 41
group: Delivery, evaluation, and caching
kind: Evaluation CI
repo: harsha-moparthy/evalgate
description: >-
  Evaluation-driven CI for AI features: tiered golden sets, paired bootstrap significance on per-case
  score deltas, judges validated against programmatic truth, and a PASS / BLOCK / INCONCLUSIVE merge
  gate that escalates tiers only when it cannot decide. On the 20-scenario matrix it blocks 12/12
  true regressions with 0/8 false blocks.
stack: [Python, Typer, Ollama, GitHub Actions, uv]
highlights:
  - value: "12/12"
    label: true regressions blocked, 0 missed
  - value: "0/8"
    label: false blocks on not-worse changes
  - value: "87%"
    label: false-pass rate of the naive judge, vs 0% strict
  - value: "4/4"
    label: live prompt variants, verdict matches oracle
---

## Why this project exists

Teams change a prompt, ship it, and find out a week later that quality fell. The fix mirrors ordinary
software — golden datasets and an evaluation gate in CI — and the interesting part is that a naive
version of this gate does not work. Three reasons, each exposed by measurement: a 20-case golden set
has almost no power if you compare the arms unpaired (case difficulty swamps the effect; pairing
cancels it inside each per-case delta); treating sampling repeats as independent observations triples
the apparent sample size and makes the gate confidently block changes it has no evidence against; and
a weighted score lets a broken output contract buy itself back — an unparseable response can still
score ~0.8 on a naive weighted sum.

## What it does

- Scores responses programmatically — JSON validity, an enum-constrained schema, label correctness —
  so the primary signal never depends on a model's opinion
- Tiers the golden set: smoke (8 cases) on every PR, full (20) nightly or on escalation, with smoke a
  strict subset of full, enforced by test
- Pairs baseline against candidate on identical cases and bootstraps the per-case deltas, resampling
  cases as the exchangeable unit; repeats are averaged per case before pairing
- Decides from the confidence interval alone: BLOCK when confidently worse, PASS on non-inferiority,
  INCONCLUSIVE otherwise — which is not indecision but the trigger that escalates to the expensive tier
- Enforces a format floor (JSON-valid rate under 90% blocks regardless of score), so format can never
  be traded against label accuracy
- Validates judges against programmatic truth, reporting false-pass rate separately because that is
  the error that ships regressions
- Caps cost per run and reports the marginal generations, tokens, and seconds a PR pays
- CI integration: smoke gate on PRs with a readable comment, full tier nightly, plus a claim checker
  that re-derives every README number from committed artifacts and fails the build on drift

## Measured results

300 responses harvested once from Ollama `gemma4:31b-it-qat` (5 prompt variants x 20 cases x 3
repeats), committed so everything reproduces offline with no model.

| Evidence | Result |
|---|---|
| 20-scenario confusion matrix | **12/12 truly-worse blocked, 0 missed; 8/8 not-worse passed, 0 false blocks** |
| Live variants vs pre-fixed oracle labels | **4/4 match**: cosmetic PASS, improved PASS, no_rules BLOCK (score CI), chatty BLOCK (format floor) |
| Two regression mechanisms | no_rules keeps 100% JSON validity and is caught purely by the interval; chatty is caught by the floor at 0% validity |
| Tier cost | every live verdict reached on the smoke tier — 8 cases, 24 generations |
| Judge validation over 300 responses | lenient judge: 80% agreement but **87% false-pass**; strict parse-checking judge: **0% false-pass**, kappa +1.0 |
| Verdict stability, 200 bootstrap seeds | 3/4 variants 100% stable; `improved` reported as a knife-edge (CI bound exactly on the margin), not smoothed over |
| Paired vs unpaired estimator | on the cosmetic no-op, pairing yields a zero-width interval and PASS; unpaired straddles the margin and would escalate a no-op for nothing |
| Repeat averaging | dropping 3 repeats to 1 flips a confident BLOCK to inconclusive on 42/200 draws — the cost of skipping it, measured |

## Tech stack

| Component | Choice |
|---|---|
| Language | Python 3.12; checkers, statistics, gate, and matrix need no third-party code |
| CLI | Typer |
| Statistics | Percentile bootstrap, paired on per-case deltas; unpaired retained for the power comparison |
| Live model | Ollama `gemma4:31b-it-qat`, touched only by the resumable harvester |
| Providers | Live Ollama plus an offline replay provider over committed responses |
| CI | GitHub Actions: smoke on PRs, full nightly, claim-checking evidence gate |
