---
title: PGShift
track: backend
order: 68
group: Postgres as a platform
kind: Schema migration
repo: harsha-moparthy/pgshift
description: >-
  Zero-downtime PostgreSQL schema migration in zero-dependency Go: expand, backfill, verify,
  cutover, contract, with cross-node verification fenced on xmin. It widens a write-hot 2M-row
  integer column to bigint holding its lock 3-4 ms for a 2.6-8.5 ms write stall, where the naive
  ALTER stalls every writer for 1,145 ms — and the fenced verifier avoided 20,000 lag-induced
  false alarms while catching all three injected faults.
stack: [Go, PostgreSQL 16, Streaming replication, SCRAM-SHA-256, PL/pgSQL]
highlights:
  - value: "3-4 ms"
    label: lock held at cutover, vs 1,145 ms naive stall
  - value: "20,000"
    label: lag false alarms fenced on a correct migration
  - value: "3/3"
    label: injected dual-write faults caught
  - value: "4/4"
    label: pre-contract phases roll back, catalog-verified
---

## Why this project exists

Changing a large table's column type without blocking production writes is unglamorous and
permanently in demand. The naive `ALTER TABLE ... TYPE` takes an ACCESS EXCLUSIVE lock and
rewrites the entire table under it — 1.1 seconds of total outage on the 2-million-row table
measured here, minutes on a real one. The safe alternative is the expand-and-contract dance, and
the engineering is in the parts that are silent when done wrong: dual-write correctness, the
cutover lock window, rollback that preserves data, and verification under concurrent writes.

The subtle problem is not torn reads. The operationally correct place to verify is a read
replica, and replicas lag: a verifier that compares primary to replica directly cries corruption
on every recently-written row. PGShift fences on `xmin`, the tuple version id Postgres replicates
physically — no comparison is evidence unless both nodes show the same tuple version, applied
symmetrically to equality and inequality.

## What it does

- Runs a phase-gated cycle — preflight, expand (shadow column plus trigger dual-write), throttled
  backfill, cross-node verify, rename cutover, contract — each a separate resumable command with
  persisted state.
- Bounds the cutover: a short `lock_timeout` with yield-and-retry means the worst a single attempt
  can cost writers is one timeout, and between attempts the table is completely free.
- Throttles the backfill on replication lag (18 back-offs held peak lag ~20% lower at a ~34%
  duration cost) so the standby stays a viable failover target.
- Rolls back from all four pre-contract phases, with a reverse trigger that preserves writes made
  after cutover.
- Hand-rolls the PostgreSQL v3 wire protocol including SCRAM-SHA-256 pinned to the RFC 7677
  vector, so per-statement latency measures the migration rather than a driver's re-prepare.

## Measured results

Apple M4 Pro, Go 1.26.5, PostgreSQL 16.14, primary plus streaming replica, fsync on, 16
connections at 3,000 writes/s throughout every phase.

| Evidence | Result |
|---|---|
| Naive `ALTER ... TYPE`, 2M rows, under load | 1,145 ms write stall, ~1,148 ms lock held — unavoidable |
| PGShift, same migration, same load | 2.6-8.5 ms stall uncontended, lock held 3-4 ms, 0 client errors, bigint confirmed in pg_catalog |
| Contended cutover | bounded by one 200 ms lock_timeout, then yield and retry |
| Verification, correct migration under induced lag | re-check verifier: 0 mismatches, 20,000 lagging rows fenced; single-pass control: 20,000 false alarms |
| Verification, 3 fault-injected triggers (skip UPDATE, lossy cast, dropped keys) | every genuine divergence caught (20,000 / 20,000 / 2,857 mismatches) |
| Backfill write impact | p99 1.21 ms vs 0.33 ms baseline; verify p99 1.49 ms (runs on the replica) |
| Rollback drills from expand, backfill, verify, cutover | schema clean per catalog, data preserved, post-cutover write survives via reverse trigger |

Thirteen documented bugs include a verifier that certified corrupt data when a stale replica
value coincided with the source (the fence now applies to equality too), and a cutover that held
its lock 40× longer than necessary because a PL/pgSQL function was compiled inside it.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go 1.26, zero external dependencies (stdlib only) |
| Wire protocol | Hand-rolled PostgreSQL v3: SCRAM-SHA-256 (RFC-pinned), extended query, COPY, cancel; fuzzed reader |
| Migration | Expand → backfill → verify → cutover → contract, phase-gated, state persisted in the database |
| Verification | Primary-source vs replica-shadow fenced on xmin; single-node intra-row fallback |
| Throttle | Multiplicative increase/decrease on replication lag and write p99 |
| Safety | lock_timeout with yield-and-retry on all DDL; catalog preflight guards; type allowlist |
| CI | gofmt, vet, race, fuzz, plus a job standing up a real primary+replica for the fault and rollback drills |
