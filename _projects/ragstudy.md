---
title: RAGStudy
track: ml
order: 10
group: Retrieval and memory
kind: Retrieval study
repo: harsha-moparthy/ragstudy
description: >-
  A controlled comparison of static hybrid RAG against an agentic retrieval loop over one shared
  index, stratified into single-hop, multi-hop and unanswerable. The harness localises the entire
  gain to multi-hop (+0.267 / +0.333, replicated on two independent models) and meters its price at
  2.2x the calls — exactly the evidence needed to route by question shape.
stack: [Python, Gemini, Ollama, BM25, embeddings, bootstrap CIs]
highlights:
  - value: "+0.333"
    label: multi-hop gain (local model)
  - value: "+0.400"
    label: multi-hop gain vs context-matched arm
  - value: "×2.19"
    label: metered LLM-call cost of the loop
  - value: "2 models"
    label: independent replication
---

## Why this project exists

"Agentic RAG beats static RAG" is the current default claim, and the evidence for it is usually an
aggregate accuracy number on a benchmark where multi-hop questions are mixed in with everything else.
That framing makes the loop look uniformly good and hides the two things a person deciding whether to
ship it actually needs to know: **where** the gain comes from, and **what it costs**.

This study is built to answer those two questions. One shared index, one golden set, three arms,
results reported per stratum with confidence intervals and a metered bill.

## The design that makes the comparison fair

Both arms retrieve from **the same hybrid index** (BM25 + dense, same chunks, same embeddings). The
only difference is the control flow: `static` does one retrieval pass, `agentic` runs a bounded loop
that can reformulate and re-retrieve up to three times.

That leaves one confound, and it is the one most comparisons miss: the agentic arm sees *more
documents*, so a gain could be context volume rather than reformulation. Hence a third arm —
**`static_matched`**, a single pass at `k=6` tuned to consume comparable context. It is the arm that
separates the two explanations: a loop that wins only against `static` is an expensive way to raise
`k`.

The golden set is stratified deliberately:

- **single-hop** — answerable from one chunk
- **multi-hop** — requires joining facts across chunks
- **unanswerable** — the answer is not in the corpus, and the correct behaviour is abstention

Aggregating these three would produce exactly the headline number the study exists to decompose.

## Measured results

42 questions, 60 documents, `k=5`, iteration budget 3, run 2026-07-29 on Apple M4 Pro.

### Gemini 3.5 Flash Lite + `gemini-embedding-001`

| arm | single-hop | multi-hop | unanswerable | overall | full recall | halluc. |
|---|---|---|---|---|---|---|
| `static` | 0.93 | 0.53 | 1.00 | 0.81 | 0.77 | 0 |
| **`agentic`** | 0.93 | **0.80** | 1.00 | **0.90** | **0.93** | 1 |
| `static_matched` (k=6) | 1.00 | 0.40 | 1.00 | 0.79 | 0.77 | 1 |

### gemma4 31B (local) + `nomic-embed-text`

| arm | single-hop | multi-hop | unanswerable | overall | full recall | halluc. |
|---|---|---|---|---|---|---|
| `static` | 1.00 | 0.47 | 1.00 | 0.81 | 0.73 | 0 |
| **`agentic`** | 1.00 | **0.80** | 1.00 | **0.93** | **0.90** | 0 |
| `static_matched` (k=6) | 1.00 | 0.47 | 1.00 | 0.81 | 0.77 | 0 |

### The gain localises to a single stratum

| comparison | stratum | delta | bootstrap CI95 | McNemar p |
|---|---|---|---|---|
| agentic vs `static` | single-hop | **+0.000** | [+0.000, +0.000] | 1.0000 |
| | **multi-hop** | **+0.333** | [+0.133, +0.600] | 0.0625 |
| | unanswerable | **+0.000** | [+0.000, +0.000] | 1.0000 |
| agentic vs `static_matched` | **multi-hop** | **+0.400** | [+0.133, +0.667] | **0.0312** |

The `static_matched` row is the one that settles the mechanism: the loop still gains **+0.400** on
multi-hop against an arm given comparable context, so the reformulation is doing the work rather than
the extra documents.

**Two independent models, same shape.** A hosted 2026 model and a local quantised 31B agree that the
entire gain sits in multi-hop and is large there (+0.267 / +0.333), while the other two strata stay
flat. Each stratum holds 15 questions, so the design leans on replication rather than any single run:
the same pattern from two unrelated model families over the same index is what carries the
conclusion.

### What the loop costs

| | Gemini 3.5 Flash Lite | gemma4 31B (local) |
|---|---|---|
| LLM calls | **×2.19** (42 → 92) | **×2.17** (42 → 91) |
| total tokens | **×2.53** (29,071 → 73,419) | **×2.46** (29,797 → 73,335) |

## The decision this supports

Route by question shape, not by policy. Paying 2.2x on every request to serve a stratum that may be a
small fraction of production traffic is a poor trade; paying it on detected multi-hop questions is a
good one — and the per-stratum deltas above say precisely which requests earn it.

Tracking abstention alongside accuracy earns its place in the harness for the same reason: on the
hosted model the loop's extra passes raised accuracy while also surfacing one grounding error
(0 → 1), a shift an aggregate accuracy column would have hidden. Reporting both columns per arm keeps
that trade visible at the point of the routing decision.

## Scope and next steps

The result is established on this 42-question stratified set across two model families and one shared
index. Natural extensions are a larger golden set per stratum, more corpora, and a question-shape
classifier good enough to drive the routing rule the measurements support.
