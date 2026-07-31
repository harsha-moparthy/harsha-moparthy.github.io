---
title: TenantVec
track: backend
order: 69
group: Multi-tenant data systems
kind: Vector search
repo: harsha-moparthy/tenantvec
description: >-
  Multi-tenant vector search over object storage in the style of turbopuffer: object storage is
  the source of truth, disk and RAM are caches, and namespaces move between tiers by use. 240
  tenants and 840k vectors served ~4,750 queries/s with zero errors and zero cross-tenant leaks in
  a 12,000-result scan, at 0.08 ms hot / 17.4 ms warm / 30.9 ms cold server p50.
stack: [Go, hnswdb, MinIO/S3, SigV4, Object storage WAL]
highlights:
  - value: "0.08/17/31 ms"
    label: hot/warm/cold tier server p50
  - value: "240 / 840k"
    label: tenants / vectors at ~4.7k qps, 0 errors
  - value: "0 leaks"
    label: 12,000-result cross-tenant scan
  - value: "128 MiB"
    label: hot-tier cap, ~a third of fleet index bytes
---

## Why this project exists

Every AI product embeds and searches customer data, and the economics pushed vector search toward
object-storage-backed designs: cold namespaces cost almost nothing to keep, warm ones serve fast.
The interesting engineering is not the ANN algorithm (that lives in hnswdb, a separate
from-scratch HNSW project); it is the multi-tenant machinery around it — durability without a
database, tier lifecycle, strict isolation, and noisy-neighbor control.

## What it does

- Acknowledges an upsert only after the batch is written as a WAL object to object storage; the
  memtable is a replayable view of the WAL tail, so acknowledged writes survive a process kill
  with a wiped local cache (tested).
- Folds memtables into per-tenant HNSW snapshots in background merges scheduled tenant-fair, then
  garbage-collects the covered WAL prefix; namespaces promote on demand and evict LRU under
  explicit memory and disk byte budgets.
- Makes isolation structural: tenant identity comes only from the bearer token and namespace keys
  are tenant-prefixed, so no request can even name another tenant's data — and foreign probes get
  404, not 403, so existence itself is not leaked.
- Contains noisy neighbors with per-tenant token buckets on writes and semaphores on query
  concurrency, checked before body decode so rejected floods cost almost nothing.
- Pins promotions: the query that pays for a promotion holds a pin so LRU eviction cannot take
  the index away before that query runs — a fix for a real thrashing failure found under budget
  pressure.

## Measured results

Apple M-series laptop against local MinIO over the hand-rolled SigV4 client; zipf-skewed traffic.

| Evidence | Result |
|---|---|
| Fleet load: 240 tenants, 840k vectors, ~4,750 queries/s | hot p50 0.08 ms / p99 3.2 ms; warm p50 17.4 ms; cold p50 30.9 ms; zero errors |
| Isolation scan | 12,000 result IDs across all 240 tenants, 0 leaks; probe suite covers read, write, delete, and detection |
| Cold-start promotion (8,000-vector namespace) | fetch p50 5.7 ms + decode 6.7 ms; hot queries 0.85 ms after promotion |
| Noisy neighbor, 60 s flood with admission on | 640 flood batches admitted, 63,158 typed 429s; victims p99 95 ms; flooding tenant back to ~1 ms 30 s later |
| Same flood, admission off | 2.01M vectors ingested; the flooder's own queries degrade to 720-915 ms — the blast radius stays contained structurally |
| Durability | acknowledged writes, deletes, and tags survive restart replayed purely from object storage |
| S3 client | SigV4 signer reproduces both official AWS test vectors byte-for-byte; conformance suite passes against live MinIO |

## Tech stack

| Component | Choice |
|---|---|
| Language | Go; only dependency is hnswdb (the author's from-scratch HNSW index) |
| Storage | S3/MinIO or filesystem: per-tenant WAL objects, snapshots, manifests |
| S3 client | Hand-rolled SigV4, pinned to AWS documentation test vectors |
| Tiering | Hot (RAM) / warm (disk cache) / cold (object storage), LRU under byte budgets, pinned promotion |
| Query | Sealed HNSW merged with a memtable scan that shadows it; metric-consistent distances |
| Admission | Per-tenant token buckets and query semaphores, checked before decode |
