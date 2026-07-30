---
title: Synth Pipeline
order: 14
group: Data and post-training
kind: Data pipeline
repo: harsha-moparthy/synth-pipeline
description: >-
  A synthetic data pipeline with ruthless quality filtering: persona-conditioned generation, a
  validated four-stage filter stack, and a three-way comparison showing raw synthetic data made the
  model *worse* than no synthetic data at all — while the same generations, filtered, beat both.
stack: [Python, embeddings, SQLite, Ollama, Gemini]
highlights:
  - value: "16.7%"
    label: raw synthetic — worse than none
  - value: "33.3%"
    label: filtered synthetic — beats both arms
  - value: "126 → 38"
    label: candidates surviving the filter stack
  - value: "81 / 81"
    label: tests passing
---

## Why this project exists

Generating synthetic training data is easy and mostly produces garbage. The interesting engineering is
in the filtering — and the only way to prove a filter stack earned its keep is to train with and
without it and compare on held-out evaluation.

Most write-ups skip that step, showing a filter funnel and some kept/dropped counts. Counts prove
nothing about whether the surviving data helps.

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

**Raw synthetic data made the model worse than no synthetic data at all** — 25.0% down to 16.7%. More
data, worse results. The mechanism is visible in the traces: wrong-SQL items and near-copies of
evaluation questions sit nearest the eval questions in embedding space and get retrieved verbatim, so
the model confidently reproduces broken queries.

The same generations after filtering reach 33.3%, beating both arms with **less than half the raw
arm's training data**. That comparison is the whole point of the project: it converts "filtering is
good practice" into a measured claim, and it quantifies the damage unfiltered generation does.

## The filter stack, with its ledger

Four stages, each with a recorded reason for every drop:

| stage | in | kept | dropped | reasons |
|---|---|---|---|---|
| dedup | 126 | 56 | 70 | exact_duplicate=44, near_duplicate=26 |
| verify | 56 | 52 | 4 | not_a_select=4 |
| judge | 52 | 45 | 7 | judge_score_2=7 |
| decontam | 45 | 38 | 7 | embedding_match=6, ngram_match=1 |

**Decontamination is not optional.** Seven candidates were near-duplicates of *evaluation* questions.
Left in, they would have inflated the score of the very arm meant to demonstrate the filter's value —
the pipeline would have proved its own effectiveness using leakage.

The judge stage is itself validated against a labelled subset rather than trusted: accuracy 1.00,
bad-precision 1.00, bad-recall 1.00 on 20 labelled pairs with the deterministic oracle, which
demonstrates the validation harness works before any model judge is believed.

## Leave-one-stage-out

Each stage is removed individually and the arm retrained, so the funnel's stages are attributed rather
than assumed. That ablation is what distinguishes a filter stack that works from four stages where one
does the work and three are cargo cult.

## Honesty note

All headline numbers are produced offline with the deterministic `fake` provider and a seeded RNG, so
anyone can reproduce them exactly with `uv sync && synth all`. The absolute accuracies are low —
33.3% is not a good text-to-SQL model — because the point is the *contrast between arms* on a
deliberately small budget, not a competitive result. Stated plainly rather than dressed up.
