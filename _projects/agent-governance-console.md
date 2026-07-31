---
title: Governance Console
track: fde
order: 20
group: Agent operations
kind: Operations console
repo: harsha-moparthy/agent-governance-console
description: >-
  A governance console for a fleet of heterogeneous agents: three frameworks with unrelated native
  event formats normalized into one audit timeline with exact cost attribution, session replay, and
  capability-token revocation whose mid-flight halt bounds are measured — 26ms mean online, and
  TTL-bounded (with up to 7 leaked effects quantified) behind an offline verifier.
stack: [Python, LangGraph, SQLite, HMAC capability tokens]
highlights:
  - value: "26ms / 50ms"
    label: mean / max mid-flight halt, online gateway, 10/10 within bound
  - value: "7 effects"
    label: max leakage behind an offline verifier before TTL expiry — quantified
  - value: "exact"
    label: cost reconciliation across per-agent and per-tenant rollups
  - value: "33/33"
    label: tests passing
---

## Why this project exists

Once a company runs dozens of agents, leadership asks questions nobody can answer: what did the
agents do yesterday, what did they cost, which ones fail, who approved that action — and can we stop
one *right now*? The governance layer (inventory, audit, replay, revocation) is the missing
enterprise product of the agent era. Its two hard parts are unglamorous: normalizing activity across
frameworks that agree on nothing, and revocation that actually stops an agent mid-flight rather than
asking it nicely.

## Three agents, three frameworks, three unrelated formats

| agent | framework | native event format | cost convention |
|---|---|---|---|
| `loopy-1` | hand-rolled while-loop | terse dicts, epoch-float timestamps | dollars per step |
| `gr-7` | LangGraph `StateGraph` | node-stream records, ISO timestamps | tokens only — priced later from a price sheet |
| `crew-2` | declarative pipeline | pipe-delimited **text log lines** | dollars embedded in the line |

Per-framework adapters translate each into one `ActivityEvent` schema; everything downstream —
timeline, cost attribution, replay, metrics, investigations — consumes only that schema. The
text-log adapter is a parser on purpose: that is the authentic worst case for normalization.

## Revocation: cryptography plus a kill list, not a flag

Agents hold short-lived HMAC capability tokens (TTL 0.5s) naming tenant, agent, and allowed
capabilities. Every effect executes inside a gateway, *behind* the token check — so a rogue agent
that ignores denials and hammers accomplishes zero side effects (tested: 20 retries, 0 effects).
Revocation bites through two mechanisms, and measuring the difference is the core result:

- **online gateway** — checks the revocation list per call: the next call is denied
- **offline verifier** — signature + TTL only (an edge that cannot reach the list): the agent works
  until its token expires and the refresh is refused

## Measured results

### Revocation halt bounds (10 trials per mode, agent working every 40ms)

| mode | halt latency mean | max | effects after revoke (max) | declared bound | within bound |
|---|---|---|---|---|---|
| online | 0.026s | 0.050s | 1 (the in-flight call) | 0.14s | 10/10 |
| offline | 0.339s | 0.392s | **7** | 0.64s (TTL + interval) | 10/10 |

The offline row is the architecture lesson quantified: a revoked agent behind a verifier that cannot
see the kill list kept executing up to seven effects until its token died. The halt bound *is* the
TTL — the measured argument for embarrassingly short token lifetimes. Bounds are asserted per trial
in tests, not tuned to fit a run.

### One timeline, exact attribution

A seeded workload (9 sessions, 2 tenants) lands 57 normalized events in one queryable timeline.
Cost attribution per agent and per tenant reconciles exactly (tested), and a scheduled kill-switch
drill on `crew-2` — revoked mid-session, halted by the gateway at stage 3 of 5, then reinstated —
is part of the workload so the timeline shows what a mid-flight halt looks like from the audit side.

### The investigation walkthrough

Incident: tenant acme reports data was exported and nobody approved it. The walkthrough is generated
from real store queries, not hand-written: filter the timeline to `data.export` calls, join against
in-session approval events (**one unapproved export found**, attributed to `gr-7` with exact session
and timestamp), replay the offending session — the approval gap is visible in the step sequence —
cost the blast radius, contain via revocation. The closing finding: detection worked because three
frameworks normalize into one schema, and the durable fix is moving the approval check *into* the
gateway so the gap becomes structurally impossible.

## Honesty notes

The three agents are stand-ins built for this project; their heterogeneity (execution models, log
formats, cost conventions) is real, their tasks are simulated effects behind the gateway. Timing
numbers are wall-clock real. The investigation document regenerates from queries at run time — if
the workload changes, the narrative changes with it.
