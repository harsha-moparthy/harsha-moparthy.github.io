---
title: Two-Week Prototypes
track: fde
order: 17
group: Agent deployment
kind: Engagement kit
repo: harsha-moparthy/two-week-prototype-portfolio
description: >-
  One reusable engagement kit built once (1,455 lines), then three agent-powered apps for three
  customers — grounded RAG, a human-in-the-loop quoting agent, and governed MCP tools — each on a
  two-week clock with a measured before/after. The quoting agent scores 8/8 where the flat-fee
  baseline scores 0/8, and a rogue read-only token is denied on all 15 mutation attempts.
stack: [Python, MCP, SQLite, Ollama, Gemini, GitHub Actions]
highlights:
  - value: "86"
    label: offline tests, kit + three engagements
  - value: "8/8 vs 0/8"
    label: Frontdesk quotes vs flat-fee baseline
  - value: "15/15"
    label: rogue read-only calls denied, 0 mutations
  - value: "13/15"
    label: held-out generalization probe
---

## Why this project exists

Forward-deployed teams ship working software inside a customer's sprint — roughly two weeks from
first conversation to deployed value. The skill on display is not depth in one system; it is scope
discipline under a hard deadline: discovery, ruthless cutting, deployment plumbing reused across
engagements, usage instrumented from day one, and honest measurement of whether the thing helped.

So this is deliberately not one big system. It is a kit built once plus three small apps on top of
it, each leaning on a different capability, each documented like an engagement with requirements,
cut scope, trade-offs, and a measured outcome. The reuse claim is checkable: no kit module imports
an engagement, and the line counts show where the work went — 1,455 lines of kit against 188, 524
and 543 lines per app.

## What it does

- The kit provides one LLM seam (fake, Ollama, Gemini) with uniform cost accounting, a RAG pipeline
  with an honest "not in the context" path, a human-in-the-loop agent loop whose review gate is
  structurally unbypassable, HMAC capability tokens, shared telemetry, stdlib HTTP hosting, and a
  before/after eval harness.
- Trailhead (running club): grounded, cited RAG over route notes — 6/6 vs 5/6 for keyword search,
  with an honest decline on the unanswerable question.
- Frontdesk (one-person bike repair): messy inbound texts become structured quotes parked for human
  approval — 8/8 vs 0/8 for the rushed flat fee, which under-charges the premium job by $209.
- Benchtop (research lab): governed MCP tools over shared inventory plus SOP RAG — 5/5 vs 1/5 for
  ctrl-F, and the baseline hallucinates on the question the SOPs never answer.
- CI is load-bearing: it re-runs every before/after eval and fails if an app stops beating its
  baseline, if a read-only token can mutate inventory, if a high-stakes quote can send without a
  human, or if sabotaged retrieval still produces the right answer.

## Measured results

| Evidence | Result |
|---|---|
| Test suite (kit + three engagements, fully offline) | 86 passed |
| Trailhead — grounded RAG vs keyword search | 6/6 vs 5/6, every answer cited |
| Frontdesk — agent quotes vs a rushed flat fee | 8/8 vs 0/8; baseline under-charges the premium job by $209 |
| Benchtop — SOP Q&A vs ctrl-F | 5/5 vs 1/5; the baseline hallucinates on the unanswerable question |
| Benchtop — governance under attack | read-only token: 15 mutating calls, 15 denied, 0 mutations, counted from inventory state |
| Eval honesty — sabotaged retrieval | both RAG apps return NOT_IN_CONTEXT, never the right answer |
| Generalization — 15 held-out questions | 13/15, including both correctly declined unanswerables |
| All three HTTP apps over real sockets | health 200, missing key 401, tech mutation 403, manager mutation 200 |
| Cross-engagement usage rollup | 45 events across 3 engagements, 21 sessions in one shared store |
| Engagement cadence | 14 / 12 / 11 days |

The baselines are not strawmen: the keyword baseline genuinely wins most of Trailhead's tasks, and
saying so is the finding — on a small tidy corpus, retrieval is not the expensive part. What
survives is the multi-constraint question a single best line cannot answer.

## Tech stack

| Component | Choice |
|---|---|
| LLM seam | fake / Ollama / Gemini, one interface, uniform cost accounting |
| Governed tools | MCP low-level Server API, scoped capability tokens |
| Storage | SQLite; hosting is stdlib `http.server` with per-route auth |
| Retrieval | in-process chunk/embed/retrieve with a deterministic offline embedder |
| Evals | before/after harness, checkers over end state, no LLM graders |
| CI | GitHub Actions gate re-running every eval and every governance check |
