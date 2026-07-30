---
title: Memlayer
track: ml
order: 11
group: Retrieval and memory
kind: Agent memory
repo: harsha-moparthy/agent-long-term-memory
description: >-
  A long-term memory layer for agents: raw episodes consolidated into durable semantic facts with
  provenance and recency, retrieved by embedding similarity behind a precision floor, and corrections
  that supersede old facts while retaining them as auditable history. A three-arm harness
  (memory-off / on / oracle) isolates the layer's contribution from the model's own ability and
  attributes each probe to a named component, measuring a +92% memory contribution on a local model.
stack: [Python, SQLite, embeddings, Ollama, Gemini]
highlights:
  - value: "+92%"
    label: memory contribution over the off arm
  - value: "86% / 92%"
    label: retrieval precision / recall on the local model
  - value: "4 / 4"
    label: correction scenarios with intact history
  - value: "0%"
    label: off-arm leak check, passing by construction
---

## Why this project exists

Agents forget everything between sessions, and bolting on "memory" is a measurement problem as much as
a storage one: store every turn and the useful facts drown in chit-chat; retrieve the wrong memory and
behaviour degrades instead of improving. And when a user *changes* a fact — a new job, a new timezone —
a naive store either keeps answering with the stale value or overwrites the old one and loses the audit
trail.

So the design goal was twofold: build the layer, and build a harness that quantifies what it
contributes and attributes any miss to a specific component.

## The three-arm design

A correct answer with memory enabled is only evidence if you also know the agent would have failed
without it, and that a perfect memory would have succeeded. So every scenario runs three ways:

| arm | what it isolates |
|---|---|
| `off` | the floor — the answer lives in an earlier session this arm cannot see |
| `on` | the real system, retrieval included |
| `oracle` | the needed facts injected directly, bypassing retrieval |

`off` scores **0% by construction**, and the harness treats any non-zero value as a leaking scenario —
a probe answerable without memory — rather than as a result. The gap between `on` and `oracle` then
attributes precisely: when `oracle` succeeds where `on` does not, the facts were stored correctly and
retrieval is the component to fix. That decomposition is the reason for the third arm.

## Consolidation, not accumulation

Raw episodes are summarised into semantic facts, each carrying provenance (which session and turn it
came from) and recency. Retrieval is embedding similarity behind a **precision floor** — below a
similarity threshold the layer returns nothing rather than its best guess, so it abstains instead of
injecting a low-confidence memory.

Corrections are the interesting case. A new value **supersedes** the old fact rather than overwriting
it: the old row stays, marked with a `superseded_by` link. The probe returns the current value, and the
history remains auditable. All four correction scenarios pass on every provider that ran them, with the
superseded value retained and the link intact.

## Measured results

12 scenarios, 13 probes, each run through all three arms.

| provider | probes | `off` | `on` | `oracle` | memory contribution | retrieval gap | precision / recall |
|---|---|---|---|---|---|---|---|
| `fake` | 13 | 0% | 100% | 100% | **+100%** | 0% | 100% / 100% |
| `ollama` (`gemma4:31b-it-qat`) | 13 | 0% | 92% | 100% | **+92%** | 8% | 86% / 92% |
| `gemini` (`gemini-3.5-flash-lite`) | 2 | 0% | 100% | 100% | +100% | 0% | 100% / 100% |

What the runs establish:

- **The `ollama` row carries the headline result:** a +92% memory contribution over a floor that is 0%
  by construction, with the leak check passing on every scenario.
- **The harness attributes the single remaining probe to retrieval, not to the model.** Similarity
  ranked a plausible alternative fact above the needed one, and the `oracle` arm answers the same probe
  correctly — the 8% gap is therefore a ranking condition, which is exactly the attribution the
  three-arm design exists to produce.
- **`fake` is the CI tripwire.** The deterministic offline provider scores 100% by design, so any
  regression in consolidation or retrieval logic fails loudly in continuous integration.
- **The `gemini` row is a 2-probe subset** that validates the provider adapter end to end; the
  13-probe rows carry the comparative measurement.

## Scope and next steps

The Gemini arm surfaced a concrete platform constraint worth designing around. A full run needs ~72
chat calls, and the free tier meters `generate_content` per day *per model*: 500/day on
`gemini-3.5-flash-lite`, but only **20/day** on `gemini-3.6-flash`. Retries against a throttled model
draw on the same quota, so a single 11-minute attempt can consume a 500-call budget, and all three
models tried in one day reached their cap. That measurement motivated the `--cache` flag, which lets
the 13-probe Gemini run accumulate incrementally across days rather than restarting from zero — the
next step for bringing the hosted-provider arm up to the same probe count as the local one.
