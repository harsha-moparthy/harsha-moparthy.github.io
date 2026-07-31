---
title: Ops Copilot
track: fde
order: 25
group: Analysis copilots
kind: Analytics copilot
repo: harsha-moparthy/ops-copilot-semantic-layer
description: >-
  A copilot that answers plain-English questions about a business warehouse by choosing a metric
  from a curated semantic layer — never by writing SQL. It scores 100/100 on a 100-question
  benchmark (70 answered, 30 refused with the right reason), every answer ships with lineage, and
  the modelling traps the layer prevents are measured: a fluent query that joins shipments to order
  lines overstates revenue by 9.9%.
stack: [Python, SQLite, YAML, Ollama, Rich, GitHub Actions]
highlights:
  - value: "100/100"
    label: benchmark — 70/70 answered, 30/30 refused
  - value: "30/30"
    label: refusal reasons correct, across 9 classes
  - value: "+9.9%"
    label: revenue overstatement from the fan-out trap, measured
  - value: "0"
    label: string literals in 177 compiled query shapes
---

## Why this project exists

An executive asking "how did the northeast do last week" wants a number they can repeat in a
meeting. Text-to-SQL gets them a number that is usually close and occasionally wrong in a way
nobody can see, because the interesting decisions are not syntactic. On this warehouse, a
competent-looking query has to know that an order can ship in two parts (+9.90% revenue if it
doesn't), that cancelled orders carry priced line items (+16.48%), that discounts come off the line
(+3.19%), and that revenue means net of refunds here (+3.98%). Those are measured, not estimated —
and they are the easy ones.

## What it does

- Implements the pattern the BI world converged on: definitions live in a semantic layer, and the
  model chooses which metric, never how it is computed. The planner's output type has no field a
  string can travel in, so "the model never writes SQL" is a property of the types.
- Compiles selections through an AST where a `Param` node is the only representation of a value —
  no AST node can put a string into SQL text, asserted across all 177 legal query shapes.
- Stacks metric components with UNION ALL instead of joining facts, so average order value cannot
  be wrong by the average basket size, and line-grain queries structurally cannot touch the
  shipment table.
- Derives allowed dimensions from fact intersections rather than declaring them, producing
  explainable refusals: on-time delivery rate cannot be broken down by product category because a
  shipment can carry several products.
- Refuses across nine classes — unknown metric, no metric named, disallowed dimension, unknown
  grain, out-of-range dates, unsupported operations — each with a reason and a way forward.
- Grades every answer against an independent oracle that recomputes each number in plain Python,
  imports none of the compiler stack, and issues no SQL aggregates — enforced structurally.

## Measured results

| Evidence | Result |
|---|---|
| Benchmark, deterministic arm | 100/100 — 70/70 answered correctly, 30/30 refused |
| Refusal reasons correct | 30/30 across all 9 refusal classes |
| Compiler vs independent oracle | 0 disagreements across every metric × dimension × grain × filter shape |
| Legal query shapes compiled | 177, of which 0 contained a string literal |
| Line-grain queries touching the shipment table | 0 — fan-out is structurally impossible |
| Semantic layer | v1.4.0: 18 metrics, 14 measures, 8 dimensions, 5 grains, 9 validation rules |
| Layer validation rules | 9/9 each tested against a deliberately violating layer |
| Mutation check | 24/24 mutants caught by a named test |
| Test suite | 178 passed |
| Warehouse | 9,496 orders, 24,999 order lines, 8,899 shipments, 1,170 returns; one seed |

The 100/100 is framed honestly: the deterministic planner is the control that makes any model arm's
score attributable to the model, not evidence an LLM would score 100. The local-model versus raw
text-to-SQL comparison harness is complete and gated, but no comparison number is claimed until
complete transcripts are committed — CI treats a partial transcript as a hard failure.

## Tech stack

| Component | Choice |
|---|---|
| Semantic layer | YAML metrics/measures/dimensions with expressions as nested lists, not SQL snippets |
| Compiler | selection to SQL through an AST; values render only as parameters |
| Warehouse | deterministic SQLite operations mart with every trap asserted present |
| Ground truth | independent Python oracle, structurally isolated from the compiler |
| Planners | deterministic (CI), local model via Ollama, and transcript replay |
| Surface | Rich-rendered CLI and chat with lineage on every answer |
