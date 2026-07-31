---
title: BotShop
track: backend
order: 72
group: Platform studies
kind: API design study
repo: harsha-moparthy/botshop
description: >-
  Agent-facing API design, measured instead of asserted: one commerce store, two API surfaces of
  identical functionality, and a 20-task agent evaluation judged only by final store state. The
  same 8B model nearly doubles task success on the agent-optimized surface (63% vs 35%), recovers
  9/9 fault-injected tasks, and produces zero duplicate purchases thanks to required idempotency
  keys.
stack: [Go, Ollama, qwen3:8b, MCP, JSON Schema, REST]
highlights:
  - value: "63% vs 35%"
    label: task success, agent surface vs baseline
  - value: "9/9"
    label: fault-injected tasks recovered, vs 4/9 baseline
  - value: "0"
    label: duplicate purchases under response loss
  - value: "0"
    label: cap violations in all 9 capped runs
---

## Why this project exists

The claim "agents need different API design" is usually asserted, not measured. Here it is
measured: the same off-the-shelf local model (qwen3:8b via Ollama) runs the same 20 shopping
tasks against three conditions — a conventional well-built REST API driven by raw HTTP, the same
API behind typed tool wrappers, and a redesigned agent surface — and success is judged only by
final store state, never by what the agent says it did. The typed-wrapper condition exists to
isolate the variable: any remaining gap is attributable to the surface design itself, not tool
typing.

## What it does

- Requires an `Idempotency-Key` on every mutation: replays return the stored response verbatim,
  50 simultaneous identical checkouts produce exactly one order (tested), and reusing a key for a
  different request is a 422.
- Returns errors that say what to do next: `{code, message, retriable, details, remediation}`,
  where remediation names the exact tools that fix the situation.
- Mints scoped capability tokens with server-enforced spend and order caps using
  reservation-before-action — 10 simultaneous $12 checkouts against a $36 cap succeed exactly 3
  times (tested).
- Publishes a machine-readable tool catalog (`GET /agent/v1/tools`, name + JSON Schema + HTTP
  binding); the MCP server and the eval harness both bind to it — the catalog is the contract.
- Injects faults deterministically: three tasks "lose" the response of a mutation the server
  actually processed, the classic duplicate-mutation window.

## Measured results

qwen3:8b, 20 tasks × 3 trials per condition, state-judged.

| Evidence | Result |
|---|---|
| Task success | agent surface 38/60 (63%) vs baseline HTTP 21/60 (35%) and baseline typed 19/60 (32%) — typed tools alone did not help |
| Fault injection (response loss on mutations, 3 tasks) | agent surface 9/9; baseline typed 6/9; baseline HTTP 4/9 |
| Duplicate purchases under fault | 0 on the agent surface — transcripts show retries with the same idempotency key getting the replayed order back |
| Spend caps | 0 violations in all 9 capped runs; enforcement is structural |
| Recovery tasks | out-of-stock-with-alternative and price-conditional purchase: 3/3 on the agent surface vs 0/3 on both baselines |
| Honest loss | conditional-skip ("buy only if under 1000 cents") went 0/3 on the agent surface vs 3/3 baseline — workflow-reinforcing tool descriptions bias an 8B model toward completing purchases; all 3 unintended orders are this task |

Five tasks failed everywhere (multi-constraint arithmetic, vocabulary mismatch): surface design
does not fix reasoning. The higher failed-tool-call count on the agent surface (49, at 5.7
calls/run vs 2.8) is the design working — typed rejections are recoverable signposts the agent
kept operating through, where the baselines gave up early.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go, zero dependencies (`go.mod` has no requires) |
| Store | In-memory commerce core shared by both surfaces |
| Baseline surface | Conventional REST: correct status codes, prose errors, bearer auth |
| Agent surface | Required idempotency, typed errors with remediation, capability tokens, tool catalog |
| MCP | Minimal JSON-RPC 2.0 over stdio, bridging to the agent surface |
| Evaluation | 20 tasks, fault injection, state-based checkers, resumable harness against Ollama |
