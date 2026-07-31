---
title: Tailpipe
track: backend
order: 70
group: Multi-tenant data systems
kind: Telemetry pipeline
repo: harsha-moparthy/tailpipe
description: >-
  An OTLP trace collector for GenAI workloads in zero-dependency Go. Tail sampling kept 100.0000%
  of every must-keep class — error, high-cost, slow, flagged — verified per-trace over 800k+
  traces while cutting stored wire bytes 89.7%, and per-tenant AI spend reconciles exactly against
  the generator's ledger, to the picodollar, while absorbing 35,043 injected duplicate deliveries.
stack: [Go, OTLP/HTTP, OpenTelemetry GenAI semconv, JSONL, gzip, Prometheus]
highlights:
  - value: "100.0000%"
    label: must-keep retention, verified over 800k traces
  - value: "89.7%"
    label: wire-byte reduction (98.4% on disk)
  - value: "exact"
    label: per-tenant spend, to the picodollar
  - value: "45,644/s"
    label: unthrottled trace capacity (~167k spans/s)
---

## Why this project exists

AI spans are fat — a single LLM call carries its prompt and completion, routinely 10-100x the
bytes of an ordinary RPC span. Storing all of it blows up the telemetry bill; head-sampling 10%
throws away the one trace that mattered, because at decision time nobody knows yet whether the
trace will error, hang, or cost $4. The vendor fix is tail sampling: buffer spans per trace,
judge the finished trace, keep the interesting ones, meter what you kept per tenant. That
architecture is full of traps — the late error span, the retry that double-bills, the spend
dashboard that under-reports by the sampling rate, the prompt on disk for a tenant who never
consented — and this project attacks each with a verifier that fails the build if the claim does
not hold.

## What it does

- Meters every accepted span at ingest, before and independently of sampling — a spend dashboard
  computed from stored traces under 90% tail-drop under-reports the bill by roughly 90%.
- Deduplicates spend by (trace ID, span ID) over at-least-once OTLP delivery, and keeps all money
  as integer picodollars with inexact prices rejected at config load.
- Tail-samples with priorities: error, high-cost (using the same exact cost the ledger billed),
  slow, and flagged traces always kept; the boring majority kept at deterministic probability p.
- Handles the edges: late spans append to kept traces or salvage dropped ones when they carry an
  error; buffer overflow forces the oldest traces to decide early — everything counted, nothing
  silently discarded.
- Enforces per-tenant payload policies (raw / truncate / hash / drop, drop by default) before
  disk, then proves it: planted canary strings are scanned for in every storage segment, with
  raw tenants as the positive control proving the scanner works.

## Measured results

Apple M4 Pro (14 cores, 48 GB), Go 1.26.5; reproduce with `make bench`.

| Evidence | Result |
|---|---|
| Retention, sustained run of 180,150 traces | error 1,848/1,848, high-cost 3,588/3,588, slow 3,615/3,615, flagged 948/948 — 100.0000% each; identical across all four scenarios (800,604 traces) |
| Storage | 10.27% of traces kept, 89.7% wire-byte reduction; 98.4% on disk after segment gzip |
| Spend reconciliation | every tenant row and every (tenant, model) cell exact to the picodollar; 0 mismatched, 0 phantom; 35,043 duplicate deliveries absorbed |
| Sustained load | 3,000 traces/s (~11.6k spans/s) for 60 s at 7.4 ms p50 / 13.8 ms p99 per 50-trace batch, 0 shedding |
| Pressure scenario, deliberately undersized collector under a 12k traces/s flood | 12 shed batches, all retried, 0 give-ups, books still close exactly |
| Unthrottled capacity | 45,644 traces/s ≈ 167k spans/s on one workstation |
| Privacy leak scan | 0 canaries from protected tenants in any segment; raw-tenant canaries present as the positive control |

## Tech stack

| Component | Choice |
|---|---|
| Language | Go, zero external dependencies (stdlib only) |
| Protocol | OTLP/HTTP JSON with tolerant decoding (hex+base64 IDs, string+number int64s) |
| Semantics | OpenTelemetry GenAI semantic conventions, current plus deprecated names |
| Money | Integer picodollars; exactly-once accounting over at-least-once delivery |
| Sampler | Single-goroutine per-trace buffer: classes, late spans, salvage, bounded memory |
| Privacy | Per-tenant raw/truncate/hash/drop, applied post-decision, audited per (tenant, mode) |
| Storage | JSONL segments with gzip sealing; backpressure as bounded queues ending in 429 + Retry-After |
