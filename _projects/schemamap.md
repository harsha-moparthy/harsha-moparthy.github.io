---
title: SchemaMap
track: fde
order: 19
group: Legacy modernization
kind: Data integration
repo: harsha-moparthy/schemamap
description: >-
  LLM-assisted schema mapping with human confirmation. Proposes source-to-target column mappings
  from name, type and value-distribution evidence, calibrates its own confidence on a held-out
  split, and flags proposals where its evidence disagrees with itself. Top-1 accuracy is 51/54
  against 8 planted name traps, all 3 errors land inside the flagged set, 0 of 29 auto-accepts are
  wrong, and reviewer effort drops 43%.
stack: [Python, SQLite, Typer, Ollama, Gemini]
highlights:
  - value: "51/54"
    label: top-1 accuracy, vs 8 planted name traps
  - value: "0/29"
    label: wrong mappings auto-accepted
  - value: "43%"
    label: fewer column inspections, 504 to 289
  - value: "0.0105"
    label: ECE calibrated, vs 0.2429 uncalibrated
---

## Why this project exists

The slowest part of every enterprise data project is mapping source schemas onto target schemas:
hundreds of cryptically-named columns, tribal knowledge, and no ground truth to check against. LLMs
are genuinely good at proposing these mappings. The engineering is everywhere else. Confidence has
to mean something — the only thing a reviewer needs from a score is permission not to look, so it
is fitted with isotonic regression on a validation split and reported on a held-out one. And value
evidence has to be doing the work, not name similarity: the corpus plants eight decoys that beat
the truth on names, like an exact-match `ord_status` holding a coarse legacy domain and a bare
`EMAIL` that is 78% null.

## What it does

- Profiles 72 source columns across 4 legacy systems against 54 documented target columns, keeping
  three evidence blocks deliberately separate: name (through an abbreviation dictionary or model
  semantics), type, and value distributions — format signatures, null rates, domain overlap,
  discovered unit conversions, cross-table linkage.
- A five-arm ablation over the same cached evidence shows names alone fail every trap (0/8), model
  semantics beat the dictionary (51 vs 33), and value-only cannot decide the two value-blind pairs
  it got right by coin flip.
- Calibrates confidence at the pair level (~950 labelled examples), fits the abstain threshold for
  balanced accuracy, and abstains correctly on all 4 targets with no source.
- Flags every proposal where name evidence and value evidence picked different columns: 25 of 54
  flagged, containing 3 of 3 errors — both name-trap errors are high-confidence (86% and 83%) and
  only the conflict flag catches them.
- Confirmed mappings become SQL that loads the warehouse, validated per column against the
  documented contract: 9,100 rows, 50 mapped columns, 0 violations. The range check catches a
  grams-into-kilograms load that type-checks and is wrong by three orders of magnitude.

## Measured results

| Evidence | Result |
|---|---|
| Test suite | 190 passed |
| Top-1 mapping accuracy | 51/54 (94.4%), 90% CI 88.9–98.2% |
| By tier | easy 5/5, medium 18/19, hard 16/16, trap 6/8, merge 2/2, no-source 4/4 |
| Calibration (pair level, held-out split) | ECE 0.0105 vs 0.2429 uncalibrated; Brier 0.014 vs 0.088 |
| Proposals at ≥90% confidence | 7 pairs, 100% correct |
| Errors inside the flagged set | 3/3 (100%), from 46% of proposals flagged |
| Wrong mappings auto-accepted without review | 0 of 29 |
| Review effort | 43% fewer column inspections (504 to 289) |
| Transform and load | 9,100 rows, 50 mapped columns, 0 contract violations |
| Mutation check | 30/30 mutants caught by a specific test |

The time claim is kept honest: action counts are measured, seconds per action are assumed, and the
headline is the breakeven — assisted wins whenever an inspection costs more than 1.3 seconds, and
the modelled band starts at ten.

## Tech stack

| Component | Choice |
|---|---|
| Corpus and warehouse | deterministic generator into SQLite, one seed |
| Evidence | three separated blocks: name, type, value distributions |
| Calibration | isotonic regression (PAV, Jeffreys-smoothed), held-out reporting |
| Name semantics | offline synonym matcher; optional Ollama / Gemini arms via LangChain |
| CLI and review UI | Typer commands plus a stdlib `http.server` review screen |
| Verification | mutation check (30 mutants) and CI steps parsed from the workflow YAML |
