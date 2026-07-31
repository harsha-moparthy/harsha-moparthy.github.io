---
title: Meterd
track: backend
order: 62
group: Metering, billing, and payments
kind: Metering and billing
repo: harsha-moparthy/meterd
description: >-
  Usage metering and billing for AI products in zero-dependency Go: an idempotent event ledger,
  windowed aggregation with an explicit late-event policy, versioned plans with credits and caps,
  and ledger-replay reconciliation. A chaos harness delivered 292,792 events — duplicates,
  replays, global shuffle, 5% beyond grace, 1% dropped — and every cell, invoice, and gap
  reconciled exactly.
stack: [Go, HTTP, JSONL, CRC32-framed WAL]
highlights:
  - value: "292,792"
    label: chaos deliveries reconcile exactly
  - value: "19/19"
    label: billing scenarios vs hand-computed invoices
  - value: "50/50"
    label: corrupted cells caught by drift detection
  - value: "26,620"
    label: usage cells match ground truth both ways
---

## Why this project exists

AI products bill by usage — tokens, seats, agent runs — and a billing dispute is the new
production incident. Product services emit usage events with at-least-once delivery (duplicates
and replays), through queues (reordering and late arrival), over networks (gaps), and the
pipeline has to turn that into invoices that are exactly right, because "approximately right" is
a refund and an apology.

Two commitments drive everything: the append-only ledger is the only truth (every aggregate and
invoice is a deterministic pure function of it, diffed with zero tolerance), and billed exactly
once is a storage invariant, not a code path — dedup happens at the ledger, before anything else
sees the event.

## What it does

- Appends events to a length-and-CRC32-framed ledger with one fsync per batch; a crash mid-write
  leaves a torn tail that `Open` detects and truncates, verified by cutting the file at every
  byte offset.
- Applies an explicit window policy: events within a 2-hour grace fold into their true hourly
  window; later arrivals post to their arrival hour, flagged late, billed as an adjustment —
  never silently merged into a billed window, never dropped.
- Rates usage with versioned immutable plans, cumulative tiering that survives plan changes,
  credits applied earliest-expiry-first at finalization, and a gross spend cap applied before
  credits.
- Keeps all money as integer micro-dollars; rounding happens exactly once per tier line per
  invoice, and the arithmetic is verified against a `big.Rat` oracle on 200,000 random inputs.
- Reconciles by replaying the ledger through a fresh aggregator, diffing every cell in both
  directions and re-rating every invoice — clean means identical, not close.

## Measured results

| Evidence | Result |
|---|---|
| Chaos harness: 200k ground-truth events, 292,792 deliveries (94,751 dups/replays, shuffled, 5% beyond grace, 1% dropped) at ~111k deliveries/s | exactly 198,041 unique events accepted; 26,620 cells match ground truth both directions |
| Invoice recomputation from raw ledger, 50 customers | 50/50 match field-for-field |
| Dropped-event detection | 1,959/1,959 dropped events reported as sequence gaps, by number |
| 19-scenario billing suite (plan changes, tier boundaries, credits, caps, cross-period late arrivals) | 19/19 vs hand-computed invoices |
| Injected lost-update bug (every 1,000th aggregate apply silently dropped) | reconciliation flagged 50/50 corrupted cells; quantity delta exact (−53,703); under-billing pinned to 32,222 micro-dollars |

The drift result matters most operationally: the injected bug produces no errors and no latency
change — invoices simply come out low — which is exactly why a daily replay against the raw
ledger is the only structural defense.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go, zero external dependencies (stdlib only) |
| Ledger | Append-only, CRC-framed, fsync per batch, idempotency index rebuilt from the file on start |
| Windows | Hourly UTC by event time; pure function of (event time, ingest time, grace) |
| Rating | Versioned plans, cumulative tiers, credits, caps; rate then cap then credits |
| Money | Integer micro-dollars, half-up rounding once per tier line, `big.Rat` oracle-checked |
| Reconciler | Full ledger replay and two-way diff, zero tolerance |
| CI | Full suite including the chaos harness and drift demo on every push; hermetic, no docker |
