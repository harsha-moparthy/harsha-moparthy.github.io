---
title: Trajeval
track: ml
order: 4
group: Agent reliability
kind: Agent evaluation
repo: harsha-moparthy/trajeval
description: >-
  A regression-testing harness for AI agents: pass@k / pass^k with bootstrap confidence intervals,
  step-level trajectory scoring, and a CI gate that statistically distinguishes real regressions
  from run-to-run noise — with every estimator validated against agents whose true success rate is known.
stack: [Python, numpy, SQLite, Gemini, Ollama, GitHub Actions]
highlights:
  - value: "6.0%"
    label: measured A/A false-alarm rate
  - value: "100%"
    label: gate detection of 20-point regressions
  - value: "1e-12"
    label: estimator agreement with closed form
  - value: "31/31"
    label: tests passing
---

## Why this project exists

Teams change a prompt, ship it, and find out a week later that agent quality fell. Ordinary code has
unit tests; agents mostly have vibes. The reason is nondeterminism: a single run is one sample, so naive
"run it once and eyeball it" testing cannot tell a regression from noise — and CI gates built on single
runs either block good changes or wave through bad ones.

The fix mirrors classical software practice, with statistics where determinism used to be:

1. **Repeated runs** (n ≥ 5 per task) instead of single runs.
2. **pass@k and pass^k** semantics instead of a single pass/fail — "would at least one of k tries
   succeed" (agent with retries) vs. "would all k tries succeed" (agent you must trust every time).
3. **Paired baseline-vs-candidate comparison** with resampling statistics, so the gate fires on
   evidence, not on luck.
4. **Step-level scoring** so partial credit and *where* a trajectory went wrong are visible.

## The credibility problem this design solves

Every eval harness reports statistics; almost none can show its statistics are *correct*. The core
design move: alongside real agents, this ships **synthetic stochastic agents with known true success
probabilities** (seeded and reproducible). Because the truth is known analytically, the estimators and
intervals are validated the way numerical code should be:

- the unbiased pass@k estimator is checked against closed-form values,
- bootstrap confidence intervals are checked for empirical coverage (does a 95% CI contain the true
  value ~95% of the time),
- the regression gate's false-alarm rate is measured on A/A comparisons (same agent twice) before it is
  trusted on A/B.

The machinery passes on agents where the answer is known, which is what makes its reports on real agents
trustworthy. That validation-first stance is the project.

## Architecture

```text
 tasks/*.yaml            agents (adapter interface)
 (suite + checks +   ┌──────────────────────────────────┐
  expected steps)    │ synthetic: known p, seeded RNG   │
      │              │ demo: tool-calling LLM agent     │
      │              │       (prompt v1 / v2)           │
      ▼              └────────────────┬─────────────────┘
 ┌──────────┐                         │
 │  runner  │◀────────────────────────┘
 │ n runs/  │
 │  task    │──────▶ SQLite trajectory store (runs, steps, costs)
 └────┬─────┘
      │
      ▼
 ┌────────────┐   ┌──────────────┐   ┌─────────────────────────┐
 │  scoring   │   │   metrics    │   │        compare          │
 │ outcome +  │──▶│ pass@k/pass^k│──▶│ paired bootstrap Δ,     │
 │ step-level │   │ bootstrap CI │   │ gate: fail if Δ beyond  │
 └────────────┘   │ percentiles  │   │ noise threshold         │
                  └──────┬───────┘   └───────────┬─────────────┘
                         ▼                       ▼
                  report.md / report.json   exit code for CI
```

## Statistical design

- **pass@k** uses the unbiased estimator from the Codex paper: with c successes in n runs,
  `pass@k = 1 − C(n−c, k) / C(n, k)`. Naive `1−(1−c/n)^k` is biased; the difference is measurable at
  small n, and the tests prove it.
- **pass^k** ("all k succeed") uses the analogous unbiased form `C(c, k) / C(n, k)`.
- **Confidence intervals** are percentile bootstrap over tasks (resampling tasks, keeping each task's
  runs together), because run-level resampling understates between-task variance — the dominant term in
  real suites.
