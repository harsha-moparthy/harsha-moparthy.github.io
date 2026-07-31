---
title: Broker Rails
track: hft
order: 55
group: Risk and surveillance
kind: Risk rails
repo: harsha-moparthy/broker-rails
description: >-
  An MCP trading server with non-bypassable pre-trade risk rails: enforcement runs in the SDK
  dispatcher, so a refused order never reaches the handler. 21 adversarial attempts to exceed a
  limit produce zero rail violations, a 7-day unattended session holds every limit against a
  deliberately greedy agent, and the whole session rebuilds from a tamper-evident audit log of
  1,710 records.
stack: [Python, MCP, YAML, Alpaca paper API, pytest, uv]
highlights:
  - value: "21/21"
    label: adversarial attacks refused by the expected rail
  - value: "0"
    label: rail violations across direct, protocol, injection channels
  - value: "7 days"
    label: unattended, 233 refusals, every limit held
  - value: "1,710"
    label: audit records — chain verified, session rebuilt
---

## Why this project exists

Major brokers now expose MCP interfaces so users can point AI agents at trading accounts. The
unsolved part is not the plumbing — it is the safety layer. An LLM cannot be trusted with an order
path, and the tempting fix, a very firm system prompt, does not hold: a prompt is a suggestion, and
a jailbroken, confused, or merely goal-directed agent routes around it. The load-bearing mechanism
here is that the order path contains no decision the model can influence. The rails are not
persuasive; they are unreachable.

## What it does

- Enforcement runs in the MCP dispatcher middleware, before params validation and handler lookup —
  a refused order never enters `place_order`'s body, so `broker.submit` is unreachable for that
  request rather than merely not called
- The risk engine is a pure function of (intent, limits, market, portfolio, history); it holds no
  reference to the session, the prompt, or the model — there is nothing for a prompt to talk to
- 22 rules across five families (instrument, size, position, collars, session), all evaluated with
  no short-circuiting, so an order breaking eight rails reports all eight
- Every test asserts on world state, never on error messages: an error proves the server said no;
  only an unchanged book proves it did nothing
- `market_context` deliberately serves headlines containing real injection attempts; a persuaded
  model still has exactly one write tool, guarded by an engine that never reads headline text
- A hash-chained audit log carries the limits fingerprint on every record, rebuilds the entire
  session, and makes selective edits detectable

## Measured results

| Evidence | Result |
|---|---|
| Adversarial suite (direct, protocol, injection channels) | **21/21 refused by the expected rail, 0 rail violations** — wrong-reason refusal counts as failure |
| Rate burst, 15 orders as fast as possible | **exactly 10 filled** — the 10/min cap binds precisely at the boundary |
| Position accumulation, 10 x 60-share clips | 300 shares held, under the 500-share cap |
| Unattended 7-day session, deliberately greedy scripted agent | **362 submitted / 129 filled / 233 refused, 0 errors**, every limit verified against observed state |
| Peak exposure during the session | $98,965.81 gross (limit $250,000); peak position 292 shares (limit 500) |
| Audit chain | **VERIFIED over 1,710 records**; reconstruction matches broker state exactly, 129 fills = 129 filled |
| Tamper demo | flipping one recorded verdict breaks the chain at that record and every record after |
| Offline tests | **86**, no credentials, no network |

Findings that generalize: a limit set is a lattice, not a checklist — the position cap was
unreachable behind the per-minute notional rail, and a declared-but-unenforced market-hours limit
was caught only because the suite asserts which specific rail fired.

## Tech stack

- Python MCP server (stdio and streamable HTTP transports) with dispatcher middleware enforcement
- Decimal-only domain types; non-finite values rejected twice, at parse and in `check()`
- Frozen YAML limits with a content fingerprint written into every audit record
- Hash-chained audit log with full session reconstruction; deterministic broker simulator plus a
  wired Alpaca paper adapter; pytest
- Read and write tool surfaces split as data (frozensets consulted by middleware), not naming
  convention; `get_limits` is readable on purpose and there is no setter anywhere
