---
title: Enterprise Agent Deployment
track: fde
order: 16
group: Agent deployment
kind: Agent deployment
repo: harsha-moparthy/enterprise-agent-deployment
description: >-
  Three business workflows executed by LangGraph agents over a simulated customer's CRM, ticketing
  and document systems, each wrapped as a governed MCP server with human approval gated on effects
  rather than tool names. The trap that beat a per-tool gate is refused on all three routes with zero
  writes, and every action is provable after the fact against a tamper-evident audit chain of 4,200+
  events.
stack: [Python, LangGraph, MCP, Postgres 16, Ollama, FastAPI]
highlights:
  - value: "99"
    label: tests, real Postgres + MCP over HTTP
  - value: "3/3"
    label: evasion routes refused by the effect gate, zero writes
  - value: "108/108"
    label: deterministic control arm, proving the harness
  - value: "0"
    label: unlogged, phantom, ungranted writes in audit reconciliation
---

## Why this project exists

The forward-deployed job in one sentence: take a customer's real systems, wrap them so agents can
act on them safely, and deploy agents that do useful work under human oversight. The hard parts are
not the agent loop. They are deciding which actions need a human's signature and making that
boundary impossible to walk around, proving what happened to someone who does not trust the agent,
and measuring reliability well enough to justify trust.

The project is built around a specific inherited failure: in a sibling system, approval gates were
attached to tool names, and an agent denied on `update_account_status` achieved the same outcome
through the ungated `create_account`. The recorded lesson — gating must be defined over effects,
not individual tool names, because per-tool gates invite workarounds — is the design center here.

## What it does

- Three LangGraph workflows (plan, act, verify, finish) drive a simulated customer's CRM, ticketing
  and document systems, each exposed as an MCP server over streamable HTTP with a scoped JWT per run.
- Mutating tool calls are planned, never executed directly: the server resolves the proposed write
  into effect instances from current database state, and anything requiring approval returns
  `approval_required` without touching data.
- The graph interrupts on the effect set; the run parks durably in Postgres until a human approves
  or denies. Approval inserts a single-use grant, and the server re-resolves effects before
  executing, closing the TOCTOU window.
- Three independent layers keep the resolver honest: the MCP role holds no INSERT/UPDATE/DELETE on
  business tables, an effect-coverage test diffs observed history deltas against predictions, and
  audit reconciliation joins claimed effects against the systems' own row-version history.
- Scoped credentials are enforced over real HTTP: no-token, wrong-scope, and foreign-row calls are
  refused and audited, and revocation stops an in-flight run.
- An operations dashboard drills every figure to primary evidence: a rate to its runs, a run to its
  effect contract, its grants with the approving human, and its ordered event log.

## Measured results

| Evidence | Result |
|---|---|
| Test suite (real Postgres, real MCP servers over HTTP) | 99 passed |
| Effect gate vs the trap that beat per-tool gating | per-tool gate: ticket closed; effect gate: all 3 routes refused, zero writes |
| Deterministic control arm, 36 instances × 3 repeats | 108/108 — model failures are attributable to the model |
| Audit chain over 4,200+ events | intact; a privileged edit is caught at the exact row |
| Audit reconciliation | unlogged=0, phantom=0, ungranted=0 — and an injected bypass write is detected |
| Scoped credentials | no-token, wrong-scope, foreign-row calls all refused and audited; revocation stops an in-flight run |
| Local-model pilot (3 instances, one per workflow) | 3/3, mean 118 s per run |
| Warm tool-calling step, `reasoning=False` on the local model | 2.2 s, vs 8–20 s with reasoning on |

One measured sweep is committed as void, on purpose: a repaired-arm run whose MCP servers were
stopped mid-flight rendered a plausible-looking 11.1%, so the harness now preflights the
environment and aborts on consecutive infra failures. A dead environment is not evidence about a
model.

## Tech stack

| Component | Choice |
|---|---|
| Agent framework | LangGraph (plan, act, verify; interrupts on effects) |
| Tool surface | MCP over streamable HTTP, scoped JWT per run |
| Database | Postgres 16 — business tables, effect plans/grants, chained audit events |
| LLM (local) | Gemma 4 31B via Ollama, `reasoning=False` |
| Dashboard | FastAPI + one static page, no build step |
| Policy | YAML effect catalog, scopes, and per-workflow contracts |
