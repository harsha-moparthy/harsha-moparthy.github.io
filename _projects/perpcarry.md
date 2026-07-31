---
title: PerpCarry
track: hft
order: 57
group: Funding and payments
kind: Arb monitor
repo: harsha-moparthy/perpcarry
description: >-
  A cross-venue perp funding-rate arbitrage monitor normalizing 4 venues and 3 funding conventions
  into one no-lookahead expected-carry model with all-in costs and isolated-margin liquidation on
  both legs. A 30-day paper replay over real data delivers the honest verdict: $143.96 of funding
  collected, -$29.23 net after $206.22 of execution costs, with the model-vs-realized gap
  decomposed exactly per trade.
stack: [Go, Bybit API, Gate API, Hyperliquid API, Deribit API]
highlights:
  - value: "-$29.23"
    label: net after costs — the honest 30-day verdict
  - value: "$206.22"
    label: execution costs vs $143.96 funding collected
  - value: "4 venues"
    label: 3 funding conventions normalized, no lookahead
  - value: "10/11"
    label: trades liquidated at 20x; zero at 5x or below
---

## Why this project exists

Funding-rate arbitrage is the hello-world of delta-neutral crypto strategies, and almost every
write-up stops at "venue A pays 15% APR, venue B pays 5%, free money." The engineering problem is
everything that sentence hides: funding conventions differ per venue and even per contract, a
taker-taker round trip costs 24-34 bp on both legs — a ~7-11% APR hurdle over a 14-day hold before
a cent of carry is banked — and the short leg can be liquidated even though the trade is
market-neutral in P&L. A monitor that ignores costs finds opportunities everywhere; this one
mostly, correctly, says no.

## What it does

- Four venue adapters — Bybit and Gate (discrete 8 h funding), Hyperliquid (discrete 1 h), Deribit
  (continuous hourly accrual) — normalized to a common hourly rate, accruing at real payment
  timestamps rather than idealized ones
- A no-lookahead EWMA predictor (half-life 72 h, interval-weighted); only events at or before the
  decision hour are visible, enforced by tests
- An all-in cost model: taker fees, median sampled half-spread crossing, slippage, and per-leg
  isolated-margin liquidation prices using venue-reported margin parameters
- A 30-day paper replay over real July 2026 data — 5 symbols, 20 instruments, 8,100 normalized
  funding events, ~156k five-minute bars — with liquidation checked on the 5-minute high/low path
- Exact per-trade attribution: realized = expected-at-hold + funding drift + basis + execution
  delta, an identity that holds to float precision
- A leverage grid re-running identical signals at 2/3/5/10/20x; a live scan command for current
  opportunities

## Measured results

| Evidence | Result |
|---|---|
| 30-day replay verdict, 8 trades | **$143.96 funding collected, -$29.23 net** after $206.22 of execution costs ($154.79 fees) |
| Ex-ante promise vs realized | +$28.61 promised → -$29.23 realized; gap decomposed exactly: **funding drift -$88.64, basis +$33.03** |
| Leverage grid, identical signals | **0 liquidations at 5x or below, 2 at 10x, 10 of 11 trades at 20x** for -$598.89 |
| Cost bar | 24-34 bp round trip taker-taker — exceeded what realized carry delivered this month |
| Data normalized | 4 venues, 3 funding conventions, 8,100 funding events, ~156k bars, 3,456 funding accruals in the ledger |
| Reproducibility | deterministic replay; CI re-runs from the committed snapshot and requires the ledger to match **byte-for-byte** |

The two headline findings are negative, and that is the point: taker-taker execution lost this
month, and the EWMA predictor over-promises at entry because entries trigger on smoothed carry
spikes that then mean-revert — pinned per trade by the attribution identity, which is the
difference between a monitor you can trust and a backtest that flatters itself.

## Tech stack

- Go, stdlib only — including the HTTP clients for all four venue APIs (no keys needed)
- Bybit, Gate, Hyperliquid, and Deribit public APIs with per-venue normalization of funding,
  klines, top-of-book, fees, and maintenance-margin parameters
- A snapshot store with a manifest pinning the window; the replay is a pure function of it
- Hermetic tests on fixtures and synthetic replays; a make-driven workflow (test, replay, riskgrid,
  scan, fetch)