- **The gate** compares paired per-task success rates. Decision rule: block if the one-sided bootstrap
  CI for (baseline − candidate) pooled success lies above the noise threshold θ (default 2 points). Both
  θ and confidence level are explicit config, so the gate's sensitivity is a stated number rather than a
  guess.

## Measured results

Offline results are deterministic and reproducible; live results depend on the free-tier model of the day.

| Evidence | Result |
|---|---|
| Test suite | **31/31 passed** |
| pass@k / pass^k unbiasedness | exact to 1e-12 by binomial expectation |
| Naive pass@k plug-in bias (n=5, p=0.6, k=3) | **−6.5 points** (quantified, not assumed) |
| Bootstrap 95% CI empirical coverage (300 experiments) | within [0.90, 0.99] band |
| Gate A/A false-alarm rate (200 experiments, p=0.8 vs p=0.8) | **6.0%** |
| Gate detection: 20-point true drop (100 experiments) | **100%** |
| Gate detection: 5-point true drop (200 experiments) | **25.5%** — the measured minimal detectable effect at n=5 × 20 tasks |
| Regression-catch demo (deterministic) | **PASSED** — v1 100/100, v2 85/100, gate blocks |
| A/A demo (deterministic) | **PASSED** — gate stays open |
| Judge validation: Gemini (`gemini-3.5-flash-lite`) | **100% agreement, kappa 1.0** (30 labels) |
| Judge validation: local Gemma 4 (`gemma4:31b-it-qat`) | **96.7% agreement, kappa 0.933** (30 labels) |
| Judge validation: rule-based surrogate | 86.7% agreement, kappa 0.735 |

The gate is characterised in both directions: a measured 6.0% false-alarm rate on A/A comparisons, 100%
detection of 20-point regressions, and a measured 25.5% detection rate at 5-point drops. That last row is
what lets a team choose n and suite size deliberately — the harness reports its own minimal detectable
effect instead of leaving it unstated.

### The live finding, worth more than a staged catch

The planted "regression" — deleting the *use tools for all arithmetic* instruction from the prompt — did
**not** regress the real model. `gemini-3.1-flash-lite` called the discount/conversion tools anyway on
all 80 runs, and the gate correctly stayed open, which is exactly the behaviour a well-calibrated gate
should have when there is nothing to catch. Two results the harness surfaced on its own:

1. prompt edits you fear are sometimes harmless, and only measurement tells you which;
2. the offline simulator's assumption (v2 skips tools 35% of the time) did not describe this model —
   simulators are for exercising the *machinery*, and real verdicts come from real runs.

Total live cost: ~$0.009 at list price (75.8k input / 3.9k output tokens); mean wall time 25 s/run under
free-tier rate-limit retries.

### Local replication (Ollama)

The full live protocol was replicated on a local `gemma4:31b-it-qat` via Ollama — no API key, no quota,
$0:

- **A/B (20 tasks × 2 runs per arm):** v1 40/40, v2 40/40, step score 1.0 on every run; gate verdict *no
  regression detected* (Δ +0.000). The planted prompt degradation left this model unaffected too,
  independently confirming the Gemini finding on a second, unrelated model family. 80,208 input / 17,468
  output tokens; mean 44 s per run.
- **Judge validation:** 96.7% agreement, kappa 0.933 on the 30 human labels — between the rule surrogate
  (86.7%) and Gemini (100%). The single disagreement is committed in the report rather than relabeled
  away, so the kappa is reproducible from the published labels.

Two providers, two verdicts, same conclusion — exactly what you want from a harness whose job is to
distinguish signal from model quirks.

## What makes the numbers trustworthy

Every statistic this harness reports is validated against cases where the true answer is known before it
is applied to cases where it is not. The gate's false-alarm and detection rates are measured and
published at both effect sizes tested, including the 5-point regime where more runs are needed. The
judge-validation labels were written and labeled by me, stated plainly so a reader can weigh the
agreement figures for exactly what they are.
