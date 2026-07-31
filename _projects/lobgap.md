---
title: LOBGap
track: hft
order: 50
group: Prediction and research
kind: Prediction study
repo: harsha-moparthy/lobgap
description: >-
  DeepLOB on FI-2010, evaluated twice: 75.7% accuracy under the published split versus 73.4% under
  purged per-instrument walk-forward, with the +2.2-point gap counted leak by leak — 10 footprint
  overlaps, 396 train and 1,386 test windows mixing spliced instruments. The tape's own oracle
  bound settles the economics: -13.15 bps net per trade at any classifier accuracy.
stack: [Python, PyTorch, FI-2010, NumPy, uv]
highlights:
  - value: "+2.2 pts"
    label: accuracy bought by the published protocol's leakage
  - value: "73.4%"
    label: purged walk-forward accuracy, the believable number
  - value: "-13.15 bps"
    label: oracle net per trade after costs — uneconomic at any accuracy
  - value: "1,386"
    label: test windows mixing spliced instruments, counted
---

## Why this project exists

Most amateur DeepLOB reproductions fail the same way: subtle evaluation leakage makes results look
great until real money disagrees. This project evaluates the same architecture twice — once under
the published FI-2010 protocol for comparability with the literature, and once under purged,
embargoed, per-instrument walk-forward — and counts each leak individually instead of asserting
that leakage exists. The gap between the two numbers, plus an after-cost verdict computed from the
tape itself, is the result; the model is not.

## What it does

- A DeepLOB-class CNN+LSTM on the FI-2010 limit-order-book benchmark, same seed and same 60k-sample
  training budget across both protocols so the comparison is protocol-only
- Purged, embargoed walk-forward splits that respect each sample's 110-tick footprint (window plus
  horizon) — overlapping footprints are not independent observations
- Splice detection: FI-2010's files are 5 instruments spliced end-to-end with no marker, detected
  at 7.6x separation (worst within-instrument move 350 bps vs smallest splice jump 2,655 bps)
- A leakage audit that counts train-test footprint overlaps and instrument-mixing windows under
  each protocol, plus three named malpractices measured under identical budgets
- An oracle cost bound computed before training anything: perfect direction prediction, crossing
  the spread to enter and exit
- Momentum, logistic, and MLP baselines under the same strict protocol

## Measured results

| Evidence | Result |
|---|---|
| Published protocol (80/20 index split, days 8-10 test) | **0.7565 accuracy, 0.7553 macro-F1** |
| Strict purged walk-forward, 4 folds, 313,729 test samples | **0.7344 accuracy, 0.7330 macro-F1** (per-fold 0.7043-0.7511) |
| The protocol gap | **+2.2 points** accuracy and macro-F1 — what the published protocol's leakage buys |
| Leaks counted, published protocol | 10 train-val footprint overlaps; 396 train + **1,386 test** instrument-mixing windows |
| Leaks counted, strict protocol | 0, 0, and 0 |
| Oracle bound (perfect foresight, this tape's spreads) | gross 4.07 bps/trade, round trip 17.21 bps, net **-13.15 bps/trade** |
| Model economics | 0.792 bps gross per directional trade — genuinely positive signal, economically worthless after costs |
| vs baselines, strict protocol (edge over majority class) | DeepLOB **+0.354** vs momentum +0.083, MLP +0.065, logistic +0.060 |
| Ablations, strict protocol | 1 book level 0.600 acc, 5 levels 0.684, 10 levels 0.719 — the deep book carries real signal |
| Tests | **109**, dataset-free in CI via a structured synthetic tape with the same splice structure |

Only 2.0% of moves at this horizon are larger than their own round-trip cost, so the negative
verdict is a property of the tape — reported next to the model's real statistical edge because
both facts are true.

## Tech stack

- Python + PyTorch (CNN+LSTM, trained on Apple Silicon MPS)
- FI-2010 benchmark, sha256-verified fetch, splice-aware loading
- Purged walk-forward split engine, leakage auditor, and spread-crossing cost model
- Every cited number lives in committed JSON assembled by the CLI — nothing transcribed by hand
- Load-bearing properties run as named CI gates: purge arithmetic, splice-refusing cost model,
  scaler field-of-view
