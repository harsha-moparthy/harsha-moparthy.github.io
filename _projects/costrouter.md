---
title: CostRouter
order: 12
group: Cost and observability
kind: Routing study
repo: harsha-moparthy/costrouter
description: >-
  A cost-aware LLM router over three tiers, evaluated on 180 public-benchmark items against the
  strictest available null: random routing at a matched escalation rate. The learned router leads that
  null across the budget grid, its margin is statistically significant from 40% escalation upward, and
  13 interpretable surface features outperform 768-dimensional embeddings.
stack: [Python, scikit-learn, Gemini, Ollama, MMLU-Pro, IFEval]
highlights:
  - value: "0.8496"
    label: frontier area (random 0.8276, oracle 0.9307)
  - value: "13 > 768"
    label: surface features beat embeddings
  - value: "+5.8%"
    label: over random at 50% escalation (p=0.0002)
  - value: "+35 pts"
    label: tier gap on reasoning vs +6.7 creative
---

## Why this project exists

Most requests sent to an expensive model could be answered just as well by a cheap one. Routing each
query to the cheapest model that can handle it is a live commercial problem — Martian, NotDiamond,
OpenRouter and LiteLLM all sell some version of it.

The claim is easy to make and hard to substantiate, because the obvious evaluation is rigged. Compare
a router against all-cheap and all-expensive and it wins by construction, since it sits between them.
The one null hypothesis that carries information is **random routing at the same escalation rate** — a
coin flip that spends exactly as much money. Almost nobody publishes that comparison. This project's
central result is what happens when you do.

## The evaluation design

- **180 items** from public benchmarks: 60 reasoning (MMLU-Pro), 60 factual, 60 creative
  (IFEval-style verifiable instruction-following).
- **Three tiers** — local, cheap-hosted, expensive-hosted — with per-token cost charged from real
  measured token counts, including the router's own embedding-call overhead.
- **A fixed budget grid** from all-cheap to all-expensive, so every policy is integrated over the same
  interval. Scoring policies on different budget ranges is the easy way to manufacture a win.
- **Out-of-fold prediction** for every learned router, so no item is scored by a model that trained on
  it.
- **Permutation testing**, 5,000 draws per cell, with the escalated fraction held fixed — this is what
  separates routing skill from simply spending more money.

## Measured results

180 items harvested 2026-07-29 on Apple M4 Pro.

| policy | frontier area | savings at matched quality | escalated |
|---|---|---|---|
| **oracle** (unachievable ceiling) | **0.9307** | 73% | 22% |
| `predictive/surface` (13 features) | **0.8496** | 18% | 85% |
| `predictive/embedding+surface` (781) | 0.8398 | 5% | 95% |
| `predictive/embedding` (768) | 0.8387 | 2% | 98% |
| `random` (matched-cost null) | 0.8276 | 0% | 100% |

The learned surface router leads the matched-cost null across the grid and delivers 18% savings at
matched quality.

**The 13 interpretable surface features beat 768-dimensional embeddings.** The harness pins down the
mechanism: with 180 items against 768 dimensions the embedding router memorises, showing train AUC
1.000 against out-of-fold AUC 0.640 — an overfit gap of +0.360, versus +0.105 for surface features.
The embedding call is also charged to the router as real cost overhead, which it does not recover on
this sample. That makes the cheap, inspectable feature set the right choice here, and it is the one
the router ships with.

### Which router pays off in which budget region

| escalated | `surface` router | random | delta | p (one-sided) |
|---|---|---|---|---|
| 20% | 77.8% | 76.9% | +0.9% | 0.302 |
| 30% | 81.7% | 78.9% | +2.7% | 0.053 |
| 40% | 85.0% | 81.0% | **+4.0%** | **0.009** |
| 50% | 88.9% | 83.1% | **+5.8%** | **0.0002** |
| 60% | 91.1% | 85.1% | **+6.0%** | **<0.0001** |

**The surface router's advantage over random is statistically significant from 40% escalation upward**,
reaching +6.0% at 60% escalation. Below 30% escalation its margin sits within sampling noise on this
sample — and the embedding router has the mirror-image profile, carrying the significant margin exactly
there (+3.7%, p=0.006 at 20–30%) and not above 40%. The measurement therefore supports a concrete
design decision: which feature set to route with depends on the budget region you operate in, and the
permutation grid is what makes that region boundary visible instead of averaged away by a single
headline number.

### The tier gap is not where you'd guess

| tier | reasoning | factual | creative |
|---|---|---|---|
| cheap | 60.0% | 68.3% | **90.0%** |
| expensive | 95.0% | 88.3% | 96.7% |
| **gap** | **+35.0** | +20.0 | **+6.7** |

Thinking buys +35 points on math and physics but only +6.7 on verifiable instruction-following, where
the cheap tier already sits at 90%. **Escalating a creative request is nearly always wasted money** —
the cheap model can already follow the format, and reasoning does not help it follow the format
better. A slice-blind router pays the same premium on all three, which locates where the remaining
headroom sits.

## Scope and next steps

Results are measured on this 180-item benchmark set with out-of-fold prediction and a matched-cost
null. The oracle row bounds what perfect per-item difficulty knowledge is worth on this data, and the
tier-gap table points at the next build: a slice-aware policy that spends its escalation budget on
reasoning items and holds the cheap tier for verifiable instruction-following.
