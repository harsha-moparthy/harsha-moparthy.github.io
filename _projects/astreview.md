---
title: ASTReview
track: sde
order: 33
group: Coding-agent infrastructure
kind: Code review bot
repo: harsha-moparthy/astreview
description: >-
  An AST-aware AI code-review bot: tree-sitter semantic diffing classifies each change at the symbol
  level, rules catch the mechanical bug classes for zero tokens, and the LLM reviews only hunks that
  can contain a behavior bug. On the labeled corpus it scores 1.000 precision and 1.000 recall vs
  0.833 and 0.500 for a naive whole-diff baseline, with fewer LLM calls.
stack: [Python, tree-sitter, httpx, uv, pytest]
highlights:
  - value: "10/0"
    label: findings TP/FP, vs 5/1 for the baseline
  - value: "1.000"
    label: precision, vs 0.833 whole-diff baseline
  - value: "2x"
    label: recall, 1.000 vs 0.500 baseline
  - value: "8 vs 12"
    label: LLM calls — triage skips a third of spend
---

## Why this project exists

Line-diff prompting produces shallow review comments: the model sees hunks without structure and
pattern-matches on syntax. This bot reviews changes structurally — it classifies what changed at the
symbol level (signature vs behavior vs pure rename vs formatting), spends LLM budget only on hunks
that can actually contain a behavior bug, and filters anchors so a comment can never point at a line
the PR did not touch. The goal metric is the one that decides whether developers mute the bot:
false-positive rate.

## What it does

- Tree-sitter semantic diff classifies every symbol-level change: `signature_change`,
  `behavior_change`, `pure_rename`, `docstring_only`, `formatting_only`, `added`, `removed`
- Formatting vs behavior is decided on the AST, not text: bodies normalize to a comment-stripped
  structural token stream, so a Black-style reflow is `formatting_only` while `(a + b) * c` vs
  `a + b * c` is correctly a behavior change
- Renames are matched, not guessed: an added symbol counts as a rename only when signature and
  normalized body are both identical
- A rule engine (AST matchers on changed lines only) catches mutable-default-arg, bare-except,
  silent-except, eval/exec, `== None`, and `subprocess shell=True` for zero tokens, with high
  confidence by construction
- Hunk triage skips renames, docstring edits, reformatting, and test files before the LLM — every
  skip carries an explicit, unit-tested reason
- An anchor filter drops any LLM finding outside changed lines: a hallucinated location is a wrong
  finding, made impossible by construction
- Dedup (rule wins ties), suppression files, and a provider seam: mock, offline heuristic, or any
  OpenAI-compatible endpoint

## Measured results

Corpus: 12 PR-style cases — 8 with labeled bug lines and 4 benign honeypots (pure rename, formatting
reflow, docstring rewrite, test-only change) where any finding is a false positive. Benign cases
include pre-existing smells in unchanged context lines as bait. A finding is a true positive within
±2 lines of a label. Run offline with the deterministic provider, no API keys.

| Evidence | Result |
|---|---|
| Precision | **1.000** vs 0.833 naive whole-diff baseline |
| Recall | **1.000** vs 0.500 baseline |
| Findings (TP/FP) | **10/0** vs 5/1 |
| LLM calls | **8** vs 12 — triage skipped 4 hunks, a third of the spend |
| Tokens sent | 2112 vs 2448 |
| Test suite | 52 tests pass |

Where the delta comes from, mechanically: the baseline's false positives are context-line comments
(the whole-diff prompt shows unchanged lines and the reviewer comments on them — the anchor filter
makes that impossible); the baseline's misses are the mechanical classes (mutable defaults, `eval`,
`shell=True`, `== None`) that rules catch deterministically and a one-shot prompt does not.

Honesty notes preserved from the project: the offline provider is a deterministic stand-in so CI is
reproducible with zero keys; numbers with a real model will differ. The corpus is small and
self-built — the harness is the point, and the same pipeline runs against real git ranges.

## Tech stack

| Component | Choice |
|---|---|
| Parsing and semantic diff | tree-sitter symbol extraction, AST normalization, change classification |
| Rules | AST matchers reporting on changed lines only |
| LLM seam | mock / offline heuristic / OpenAI-compatible endpoint via httpx |
| Evaluation | 12-case labeled corpus, TP/FP scoring, pipeline-vs-baseline harness |
| Runtime | Python 3.12+, uv — tree-sitter and httpx are the only runtime deps |
