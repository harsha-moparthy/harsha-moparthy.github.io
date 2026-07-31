---
title: TokenWire
track: backend
order: 61
group: Serving AI traffic
kind: Streaming backend
repo: harsha-moparthy/tokenwire
description: >-
  A streaming inference backend in zero-dependency Go — SSE plus a hand-rolled RFC 6455
  WebSocket — with bounded per-connection buffering. 200 streams force-disconnected six times each
  resumed exactly: 40,000 tokens verified token-for-token with 0 lost and 0 duplicated, and
  cancellation reaches the model backend in about a millisecond, saving 97.5% of the token spend.
stack: [Go, SSE, RFC 6455 WebSocket, Prometheus]
highlights:
  - value: "0 / 0"
    label: tokens lost / duplicated over 1,200 disconnects
  - value: "40,000"
    label: tokens verified against the model's own log
  - value: "~1 ms"
    label: cancellation propagation, 97.5% spend saved
  - value: "1,000"
    label: concurrent streams, +12.7 ms added ITL p99
---

## Why this project exists

Every AI product streams tokens to a browser, which resurrected a class of backend problems most
services never had: thousands of connections that live for minutes, clients that read slower than
the model generates, network blips in the middle of an answer, and users who navigate away while
you keep paying for tokens nobody sees. This project is those four problems, solved and then
measured — every claim backed by a bench harness whose raw output is committed with the repo.

## What it does

- Gives every stream a fixed-capacity ring of sequence-numbered events (the resume window);
  subscribers attach under the same lock as the append, so an event is delivered live or found in
  the backlog — never both, never neither.
- Makes resume refuse-or-exact: `Last-Event-ID` or `?after=` serves precisely the events after
  that point, or fails with HTTP 409 if the window evicted them. A client can be told to restart,
  but never handed a stream with an invisible hole.
- Offers two documented backpressure policies: `drop_slow` detaches a full subscriber with an
  explicit error naming its resume point; `pause_producer` blocks generation and stops reading the
  backend entirely while nobody is attached.
- Propagates cancellation as context teardown: DELETE, client disconnect (after a linger window),
  and shutdown all cancel the same context, and the 204 is sent only after the producer actually
  exited — so the ~1 ms figure is externally observable.
- Implements RFC 6455 and SSE by hand so no library puts an unowned, unbounded buffer in the
  middle of the path being measured; per-connection buffering is bounded and configured.

## Measured results

M-series MacBook (arm64, 14 cores), Go 1.26; load generator, server, and mock model share one
process on real loopback listeners, which is what makes millisecond cancellation measurable.

| Evidence | Result |
|---|---|
| Resume: 200 streams × 6 forced disconnects, reassembled and compared to the model's emission log | 1,200/1,200 resumes; 40,000 tokens verified; 0 lost, 0 duplicated, 0 sequence gaps |
| Cancellation, timed to the model's own handler | p50 0.50 ms (1 stream), 2.07 ms (10), 0.75 ms (50); 97.5% of tokens saved |
| Abandonment under `pause_producer` | 52.8% of a 20,000-token generation saved with no DELETE at all |
| Latency at 1,000 concurrent streams (20,000 tokens/s aggregate) | TTFT p99 219 ms vs the model's 200 ms floor; added inter-token latency p99 12.7 ms; 355 MB heap |
| Idle soak: 1,000 streams at 5 tokens/s for 60 s with heartbeats | 1,000 still open, zero drops, zero slow-consumer detaches |

Failures above ~1,500 concurrent streams belong to the single-process harness (macOS accept
backlog), not the server, and the results record how many streams were actually held.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go 1.26, zero external dependencies (stdlib only) |
| Transports | SSE field grammar and RFC 6455 WebSocket (framing, fragmentation, close handshake), both hand-rolled |
| Core | One ring per stream, contiguous sequence numbers, bounded subscriber queues |
| Backpressure | `drop_slow` (default) or `pause_producer`, both documented policies |
| Cancellation | Context propagation to the backend adapter; linger timer for vanished clients |
| Errors | Machine-readable with an explicit `retryable` field (a 409 must not be retried; a 503 should) |
| Metrics | Prometheus text format; heartbeats on both transports |
