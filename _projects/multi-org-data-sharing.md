---
title: Multi-Org Data Sharing
track: fde
order: 29
group: Governed data access
kind: Data sharing
repo: harsha-moparthy/multi-org-data-sharing
description: >-
  Two organizations share a governed slice of one Postgres database, where the caller is often a
  partner's AI agent acting on a human's delegated authority. Row and column limits are enforced by
  Postgres RLS from grant tables, credentials are short-lived signed claims the database verifies
  for itself, and 30 adversarial attacks across four families pass with zero bypasses while
  revocation halts an agent in 7.9 ms mean.
stack: [Python, Postgres 16, plpgsql, pgcrypto, uv]
highlights:
  - value: "30/30"
    label: adversarial attacks held, zero bypasses
  - value: "7.9 ms"
    label: mean revocation halt, 0 rows after commit
  - value: "4"
    label: bypasses in the app-filter control arm, all masked-column channels
  - value: "12/12"
    label: mutation-check mutants caught
---

## Why this project exists

Sharing governed data with a partner is an old problem. What is new is who shows up holding the
credential. When org B's planning agent reads org A's data on behalf of org B's analyst, three
things have to be true at once: the partner sees exactly the approved rows and columns, the agent
sees no more than the human who delegated to it and revoking it actually stops it, and both
organizations can reconstruct later who saw what under whose authority. The tempting implementation
filters in the application — so this project builds that version too, as a control arm, because the
comparison is the interesting result: application-level filtering leaks masked values through the
caller's own SQL, and database-enforced masking does not.

## What it does

- Enforces row limits with RLS policies and column limits as per-grant CASE masking in a guarded
  view, both driven by grant tables. The portal role holds zero privileges on every base table, so
  a query that escapes the views fails at Postgres, not at code review.
- Verifies identity inside the database: credentials are HMAC-signed short-lived claims checked by
  a SECURITY DEFINER function using a key the application cannot read, because a bare `set_config`
  identity is forgeable by whoever runs the query.
- Walks the whole delegation chain to its root, intersecting scope at every hop — a delegation
  cannot widen the grant's regions or columns, cannot outlive it, and agents never hold standing
  authority (a trigger refuses grants to agents). Eleven such rules are trigger-enforced.
- Demonstrates the side-channel result: with costs masked, the app-filter arm binary-searches
  hidden values through WHERE predicates, leaks the true ranking through ORDER BY, and returns real
  aggregates; the RLS arm returns one identical result set because the value is already NULL.
- Appends one HMAC-chained audit row per request — allowed or denied — with org-scoped views, and
  catches an insider who disables the trigger and rewrites a row at the exact sequence number.
- Measures revocation across three enforcement designs, with bounds declared in advance.

## Measured results

| Evidence | Result |
|---|---|
| Test suite (real Postgres, real RLS policies) | 88 passed |
| Adversarial suite, RLS arm — 4 families | 30 attacks, 0 bypasses |
| Positive controls | 5/5 exact match against an independent oracle |
| Control arm (competent application-level filtering) | 4 bypasses — all masked-column channels |
| Revocation, DB-checked | halts in 7.9 ms mean (bound 40 ms), 0 rows to any request starting after the commit |
| Revocation, token-TTL-only enforcement | keeps working 395 ms, serving 50 rows after revocation |
| Revocation, 5-second authorization cache | keeps working 4.93 s, serving 945 rows |
| Audit chain over 45 events | intact; an insider's edit caught at the exact row |
| Audit reconciliation | rows served outside grant scope: 0; reads under an unapproved grant: 0 |
| Mutation check | 12/12 mutants caught by the attack suite |

The claims are scoped honestly: zero bypasses covers 30 attacks against the read API, not arbitrary
SQL or timing channels, and one limitation stays open — `pg_class.reltuples` leaks true base-table
cardinality to a role that cannot read the table. RLS protects row contents, not relation
cardinality.

## Tech stack

| Component | Choice |
|---|---|
| Enforcement | Postgres 16 RLS policies plus per-grant column masking in guarded views |
| Identity | HMAC-signed short-lived credentials verified by a SECURITY DEFINER function |
| Delegation | grant and delegation tables with 11 trigger-enforced narrowing rules |
| Audit | append-only HMAC-chained events with org-scoped views |
| Oracle | independent expected-answer derivation from raw fixture rows |
| Tooling | Python portal and attack suite via uv; repo-local Postgres, no Docker |
