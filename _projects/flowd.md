---
title: Flowd
track: backend
order: 64
group: Durable execution and sandboxing
kind: Durable execution
repo: harsha-moparthy/flowd
description: >-
  A durable-execution backend for agent workflows in zero-dependency Go: an event-sourced control
  plane with task leases, durable timers, and human signals, plus stateless replay workers. A chaos
  suite ran 300 executions through 165 worker SIGKILLs, 20 server SIGKILLs, and 10 rolling deploys
  mid-execution with zero lost and zero duplicated external effects.
stack: [Go, Event sourcing, JSONL WAL, HTTP, Deterministic replay]
highlights:
  - value: "0 / 0"
    label: lost / duplicated effects under chaos
  - value: "165 + 20"
    label: worker and server SIGKILLs survived
  - value: "300/300"
    label: histories byte-consistent under strict replay
  - value: "10"
    label: rolling v1→v2 deploys with executions in flight
---

## Why this project exists

Agent workflows run for hours, mix LLM calls with tool calls, and park on human approvals that
arrive days later — while workers get deployed and machines die. Durable execution (Temporal,
Restate, Inngest) solves this by replaying an event-sourced history; this project builds the
backend-service version of that primitive, where the interesting problems are worker/server
separation, lease-based redelivery, zombie fencing, signal idempotency, and deploy versioning —
not just the replay loop.

## What it does

- Keeps workers stateless: a task is "fetch history, replay deterministic code from the top, post
  the one decision history doesn't know about." Any worker — including a newer build after a
  server restart — re-derives a parked wait from history alone.
- Fences zombies: every decision carries `based_on` (the history length it replayed), and the
  server drops anything based on a stale prefix, so a worker whose lease expired cannot corrupt
  the run.
- Appends per-execution histories as CRC-checked, fsync'd JSONL with torn-tail recovery; signals
  dedupe by sender-chosen `signal_id`.
- Versions deploys with `GetVersion` guards: in-flight executions keep the old code path, new ones
  take the new path with a version marker, and the same change deployed without a guard is
  detected as nondeterminism and quarantined with history untouched.
- Routes all external effects through idempotency-keyed activities against a mock world whose
  ledger the chaos audit recomputes from first principles.

## Measured results

10 seeds × 30 agent-pipeline executions: workers SIGKILLed every 300–700 ms, the server SIGKILLed
twice per run, a rolling v1→v2 deploy with 55 executions in flight, ~20% of approvals withheld
until after the full fleet and server were replaced, ~15% delivered twice, and a world failing
~1/3 of first deliveries.

| Evidence | Result |
|---|---|
| External effects, audited against the world's ledger | 0 lost, 0 duplicated across 300 executions |
| Duplicate deliveries absorbed by idempotency keys | 10 — proof the worst crash window (effect committed, worker killed before reporting) was hit and handled |
| Strict deterministic replays | 300/300 byte-consistent, 0 quarantines |
| Deploy semantics | 210 executions kept the old path, 43 took the new; path ⇔ marker checked on every history |
| Delayed signal demo | approval delivered after worker and server SIGKILL plus a fleet upgrade resumed the run at event 6 of 24 |
| Load: 2,000 executions parked on approval | stats API 0.35 ms p50 / 1.2 ms p99 at peak occupancy; backlog drained at ~56 completions/s, bounded by per-event fsync |

## Tech stack

| Component | Choice |
|---|---|
| Language | Go, zero external dependencies (stdlib only) |
| History | Append-only, CRC-checked JSONL, fsync per event, torn-tail recovery |
| Replay | Deterministic workflow code: no `time.Now`, no `math/rand`, no I/O — injected via context |
| Dispatch | Lease-based task delivery with expiry redelivery; stale decisions fenced by `based_on` |
| Signals | Deduped by `signal_id`; waits are pure functions of history |
| Versioning | `GetVersion` markers; wrong deploys quarantined, not corrupted |
| Evidence | Chaos suite (10 seeds), rolling-deploy and delayed-signal demos, all run in CI |
