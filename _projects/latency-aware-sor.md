---
title: Latency-Aware SOR
track: hft
order: 49
group: Execution and routing
kind: Order router
repo: harsha-moparthy/latency-aware-sor
description: >-
  A latency-aware smart order router replayed over recorded multi-venue crypto book data with honest
  arrival modeling: +4.68 bps of fee-adjusted execution price versus best-displayed routing,
  decomposed into 4.26 bps fees, 0.20 staleness, 0.22 splitting. The win holds at 4.58-4.75 bps
  across a 4x sweep of latency-model error, and drops to -0.16 bps with all fees zeroed — most of
  the win is fees, measured.
stack: [Python, Decimal arithmetic, YAML, pytest, uv]
highlights:
  - value: "+4.68 bps"
    label: vs best-displayed routing, fees included
  - value: "4.26/0.20/0.22"
    label: bps from fees, staleness, splitting — residual zero
  - value: "4.58-4.75"
    label: bps held across a 4x latency-model-error sweep
  - value: "-0.16 bps"
    label: with every fee zeroed — the honest counterfactual
---

## Why this project exists

When the same asset trades on several venues, the best displayed price may be stale by the time
your order lands, fees differ per venue, and splitting trades a better average price against leg
risk. The load-bearing pieces here are not the router but what surrounds it: honest arrival
modeling (fills against the arrival-time book, not the decision quote), an attribution
decomposition of where the win actually comes from, and a sensitivity sweep over the router's own
latency-model error — a router that only wins under a perfectly calibrated model is a gift from an
oracle, not a router.

## What it does

- The LatencyAware policy scores each venue as displayed price + fee + staleness cost per ms of
  latency + expected miss cost, splitting child orders when scores tie
- The fill model applies one-way latency plus jitter and fills against the venue's book at arrival
  time, so racing a slow venue for a stale price gets missed in proportion to the staleness
- Replays 188 parent orders (Poisson arrivals, log-normal sizes) over 6.6 minutes of real recorded
  Binance BTCUSDT bookTicker (~300 events/s); Coinbase and Kraken books are derived with documented
  seeded Ornstein-Uhlenbeck basis processes and per-venue spread/size multipliers
- Attribution runs counterfactual policies over the same tape so each source of improvement is
  identified separately, with the interaction residual reported
- Sensitivity distorts the router's latency belief by k in [0.5, 2.0] while ground truth stays fixed
- A zero-fees counterfactual isolates the non-fee win

## Measured results

| Evidence | Result |
|---|---|
| LatencyAware vs best-displayed baseline (87 common parents) | **+4.68 bps** effective price, fees included |
| vs the strongest single-venue baseline (Coinbase, +2.66 bps) | +2.0 bps — the real value of routing over pick-a-venue |
| Attribution decomposition | fees **+4.26**, staleness **+0.20**, splitting **+0.22**, residual 0.00 — ~91% of the win is fees |
| Latency-model-error sweep, k = 0.5x to 2.0x truth | win holds at **+4.58 to +4.75 bps** across the entire sweep |
| All venue fees set to zero, same tape and seed | **-0.16 bps** vs baseline — the router draws with best-displayed |
| Worst single-venue baseline (Kraken, high fee) | -12.71 bps — venue choice alone can cost more than routing wins |
| Offline tests | **64**, no credentials, no network |

Reporting "the router won by 4.7 bps thanks to latency-aware routing" would be true and misleading:
at current crypto fee tiers the fee gaps (5-26 bps) are one to two orders of magnitude larger than
expected staleness cost, so the fee signal carries roughly twenty times the staleness and splitting
contributions. Only decomposing the improvement surfaces that. The venue config is chosen so no
single venue wins on every axis — fastest and tightest, cheapest, or middle everywhere — which is
what makes the routing decision non-trivial.

## Tech stack

- Python with Decimal-only domain types — non-finite values rejected at ingress, since
  a NaN reaching a comparison would abort the routing decision mid-check
- Real Binance public bookTicker data as the committed anchor tape
- Seeded Ornstein-Uhlenbeck venue derivation and a deterministic arrival-time fill model
- YAML venue config loaded once and fingerprinted; pytest; uv
- Every command exits non-zero on regression, so the headline table is a CI gate, not a printout
