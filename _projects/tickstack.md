---
title: TickStack
track: hft
order: 52
group: Prediction and research
kind: Research stack
repo: harsha-moparthy/tickstack
description: >-
  The modern tick research stack — Arrow in memory, Parquet on disk, DuckDB for queries —
  benchmarked against a fair pandas baseline on the five canonical quant queries, with wins from
  2.8x to 19.5x. Every timing is gated by a correctness check that reconstructs the order book from
  the market-by-price stream and matches ground truth at 1,048,318 of 1,048,318 quote timestamps.
stack: [DuckDB, Apache Arrow, Parquet, pandas, Python, pytest]
highlights:
  - value: "2.8-19.5x"
    label: DuckDB over fair pandas, all five queries
  - value: "1.05M/1.05M"
    label: book timestamps matched against ground truth
  - value: "~200x"
    label: harness distortion found and fixed before recording
  - value: "207 ms"
    label: per-symbol partitioning at 30 days vs 14 ms single file
---

## Why this project exists

Quant research data infrastructure was long dominated by kdb+ — powerful, proprietary, and
expensive. The open columnar stack now credibly challenges it, and firms are actively migrating.
The question a research team actually has is not "is DuckDB fast" but "is it fast and correct on my
real queries, and what do I have to get right in schema and layout to make the migration pay off."
The benchmark is the deliverable: a genuinely reasonable-effort pandas baseline, a compute-vs-I/O
separation that measures the right thing, and correctness gates on every timing.

## What it does

- Five canonical quant queries, each stressing the engine differently: as-of join, VWAP/OHLCV bars,
  order-book reconstruction, event study, and cross-symbol correlation
- Every timing is gated by two checks that exit non-zero on failure: engine agreement (DuckDB and
  pandas results diffed, exact on integer columns) and ground truth (the book rebuilt from the MBP
  stream without ever reading the quotes table, then diffed against it)
- A deterministic LOB simulator emits trades, quotes, and book events from one book object in one
  pass, so the three streams are consistent by construction and the book stream is an independent
  oracle
- Four Parquet layouts hold the same rows — single file, by date, by date+symbol, and sorted — to
  measure what physical organization is actually worth
- A scaling study from 1 to 20 days (112k to 2.26M trades)

## Measured results

| Evidence | Result |
|---|---|
| Q1 as-of join | DuckDB 88 ms vs pandas 504 ms — **5.8x** |
| Q2 VWAP + OHLCV bars | 9.6 ms vs 135 ms — **14.1x** |
| Q3 book reconstruction | 680 ms vs 4.90 s — **7.2x** |
| Q4 event study | 101 ms vs 285 ms — **2.8x** |
| Q5 cross-symbol correlation | 21 ms vs 408 ms — **19.5x** |
| Ground-truth reconstruction | matches at **1,048,318 of 1,048,318** quote timestamps |
| Partition study, scoped query at 30 days | by_date_symbol **207 ms** (720 files) vs single 14 ms — per-symbol partitioning loses to row-group statistics |
| Harness trap caught before any number was recorded | DuckDB's ASOF JOIN over Arrow views fell back to a quadratic plan, making DuckDB look **~200x slower**; fixed by loading native tables |
| Scaling, 1 to 20 days (112k to 2.26M trades) | aggregations flat to sublinear; as-of join roughly linear; book reconstruction superlinear — the honest cost of rebuilding a book in SQL |

Two bugs the gates caught, both invisible to a spot check: Q3 did not reset the book across days
(100% match on day 1, near-zero on day 2), and same-nanosecond trades made Q1/Q2 ambiguous until
every event carried a global monotonic sequence number — the same reason real feeds carry one. An
early pandas Q3 was also accidentally quadratic, making DuckDB look 40x better than it is; fixed
before any number was recorded, because the speedup is only meaningful against a fair baseline.

## Tech stack

- DuckDB 1.5.5: SQL windows, ASOF JOIN, native tables for the compute-vs-compute comparison
- Apache Arrow in memory, Parquet on disk with four committed layout experiments
- pandas as the fair vectorized baseline (`merge_asof`, `groupby`, stateful replay for Q3)
- Python; a deterministic seeded order-book generator; pytest correctness suite in CI
- The migration takeaway: partition coarsely by date and lean on sort order plus row-group
  statistics — layout choices matter more than the engine
