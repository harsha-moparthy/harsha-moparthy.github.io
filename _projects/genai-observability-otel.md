---
title: GenAI Observability
order: 13
group: Cost and observability
kind: Observability
repo: harsha-moparthy/genai-observability-otel
description: >-
  An instrumented RAG agent emitting OpenTelemetry GenAI-convention telemetry through a collector into
  Jaeger/Prometheus/Grafana — with conformance enforced against the vendored spec model, cost
  attribution per feature and tenant, tail sampling that keeps every error and regressed trace, and a
  staged prompt regression diagnosed from telemetry alone.
stack: [Python, OpenTelemetry, OTel Collector, Jaeger, Prometheus, Grafana, Ollama, Gemini]
highlights:
  - value: "356 / 0"
    label: spans validated / violations
  - value: "20 / 20"
    label: error traces kept by the sampler
  - value: "56 / 94"
    label: exemplars resolving to stored traces
  - value: "2.8x"
    label: spend understated if sampling ignored
---

## Why this project exists

Teams shipping LLM features cannot answer basic questions: what did this request cost, which prompt
version produced this bad answer, where did the latency go. OpenTelemetry standardized how to record AI
calls in 2025–26, and wiring it up properly is a new skill with very little accumulated folklore.

The interesting knowledge isn't "can you emit a span." It's what the conventions **under-specify**, and
which parts of the pipeline fail **silently** — because that is the characteristic failure of
observability work. Nothing throws. The dashboard renders. The numbers are just absent, or quietly
wrong by a factor of five, and you find out during an incident.

## The claim that needed proving

"Follows the GenAI semantic conventions" is a claim, and the conventions are marked *development* —
they moved repositories mid-2026 and are explicitly allowed to break. So the **machine-readable spec is
vendored into the repo and parsed at runtime**, and a conformance checker validates emitted telemetry
against the actual requirement levels rather than attribute names typed from memory.

It checks span names, span kinds, required attributes, enum membership, event names, unknown `gen_ai.*`
attributes, and the project's own cardinality rule. It is fed deliberately broken telemetry in tests,
because **a checker that can only pass is indistinguishable from no checker**.

```
$ obs conformance --source jaeger
spans checked:   356
by operation:    chat=66, execute_tool=92, invoke_agent=66, invoke_workflow=66, retrieval=66
CONFORMANT: no violations
```

## Architecture

```text
                    ┌─────────────────────────── 100% of spans
                    ▼
  RAG agent ──OTLP──► collector ──► spanmetrics ──► Prometheus ──► Grafana
  (instrumented)      │                              (exemplars)      │
                      └─ tail_sampling ──► Jaeger ◄─────trace_id──────┘
```

Two trace pipelines, deliberately. RED metrics are derived from **unsampled** spans so rates stay
exact; only storage is sampled. Deriving them after the sampler would make every rate in Grafana wrong
by the sampling factor, and nothing would look broken.

There is no Docker on the target machine and Grafana ships no macOS Tempo build, so Jaeger v2 — itself
built on the OTel Collector, and OTLP-native — is the trace store. The whole stack is four native
processes.

## Measured results

All figures produced by scripts in the repo against the live stack. 94 offline tests pass;
`obs verify-stack` reports 10/10 checks.

| | |
|---|---|
| spans validated (read back from Jaeger) | **356**, **0 violations** |
| GenAI metrics emitted, all spec-named | **7 / 7** |
| error traces retained by the sampler | **20 / 20 (100%)** |
| regressed traces retained by the quality policy | **6 / 6**, while 84 healthy ones were dropped |
| exemplars resolving to stored traces | **56 / 94** |
| sampled spend → estimate scaled by keep rate | $0.004112 → **$0.011362** |

Cost is an integer count of USD-micros on each span — floats accumulate error, and a cost report that
disagrees with itself is worse than none. Reporting the sampled sum as total spend would understate it
by **2.8x** here, so the report gives both figures and labels which is which. A model with no rate card
is recorded as **unpriced, not free**, because treating unknown models as $0 is exactly how a cost
dashboard under-reports a new model rollout.

## The staged incident

A plausible Friday prompt edit — friendlier tone, "feel free to speculate," grounding instruction
dropped — shipped as `rag-answer` v2.0.0 and diagnosed from stored spans alone:

| signal | v1 grounded (60 traces) | v2 chatty (6 traces) | change |
|---|---:|---:|---:|
| eval: groundedness | 0.808 | 0.000 | **−100%** |
| avg output tokens | 163 | 400 (capped) | **+145%** |
| avg cost (USD-micros) | 51.0 | 174.8 | **+242%** |
| avg end-to-end latency | 26.7s | 50.9s | **+91%** |
| responses truncated at `max_tokens` | 0 | **6 of 6** | |

The chatty prompt spends its whole token budget on preamble and gets truncated **before answering**.
One edit tripled per-request cost, doubled latency, and produced no usable answer.

An earlier probe caught the other shape of the same bug: when the verbose answer did complete, keyword
correctness **rose to 1.00** while groundedness collapsed to 0.126 — the rambling reply happened to
contain the expected words. A single correctness score would have reported the regression as an
improvement. That is why the pipeline records several independent quality signals per request.

## What the conventions under-specify

1. **A tail sampler cannot read span events.** The conventions correctly model evaluation results as
   `gen_ai.evaluation.result` events — but sampling policies match span *attributes*, so "keep every
   trace whose answer quality failed" is inexpressible as specified. It needs a deliberate
   denormalisation onto the root span.
2. **`decision_wait` is a correctness constraint, not a tuning knob.** It must exceed p100 request
   duration. At 8s against 40s inference the sampler judged trace *fragments* — the root span carrying
   cost and quality hadn't arrived — and every cost- and quality-based policy voted to drop. **4/4
   traces lost, silently.**
3. **No cost attribute exists anywhere in the registry.** `gen_ai.usage.*` is tokens only; money is
   entirely the application's problem.
4. **Thinking tokens are billed but easy to miss.** Gemini reports `thoughtsTokenCount` separately and
   bills it as output; on one measured call the hidden reasoning was 11x the visible answer. The local
   model exposes no thinking field at all and returns an *empty string* with `done_reason="length"`
   when its budget is too small — an empty answer, HTTP 200, and a token count proving work was done.
5. **The monitoring system observes itself.** Jaeger's query extension has its own `enable_tracing`
   switch, separate from the service-level one, so this project's own verification scripts were
   inflating the span counts they measured.

Twelve such silent failures are written up in the repo's findings document, each diagnosed rather than
worked around.
