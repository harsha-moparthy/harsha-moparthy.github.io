---
title: PGSieve
track: backend
order: 67
group: Postgres as a platform
kind: Sync backend
repo: harsha-moparthy/pgsieve
description: >-
  A permission-scoped sync backend on Postgres logical replication: clients subscribe as a user
  and get a snapshot plus a live stream containing only rows that user may see, with grants and
  revokes enforced in the replication path itself. A 19-test leak suite including 30-cycle
  revocation races converged exactly to SQL ground truth, and fan-out runs at 1.61 ms p50 to 100
  subscribers.
stack: [Go, Postgres 16, Logical replication, pgoutput, SSE]
highlights:
  - value: "0 leaks"
    label: 19-test suite under -race, incl. revocation races
  - value: "13,028"
    label: events in the race hammer, all authorized
  - value: "1.61 ms"
    label: p50 write-to-client, 100 subscribers
  - value: "75k/s"
    label: peak deliveries at 2,500 subscribers
---

## Why this project exists

This is the query-subscription problem ElectricSQL, Rocicorp Zero, and PowerSync are racing to
solve: serving partial database replicas to many clients, keeping them live from a change stream,
and never leaking a row. Scoping the initial snapshot is easy — it is a SQL join. The hard parts
are all in the live path: a write to a membership table changes which rows a client can see, so a
grant must synthesize inserts and a revoke synthetic deletes; a revoke committed while writes are
in flight must not let a single row slip through; and snapshots query "now" while the engine is at
an older stream position.

## What it does

- Serializes everything through one matcher goroutine that owns the membership index and all
  subscriber shapes, processing replication changes and subscribe commands as points on one total
  order — permission changes and data changes cannot race because the WAL orders them.
- Seeds the membership index under the replication slot's exported snapshot, so the index and the
  stream start are exactly aligned.
- Joins snapshot and stream by idempotence: changes in the overlap window apply twice, safely,
  because upserts are idempotent by key and removes of absent keys are no-ops.
- Tracks each subscriber's exact row set (table, pk, scope), so a revoke emits precise synthetic
  deletes and a deletion goes only to subscribers who hold the row.
- Backstops authorization explicitly: every emitted upsert is checked against the index at that
  stream position, with a counter that must stay zero — and in connect-time races it fires and
  suppresses rows the stream has not authorized yet, which are re-delivered when the grant arrives.

## Measured results

Apple M-series laptop, scratch Postgres 16, real HTTP/SSE over loopback; latency is end-to-end
from the writer's INSERT call to subscriber receipt.

| Evidence | Result |
|---|---|
| Fan-out, one write to N subscribers | 100 subs: 1.61 ms p50 / 3.38 ms p99; 1,000 subs: 6.45 ms p50; peak ~75k deliveries/s at 2,500 subs |
| Sharded: 1,000 users each watching their own project, 5,000 writes | p50 1.31 ms end-to-end |
| Revocation-race hammer: 30 grant/revoke cycles under continuous contested writes | 13,028 events delivered, zero task upserts while the project was invisible, final state equal to SQL ground truth |
| Post-revocation quiescence | writes to a revoked project produce zero events at the revoked client |
| Subscribe mid-storm (3 concurrent writers) | client converges to exactly the SQL-visible row set |
| Leak suite | 19 tests, all passing under -race; unauthorized_drops stayed 0 throughout |

## Tech stack

| Component | Choice |
|---|---|
| Language | Go |
| Change source | Postgres 16 logical replication (pgoutput), REPLICA IDENTITY FULL for scope-move detection |
| Engine | Single serialized matcher: membership index, shape tracking, synthetic grant/revoke events |
| Transport | SSE with per-subscriber pending buffers; batches grow under load, flush immediately when idle |
| Consistency | Exported-snapshot seeding; idempotent snapshot/stream join |
| Testing | Hermetic scratch-Postgres harness (initdb per run), 19-test e2e leak suite |
