---
title: TPMGate
track: backend
order: 60
group: Serving AI traffic
kind: Rate limiter
repo: harsha-moparthy/tpmgate
description: >-
  A distributed token-based rate limiter for AI APIs in zero-dependency Go on Redis, including a
  hand-rolled RESP client. Admission spends an estimate inside an atomic Lua script and settles
  against the true cost: three independent nodes firing 20,000 concurrent requests at a bucket that
  fits 2,000 admit exactly 2,000, and the decision ledger reconciles 120 of 120 rows against the
  provider log with no tolerance term.
stack: [Go, Redis, Lua, RESP2/RESP3, Prometheus]
highlights:
  - value: "2,000/2,000"
    label: admitted from 20k concurrent, 3 nodes
  - value: "0"
    label: over-admissions, zero errors
  - value: "120/120"
    label: ledger rows reconcile, no tolerance
  - value: "<0.02 ms"
    label: enforcement cost above a bare Redis PING
---

## Why this project exists

Classic rate limiting counts requests, but two calls to an LLM API can differ in cost by three
orders of magnitude — the scarce resource is tokens. Limiting on tokens introduces a problem
request counting never had: at admission time the request's cost is unknowable, because the
completion does not exist yet. Enforcement therefore has to be estimate, reserve, run, settle
against the truth, and every hard property here is a property of that loop.

It is also the direct answer to its sibling llmgw's stated limitation that all enforcement state
was per-process: this moves reservations to Redis, done and measured across three nodes.

## What it does

- Evaluates every enforcement decision as one atomic Redis Lua script, so the read ("is there
  room?") and the write ("take it") cannot race: N callers racing for room that fits K admit
  exactly K, guaranteed rather than bounded.
- Carries under-estimation as debt: a completion that runs long has its shortfall taken from the
  tenant's bucket at settlement, driving it negative until refill clears it — which bounds any
  overshoot to one window instead of forgiving it forever.
- Uses a hand-rolled RESP2/RESP3 client where any protocol desync poisons the connection, making
  it structurally impossible for one tenant to receive another tenant's admission decision.
- Works in scaled integer units chosen to stay below Lua 5.1's 2^53 float precision boundary;
  configs that would breach it are rejected at load (that check rejected two of the project's own
  benchmark configs on first run).
- Adds a start-time fair-queueing waiting room, idempotent settlement, and crash recovery via
  bounded lazy sweeps on the admission path itself — no daemon required.

## Measured results

Apple M4 Pro, Go 1.26.5, Redis 8.10.0 over loopback; every figure reproduces with `make bench`.

| Evidence | Result |
|---|---|
| 20,000 concurrent attempts, 3 independent limiter nodes, capacity 2,000 | exactly 2,000 admitted, 0 over-admitted, 0 errors |
| Adversarial suite: max-size bursts, long streams, sustained 10× under-estimation, retry storms | every scenario at or under 1.00× of the configured limit |
| 200 settlements replayed against already-settled reservations | 0 wrongly applied |
| Decision ledger vs independent provider usage log | 120/120 exact, 0 mismatches, 0 orphans, no tolerance parameter anywhere |
| Enforcement script overhead vs bare Redis PING on the same pool | under 0.02 ms p50 |
| 5,000 abandoned holds after a node crash | 5,000 reclaimed in 7.1 ms, bucket fully recovered |
| Weighted fairness under scarcity (weight 8 vs weight 1) | 18/2 of 20 slots; a large request waited 27 ms while 56,181 small requests were admitted |

Ten documented bugs include a fair-queueing weight that had no measurable effect (a units error
found only by measuring), a duplicate request id that could release another request's live
reservation, and a test of the author's own that used the exact epsilon the project criticizes.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go 1.26, zero external dependencies (stdlib only) |
| Enforcement | Redis 7+ Lua scripts via EVALSHA with NOSCRIPT reload-and-retry |
| Redis client | Hand-rolled RESP2/RESP3 codec and pool; desync poisoning is structural; fuzzed |
| Bucket | Token bucket in scaled integer units, server-authoritative Redis TIME clock |
| Accounting | Estimate, reserve, settle; idempotent, debt-carrying true-up |
| Waiting room | Start-time fair queueing on a virtual clock, weighted per tier |
| Metrics | Hand-rolled Prometheus exposition with bounded label cardinality |
