---
title: HNSWdb
track: sde
order: 40
group: Durable and from-scratch systems
kind: Vector database
repo: harsha-moparthy/hnswdb
description: >-
  A vector database from scratch in zero-dependency Go: HNSW index plus filtered search with
  cost-based strategy switching, benchmarked against exact ground truth on SIFT1M. 0.994 recall@10 at
  1.8 ms p50, ~100x faster than brute force at 0.97 recall, and an auto filter planner 2,500x faster
  than fixed graph traversal at 0.1% selectivity.
stack: [Go, HNSW, HTTP, SIFT1M, Make]
highlights:
  - value: "0.994"
    label: recall@10 at 1.8 ms p50, SIFT1M
  - value: "~100x"
    label: vs exact scan (~81 ms) at 0.97 recall
  - value: "2,500x"
    label: auto planner vs fixed traversal at 0.1% selectivity
  - value: "127 s"
    label: to build 1M vectors, ~7,900 vec/s
---

## Why this project exists

Vector search sits under every RAG and memory system, and the hard part is not the textbook index —
it is filtered search ("nearest neighbors where tenant = X and year > Y"), which breaks naive HNSW at
both ends of the selectivity spectrum: pre-filtering strands the beam when few nodes match, and
post-filtering throws away almost all its work. This repo implements the index from scratch and
treats filtered search as a query planning problem, with measurements against exact brute-force
ground truth backing every claim.

## What it does

- HNSW index in stdlib-only Go: lock-free reads via chunked storage behind an atomic snapshot
  pointer, per-node RWMutex neighbor lists, pooled epoch visited-sets — parallel build plus
  concurrent search/delete pass the race detector
- Neighbor selection uses the paper's pruning heuristic (Algorithm 4), which keeps the graph
  navigable; plain closest-M selection clusters edges and quietly wrecks recall
- Filtered search with three execution strategies — brute force over matches, filtered traversal,
  post-filter — and a cost-based `auto` switch; because match bitmaps come from inverted metadata
  indexes, selectivity is known exactly before choosing, no cardinality estimation involved
- Deletions are tombstones (removing edges would fracture the graph) with a parallel rebuild
  compaction path
- Binary snapshots for persistence, and an HTTP API with collections, metadata filters (`eq`, `in`,
  numeric ranges under `must`), forced or automatic strategy, compaction, and snapshots

## Measured results

SIFT1M (1M x 128d), Apple M4 Pro, single-threaded queries, ground truth from the dataset's official
files.

| Evidence | Result |
|---|---|
| Recall@10 at M=16, efSearch=200 | **0.994** at p50 1.8 ms (519 QPS) |
| Recall@10 at M=16, efSearch=80 | 0.971 at p50 0.76 ms — **~100x faster** than the 81 ms exact scan |
| Best measured operating point | 0.998 recall at p50 2.8 ms (M=32, efSearch=400) |
| Build | 1M vectors in **127 s** (~7,900 vec/s), 14 parallel workers |
| Filter planner at 0.1% selectivity | auto picks brute force: 0.08 ms vs 208 ms fixed traversal — **2,500x** |
| Filter planner across 0.1%–90% selectivity | within ~25% of the per-point winner everywhere except 90%, where it pays 2x latency for post-filter's higher recall (0.996 vs 0.988) |
| Filtered recall floor | every strategy holds recall >= 0.987 |
| Deletions | recall stays healthy to 50% tombstones but p50 grows 2.6x (0.56 → 1.44 ms); a 56 s rebuild restores 0.83 ms — why real vector databases compact |

The strategy-switch thresholds (5%, 50%) come from the measured crossovers, not guesses: brute force
costs exactly `matchCount` distance computations, graph traversal roughly `ef*M/selectivity`.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go, standard library only |
| Index | HNSW with heuristic neighbor pruning, tombstone deletes, compaction |
| Concurrency | Atomic snapshot pointer, copy-on-write growth, `-race`-clean |
| Filters | Inverted metadata indexes producing exact match bitmaps |
| API | HTTP: collections, upserts, filtered search reporting the executed strategy |
| Benchmarks | SIFT1M recall/latency grid, filter-strategy sweep, deletion study — all committed as CSV |
