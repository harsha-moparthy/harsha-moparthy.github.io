---
title: PGLimits
track: backend
order: 66
group: Postgres as a platform
kind: Limits study
repo: harsha-moparthy/pglimits
description: >-
  An evidence-based limits study of "just use Postgres for everything": queue, full-text search,
  pub/sub, and vector workloads on one tuned Postgres 16 versus Redis, Elasticsearch, and Qdrant
  on identical data. SKIP LOCKED sustained 45-47k jobs/s against Redis's 8-11k, GIN beat
  Elasticsearch 22.9k to 15.2k qps, and interference was instrumented down to the autovacuum cycle.
stack: [Postgres 16, Go, Redis, Elasticsearch, Qdrant, pgvector]
highlights:
  - value: "45-47k"
    label: jobs/s SKIP LOCKED, vs 8-11k Redis pattern
  - value: "22.9k"
    label: FTS qps vs 15.2k Elasticsearch
  - value: "0.949"
    label: pgvector recall ceiling; Qdrant hit 0.994
  - value: "p99 328 ms"
    label: episodic autovacuum interference spike, root-caused
---

## Why this project exists

A strong current in backend architecture says: skip the queue service, the search engine, and the
vector database — Postgres does queues (`FOR UPDATE SKIP LOCKED`), full-text search (GIN +
`tsvector`), pub/sub (`LISTEN/NOTIFY`), and vectors (pgvector). The debate is loud and mostly
evidence-free. This repo measures where one tuned Postgres actually holds up, where it breaks,
and why — with dedicated systems run under equal tuning effort, and interference instrumented
down to root cause (dead tuples, autovacuum, WAL, buffer cache).

## What it does

- Runs four workloads against one tuned Postgres 16 (7 vCPU / 24 GB, tuned autovacuum, 4 GB
  shared_buffers) and dedicated baselines given the same care: pipelined Redis with the
  BLMOVE+LREM reliable-queue pattern, single-shard force-merged Elasticsearch, Qdrant with HNSW
  parameters matched to pgvector exactly.
- Indexes byte-identical, seeded synthetic datasets everywhere: a 200k-doc Zipf corpus over a 50k
  vocabulary and 200k Gaussian-clustered 384-dim vectors, with tokenization matched.
- Avoids coordinated omission: open-loop latencies are measured from each operation's intended
  send time, so server stalls show up as latency.
- Computes vector recall@10 exactly, against brute-force ground truth, for both systems at each ef
  setting — because matched-ef comparisons flatter pgvector.
- Reruns the search workloads while a two-phase queue churns ~40k jobs/s on the same instance,
  with a per-second sampler polling pg_stat internals so a p99 spike lines up against the exact
  second autovacuum kicked in.

## Measured results

| Evidence | Result |
|---|---|
| Job queue throughput (closed loop) | Postgres 45-47k jobs/s two-phase, 72k delete-mode; Redis reliable-queue pattern 8-11k |
| Job queue latency at a matched 5k jobs/s | p99 2.46 ms vs 2.35 ms — a tie; durable SQL queueing costs nothing extra at moderate rates |
| Full-text search, ranked 2-term AND, 200k docs | Postgres 22.9k qps p99 4.6 ms at 32 clients; Elasticsearch 15.2k qps p99 3.4 ms |
| Vector search at matched recall | pgvector 3.6k qps at recall 0.949, could not reach 0.97 in the sweep; Qdrant 4.7k qps at 0.968 and 3.9k at 0.994 |
| Pub/sub fan-out ×10 | Postgres ~11.7k msgs/s published (117k deliveries/s) p99 2.0 ms; Redis ~14.2k/142k p99 1.7 ms — 20%, not an order of magnitude |
| Interference under 40k jobs/s churn | usually +1-2 ms p99; one repeat hit p99 328 ms / max 796 ms, coinciding with an autovacuum cycle (dead tuples 376k→80k) at 1.0-1.5 GB/min WAL |

The interference finding is the honest shape of "one Postgres for everything": steady-state cost
is small, but vacuum debt from queue churn converts into episodic few-hundred-ms tail events for
every co-located workload — the line item that eventually forces the split.

## Tech stack

| Component | Choice |
|---|---|
| Primary system | Postgres 16, tuned (autovacuum naptime 10s, cost limit 2000, lz4 WAL compression, jit off) |
| Baselines | Redis 7 (pipelined, BLMOVE+LREM), Elasticsearch 8.13 (1 shard, force-merged), Qdrant 1.9 (matched HNSW) |
| Harness | Go CLI: queue, fts, vector, mixed-interference benchmarks plus report generation |
| Vector | pgvector 0.7 HNSW (m=16, ef_construction=64), exact ground-truth recall |
| Instrumentation | Per-second sampler over pg_stat_wal, pg_stat_database, dead tuples, bgwriter, live autovacuum workers |
| Reproducibility | Whole study reruns with three commands; raw JSON committed |
