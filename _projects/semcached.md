---
title: SemCached
track: sde
order: 43
group: Delivery, evaluation, and caching
kind: Caching proxy
repo: harsha-moparthy/semcached
description: >-
  A semantic caching proxy for LLM APIs that treats the wrong-hit rate as a first-class, measured
  number: on human-labeled replay traffic the shipped 0.92 threshold buys a 33.1% hit rate at a 6.0%
  wrong-hit rate and a 32.4% cost reduction, with tenant and prompt isolation that is structural
  rather than probabilistic.
stack: [Python, FastAPI, ONNX Runtime, bge-small-en-v1.5, uvicorn]
highlights:
  - value: "6.0%"
    label: wrong-hit rate at the shipped 0.92 threshold
  - value: "32.4%"
    label: cost reduction on the QQP replay
  - value: "33.1%"
    label: overall hit rate at 0.92
  - value: "1.4 ms"
    label: exact-hit p50; semantic hit 7.3 ms
---

## Why this project exists

LLM calls are expensive and much real traffic is near-duplicate: the same question phrased slightly
differently. Caching by meaning instead of exact bytes can cut real bills — Portkey, LiteLLM,
Helicone, and Cloudflare's AI Gateway all ship this. The catch is that a wrong semantic hit silently
serves someone an answer to a different question. The engineering problem is not the cache; it is the
correctness accounting around the cache.

Two questions get first-class answers here. How many hits were wrong? Measured against human labels:
replay traffic is built from Quora Question Pairs, with `is_duplicate=0` pairs kept as hard negatives —
lexically close, semantically different, exactly the pairs that punish a loose threshold. And what
stops a hit crossing a tenant or prompt boundary? The index is partitioned by (tenant, cache version,
model, sampling params, hash of the full conversation context); similarity search never crosses a
partition, proven by a test with a deliberately over-eager fake embedder reporting cosine 1.0 for
every pair.

## What it does

- Two-tier lookup: exact (SHA-256 of the normalized request — Unicode NFKC, whitespace, key order,
  float noise) then semantic (bge-small-en-v1.5 ONNX embedding of the final user message, brute-force
  cosine inside the partition only)
- Semantic matching applies only to the final user message; system prompt, tools, and prior turns are
  hashed into the partition key and must match exactly — cross-conversation matching is where wrong
  hits explode
- Requests with temperature above 0.3 are never cached in either direction: serving a cached sample
  to a caller who asked for a high-entropy distribution is a correctness bug, not a savings
- Streaming: a stream miss is teed to the client while being assembled, cached only on a clean
  `finish_reason: stop`; a hit can be re-served as OpenAI-style SSE chunks
- Savings are credited from upstream-reported usage stored per entry — no token heuristics in the
  accounting path
- Client contract: `X-Tenant`, `X-Cache-Version` (bump to invalidate after a prompt change), bypass
  header, and response headers reporting hit type, similarity, and matched tag; admin endpoints for
  stats, flush, and purge

## Measured results

QQP replay: 3,658 requests over 2,098 human-labeled duplicate clusters. A semantic hit is wrong iff
the matched cached question lives in a different cluster — no LLM judge, no self-grading.

| Evidence | Result |
|---|---|
| Threshold sweep (15 points) | at 0.80: 48.4% hits but **20.7% wrong**; at 0.92: **33.1% hits, 6.0% wrong**; at 0.97: 21.8% hits, 1.7% wrong — the curve says out loud that hit rate is bought with wrong answers |
| Live replay through the real HTTP proxy at 0.92 | reproduced the offline simulation exactly: 393 exact hits, 818 semantic hits (49 wrong), 2,447 misses, **0 upstream errors** |
| Cost accounting (gpt-4o-mini list prices, upstream-reported usage) | **$0.0451 saved on $0.1391 of would-be spend — 32.4%**, every credited token traceable to a stored usage record |
| Latency | exact hit p50 **1.4 ms**, semantic hit p50 **7.3 ms**, miss (forward) p50 133.6 ms |
| Isolation | byte-identical questions under a different tenant, model, system prompt, or version tag cannot cross buckets even at threshold 0 |
| Test suite | 24 tests, offline, no model download |

The committed wrong-hit examples are the argument for the strict end of the curve: "What are the
differences between a girl and a lady?" matched a different-cluster neighbor at cosine 0.9485 —
embeddings simply cannot distinguish some pairs humans labeled as different.

## Tech stack

| Component | Choice |
|---|---|
| Proxy | FastAPI + uvicorn, OpenAI-compatible pass-through with SSE streaming |
| Embeddings | bge-small-en-v1.5 via ONNX Runtime on CPU |
| Store | Two tiers, partitioned in-memory store behind a `CacheStore` interface |
| Evaluation | QQP-derived replay traffic, threshold sweep, live HTTP replay, tradeoff curve |
| Upstream | Deterministic mock (SSE + usage) for replay; any OpenAI-compatible base URL in production |
