---
title: GenAI Observability
track: ml
order: 13
group: Cost and observability
kind: Observability
repo: harsha-moparthy/genai-observability-otel
description: >-
  An instrumented RAG agent emitting OpenTelemetry GenAI-convention telemetry through a collector into
  Jaeger/Prometheus/Grafana: 356 spans validated against the vendored spec model with zero violations,
  cost attribution per feature and tenant, tail sampling that keeps every error and every
  quality-regressed trace, and a staged prompt regression diagnosed from telemetry alone.
stack: [Python, OpenTelemetry, OTel Collector, Jaeger, Prometheus, Grafana, Ollama, Gemini]
highlights:
  - value: "356 / 0"
    label: spans validated / violations
  - value: "20 / 20"
    label: error traces kept by the sampler
  - value: "6 / 6"
    label: regressed traces kept by the quality policy
  - value: "2.8x"
    label: sampling correction applied to reported spend
---

## Why this project exists

Teams shipping LLM features need to answer basic questions: what did this request cost, which prompt
version produced this answer, where did the latency go. OpenTelemetry standardized how to record AI calls
in 2025–26, and wiring it up properly is a new skill with very little accumulated folklore.

The interesting knowledge isn't "can you emit a span." It's what the conventions **under-specify**, and
which parts of the pipeline fail **silently** — because that is the characteristic failure mode of
observability work. Nothing throws, the dashboard renders, and the numbers are simply absent or quietly
wrong. This project is built to surface that class of failure before an incident does.

## Conformance, enforced against the spec

"Follows the GenAI semantic conventions" is a claim worth verifying, and the conventions are marked
*development* — they moved repositories mid-2026 and are explicitly allowed to break. So the
**machine-readable spec is vendored into the repo and parsed at runtime**, and a conformance checker
validates emitted telemetry against the actual requirement levels rather than attribute names typed from
memory.

It checks span names, span kinds, required attributes, enum membership, event names, unknown `gen_ai.*`
attributes, and the project's own cardinality rule. The checker is also fed deliberately broken
telemetry in tests, so its ability to **reject** bad telemetry is demonstrated rather than assumed.

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

Two trace pipelines, deliberately. RED metrics are derived from **unsampled** spans so rates stay exact;
only storage is sampled. Deriving them after the sampler would scale every rate in Grafana by the
sampling factor, with nothing on the dashboard looking broken.

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

Cost is an integer count of USD-micros on each span, so totals stay exact under aggregation instead of
accumulating float error. The report publishes both the sampled sum and the keep-rate-scaled estimate
and labels which is which — here the sampled sum alone would understate spend by **2.8x**. A model with
no rate card is recorded as **unpriced, not free**, so a new model rollout surfaces as missing pricing
rather than as silently free traffic.

## The staged incident

A plausible Friday prompt edit — friendlier tone, "feel free to speculate," grounding instruction
dropped — shipped as `rag-answer` v2.0.0 and was diagnosed from stored spans alone:

| signal | v1 grounded (60 traces) | v2 chatty (6 traces) | change |
|---|---:|---:|---:|
| eval: groundedness | 0.808 | 0.000 | **−100%** |
| avg output tokens | 163 | 400 (capped) | **+145%** |
| avg cost (USD-micros) | 51.0 | 174.8 | **+242%** |
| avg end-to-end latency | 26.7s | 50.9s | **+91%** |
| responses truncated at `max_tokens` | 0 | **6 of 6** | |

The telemetry localizes the mechanism: the chatty prompt spends its token budget on preamble and gets
truncated **before answering**. One prompt edit tripled per-request cost and doubled latency, and the
pipeline attributes all of it to a specific prompt version without reproducing the request.

An earlier probe surfaced the other shape of the same regression: when the verbose answer did complete,
keyword correctness **rose to 1.00** while groundedness collapsed to 0.126 — the rambling reply happened
to contain the expected words. A single correctness score would have reported that regression as an
improvement. That result is why the pipeline records several independent quality signals per request.

## What the conventions under-specify

These are findings the harness produced, each reproducible against the live stack.

1. **A tail sampler cannot read span events.** The conventions model evaluation results as
   `gen_ai.evaluation.result` events — but sampling policies match span *attributes*, so "keep every
   trace whose answer quality failed" is inexpressible as specified. It requires a deliberate
   denormalisation of the verdict onto the root span, which is what makes the 6 / 6 quality-policy
   retention above possible.
2. **`decision_wait` is a correctness constraint, not a tuning knob.** It must exceed p100 request
   duration, and the cost of violating that is measurable: at 8s against 40s inference the sampler
   judges trace *fragments* — the root span carrying cost and quality has not arrived — and every cost-
   and quality-based policy votes to drop, losing **4/4 traces with no error signal**. The project pins
   `decision_wait` above measured p100 for that reason.
3. **No cost attribute exists anywhere in the registry.** `gen_ai.usage.*` is tokens only; money is
   entirely the application's problem, which is why cost attribution here is a first-class span
   attribute rather than a dashboard-side calculation.
4. **Thinking tokens are billed but easy to miss.** Gemini reports `thoughtsTokenCount` separately and
   bills it as output; on one measured call the hidden reasoning was 11x the visible answer. The local
   model exposes no thinking field at all and returns an *empty string* with `done_reason="length"` when
   its budget is too small — an empty answer, HTTP 200, and a token count proving work was done.
5. **The monitoring system observes itself.** Jaeger's query extension carries its own `enable_tracing`
   switch, independent of the service-level one, so span counts read back from the store can include
   traffic generated by the act of reading them. Verification here accounts for that explicitly.

Twelve such silent-failure modes are written up in the repo's findings document, each diagnosed to root
cause rather than worked around.
