---
title: PayPer
track: hft
order: 58
group: Funding and payments
kind: Machine payments
repo: harsha-moparthy/payper
description: >-
  An x402 machine-payable API with exactly-once payment accounting: 5,289 settlements reconcile
  exactly across 631 server kills — 0 lost, 0 double-charged, 0 double-refunded. The crypto
  (Keccak-256, secp256k1, EIP-712) is built from scratch in zero-dependency Go and verified
  byte-for-byte against eth-account ground truth.
stack: [Go, x402, EIP-3009, EIP-712, secp256k1, Keccak-256]
highlights:
  - value: "5,289"
    label: settlements reconcile exactly, 0 pending
  - value: "631"
    label: SIGKILLs mid-payment, zero money lost
  - value: "0"
    label: double-settles on chain, 0 discrepancies
  - value: "21.9 ms"
    label: p50 full paid call, probe to sign to settle to serve
---

## Why this project exists

x402 lets software agents pay APIs with signed stablecoin authorizations over HTTP 402 — no
accounts, no cards. The protocol is easy; the hard part is money-grade systems engineering: an
agent must never pay twice for a retried call, a server crash after settlement must not eat the
payment, and at the end of the day payments and served requests must reconcile exactly. This
project is about that hard part, proven by killing the server mid-payment hundreds of times and
reconciling the ledger afterwards.

## What it does

- The full loop in zero-dependency Go: a metered API server behind x402 middleware, a facilitator,
  a simulated USDC chain with real EIP-3009 semantics, and an autonomous paying agent with budget
  and per-call spend caps
- Exactly-once by construction: the EIP-3009 authorization nonce is keccak256 over payer, resource,
  and request id, so a retried logical call re-presents the byte-identical signed payment — the
  agent cannot pay twice because there is only one authorization
- A write-ahead log with crash-safe ordering: intent fsynced before settle, settled before serving,
  served stores the response for byte-identical replays; a settle outcome lost to a crash is
  recovered by asking the chain whether the nonce was consumed
- Deterministic refund nonces derived from the payment nonce, so a refund retried across crashes
  settles at most once; a sweep finds and refunds settled-but-never-served orphans
- A chaos harness that SIGKILLs the server at the two worst points of the payment state machine,
  then reconciles the chain settlement log against the WAL
- Crypto from scratch: Keccak-256 from the permutation up, secp256k1 ECDSA with RFC 6979 and low-s,
  ecrecover, and EIP-712 typed-data digests

## Measured results

| Evidence | Result |
|---|---|
| Chaos run (committed, seed 7) | 5,300 logical paid calls against real processes, **631 kills** (595 injected at the worst state-machine points + 36 random) |
| Reconciliation | **5,289 chain payments = 5,102 served + 187 refunded + 0 pending — exact** |
| Revenue identity | 5,102,000 atomic units equals the sum of served prices, exact |
| Double-settles and discrepancies | **0 and 0 — zero lost money across 631 kills** |
| Duplicate delivery (same signed payment, 2x concurrent) | 184/184 intact pairs: one fresh serve + one byte-identical cache replay, **one settlement** |
| Permanent serve failure after payment | 99/100 refunded on-chain exactly once — net-zero for the agent |
| Negative controls | a dropped chain row, a duplicated row, and forged WAL revenue are each detected — the all-clear is not vacuous |
| Latency | **p50 21.9 ms** full paid call vs 0.16 ms for a free endpoint, dominated by math/big ECDSA |

Both crash-recovery bugs (verify-vs-authorizationState, orphaned refund intents) and the WAL
torn-tail corruption were found by the chaos harness failing its invariants. That is what the
harness is for.

## Tech stack

- Go, zero dependencies outside the standard library, across five binaries (server, facilitator,
  agent, chaos harness, reconciler)
- x402 protocol wire types (HTTP 402), EIP-3009 TransferWithAuthorization, EIP-712 typed data
- From-scratch Keccak-256 and secp256k1 (RFC 6979, low-s, ecrecover), verified byte-for-byte
  against eth-account / eth-keys test vectors
- fsynced WAL state machine plus a chain-vs-WAL reconciliation CLI that exits non-zero on any
  discrepancy
