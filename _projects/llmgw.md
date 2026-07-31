---
title: LLM Gateway
track: backend
order: 59
group: Serving AI traffic
kind: LLM gateway
repo: harsha-moparthy/llmgw
description: >-
  One OpenAI-compatible API in front of many providers, in zero-dependency Go. Killing a provider
  under 120k requests of live load produced zero client-visible errors, the cost ledger reconciles
  exactly against the providers' own logs (120,901 of 120,901 rows, to the picodollar), and the
  gateway adds 1.84 ms p99 of its own latency at ~19.5k req/s on one laptop.
stack: [Go, OpenAI API, Anthropic API, SSE, Prometheus, k6]
highlights:
  - value: "1.84 ms"
    label: p99 added latency, self-timed
  - value: "120,901/120,901"
    label: ledger rows reconcile exactly
  - value: "0"
    label: client errors, provider killed under 120k reqs
  - value: "4.8×"
    label: median cache speedup, 100% hit on repeat
---

## Why this project exists

Every company calling more than one LLM provider ends up rebuilding the same middleware: one API
in front of all of them, failover when one degrades, caching, per-team budgets, and cost
visibility accurate enough to bill against. It is the API-gateway category reborn for AI traffic.

The category is easy to fake and hard to do honestly. A gateway that splices two models' partial
outputs together on a mid-stream retry produces a response no model ever generated. A cost
dashboard built from `float64` drifts a fraction of a cent per request. A reconciliation that
passes usually does so because someone added an epsilon. This project's design commitments are
aimed squarely at those failure modes, and the results report where they bite.

## What it does

- Routes each client-facing model alias across an ordered failover chain; every upstream failure
  is classified into a closed set, and only health-relevant classes count toward the circuit
  breaker — 10,000 consecutive `bad_request` failures leave it closed, sustained 5xx opens it.
- Enforces a precise streaming boundary: transparent failover only before the first content byte;
  after that, an explicit SSE `error` event — never a silent EOF, never spliced output.
- Caches responses in a byte-bounded LRU that is tenant-isolated by default, with length-prefixed
  keys so boundary-shifted messages cannot collide, and only for deterministic requests.
- Accounts every monetary value as an `int64` count of picodollars; inexact prices are rejected at
  config load. Budgets use estimate-then-true-up, with concurrent reservations proven race-safe.
- Ships with zero dependencies: SSE framing, circuit breaker, Prometheus exposition, and the token
  estimator are all stdlib, so the whole thing builds and benchmarks with `go build ./...`.

## Measured results

Apple M4 Pro, Go 1.26.5, two local mock providers over loopback; raw benchmark JSON is committed
with the repo.

| Evidence | Result |
|---|---|
| Gateway overhead (5,000 reqs, concurrency 32, ~19,500 req/s) | 1.84 ms p99 self-timed; 2.95 ms p99 client-observed upper bound |
| Primary provider killed mid-flight under load | 120,885/120,885 requests succeeded, 0 client-visible errors, 16 transparent failovers |
| Cost reconciliation vs independent provider logs | 120,901/120,901 rows matched exactly; 0 token mismatches, 0 cost mismatches, 0 orphans either direction |
| Cache, warm pass over 400 deterministic prompts | 100% hit rate, 4.8× median speedup |
| Streaming, 300 requests | 300/300 clean `[DONE]` ends, 0 truncated, TTFB p50 14.3 ms |
| k6 budget scenario, one small-budget tenant hammered | 354 rejections, every one carrying a self-explaining, retry-informative body |

Sixteen documented bugs were found and fixed along the way — from a keep-alive frame that killed
streams mid-response to picodollar overflow that turned a $5,000 budget's 80% soft threshold into
$310.65 — each caught by the reconciliation, the mid-stream tests, or an adversarial audit, and
pinned by regression tests.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go 1.26, zero external dependencies (stdlib only) |
| Wire format | OpenAI `chat.completions` schema; Anthropic adapter with real bidirectional translation |
| Cost | Integer picodollars; inexact prices rejected at load time |
| Breaker | 3-state, failure ratio over a window with minimum samples, jittered backoff |
| Cache | Byte-bounded LRU, per-tenant scoping, deterministic-only |
| Metrics | Hand-rolled Prometheus text exposition; exact-sample quantiles |
| Load test | k6 scenarios plus a dedicated overhead/failover/reconcile bench tool |
