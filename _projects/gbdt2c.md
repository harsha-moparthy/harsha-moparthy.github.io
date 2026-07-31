---
title: GBDT2C
track: hft
order: 74
group: Prediction and research
kind: ML inference
repo: harsha-moparthy/gbdt2c
description: >-
  A GBDT trading signal compiled to branch-lean C++, with bit-exactness as a first-class
  deliverable: 1,000,000 of 1,000,000 held-out book events reproduce XGBoost's own margins bit for
  bit, features included. The end-to-end hot path runs at 500 ns p50 and 1.58 µs p99 — 228x
  XGBoost's native single-row predict and 6.6x ONNX Runtime — with the honest negatives kept:
  XGBoost wins batch scoring 4.7x, and the quantized variant is slower than inlined branches.
stack: [C++, Python, XGBoost, ONNX Runtime, clang, Binance L1 data]
highlights:
  - value: "1M/1M"
    label: margins bit-exact vs XGBoost, features included
  - value: "500 ns"
    label: event-to-margin p50, incl. 16 features; p99 1.58 µs
  - value: "228x"
    label: vs native XGBoost single-row predict
  - value: "6.6x"
    label: vs ONNX Runtime single-sample, 1 thread
---

## Why this project exists

Modern market makers are ML-heavy, but a model is useless on the hot path if inference takes
milliseconds. The craft is turning a trained ensemble into native code that is fast and provably
the same function — "roughly the same" is how silent mispricing ships. This project treats
bit-exactness as a first-class deliverable with its own written numeric contract and a million-row
proof harness, then measures where the remaining nanoseconds go.

## What it does

- Ingests 6 days of Binance BTCUSDT perp L1 book archives (10-16M events/day) with exact
  decimal-string parsing to integer ticks — an ingest guard refuses sub-tick input rather than
  rounding it
- Computes 16 float32 features from a ring buffer with every cast and summation order pinned;
  numpy's silent float64 promotion is a test failure, not a 1-ULP mystery
- Trains an XGBoost binary signal (does 2·mid rise >10 ticks within 100 events?) on a
  chronological split: AUC 0.892 on the held-out final day, 200 trees, 20,282 nodes — the signal
  is deliberately modest; the deliverable is the compiler and the proof
- Generates four C++ variants from the saved model.json: if_tree (thresholds as immediates in the
  instruction stream), branchless, flat_table, and quantized
- Proves equivalence with a 1M-row bit-exactness replay against `predict(output_margin=True)`,
  plus latency and baseline benches; CI regenerates the committed codegen output and fails on any
  diff
- Pins the subtle bits by test: NaN routing (`default_left`), exact-threshold-goes-right, float
  literal round-tripping, base_score serialization, and `-ffp-contract=off` (one fused
  multiply-add rounds once where the reference rounds twice — the flag is load-bearing)

## Measured results

Apple M4 Pro, clang -O2 -ffp-contract=off, single core; clock resolution (41 ns step) published
with every table.

| Evidence | Result |
|---|---|
| Feature parity, 1M held-out real book events | 1M/1M bit-exact |
| if_tree / flat_table / branchless margins vs XGBoost | 1M/1M bit-exact each |
| End-to-end hot path (event → ring push → 16 features → margin) | p50 500 ns, p99 1.58 µs, p99.9 2.4 µs — 4x headroom under the 10 µs target |
| vs native XGBoost C API single-row (113,834 ns p50) | 228x |
| vs ONNX Runtime single-sample, 1 thread (3,292 ns p50) | 6.6x |
| XGBoost blocked batch predictor | 114 ns/row amortised — 4.7x faster than if_tree in a loop; codegen wins one-sample-now, not bulk scoring |
| Quantized variant | slower (1,541 ns p50): per-call quantisation of 16 features costs more than packed compares save |
| Cold-cache first call, full LLC eviction | 5-17 µs; the winner is the smallest table, not the best branch layout — both numbers published |
| Quantized error, measured not asserted | 85.8% rows still bit-exact, mean Δmargin 4.2e-3, sign flips 0.0585% |
| Test suite | 31 tests, including compile-and-dlopen codegen parity; CI replays a committed 20k-row fixture on every push |

## Tech stack

| Component | Choice |
|---|---|
| Model | XGBoost binary signal, chronological split, held-out final day |
| Codegen | Python: model.json → four C++ variants, committed and CI-diffed |
| Hot path | Hand-written C++ feature engine mirroring the pinned reference |
| Proof | 1M-row bit-exactness harness with a written numeric contract |
| Baselines | Native XGBoost C API and ONNX Runtime, single-sample and batch |
| Data | Binance L1 archives, checksummed download, exact tick ingest |
