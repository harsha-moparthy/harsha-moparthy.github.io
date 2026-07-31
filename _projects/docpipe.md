---
title: DocPipe
track: fde
order: 23
group: Documents and field data
kind: Document pipeline
repo: harsha-moparthy/docpipe
description: >-
  A self-verifying document pipeline: arithmetic and cross-document rules plus dual-strategy
  disagreement route only genuine uncertainty to humans, and a correction loop lifts frozen-holdout
  accuracy from 91.79% to 97.92% while a frozen control arm stays flat. Straight-through processing
  rises from 6.86% to 45.10% with an escaped-error rate held at 0.00%.
stack: [Python, SQLite, Typer, Rich, GitHub Actions]
highlights:
  - value: "91.8% -> 97.9%"
    label: frozen-holdout accuracy after 2 weeks of corrections
  - value: "+38.24 pts"
    label: straight-through processing, 6.86% to 45.10%
  - value: "0.00%"
    label: escaped-error rate at the operating threshold
  - value: "18/18"
    label: induced vendor priors match hidden ground truth
---

## Why this project exists

Extraction is table stakes; the interesting problems are downstream of it. When OCR misreads a
subtotal of 545.00 as 645.00, both extraction strategies read 645.00 — correctly, because that is
what the page says. They agree, confidently, and they are both wrong. No amount of cross-checking
readers of the same glyphs can catch that; arithmetic against the rest of the document catches it
immediately. And "it improves from corrections" is easy to claim, so the evaluation is built so the
claim has to survive a frozen control arm, a frozen holdout, two negative controls, and planted
adversaries that attack the learner itself.

## What it does

- Verifies extractions in three layers with different failure modes: arithmetic and cross-document
  rules (line math, subtotal+tax=total, PO reconciliation, duplicates) as hard gates; disagreement
  between an anchor reader and a layout reader that fail differently; and learned per-vendor priors
  that become new validation rules.
- Routes documents by a confidence threshold, but a broken hard rule goes to a human regardless —
  the routing curve never reaches 100% automation at any threshold, by design.
- Learns from whole-record reviews, confirmations included, because learning a vendor's date format
  needs dates the reviewer vouched for.
- Streams 282 documents across 7 vendors as three weekly batches plus a frozen 102-document holdout
  that is never reviewed and never learned from; a frozen control arm processes the same batches
  with a permanently cold state, subtracting out batch difficulty.
- Ships two negative controls that must stay flat for opposite reasons — a vendor unseen until
  week 3 and a vendor fully readable on day one — plus planted adversaries with specific guards,
  each proven load-bearing by a mutation check.
- Survives an imperfect reviewer: with 10% of flagged wrong fields waved through as learning
  evidence, holdout accuracy still moves 91.79% to 97.92% and every induced prior remains correct.

## Measured results

| Evidence | Result |
|---|---|
| Frozen holdout, field accuracy | 91.79% cold start, 97.92% after 2 weeks of corrections |
| Frozen holdout, straight-through processing | 6.86% to 45.10% (+38.24 pts) |
| Frozen control arm on the same surfaces | +0.00 pts accuracy, +0.00 pts STP |
| Accuracy on automated documents | 100.00% at both ends; escaped-error rate 0.00% |
| Negative controls (litware, fabrikam) | both flat, for opposite reasons |
| Learned vs true | 18/18 induced vendor priors match hidden generator truth, plus 11 field captions |
| Reviewer-error sensitivity (10% wrong confirmations) | gain survives; every induced prior remains correct |
| Test suite | 96 tests, including structural leak checks |
| Mutation check | 7/7 guards caught, each by a failing test |
| Corpus | 282 documents, 7 vendors, 105 genuine defects, 23 benign oddities, one seed |

Rule precision is reported below 1.00 because the corpus contains honest edge cases — tax-exempt
invoices, one-penny rounding residues, legitimate second tax rates — that punish over-eager rules.
Exactly 1.00 would mean it had none.

## Tech stack

| Component | Choice |
|---|---|
| Corpus | deterministic generator: 7 vendor templates, seeded OCR noise, planted defects |
| Extraction | two strategies — anchor (labels) and layout (position and arithmetic) |
| Verification | hard rules, cross-strategy disagreement, learned vendor priors |
| Storage | SQLite; ground truth structurally quarantined from pipeline SQL |
| Evaluation | two-arm, three-week temporal design with a frozen holdout |
| CLI | Typer + Rich; `docpipe report` regenerates every committed number |
