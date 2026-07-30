---
title: Synth Pipeline
order: 14
group: Data and post-training
kind: Data pipeline
repo: harsha-moparthy/synth-pipeline
description: >-
  A synthetic data pipeline built around measured quality filtering: persona-conditioned generation, a
  validated four-stage filter stack, and a three-way training comparison in which the filtered arm
  reached the best held-out accuracy on less than half the unfiltered arm's training data.
stack: [Python, embeddings, SQLite, Ollama, Gemini]
highlights:
  - value: "33.3%"
    label: filtered synthetic — best of three arms
  - value: "126 → 38"
    label: candidates surviving the filter stack
  - value: "74 vs 162"
    label: training rows for the best arm vs unfiltered
  - value: "81 / 81"
    label: tests passing
---

## Why this project exists

Generating synthetic training data is cheap; the quality of what comes out varies enormously. The
engineering that matters is in the filtering — and the way to establish that a filter stack earned its
keep is to train with and without it and compare on held-out evaluation.

Most write-ups stop at a funnel diagram and some kept/dropped counts. Counts describe the filter, not
its effect on the trained model. This pipeline measures the effect.

## The three-way comparison

One text-to-SQL task, three training arms, one held-out evaluation set:

1. **seed-only** — the human-written seed examples alone
2. **seed + raw synthetic** — everything the generator produced
3. **seed + filtered synthetic** — the same generations after the filter stack

| training arm | train size | execution accuracy | per schema |
|---|---|---|---|
| seed-only | 36 | 6/24 (25.0%) | ecommerce 2/8, hr 1/8, library 3/8 |
| seed + raw synthetic | 162 | 4/24 (**16.7%**) | ecommerce 2/8, hr 0/8, library 2/8 |
| **seed + filtered synthetic** | 74 | **8/24 (33.3%)** | ecommerce 3/8, hr 2/8, library 3/8 |

The filtered arm reaches 33.3%, the best of the three, using **less than half the raw arm's training
data**. Unfiltered generation is the arm that does not pay off at this budget: 16.7% against
seed-only's 25.0%, so volume alone moves the metric in the wrong direction.

The harness also identifies the mechanism behind that result. Wrong-SQL items and near-copies of
evaluation questions sit nearest the eval questions in embedding space and get retrieved verbatim, so
the model reproduces broken queries. That is an actionable finding: the cost of unfiltered generation is
concentrated in exactly the items a retriever prefers, which is what makes filtering worth its compute
rather than a matter of taste.

## The filter stack, with its ledger

Four stages, each with a recorded reason for every drop:

| stage | in | kept | dropped | reasons |
|---|---|---|---|---|
| dedup | 126 | 56 | 70 | exact_duplicate=44, near_duplicate=26 |
| verify | 56 | 52 | 4 | not_a_select=4 |
| judge | 52 | 45 | 7 | judge_score_2=7 |
| decontam | 45 | 38 | 7 | embedding_match=6, ngram_match=1 |

**Decontamination earns its stage.** Seven candidates were near-duplicates of *evaluation* questions.
Left in, they would have inflated the score of the arm meant to demonstrate the filter's value, so the
stage removes them before that arm is trained.

The judge stage is validated against a labelled subset rather than trusted on assertion: accuracy 1.00,
bad-precision 1.00, bad-recall 1.00 on 20 labelled pairs with the deterministic oracle, establishing
that the validation harness works before any model judge is relied on.

## Leave-one-stage-out

Each stage is removed individually and the arm retrained, so the funnel's stages are attributed rather
than assumed. The ablation is what distinguishes a filter stack where every stage contributes from one
where a single stage carries the result.

## Scope and next steps

All headline numbers are produced offline with the deterministic `fake` provider and a seeded RNG, so
the full set reproduces exactly with `uv sync && synth all`. The claim the harness supports is the
contrast between arms at a deliberately small budget; scaling the budget and the evaluation set is the
natural extension of the same harness.
