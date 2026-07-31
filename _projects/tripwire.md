---
title: Tripwire
track: sde
order: 42
group: Delivery, evaluation, and caching
kind: Progressive delivery
repo: harsha-moparthy/tripwire
description: >-
  Progressive delivery for prompts and models: sticky canary routing plus an always-valid mSPRT
  sequential test driving automatic promote and rollback. It peeks after every request without
  inflating the false-rollback rate — 0/2000 false rollbacks on A/A traffic where a naive peeked
  interval fires 234/2000 times.
stack: [Python, Typer, Ollama, http.server, GitHub Actions]
highlights:
  - value: "0/2000"
    label: A/A false rollbacks, vs 234/2000 naive
  - value: "2.3x"
    label: how far the naive peeked test overshoots alpha
  - value: "400/400"
    label: "-0.20 regressions caught, median 131 labels"
  - value: "24/24 to 0/24"
    label: live prompt regression, auto-rolled back
---

## Why this project exists

Offline evals tell you a prompt change looks good on a golden set. The real test is production
traffic, and the mechanism teams reach for is a canary: send the new prompt to a small slice, watch
the quality signal, roll back automatically if it dips. The infrastructure looks like a feature flag,
but the statistics underneath are where it goes wrong.

The trap is peeking. A canary checks its metrics continuously and stops the moment they look bad; a
textbook confidence interval assumes you look once at a fixed sample size. Look after every
observation and the probability of some look producing a false alarm compounds toward one. This repo
measures it: the same A/A traffic through the identical controller with only the test swapped — the
naive peeked z-interval rolls back a healthy candidate 11.7% of the time (2.3x over the nominal
alpha of 0.05), the always-valid mSPRT sequence 0.0%.

## What it does

- Routes traffic stickily by hashing the user id, so a user sees one variant for the whole ramp;
  ramps monotonically 5% to 10% to 25% to 50%
- Accumulates online metrics under sparse, delayed labels — only a fraction of requests get a quality
  label, landing some steps later, matching how judge scoring and thumbs actually arrive
- Rolls back on an always-valid confidence sequence (Robbins' normal-mixture mSPRT): rollback when
  the upper bound clears the margin, promote on non-inferiority or bake-window completion, continue
  otherwise
- Guards latency and refusal as secondary rails using the same anytime-valid machinery, so the
  guardrails do not reintroduce a peeking leak
- Distinguishes rollback triggers (`quality` / `guardrail` / `horizon`), so a safety default firing
  at the horizon is never miscounted as a quality rollback
- Serves a zero-dependency web UI to watch the confidence sequence close in on the margin
- Coverage cannot be gamed by a lucky variance: quality is bounded in [0,1], so sigma-squared = 0.25
  is a universal sub-Gaussian bound — conservative in the safe direction for a rollback controller

## Measured results

Seeded simulation; a CI claim checker re-derives every number from committed artifacts.

| Evidence | Result |
|---|---|
| A/A calibration, 2000 seeds, alpha 0.05 | mSPRT **0/2000 (0.0%)** false rollbacks; naive peeked z **234/2000 (11.7%)** — the negative control is pinned by a test that fails if the naive arm ever behaves |
| Detection, -0.20 quality drop | **400/400 caught**, median **131** candidate labels at rollback (p90 234) |
| Detection, -0.10 drop | 400/400 caught, median 864 labels |
| Detection, -0.05 drop | 52/400 within the horizon — reported as measured, a consequence of the worst-case variance bound |
| Injected improvement (0.70 to 0.85), 400 seeds | **400/400 promoted, 0 false rollbacks** |
| Live prompt regression (ZIP extraction, strict vs "friendly" prompt) | baseline **24/24** pass, candidate **0/24** — correct ZIPs wrapped in prose that breaks the contract; the controller rolled back at request **416** |

The live demo is the cautionary tale: a "does the answer contain the right ZIP" check would pass all
24 candidate responses. The strict programmatic checker fails all 24, and the canary caught what an
offline vibe-check would have shipped.

## Tech stack

| Component | Choice |
|---|---|
| Language | Python 3.12; router, confidence sequence, controller, and simulator need no third-party code |
| Statistics | Robbins normal-mixture mSPRT, closed-form and dependency-free |
| Routing | Sticky hash-based assignment with a monotone ramp |
| Live model | Ollama `gemma4:31b-it-qat`, touched only by the resumable harvester; demo replays committed completions offline |
| Web UI | `http.server` plus one static page |
| CI | GitHub Actions: test suite with negative controls, plus the README claim checker |
