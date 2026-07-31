---
title: FieldSync
track: fde
order: 24
group: Documents and field data
kind: Field data sync
repo: harsha-moparthy/fieldsync
description: >-
  Offline-first field data capture with sync: per-field merge policies over a causal oplog,
  resumable media upload, and schema-version negotiation. Across 200 randomised offline-edit
  schedules this design loses nothing, while three control designs replaying the identical op log
  lose 1,255–1,340 pieces of inspection content and silently settle 279–436 professional
  disagreements by whichever clock ran fast.
stack: [Python, FastAPI, SQLite, IndexedDB, Hypothesis, Chromium]
highlights:
  - value: "0 / 0 / 0"
    label: content lost, corrections reverted, disagreements swallowed
  - value: "1,255–1,340"
    label: pieces lost by the control designs, same op log
  - value: "13/13"
    label: interrupted uploads resume byte-exact, 0 chunks wasted
  - value: "1.6 s"
    label: 20-device storm convergence, 1,500/1,500 ops durable
---

## Why this project exists

Offline sync is a problem everyone thinks they have solved with `updated_at` and a `MAX()`, and the
reason that keeps shipping is that its failures are invisible. The crew's tablet says the note is
there. The report does not have it. Nobody knows when it went missing, or which of two inspectors
was overruled by a clock that happened to be nine minutes fast. So this project makes that class of
failure visible and measurable, with three oracles — data loss, reverted corrections, swallowed
disagreements — and three control arms that are not strawmen. The strongest control commits zero
causal violations and still loses 1,338 pieces of content, because causal ordering gets you a
consistent answer, not the right one.

## What it does

- Records one content-addressed op per field edit — its id is the hash of its content, so
  retransmission through five flaky reconnects collapses on the primary key with no dedupe table.
- Commits ops durably before interpreting them: a future schema version or unknown field is
  deferred and recovered after a deploy, never rejected while the device has already cleared its
  outbox.
- Merges as a pure fold over the unordered op set with per-field policies — last-writer-wins,
  max-wins, append, OR-set, best-accuracy, and manual review, which emits a conflict rather than
  letting a fast clock settle a pass/fail disagreement.
- Ops carry declared causality: an op names the values it supersedes, which is the only sound way
  to tell "someone considered this and changed it" from "two people wrote without seeing each
  other".
- Resumes chunked media uploads from the server's own bitmap across every interruption boundary and
  both failure modes, including the lost-ack case a client-owned progress record cannot solve.
- Ships an installable, dependency-free PWA (IndexedDB, service worker) that reimplements the HLC
  format and op-id hash in JavaScript, with byte-identical digests verified against Python.

## Measured results

| Evidence | Result |
|---|---|
| Test suite (unit + property, real SQLite, real HTTP) | 127 passed, plus 7 browser tests in Chromium |
| Property suite over randomised schedules | 5,942 ops created, 5,942 durable, 0 unsynced; 0/200 failed to converge |
| This design — lost / reverted / swallowed | 0 / 0 / 0 across 200 schedules |
| Whole-record last-writer-wins control | 1,255 / 125 / 436 |
| Per-field wall-clock control | 1,340 / 86 / 308 |
| Per-field causal LWW control | 1,338 / 0 / 279 |
| Interrupted upload, 13 boundaries × 2 failure modes | 13/13 byte-exact resumes, 0 chunks wasted |
| 20-device reconnection storm | converged in 1.6 s, 1,500/1,500 ops durable, 1.4x over the serial control |
| Mixed-version fleet (v1 + v2 + v3 into one backend) | 13 ops, 2 deferred and recoverable, 0 lost |
| Mutation check | 22/22 caught, each by its named guard |

Driving the real browser found five genuine bugs invisible to 124 passing Python tests — including
a background sync that wiped a half-typed note. A system whose whole purpose is never losing a
field observation was losing them in the text box.

## Tech stack

| Component | Choice |
|---|---|
| Causal ordering | hybrid logical clocks; resolutions are ops that supersede candidates |
| Server | FastAPI over SQLite; durable-before-interpreted ingest, deferral, reprojection |
| Client | PWA with IndexedDB outbox and service worker; no framework, no build step |
| Media | chunked resumable upload; the server owns the progress bitmap |
| Property testing | Hypothesis-generated offline-edit schedules against three oracles |
| Browser suite | the shipped PWA driven in Chromium with the network genuinely down |
