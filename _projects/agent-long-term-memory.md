---
title: Memlayer
order: 11
group: Retrieval and memory
kind: Agent memory
repo: harsha-moparthy/agent-long-term-memory
description: >-
  A long-term memory layer for agents: raw episodes consolidated into durable semantic facts with
  provenance and recency, retrieved by embedding similarity behind a precision floor, and corrections
  that supersede old facts while retaining them as history. Measured with memory-off / on / oracle
  arms so the layer's contribution is isolated from the model's own ability.
stack: [Python, SQLite, embeddings, Ollama, Gemini]
highlights:
  - value: "+92%"
    label: memory contribution over the off arm
  - value: "8%"
    label: retrieval gap localised by the oracle arm
  - value: "4 / 4"
    label: correction scenarios with intact history
  - value: "0%"
    label: off-arm score (leak check, by design)
---

## Why this project exists

Agents forget everything between sessions. Bolting on "memory" sounds simple and is not: store every
turn and the useful facts drown in chit-chat; retrieve the wrong memory and you corrupt behaviour in a
way that is worse than having no memory at all. And when a user *changes* a fact — a new job, a new
timezone — a naive store either keeps answering with the stale value or destroys the old one and loses
the audit trail.

The hard part is not storage. It is proving the layer helps, and being able to say *which component*
failed when it doesn't.

## The three-arm design

The central measurement problem: if an agent answers a question correctly with memory enabled, that
proves nothing unless you know it would have failed without it, and that a perfect memory would have
succeeded. So every scenario runs three ways:

| arm | what it isolates |
|---|---|
| `off` | the floor — the answer lives in an earlier session this arm cannot see |
| `on` | the real system, retrieval included |
| `oracle` | the needed facts injected directly, bypassing retrieval |

`off` should score **0% by construction**. Any non-zero value means a probe was answerable without
memory and the scenario was leaking — it is a harness check, not a result. And the gap between `on`
and `oracle` attributes failure precisely: if `oracle` succeeds where `on` fails, the facts were
stored correctly and *retrieval* is what broke. That decomposition is the reason for the third arm.

## Consolidation, not accumulation

Raw episodes are summarised into semantic facts, each carrying provenance (which session and turn it
came from) and recency. Retrieval is embedding similarity behind a **precision floor** — below a
similarity threshold the layer returns nothing rather than its best guess, because a confidently wrong
memory is worse than an absent one.

Corrections are the interesting case. A new value **supersedes** the old fact rather than overwriting
it: the old row stays, marked with a `superseded_by` link. The probe returns the current value, and
the history remains auditable. All four correction scenarios pass on every provider that ran them,
with the superseded value retained and the link intact.

## Measured results

12 scenarios, 13 probes, each run through all three arms.

| provider | probes | `off` | `on` | `oracle` | memory contribution | retrieval gap | precision / recall |
|---|---|---|---|---|---|---|---|
| `fake` | 13 | 0% | 100% | 100% | **+100%** | 0% | 100% / 100% |
| `ollama` (`gemma4:31b-it-qat`) | 13 | 0% | 92% | 100% | **+92%** | 8% | 86% / 92% |
| `gemini` (`gemini-3.5-flash-lite`) | 2 | 0% | 100% | 100% | +100% | 0% | 100% / 100% |

Reading these honestly:

- **The `ollama` row is the real result.** Its 8% retrieval gap is a single probe where similarity
  ranked a plausible-but-wrong fact above the needed one. The `oracle` arm answers it correctly, which
  localises the failure to retrieval rather than to the model — exactly what the three-arm design is
  for.
- **`fake` is a tripwire, not evidence.** The deterministic offline provider scores 100% because it is
  built to; its job is to fail loudly in CI when consolidation or retrieval logic breaks.
- **The `gemini` row is a 2-probe subset and is not comparable** to the 13-probe rows. It shows the
  provider adapter works end to end, nothing more.

### Why the Gemini run is short

Not by choice. A full run needs ~72 chat calls, and the free tier meters `generate_content` per day
*per model*: 500/day on `gemini-3.5-flash-lite`, but only **20/day** on `gemini-3.6-flash`. Retries
against a throttled model consume the same quota, so one 11-minute attempt exhausted a 500-call budget
without finishing. Three models were tried in a day and all hit their cap. Hence the `--cache` flag:
the 13-probe Gemini run can be completed incrementally across days instead of restarting from zero.
Stated rather than quietly omitted.
