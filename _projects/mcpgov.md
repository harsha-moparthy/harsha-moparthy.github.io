---
title: MCPGov
track: sde
order: 36
group: Governed tool layers
kind: Governed MCP server
repo: harsha-moparthy/mcpgov
description: >-
  A governed MCP server over Postgres: FORCE-RLS tenant isolation, exactly-once mutations under
  16-thread retry storms, a loop breaker with 100% recall and 0 false breaks (median 8 wasted calls),
  and a fork-proof tamper-evident audit chain. 100 Postgres-backed tests plus a 13-act adversarial
  HTTP demo run in CI.
stack: [Python, Postgres, MCP, JWT, uv]
highlights:
  - value: "100%"
    label: runaway loops broken, median 8 wasted calls
  - value: "0"
    label: false breaks on legitimate workloads
  - value: "16 threads"
    label: retry storm, every mutation exactly-once
  - value: "13-act"
    label: adversarial HTTP demo, asserted in CI
---

## Why this project exists

Every company is wrapping internal systems in MCP servers so agents can use them. Most wrappers are
demos: the tools work, and nothing stops a retried mutation from applying twice, a token from reading
another tenant's rows, or an agent loop from hammering the same failing call all night. This repo is
the missing 80-to-100 stretch, built as five controls a tool author cannot forget, because they live
in the middleware chain and the database rather than in tool bodies. Each claim is pinned by a test
against a real database, and an end-to-end adversarial demo attacks the live server over real HTTP
in CI.

## What it does

- Identity is verified, not asserted: short-lived HS256 Bearer tokens with `exp`/`aud`/`iss`/`jti`
  required, plus RFC 7523 jwt-bearer federation with signature-by-`kid`, bounded skew, and single-use
  `jti` — 19 tests including forged signatures, `alg=none`, and replayed assertions
- Tenant isolation is enforced by the database: Postgres row-level security with `FORCE`, keyed on a
  GUC populated only from verified claims; there is no request field through which a client names a
  tenant, and cross-tenant reads return `not_found` byte-identical to genuinely absent ids
- Mutations are exactly-once: a claim-then-execute ledger commits the idempotency claim and the
  business write in one transaction; duplicates replay the stored response, a key reused with
  different arguments is refused, and only non-retryable failures are cached
- Rate limiting distinguishes a runaway loop from a legitimate burst: a GCRA shaper per
  `(principal, tool_class)` that delays, plus a loop breaker that looks for repetition without
  progress and opens a per-tool circuit
- The audit trail is tamper-evident, including truncation: every attempt is one row in an HMAC hash
  chain with a `FOR UPDATE` singleton head, verified by a separate auditor login the server never holds

## Measured results

Limiter evaluation is seeded, 200 trials per workload family, reproduced byte-for-byte in CI.

| Evidence | Result |
|---|---|
| 5 runaway families (same-error, cycle, no-op write, infinite transient retry, idempotent replay) | broken in **100% of trials, median 8 wasted calls** |
| 6 legitimate families (poll, paginate, fan-out, backoff retry, burst, small worklist) | **0 false breaks** |
| Token-bucket baseline at identical arrival rates | denies 41/80 of runaway *and* 41/80 of legitimate bursts — verdict is a function of rate, the label is a function of shape |
| Concurrent-duplicates test | 16 threads, repeated 5 times: exactly-once, plus crash-recovery on unclean death |
| Audit chain under concurrency | naive head forked (16 appends produced 9 distinct predecessors); the `FOR UPDATE` head does not |
| Test suite | **100 tests**, most against a real Postgres |
| Adversarial demo | **13 acts** over real HTTP via the official MCP client — forged signature, scope escalation, retry storm, cross-tenant probe, loop broken on attempt 7, superuser row rewrite caught with the exact seq |

The demo's superuser act matters: a superuser rewriting one row's `deny` to `allow` is caught by
chain verification with the exact sequence number, which hash-chaining alone cannot see for
truncation — the separate read-only auditor role is what makes the verdict about the data rather
than the writer's self-report.

## Tech stack

| Component | Choice |
|---|---|
| Server | Python 3.12+, MCP middleware chain — controls wrap every inbound message |
| Database | Postgres 14+: FORCE RLS policies, idempotency ledger, audit chain head |
| Auth | HS256 tokens, RFC 7523 assertion exchange, declarative group-to-team allowlist |
| Limiting | GCRA shaper plus progress-aware loop breaker, thresholds keyed on declared retryability |
| Audit | HMAC hash chain, arguments redacted to digests, separate auditor login |
| Evidence | Seeded limiter eval and demo transcript committed; CI diffs both |
