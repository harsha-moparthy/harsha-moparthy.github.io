---
title: CapBox
track: sde
order: 31
group: Sandboxing and isolation
kind: Plugin sandbox
repo: harsha-moparthy/capbox
description: >-
  A WASM plugin sandbox on Wasmtime where plugins hold explicit capability grants and nothing else —
  proven by a 12-payload hostile suite in which every containment claim is falsifiable, and priced by
  an overhead benchmark against a native plugin interface. The warm call boundary costs ~80 ns.
stack: [Rust, Wasmtime, WebAssembly, Go, WAT]
highlights:
  - value: "12/12"
    label: hostile payloads contained, all falsifiable
  - value: "~80 ns"
    label: warm call boundary vs native
  - value: "~13 µs"
    label: per-call isolation, fresh store + instance
  - value: "1.4–1.7x"
    label: fuel-metering tax on guest compute
---

## Why this project exists

Platforms want users to extend them with custom code without that code being able to harm the
platform. WebAssembly won this niche — Shopify runs customer checkout logic this way, Fastly runs
edge code this way, Extism and Fermyon sell the pattern as a product. The two hard parts are exactly
the ones that never show up in a hello-world embedding: authority (what, precisely, can a hostile
plugin reach — "it's sandboxed" is not an answer, a grant table is) and cost (plugin calls sit on hot
paths; what does the boundary cost per call?). This repo answers both with measurements.

Any sandbox project can print "12/12 payloads contained." Here, containment is asserted on typed
errors and mechanism counters — the fuel bomb must fail with `OutOfFuel` with fuel consumed equal to
the budget, the memory bomb must trap with peak memory under the cap and `denied_growths >= 1` on the
limiter. And every expectation is demonstrated to be falsifiable: a meta suite runs each payload under
a documented permissive condition (unlimited fuel, a 4x cap, the capability actually granted) and
requires the expectation to fail there. An assertion that cannot fail is not evidence, so an
unfalsifiable expectation fails CI just like an escape.

## What it does

- Runs untrusted WASM plugins from any language behind a 4-function ABI: `cb_alloc`, `cb_run`,
  `memory`, optional `_initialize`
- Grants capabilities explicitly, default-deny: `log`, `kv_read`, `kv_write`, `clock`, `http`,
  `wasi`. Denied host calls trap; an ungranted `wasi` is never even linked
- Partitions the KV store by host-chosen namespace, so cross-tenant reads are impossible by
  construction, not by validation — probed by a payload
- Bounds every resource with a mechanism that has its own counter: fuel metering (deterministic CPU),
  epoch deadlines (wall clock), a `ResourceLimiter` (guest memory), per-plugin byte quotas (KV, logs)
- Validates every guest pointer in both directions — lying allocators, out-of-bounds results, and
  oversized results are each a typed error and a hostile payload
- Isolates calls by default: fresh store + instance per call, so a trapped call cannot poison the
  next one; a warm-instance path exists for hot loops and the benchmark prices the difference

## Measured results

Apple M4 Pro, wasmtime 47. Containment: 12/12 contained, 12/12 falsifiable.

| Evidence | Result |
|---|---|
| Hostile suite (fuel bomb, memory bomb, stack overflow, capability probes, floods, pointer attacks) | **12/12 contained**, each on a typed error plus its mechanism's counter |
| Falsifiability meta-suite | **12/12** expectations fail under permissive controls |
| Warm wasm call, 0 B payload, p50 | **83 ns** vs native `Box<dyn Plugin>` under 42 ns |
| Capability-checked host call | adds ~0–40 ns — grant checks are a set lookup |
| Per-call isolation (cold: fresh store + instantiation) | **~13.5 µs** — the price of "no state survives between calls" |
| Input copy tax | ~14 µs/MiB (1 MiB warm call: 14.8 µs) |
| Fuel metering on compute-bound guest code | **1.4–1.7x** (423 µs unmetered vs 697 µs metered) |
| Memory bomb | trapped at peak 63.1 MiB under a 64 MiB cap, `denied_growths >= 1` |
| Example plugins | Rust `discount` (33 k fuel, ~210 µs cold), Go `wordstats` (3.4 M fuel, ~2.4 ms cold) |

The two example plugins are real: the Rust one is Shopify-Functions-shaped (cart JSON in, discount
decision out, config from its KV namespace); the Go one proves a garbage-collected runtime lives
happily inside the sandbox — and that revoking `wasi` stops it from even instantiating.

## Tech stack

| Component | Choice |
|---|---|
| Host runtime | Wasmtime 47, embedded from Rust |
| Resource bounds | Fuel metering, epoch deadlines, `ResourceLimiter`, host-side byte quotas |
| Capability model | Six grants, default-deny; link-time enforcement for `wasi`, call-time traps for the rest |
| Hostile payloads | 12 commented WAT modules plus control modules |
| Example plugins | Rust (`wasm32-unknown-unknown`) and Go 1.26 (`wasip1`, `go:wasmexport`) |
| CI gate | `cargo test --release` runs containment, meta, isolation, and e2e suites |
