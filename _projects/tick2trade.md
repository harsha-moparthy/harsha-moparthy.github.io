---
title: Tick2Trade
track: hft
order: 45
group: Tick-to-trade and matching
kind: Trading pipeline
repo: harsha-moparthy/tick2trade
description: >-
  A Rust tick-to-trade pipeline with a published per-hop latency budget: 625 ns p99 internal in
  replay on an idle host, 583 ns under load, 6.3 µs p99 against the live venue, and zero hot-path
  allocations proven by a counting allocator across 3.5 million traversals. The budget identified
  HMAC signing as 80% of the traversal; a one-line dependency change bought a 1.5x pipeline speedup.
stack: [Rust, rustls, WebSocket, HDR histograms, Criterion, Binance bookTicker]
highlights:
  - value: "625 ns"
    label: internal p99 in replay, 3.5M traversals
  - value: "6.3 µs"
    label: internal p99 live, same hops, gap published
  - value: "0"
    label: hot-path allocations, proven by counting allocator
  - value: "1.5x"
    label: pipeline speedup from a one-line HMAC fix
---

## Why this project exists

A newer mid-tier of HFT reaches sub-millisecond reaction times on ordinary cloud hardware through
software engineering rather than FPGAs. The engineering problem is not "make it fast" but "make a
latency claim you can defend": a single p99 number hides which stage costs what, whether the clock
can even resolve the intervals reported, and whether the fast path stays fast over a long session.
The deliverable is a budget — every hop timestamped separately, every distribution published, and
the measurement apparatus itself measured and reported next to the results.

## What it does

- Hand-rolled WebSocket client over rustls (RFC 6455 framing, ping/pong, buffer compaction), because
  every client crate returns an owned message per frame, putting the allocator inside the hop being timed
- Structural JSON scanner decoding Binance `bookTicker` frames straight to fixed-point `i64` — no heap
  traffic, no `f64`, and key lookups that are grammatically unreachable by decoy values
- Spread-making strategy with a bad-tick guard, cooldown throttle, and `i128` basis-point arithmetic
- Signed order encoder building Binance order bodies with HMAC-SHA256 into pre-allocated buffers,
  with the signed span verified against RFC 4231 vectors
- Latency harness: raw cycle-counter reads, per-hop tracing, HDR histograms, and a budget-table
  reporter that gates CI on the 1 ms target
- Soak runner with reconnect-with-backoff, per-window jitter analysis, and an outlier census

The budget paid for itself: HMAC-SHA256 signing was ~80% of the internal budget. Disassembly showed
zero `sha256h` instructions — the pure-Rust backend was not using the CPU's SHA extensions. One
feature flag made `order_encode` 2.9x faster and cut internal p99 from 875 ns to 625 ns.

## Measured results

| Evidence | Result |
|---|---|
| Per-hop budget, replay (7 real frames x 500k = 3,500,000 traversals) | internal **p50 333 ns, p99 625 ns** vs a 1 ms target |
| Same binary under host load (~6.8 load average) | p50 458 ns, **p99 583 ns** — run-to-run spread published, not hidden |
| Live soak vs real venue (300 s, 32,669 traversals, 0 reconnects) | internal **p99 6.3 µs** — the 10x replay-vs-live gap is the most informative number |
| Hot-path allocations across all 3,500,000 traversals | **0**, enforced by a counting global allocator that fails the build |
| Hardware SHA-256 fix | `order_encode` 553 ns → **193 ns** (2.9x); full traversal 684 → 362 ns |
| Test suite | **148 tests in release, 149 in debug**, weighted toward plausible wrong answers |
| Cross-architecture CI (x86_64 Linux) | p50 621 ns, p99 681 ns, 0 allocations; CI fails if internal p99 exceeds 1 ms |
| Measurement floor, measured not nominal | one clock read 10.0 ns; real counter step 42 ns (the clock claims 1 ns) |

Two measurement bugs were found by instrumenting the instrumentation: the clock claimed 42x more
precision than it had, and the original zero-allocation assertions passed unconditionally because
the counting allocator was never installed. Both fixes are now regression-tested.

## Tech stack

- Rust (release profile, fat LTO), fixed-point `i64` price/qty types throughout
- rustls for TLS; hand-rolled RFC 6455 WebSocket client
- `sha2` with the `asm` feature for hardware-accelerated HMAC-SHA256
- HDR histograms plus raw cycle-counter reads for the per-hop harness
- Criterion microbenchmarks; CI gates the p99 headline on a Linux runner
