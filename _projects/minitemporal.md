---
title: MiniTemporal
track: sde
order: 38
group: Durable and from-scratch systems
kind: Durable execution
repo: harsha-moparthy/minitemporal
description: >-
  A durable-execution engine (mini-Temporal) in ~2k lines of zero-dependency Go: workflows survive
  SIGKILL at any instant and resume at the exact step. A chaos suite killed the worker 30 times across
  100 executions and audited zero lost and zero duplicated external effects, with deterministic replay
  at ~200k events/s.
stack: [Go, JSONL, CRC32, fsync, Bash]
highlights:
  - value: "30"
    label: SIGKILLs across 100 chaos workflows
  - value: "0 / 0"
    label: lost / duplicated external effects
  - value: "~200k"
    label: events/s deterministic replay
  - value: "7"
    label: duplicate deliveries suppressed by idempotency
---

## Why this project exists

Modern workflows — especially agent workflows — run for minutes to days and must survive crashes and
deploys. Durable execution solves this by replaying an event-sourced history deterministically, and
building a small engine is the clearest proof of understanding the primitive. This one is ~2k lines
of stdlib-only Go: kill the worker anywhere, restart it, and the workflow function re-runs from the
top, consumes the recorded prefix instantly with no side effects, and continues from the first thing
history does not know about.

The interesting crash windows — killed after an effect happened but before its completion event,
killed mid-append (torn line), killed mid-timer — are enumerated in the design doc, and the chaos
suite exists to hit them for real.

## What it does

- Event-sources every execution to an append-only `history.jsonl` with a CRC per line and fsync per
  event, with torn-tail recovery on restart
- Workflow code is deterministic by contract: `ctx.ExecuteActivity`, `ctx.Sleep` (durable timers),
  `ctx.Now` / `ctx.RandomInt` (recorded, replayed verbatim), `ctx.GetVersion` (patch markers)
- Activities run at-least-once; external effects go through a provider idempotency key
  (`wf-id/seq`), so dedup at the provider makes effects effectively-once
- A `world.jsonl` effect ledger records every external effect, and the chaos suite audits it
  independently: exactly one completion per scheduled seq, exactly one committed effect per key
- Patch-marker versioning changes workflow code while executions are mid-flight: unmarked changes are
  detected as non-determinism and quarantined with histories untouched; marked changes resume old
  executions on the old path while fresh executions take the new one
- `mtctl` CLI to start workflows, inspect histories, and dump the effect ledger

## Measured results

Chaos suite: 10 seeds x 10 agent pipelines (LLM-call activities, a durable timer, a flaky activity,
an email and a chat-update effect), worker SIGKILLed after a random 60–400 ms until convergence, then
every history and the effect ledger audited.

| Evidence | Result |
|---|---|
| SIGKILLs / workflows | 30 kills across 100 executions |
| Lost external effects | **0** |
| Duplicated external effects | **0** |
| Duplicate deliveries suppressed by idempotency keys | **7** — proof the worst window (effect done, completion not recorded, worker killed) was actually hit |
| Byte-identical full replays | **100/100** |
| Versioning demo, wrong deploy (no marker) | detected as non-determinism; both executions quarantined, histories untouched |
| Versioning demo, right deploy (`GetVersion`) | old executions resume on the old path; fresh ones record the marker and take the new path |
| Replay latency, 100k-event history (17 MB) | load 210 ms, replay+verify 499 ms — linear, ~200k events/s |

The audit recomputes every expected result independently (the mock LLM is a pure function), which is
what lets "zero lost, zero duplicated" be a checked claim rather than an assertion. The linear replay
table is also the concrete argument for why real engines offer continue-as-new.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go, standard library only — the whole engine is ~2k lines |
| History | Append-only JSONL, CRC-checked per line, fsync per event, torn-tail recovery |
| Effects | Mock external provider with idempotency-key dedup and an audited ledger |
| Concurrency | One worker per store, enforced by a lockfile; single-writer history |
| Verification | Chaos runner, versioning demo, replay-latency bench — all scripted and committed |
