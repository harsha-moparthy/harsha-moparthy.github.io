---
title: RepoCtx
track: sde
order: 32
group: Coding-agent infrastructure
kind: Context engine
repo: harsha-moparthy/repoctx
description: >-
  A repository context engine for coding agents: tree-sitter symbol chunking, hybrid BM25 + dense +
  call-graph retrieval, and a hard token-budget packer — evaluated on 50 tasks mined from real merged
  PRs. 0.907 recall@16k vs 0.825 single-strategy, and the same 8B agent's file recall jumps 3.4x when
  the engine fills the window.
stack: [Python, tree-sitter, BM25, Ollama, nomic-embed-text, uv]
highlights:
  - value: "0.907"
    label: recall@16k, hybrid + graph, vs 0.825 BM25
  - value: "3.4x"
    label: agent file recall, 0.703 vs 0.205 without
  - value: "86%"
    label: task hit rate, vs 32% without engine
  - value: "63 ms"
    label: p50 full query path, p95 91 ms
---

## Why this project exists

Coding agents live or die by what code they can see. Paste the wrong files into the window and the
agent hallucinates APIs; miss the relevant helper and it reinvents it, badly. Retrieving the right
context from a large repository is the core infrastructure problem behind every AI coding tool, and
it is usually solved with the recipe used for prose — character-window chunks and an embedding index —
even though code has structure that recipe throws away.

Retrieval demos are easy to fake, so two design moves keep this honest. Ground truth is what humans
actually changed: 50 merged PRs from flask, click, httpx, rich, and jinja, with the task text stripped
of paths, code blocks, and URLs so it cannot leak its own answer, and the engine indexing the repo
exactly as it stood one commit before the merge. And every number has a baseline next to it — four
retrieval arms are reported so the marginal value of each signal is visible, including where it is zero.

## What it does

- Chunks are symbols, not character windows: a tree-sitter pass extracts every function, method,
  class, and module header with signature, docstring, span, outgoing calls, and types
- Relevance is three signals: BM25 with identifier-aware tokenization (`load config` reaches both
  `load_config` and `ConfigLoader`), embeddings over signature+docstring+body, and an import/call
  graph that pulls in the callees and types of whatever the first two signals found
- Fusion is reciprocal-rank (RRF), not score interpolation — BM25 scores and cosine similarities live
  on incomparable scales
- Graph edges resolve conservatively: an ambiguous name produces no edge, because a wrong edge
  poisons expansion worse than a missing one
- The window is a budget, not a hope: the packer picks per-symbol granularity (full body if it fits,
  signature+docstring stub if not) and the hard budget is an invariant enforced by test
- Embeddings are cached by content hash, so ten snapshots of the same repo embed each unchanged
  symbol once

## Measured results

Recall@budget = fraction of ground-truth files present in the packed context, 50 tasks.

| Evidence | Result |
|---|---|
| Hybrid + graph, recall@16k | **0.907** vs 0.825 BM25-only, 0.805 dense-only |
| Hybrid + graph, recall@2k (tight budget) | **0.703** — best arm, +0.025 over plain hybrid |
| Hybrid (RRF), recall@8k | 0.848 — graph expansion *costs* recall here (0.818), reported anyway |
| Query latency (retrieve, fuse, expand, pack) | **p50 63 ms / p95 91 ms**; 8.4 ms for BM25 alone |
| Agent eval with engine (qwen3:8b, 4k budget) | **0.703 mean file recall, 86% task hit rate** |
| Agent eval without engine (file tree + README head) | 0.205 mean file recall, 32% hit rate — a 3.4x delta |
| Incremental indexing | rich (~8k symbols) cold: 58 s; subsequent snapshots under 1 s |
| Hermetic tests | 25 pass without Ollama, via injected embedder and token counter |

The 8B model was chosen small on purpose: it has no memorized knowledge of these repos to fall back
on, so the delta measures the context, not the model. Single signals plateau (BM25 at 0.825, dense at
0.805) while fusion keeps climbing — the two signals fail on different tasks, which is the whole
argument for fusion.

## Tech stack

| Component | Choice |
|---|---|
| Chunking | tree-sitter symbol extraction (functions, methods, classes, module headers) |
| Lexical retrieval | from-scratch BM25 with identifier-aware tokenization |
| Dense retrieval | nomic-embed-text via Ollama, content-hash disk cache, injectable embedder |
| Graph | import/call/type edges with decayed 1-hop expansion |
| Fusion | weighted reciprocal-rank fusion |
| Packing | hard o200k token budget with granularity degradation |
| Benchmark | 50 PR-mined tasks from flask, click, httpx, rich, jinja |
