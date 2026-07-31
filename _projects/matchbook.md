---
title: Matchbook
track: hft
order: 46
group: Tick-to-trade and matching
kind: Matching engine
repo: harsha-moparthy/matchbook
description: >-
  A zero-unsafe Rust limit-order-book matching engine verified against a BTreeMap model and two C++
  reference builds of the same written contract, plus 2.49 billion fuzz executions with every
  invariant checked after every command. Throughput lands within 1.01-1.09x of the pointer-based
  C++ build; the four-way diff found a real defect the fuzzers structurally could not.
stack: [Rust, C++, cargo-fuzz, libFuzzer, proptest]
highlights:
  - value: "2.49B"
    label: fuzz executions, 0 crashes
  - value: "1.01-1.09x"
    label: of pointer-based C++ throughput, 4 workloads
  - value: "4-way"
    label: byte-identical agreement, gated before timing
  - value: "29%"
    label: smaller order slot than the C++ pointer build
---

## Why this project exists

Banks and exchanges are rewriting trading components in Rust for memory safety without GC pauses.
The narrow question: a price level is an intrusive doubly-linked list — the canonical structure
that "needs" raw pointers — and `#![forbid(unsafe_code)]` takes them away. What does that actually
cost? Answering it fairly requires four implementations of one numbered contract: the Rust engine,
a pointer-based C++ build of the identical design, a naive `std::map` C++ build, and a BTreeMap
oracle. The gap between the two C++ builds measures how much of any result is design rather than
language — and it turns out to be most of it.

## What it does

- Price-time-priority matching: GTC/IOC/FOK, add/cancel/modify, with modify's two priority paths
  distinguished (quantity reduction keeps FIFO priority; a price change re-enters as a taker)
- Three-level hierarchical occupancy bitmap: best-price lookup in three word loads regardless of
  band width, up to 262,144 ticks
- Pre-allocated slab with an intrusive doubly-linked FIFO per level, linked by `u32` indices so
  O(1) cancel needs no `unsafe`
- Open-addressed id table with backward-shift deletion — tombstones degrade unboundedly under
  exactly this engine's add/cancel workload
- A total wire decoder: every input of every length yields `Ok` or a typed `Err` — no panic, no
  unbounded loop, no allocation
- Four fuzz targets; an auditor that re-derives share conservation and price-time fairness from the
  event stream rather than trusting engine counters
- Fifteen validator-teeth tests that deliberately corrupt book state (crossed book, stale
  aggregates, broken links) and require each checker to notice, asserting on the message — a
  checker that cannot fail is worse than no checker

## Measured results

| Evidence | Result |
|---|---|
| Throughput vs `cpp/fast` (same design, raw pointers), 4 workloads | **1.01x / 1.03x / 1.09x / 1.01x** — parity, reproduced to within 0.01x |
| Design axis vs language axis | naive C++ is **3.6-4.9x** slower than fast C++; the language costs 1-9% |
| Fuzzing, 4 targets | **2,488,461,356 executions, 0 crashes**, all 13 invariants checked after every command |
| Four-way agreement on every tape | identical stdout, stderr, and exit status — gated before any timing prints |
| Order slot size, measured | Rust 40 bytes vs C++ pointer-linked 56 bytes — **29% smaller**, 40% more slots per cache line |
| Test suite | **111 test functions**; 14 proptest properties at 2048 cases = 28,672 sequences per run |
| Defect the fuzzers could not find | unbounded `capacity` OOM-killed the pre-allocating engine (10.2 GB at 200M); found by diffing four implementations |
| Invariant audit cost, measured | full audit is **217x** plain apply (1557 ns vs 7 ns) — a deliberate trade for attribution |

An earlier draft claimed a 1.38x penalty on one workload with a plausible cache-miss story. The
measurement had a 297% spread — taken while fuzzers saturated all cores. Re-measured idle: 1.01x.
Every committed figure now records its spread so the claim is checkable.

## Tech stack

- Rust with `#![forbid(unsafe_code)]` (engine, model, tooling)
- C++ (two reference builds written from the contract, clang with LTO)
- cargo-fuzz / libFuzzer for the four fuzz campaigns; proptest for property tests
- A normative written contract with numbered rules, conformance tests, and validator-teeth tests
  proving the invariant checkers can actually fail
