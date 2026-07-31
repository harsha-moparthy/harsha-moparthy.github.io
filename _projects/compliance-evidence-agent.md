---
title: Compliance Evidence Agent
track: fde
order: 27
group: Analysis copilots
kind: Compliance agent
repo: harsha-moparthy/compliance-evidence-agent
description: >-
  An agent that collects SOC 2 evidence for 15 controls out of four company systems over scoped MCP
  tools, stores every artifact in a hash-chained ledger, and refuses to call a control done when the
  evidence is stale, partial, misaimed, or unattested. It finds all six planted deficiencies with
  the right reason for each — the same evidence through an existence-only checker reports 15 of 15
  green, including through a credential revocation that blinded it completely.
stack: [Python, MCP, SQLite, YAML, Typer, GitHub Actions]
highlights:
  - value: "6/6"
    label: planted deficiencies found, each with the correct reason
  - value: "0 vs 10"
    label: silent gaps under credential revocation, this checker vs existence-only
  - value: "8/8"
    label: tamper classes caught by the expected detector
  - value: "20/20"
    label: mutation-check guards caught
---

## Why this project exists

Every quarter, somebody assembles hundreds of evidence artifacts for an audit — repetitive,
multi-system, correctness-critical work that is exactly what agents are for. The risk is exactly
what agents are bad at: a collection pipeline that fails quietly produces a dashboard that is green
and wrong. Three failure modes drive the design. Collecting evidence today does not make it current
(freshness is measured from when a review was signed, not when the agent looked). Most compliance
evidence is an absence claim, and absence inverts badly — "no user lacks MFA" and "I can no longer
see users" are the same HTTP 200. And complete evidence of a failing control is not a pass.

## What it does

- Collects evidence for 15 controls across 12 TSC criteria from four system stand-ins — an IdP, a
  cloud account, CI, and ticketing — through four MCP servers holding one credential each, so
  asking the CI server for identity evidence is refused by name.
- Stores every artifact with a hash-chained provenance record: content digest plus a digest of the
  scope, collecting identity, timestamps, and population counts, bound to the previous ledger entry.
- Classifies each control with a specific gap reason — stale, population incomplete, control
  ineffective, unsigned, wrong scope — because the six planted deficiencies get fixed in six
  different places.
- Cross-checks populations against count endpoints on different scopes, so a revoked credential
  returning an empty roster with HTTP 200 becomes a loud collection failure instead of a clean
  "zero exceptions" artifact.
- Runs an independent auditor that recomputes every hash with its own libraries and grades artifact
  quality separately from control effectiveness — the two effectiveness failures have artifact
  quality the auditor accepts, and CI fails if that separation collapses.
- Proves the MCP path end to end: `evidence collect --via-mcp` produces artifacts byte-identical to
  the in-process path.

## Measured results

| Evidence | Result |
|---|---|
| Test suite | 172 passed |
| Scope | 15 controls across 12 TSC criteria, 4 systems, 4 needing human sign-off |
| Completeness — this checker | 9/15 audit-ready, 6 gaps across 5 distinct reasons |
| Completeness — existence-only checker, same evidence | 15/15 audit-ready, 0 gaps |
| Gap detection vs the 6 planted deficiencies | precision 1.00, recall 1.00, 6/6 with the correct reason |
| Gap detection, existence-only arm | recall 0.00 — all six missed |
| Provenance over the whole ledger | 75 artifacts, 75 ledger entries, 5 runs, chain intact |
| Tamper detection | 8/8 caught by the expected detector, 0 no-op tampers |
| Credential revocation, 4 scenarios | 7 controls damaged, 0 silent gaps; existence-only arm: 10 |
| Independent auditor | all 9 audit-ready controls accepted; each rejection names one criterion |

The scheduling consequence is worth stating: due-ness is computed from evidence effectiveness
dates, so a control whose only evidence is a 415-day-old attestation stays due forever, no matter
how many times the agent successfully re-fetches it. Re-collecting stale evidence is not progress.

## Tech stack

| Component | Choice |
|---|---|
| Control framework | 15 SOC 2 controls as validated YAML configuration |
| Collection surface | 4 MCP servers, 19 tools, one credential each |
| Evidence store | content hashing plus an append-only HMAC-chained ledger |
| System stand-ins | in-process IdP, cloud, CI and ticketing with real scope and pagination behaviour |
| Verification | independent auditor, 8 tamper classes, revocation injection, 20-mutant check |
| CLI | Typer: collect, dashboard, verify, audit, inject, review, report |
