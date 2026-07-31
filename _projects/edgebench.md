---
title: EdgeBench
track: backend
order: 71
group: Platform studies
kind: Platform study
repo: harsha-moparthy/edgebench
description: >-
  Edge vs serverless vs container, measured honestly: the same API (byte-identical responses,
  parity-tested) under workerd isolates, a Lambda-semantics host, and a long-lived container.
  Isolate cold starts land at p50 17.7 ms versus 78.5-99.1 ms of process boot, warm latency ties
  within ~1 ms, and a cost model verified against the vendors' own pricing examples shows a 6.5x
  spread on an LLM proxy at 100M requests/month.
stack: [Node.js, workerd, Go, Postgres 16, k6-style harness, Python cost model]
highlights:
  - value: "17.7 ms"
    label: isolate cold start p50, vs 79/99 ms process boot
  - value: "~1 ms"
    label: warm-latency spread across all three platforms
  - value: "207 rps"
    label: serverless LLM-proxy ceiling, a real platform limit
  - value: "$37 vs $242"
    label: Workers vs Lambda, LLM proxy at 100M req/mo
---

## Why this project exists

Teams pick between edge runtimes, serverless functions, and containers based on vendor marketing.
This repo measures instead: one identical API (three workload types), executed under the three
platforms' actual runtime mechanics, with a cold-start forcing protocol,
coordinated-omission-safe load generation, and a cost model verified against the vendors' own
published pricing examples. It states plainly what it is: a single-machine study of
execution-model mechanics, not a measurement of any vendor's production network.

## What it does

- Runs the same application code under three execution models: workerd (Cloudflare's open-source
  Workers runtime, V8 isolates), slshost (a Lambda-semantics host built for this study: init-once
  environments, one request in flight per environment, scale-out cold starts, throttling), and a
  plain long-lived Node.js container.
- Exercises three workload shapes: CPU-bound JSON transform, single-row Postgres read, and a
  proxy to a slow streaming mock LLM (200 ms TTFB, 10 ms/token) — the shape that breaks platforms
  differently.
- Enforces parity with a three-way test suite asserting byte-identical responses, so differences
  are the execution model and nothing else.
- Measures open-loop warm latency from each request's scheduled send time (no coordinated
  omission) and forces genuine cold starts (n=25 per cell).
- Models cost from cited, dated list prices driven by measured durations; `--self-test`
  reproduces Cloudflare's, AWS Lambda's, and Fargate's own published pricing examples.

## Measured results

Apple M4 Pro, Node 22.23, workerd 1.20260731.1, Postgres 16.

| Evidence | Result |
|---|---|
| Cold start, transform | edge p50 17.7 ms; serverless 78.5 ms; container 99.1 ms — isolates skip process boot entirely |
| Cold start, dbread | edge p50 21.7 ms; serverless 142 ms; container 129 ms (a ~65 ms init-time DB connect lands on whoever connects at init) |
| Warm latency at 200 rps | all three within ~1 ms (transform p50 1.1-1.5 ms) — execution model is a cold-start and cost decision, not a warm-latency one |
| Throughput, transform / dbread | container wins: 12,297 and 14,293 rps vs ~7.5k edge, 6.4-8.2k serverless |
| Throughput, llmproxy | serverless caps at 207 rps — one 520 ms upstream call per environment means you scale environments, not CPU; ramping to 256 concurrent made it drop to 187 rps. Edge and container hit the load generator's 512 rps bound, not saturated |
| Cost, LLM proxy at 100M req/mo | Workers $37 (CPU-ms billing, I/O wait free) vs Lambda $242 (wall-clock billing); at 1B: $361 vs $2,417 |
| Cost crossovers | Lambda cheapest below ~3-10M req/mo; Workers take I/O-heavy traffic; provisioned containers win CPU-bound work beyond ~300-560M req/mo |

## Tech stack

| Component | Choice |
|---|---|
| Shared workload | One implementation (`core.mjs`), parity-tested byte-identical across platforms |
| Edge | workerd, the real open-source Workers runtime, with an HTTP-to-Postgres gateway |
| Serverless | slshost (this repo, Go): Lambda semantics — init-once envs, 1 req/env, reaping, 429s |
| Container | Long-lived Node.js server with a persistent pg pool |
| Harness | Go orchestrator with open-loop and closed-loop load generation |
| Cost model | Python, cited and dated prices, self-tested against vendor pricing examples |
| Reproduce-on-cloud path | wrangler.toml, SAM template, Dockerfile + fly.toml provided (not executed for the published numbers) |
