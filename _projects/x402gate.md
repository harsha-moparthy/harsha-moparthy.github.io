---
title: X402Gate
track: backend
order: 63
group: Metering, billing, and payments
kind: Payment infrastructure
repo: harsha-moparthy/x402gate
description: >-
  Pay-per-request API infrastructure on the x402 model in zero-dependency Go: challenge, verify,
  settle, serve, with each payment bound to one response through a crash-safe write-ahead ledger.
  A failure-injection suite drove 3,000 payments through 6,432 attempts with 653 post-payment
  crashes; an independent auditor found zero double-charges, zero unpaid serves, and reconciliation
  that closes with drift 0.
stack: [Go, x402, EIP-712, EIP-3009, secp256k1, keccak256]
highlights:
  - value: "0 / 0"
    label: double-charges / unpaid serves, chain-audited
  - value: "653"
    label: post-payment crashes injected, all recovered
  - value: "drift 0"
    label: reconciliation closes exactly
  - value: "~609×"
    label: verify cost cut by caching, 10.955 to 0.018 ms p50
---

## Why this project exists

When an AI agent pays per API call with no account and no invoice, the billing relationship
collapses into the request itself: the server issues a challenge, the agent signs a payment, the
server verifies and settles it, then serves. This is the x402 model (HTTP 402 revived by Coinbase
for stablecoin micropayments). The protocol is the easy part; the unfinished backend engineering
is the accounting — binding payment to request identity so a retry neither pays twice nor gets
served twice, verification fast enough for the request path, refunds when the server fails after
taking payment, and reconciliation between on-chain settlement and served requests.

## What it does

- Orders every step around one rule: money never moves without a durable intent preceding it, and
  a response is never produced without a durable settled-record preceding it — each an fsync'd
  WAL append, so every crash point is recoverable by replaying the log and asking the chain.
- Uses the chain's own payment namespace, `(from, nonce)`, consistently across the replay guard,
  the ledger's idempotency key, the verification cache, and the recovery predicate — closing three
  attacks (free serves and a cross-payer double charge) that follow from keying on the nonce alone.
- Caches verification verdicts keyed on the full signed identity (struct hash plus signature), so
  a retried payment reuses its verdict instead of recomputing signature recovery.
- Hand-rolls keccak256 and secp256k1 over `math/big`, pinned to canonical vectors — the published
  generator points, the famous key-1 address fixture, and the EIP-712/EIP-3009 constants — with
  low-s enforcement and 2.5M+ fuzz executions per primitive.
- Recovers refund-or-serve after any crash: found settlements are adopted only when payer, nonce,
  payee, and amount all match a chain receipt.

## Measured results

Apple M4 Pro, Go 1.26.5, offline against a deterministic EIP-3009 settlement-chain model;
reproduces with `make bench`.

| Evidence | Result |
|---|---|
| Failure suite: 3,000 payments, 6,432 attempts, 653 post-payment crashes, 580 verify timeouts, 8 workers | 0 double-charges, 0 unpaid serves — audited from the chain, never the gateway's counters |
| Reconciliation | closes exactly, drift 0, 0 alerts |
| Verification latency (5 ms modelled facilitator round trip) | miss p50 10.955 ms; cache hit p50 0.018 ms — ~609× |
| 24 concurrent identical requests for one payment | exactly one settlement, one charge, all attempts converge |
| Crypto pinning | keccak vectors, generator points, key-1 address, EIP-712/3009 constants all match published values |

Ten documented bugs include a used-nonce check that let attackers get served for free, a `uint64`
truncation that under-recorded a 2e19 charge, and mid-file WAL corruption that silently destroyed
every record after it — each provoked by the auditor or a test and pinned by a regression.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go 1.26, zero external dependencies (stdlib only) |
| Payment scheme | EIP-712 typed data + EIP-3009 `transferWithAuthorization` (the x402 "exact" scheme) |
| Crypto | Hand-rolled keccak256 + secp256k1 over `math/big`, vector-pinned, fuzzed |
| Durability | Append-only WAL, fsync per append, CRC framing, torn-tail recovery |
| Idempotency | `(from, nonce)` bound to request hash: one nonce, one settlement, one served response |
| Reconciliation | Per-nonce plus aggregate identity, no tolerance, typed drift alerts |
| Harness | Failure-injection suite with independent chain-reading auditors |
