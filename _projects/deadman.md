---
title: Deadman
track: hft
order: 54
group: Risk and surveillance
kind: Kill switch
repo: harsha-moparthy/deadman
description: >-
  A provably safe trading kill switch: a two-phase halt state machine model-checked in TLA+ so no
  order passes once the stop completes, and a Go core in one atomic word mirroring the spec
  action-for-action. Conformance tests replay all 23,240 model event sequences against the
  implementation, and the order-path enabled-check costs 0.39 ns.
stack: [Go, TLA+, TLC model checker, Go race detector]
highlights:
  - value: "23,240"
    label: event sequences replayed from the model's own graph
  - value: "0.39 ns"
    label: enabled-check, a single atomic load
  - value: "4 states"
    label: for TLC to refute the naive one-phase design
  - value: "54/54"
    label: labeled model edges covered by conformance tests
---

## Why this project exists

Knight Capital lost $460M in 45 minutes to a misdeployed router with no effective kill path. That
moved the frontier of trading risk from more checks to provable control: demonstrating that the
system that halts trading is itself correct under every interleaving of order flow, risk triggers,
and manual commands. The hard part is not flipping a flag — it is the race between a halt landing
and orders already in flight past the flag check.

## What it does

- The halt state machine is specified in 120 lines of TLA+ and model-checked by TLC for the
  no-order-after-halt invariant across every interleaving, plus liveness: a requested halt always
  completes
- TLC refutes the "obvious" one-phase design in four states: an order admitted before the halt hits
  the wire after the halt is declared complete. The fix is two-phase — `Halting` refuses all new
  admissions, and `Halted` is declared only when the in-flight count drains to zero
- The Go implementation mirrors the spec action-for-action inside a single atomic `uint64`: bits
  62-63 hold the state, bits 0-61 the in-flight count; every spec guard is one compare-and-swap
- The elegant bit: "Halting with zero in-flight" is exactly one word value, so the drain condition
  is the CAS's expected operand — there is no window between observed-drained and declared-halted
- Conformance tests parse TLC's dumped state graph (17 states, 54 labeled edges) and drive the
  implementation through it in both directions: match every predicted state, refuse every
  transition the model forbids
- Richer control-plane state (halt reason, timestamps, resume epoch) stays off the hot path behind
  a seqlock; readers never block writers and never see torn snapshots

## Measured results

| Evidence | Result |
|---|---|
| Exhaustive conformance replay | all **23,240** event sequences of length up to 8, verified exhaustive, **54/54** edge coverage |
| Deep conformance | 5,000 seeded random walks of 60 steps, reaching interleavings the bounded pass cannot |
| TLC vs the naive one-phase spec | refuted in **4 states** — the admitted order lands after "halt complete" |
| Enabled-check (one atomic load) | **0.39 ns** median, p99 0.61 ns — two orders of magnitude under the 100 ns target |
| Admit + done round trip (two CAS) | ~10 ns; ~49 ns with all 14 cores contending |
| Realistic order path, guarded vs bare | **~1-3 ns added**, bounded above by the ~10 ns isolated pair — reported as a bounded delta, not a point estimate |
| Race stress under the Go race detector | 8 goroutines vs landing halts across 200 halt/resume epochs: every send timestamp strictly below halt completion |
| Racing halt sources | 16 concurrent triggers x 100 epochs resolve to exactly one winner |

The proof's scope is stated as carefully as its result: TLC checks a finite 3-gateway model (the
design is symmetric in gateways and the guard is per-word), correspondence between spec and code is
structural rather than a machine-checked refinement, and the model covers the admission state
machine — it proves no order passes the switch after halt completion, not that your risk checks
are right.

## Tech stack

- TLA+ / TLC: two-phase spec with 3 invariants plus liveness, and a committed refutation of the
  naive design
- Go with zero dependencies: one atomic `uint64` plus a seqlock, race-detector-clean
- Model-based conformance testing driven by TLC's own state-graph dump
- CI re-runs TLC from the spec, re-dumps the graph, and replays conformance against the fresh dump,
  so committed artifacts cannot silently drift from the spec
