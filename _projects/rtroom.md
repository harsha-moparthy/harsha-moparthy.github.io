---
title: RTRoom
track: backend
order: 73
group: Realtime collaboration
kind: Multiplayer backend
repo: harsha-moparthy/rtroom
description: >-
  A multiplayer backend in zero-dependency Go: room-sharded WebSocket servers with a Redis
  backplane, per-connection coalescing that cuts wire bytes and backplane publishes 3.0x at a
  measured +30 ms p50, and presence that converges 1.83 s after a node is killed with no cleanup.
  Every durable update dropped under back-pressure — 759 of them — was accounted for by a resync;
  none was lost silently.
stack: [Go, RFC 6455 WebSocket, Redis, RESP2, Lua, Prometheus]
highlights:
  - value: "3.0×"
    label: fewer wire bytes and publishes, at +30 ms p50
  - value: "1.83 s"
    label: presence convergence after node kill, 2.2 s bound
  - value: "759/759"
    label: durable drops accounted for by resync
  - value: "27/27"
    label: backplane conformance tests, both implementations
---

## Why this project exists

Multiplayer became a default expectation — cursors, presence dots, live state — and it is sold as
infrastructure by Liveblocks, PartyKit, and Ably. The category is easy to fake: a demo that
broadcasts every cursor sample looks identical to a real system at three users and falls over at
fifty, because in-room fan-out is O(members²); presence built on disconnect events accumulates
ghost cursors after the first closed laptop lid; and a coalescer that quietly drops durable edits
alongside cursor samples destroys customer data with no error anywhere. Those three failures are
what the design commitments target, and the results report where they bite — including numbers
that came out worse than theory.

## What it does

- Separates ephemeral from durable traffic structurally: cursors are coalesced last-write-wins
  per (member, key) and shed silently; durable updates are never coalesced, are sequenced by a
  backplane-allocated per-room version, and trigger a resync when they cannot be delivered.
- Coalesces in two places: per-socket flushes on a tick, and backplane publishes at the tick rate
  rather than the client's send rate — 48,000 client samples became 16,066 publishes.
- Runs presence on leases with leaderless reaping: every node sweeps independently, removals are
  atomic Lua scripts, and both convergence bounds (read: lease; notify: lease + reap) are
  reported because they differ.
- Treats backplane outage as "we do not know", never as an empty room — joins are rejected with a
  retry hint while existing members' healthy sockets are retained.
- Defines backplane semantics once as 27 executable conformance subtests run against both the
  in-process and Redis implementations, so "tested offline, ships on Redis" stays true.

## Measured results

Apple M4 Pro, Go 1.26.5, in-process backplane over loopback; reproduces with `make bench`.

| Evidence | Result |
|---|---|
| Load: 200 connections, 20 rooms, 30 Hz, 6 s | 5,640 samples/s accepted; one-way propagation p99 76.1 ms; 0 errors, 0 sequence gaps, 0 durable drops |
| Coalescing A/B at 60 Hz (control is the same binary with tick 0) | publishes 48,000 → 16,066 (3.0×); wire bytes 37.2 → 12.4 MB (3.0×); +30.5 ms p50 vs a 25 ms theoretical floor. At 30 Hz the factor is 1.5× — it scales with send rate ÷ tick rate |
| Node killed with no cleanup | presence converged in 1,830 ms, inside the advertised 2,200 ms bound; 0 surviving clients disturbed |
| Slow consumer flooded with 400 durable + 400 presence updates | 397 presence samples shed silently (correct), 759 durable drops, every one accounted for by one of 5 resyncs |
| Fan-out sweep, 2 → 50 members per room | deliveries per sample track members − 1; p99 stayed flat at 71-77 ms, cost showed up as bandwidth |
| Backplane conformance | 27/27 subtests pass on both implementations, the Redis one against real Redis 8.10 |

Eleven documented bugs include a ten-byte frame that crashed the process remotely (integer
overflow in a bounds check, found by fuzzing in under 30 seconds), a Lua pattern that silently
misaligned every stored field, and a torn read of close codes found only by CI on Linux.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go 1.26, zero external dependencies (stdlib only) |
| Transport | Hand-rolled RFC 6455 WebSocket, server and client, fuzzed; bytes counted at the syscall boundary |
| Backplane | In-process, or Redis via hand-rolled RESP2 + pub/sub + 7 Lua scripts |
| Presence | Leases with batched renewal, leaderless reaping, two reported convergence bounds |
| Coalescing | Per-connection LWW map, deterministic 8-phase tick stagger, zero-allocation merge path |
| Metrics | Hand-rolled Prometheus exposition; typed labels only, so client input can never mint a series |
| CI | gofmt, vet, race, conformance suite, 2 fuzzers, end-to-end selfcheck |
