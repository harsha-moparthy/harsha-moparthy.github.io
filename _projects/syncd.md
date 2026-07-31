---
title: Syncd
track: sde
order: 39
group: Durable and from-scratch systems
kind: Sync engine
repo: harsha-moparthy/syncd
description: >-
  A local-first sync engine — server-authoritative mutation log with client rebase and
  permission-scoped partial replication — in ~1.8k lines of zero-dependency TypeScript. Property-tested,
  not asserted: 400/400 concurrent-edit schedules converge byte-for-byte, and 11,144 replicated rows
  audited against an independent permission oracle show 0 leaks.
stack: [TypeScript, Bun, SSE, HTTP, localStorage]
highlights:
  - value: "400/400"
    label: concurrent-edit schedules converge byte-for-byte
  - value: "0 leaks"
    label: 11,144 replicated rows audited vs oracle
  - value: "10.6 ms"
    label: p50 cross-client sync latency
  - value: "4.6x"
    label: fewer pokes under a 100-client storm
---

## Why this project exists

Linear-style local-first: reads never touch the network (the UI reads a local replica), writes apply
optimistically and sync in the background. The engine is a server-authoritative mutation log with
client rebase — the Linear/Replicache/Zero model — rather than a CRDT store. The deciding factor is
that per-user visibility needs an authority anyway: revocation must actually remove rows from
replicas, and "the server said no" has no CRDT analogue.

The same mutator code runs three ways — optimistically on the client, authoritatively on the server,
and as the rebase replayer — so conflict semantics ("move of a deleted card is a no-op") are ordinary
application `if`s, written once.

## What it does

- Client view = `rebase(pending, snapshot)`: mutations apply instantly and locally, push in the
  background with `(clientID, seq)` dedup, and rebase over the server-ordered log on pull
- Partial replication via client view records (CVR): each pull computes the permission-filtered
  visible set server-side and diffs it against exactly what this client was last sent — `put`s can
  only come from the visible set, and anything no longer visible (deleted, revoked, unsubscribed)
  becomes a `del`
- Subscriptions narrow the replica further and are enforced server-side, never by client goodwill
- SSE pokes are hints only ("sync soon"), coalesced with jitter and per-client token buckets;
  correctness never depends on them
- Offline mode: the pending queue persists across app restarts, conflicting offline edits merge to
  server order, and a crash-retry double push applies exactly once
- A kanban demo runs two users side by side, including an offline toggle and a `mallory` user who
  gets an empty replica because the server never replicates rows she cannot see

## Measured results

All suites regenerate from a script and run in CI on every push.

| Evidence | Result |
|---|---|
| Convergence suite: 400 random schedules, 22,451 mutations, offline windows, membership churn | **400/400 converge byte-for-byte**, 1,422 replicas checked; quiescent pulls always empty |
| Zero-leak suite: 300 adversarial schedules, 2,567 forged foreign-board writes | **0 leaks** across 11,144 rows and 4,400 pulls audited against an independent permission oracle |
| Revocation | provably removes every row of the board from the replica on the next pull |
| Crash-retry double push | applies **exactly once** |
| Sync latency (mutate on A, visible on B; HTTP + SSE, localhost, n=300) | **p50 10.6 ms / p95 18.4 ms / p99 29.1 ms** |
| 100-client storm, 60-mutation burst | pokes 3,232 → **707** (4.6x), pulls 2,272 → **510** (4.5x), fleet converges **1.7x faster** (1,315 → 765 ms) |
| Full-fleet reconnect after an offline burst | ~one pull per client — the CVR sends the net delta, never the log |
| Suite validation | 4 deliberately seeded bugs (revocation off, rebase off, filter removed, dedup removed) — each caught by named tests |

The mutation-testing step matters: a test suite that never fails proves nothing, so the engine was
deliberately broken four ways and each break had to be caught.

## Tech stack

| Component | Choice |
|---|---|
| Language | TypeScript, ~1.8k lines, zero runtime dependencies |
| Runtime and tooling | Bun: tests, typecheck, bundling, serving |
| Transport | HTTP push/pull plus SSE pokes with coalescing, jitter, token buckets |
| Server | Versioned row store, mutation log, CVR-diffed pulls, permission checks in mutators |
| Client | Snapshot + pending queue + rebase, persisted to localStorage in the demo |
| Verification | Deterministic sim harness, property suites, real-HTTP benches, permission oracle |
