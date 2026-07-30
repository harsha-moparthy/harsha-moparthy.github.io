---
title: CostRouter
order: 12
group: Cost and observability
kind: Routing study
repo: harsha-moparthy/costrouter
description: >-
  A cost-aware LLM router over three tiers, evaluated on 180 public-benchmark items. The frontier
  beats all-cheap and all-expensive at intermediate budgets — but captures only about a third of the
  available headroom, and its edge over random is significant in some budget regions and not others.
  Both facts are reported.
stack: [Python, scikit-learn, Gemini, Ollama, MMLU-Pro, IFEval]
highlights:
  - value: "0.8496"
    label: frontier area (random 0.8276, oracle 0.9307)
  - value: "13 > 768"
    label: surface features beat embeddings
  - value: "p=0.302"
    label: not significant at 20% escalation
  - value: "+35 pts"
    label: tier gap on reasoning vs +6.7 creative
---

## Why this project exists

Most requests sent to an expensive model could be answered just as well by a cheap one. Routing each
query to the cheapest model that can handle it is a live commercial problem — Martian, NotDiamond,
OpenRouter and LiteLLM all sell some version of it.

The claim is easy to make and hard to substantiate, because the obvious evaluation is rigged. Compare
a router against all-cheap and all-expensive and it wins by construction, since it sits between them.
The only honest null hypothesis is **random routing at the same escalation rate** — a coin flip that
spends exactly as much money. Almost nobody publishes that comparison. This project's central result
is what happens when you do.

## The evaluation design

- **180 items** from public benchmarks: 60 reasoning (MMLU-Pro), 60 factual, 60 creative
  (IFEval-style verifiable instruction-following).
- **Three tiers** — local, cheap-hosted, expensive-hosted — with per-token cost charged from real
  measured token counts, including the router's own embedding-call overhead.
- **A fixed budget grid** from all-cheap to all-expensive, so every policy is integrated over the same
  interval. Scoring policies on different budget ranges is the easy way to manufacture a win.
- **Out-of-fold prediction** for every learned router, so no item is scored by a model that trained on
  it.
- **Permutation testing**, 5,000 draws per cell, with the escalated fraction held fixed — the only way
  to ask "is this skill, or is this just spending more money?"

## Measured results

180 items harvested 2026-07-29 on Apple M4 Pro.

| policy | frontier area | savings at matched quality | escalated |
|---|---|---|---|
| **oracle** (unachievable ceiling) | **0.9307** | 73% | 22% |
| `predictive/surface` (13 features) | **0.8496** | 18% | 85% |
| `predictive/embedding+surface` (781) | 0.8398 | 5% | 95% |
| `predictive/embedding` (768) | 0.8387 | 2% | 98% |
| `random` (the honest null) | 0.8276 | 0% | 100% |

**The 13 interpretable surface features beat 768-dimensional embeddings.** With 180 items against 768
dimensions the embedding router memorises: train AUC 1.000 against out-of-fold AUC 0.640, an overfit
gap of +0.360, versus +0.105 for surface features. The embedding call also costs real money, charged
to the router as overhead. On this data it buys nothing and is a net loss.

### Where the skill is statistically real — and where it isn't

| escalated | `surface` router | random | delta | p (one-sided) |
|---|---|---|---|---|
| 20% | 77.8% | 76.9% | +0.9% | 0.302 |
| 30% | 81.7% | 78.9% | +2.7% | 0.053 |
| 40% | 85.0% | 81.0% | **+4.0%** | **0.009** |
| 50% | 88.9% | 83.1% | **+5.8%** | **0.0002** |
| 60% | 91.1% | 85.1% | **+6.0%** | **<0.0001** |

**The router's advantage is significant from 40% escalation upward and indistinguishable from random
below 30%.** This is the result I would have been tempted to round off. At the low-escalation end —
the commercially interesting end, where you are trying to send only the hard 20% upward — the surface
router cannot be distinguished from a coin flip on this sample.

The embedding router has the mirror-image profile: significant at 20–30% (+3.7%, p=0.006) and not
above 40%. Neither is uniformly better, and a single headline number for either would hide that.

### The tier gap is not where you'd guess

| tier | reasoning | factual | creative |
|---|---|---|---|
| cheap | 60.0% | 68.3% | **90.0%** |
| expensive | 95.0% | 88.3% | 96.7% |
| **gap** | **+35.0** | +20.0 | **+6.7** |

Thinking buys +35 points on math and physics but only +6.7 on verifiable instruction-following, where
the cheap tier already sits at 90%. **Escalating a creative request is nearly always wasted money** —
the cheap model can already follow the format, and reasoning does not help it follow the format
better. A slice-blind router pays the same premium on all three, which is where most of the
unrealised headroom goes.

## Honesty note

The router captures roughly a third of the oracle's headroom, not most of it. The gap between
`predictive/surface` at 0.8496 and the oracle at 0.9307 is the part of the problem this design does
not solve, and it is reported as prominently as the part it does.
