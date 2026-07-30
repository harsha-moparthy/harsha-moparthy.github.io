---
title: A2A Interop
order: 7
group: Multi-agent systems
kind: Protocol engineering
repo: harsha-moparthy/a2a-interop
description: >-
  Two agents on genuinely different frameworks — a hand-rolled loop and LangGraph — cooperating
  through an A2A-style protocol built from scratch, with chaos injection driving a nine-condition
  failure matrix in which every condition lands in a defined, bounded outcome. The harness pins down
  six specific places the protocol shape under-specifies itself.
stack: [Python, FastAPI, LangGraph, httpx, SSE]
highlights:
  - value: "9 / 9"
    label: chaos conditions land in a defined outcome
  - value: "6"
    label: protocol gaps found by implementing
  - value: "23 / 23"
    label: tests passing
  - value: "0"
    label: shared code between the two agents
---

## Why this project exists

Big companies are pushing protocols — Google's A2A and kin — so agents built by different teams and
vendors can discover each other and cooperate, the way the web needed HTTP. The space is young, so
hands-on implementation experience is where the leverage is. The interesting knowledge isn't "can two
agents talk"; it's **what the protocol under-specifies**, and that becomes visible only by implementing
it and then injecting every failure a remote agent can produce.

So the protocol surface is built from scratch — no SDK, because surfacing the gaps is the point.

## Two genuinely different runtimes

| | orchestrator | specialist |
|---|---|---|
| framework | hand-rolled step loop, plain Python | LangGraph `StateGraph` |
| skills | `report` (lookup, delegation, assembly) | `statistics`, `format_table` |
| knows about the other | only its agent card | nothing |

Neither imports the other's code. Everything crosses as JSON over HTTP. Both agents are
**deterministic — no LLM — on purpose**: the protocol machinery is model-agnostic, and determinism is
what makes the chaos matrix reproducible evidence rather than anecdote.

```
GET  /.well-known/agent-card.json    discovery: name, framework, skills, auth
POST /tasks                          create (idempotent via client_ref)
GET  /tasks/{id}                     status + messages + artifacts
GET  /tasks/{id}/events              SSE state stream
POST /tasks/{id}/input               answer an input_required pause
POST /tasks/{id}/cancel              cooperative cancellation
```

The client converts an unreliable peer into one of seven defined outcomes, with bounded retries applied
*only* to plausibly-transient failures. Garbage and 401s never retry.

## The chaos matrix

Nine adversarial conditions, each with a required client behaviour asserted:

| chaos mode | expected outcome | observed | attempts | verdict |
|---|---|---|---|---|
| none | ok | ok | 1 | PASS |
| slow | ok | ok | 1 | PASS |
| flaky | ok (retry until recovery) | ok | 3 | PASS |
| error | unavailable | unavailable | 4 | PASS |
| crash | unavailable | unavailable | 4 | PASS |
| hang | canceled_deadline | canceled_deadline | 1 | PASS |
| malformed | protocol_violation | protocol_violation | 1 | PASS |
| invalid_transition | protocol_violation | protocol_violation | 1 | PASS |
| auth_reject | auth_failed | auth_failed | 1 | PASS |

Every failure mode is bounded in time and lands in a defined outcome. The orchestrator degrades rather
than dies where partial results exist: a rendering outage still produces a report with raw metrics and
an explicit `DEGRADED` step log.

## The six protocol gaps — the actual deliverable

Each was established by implementation and chaos testing, not theorised:

1. **Polling validates reachability, not transitions.** A poller observes *samples* of a state machine,
   not its transitions: a conforming peer can legally pass `submitted → working → completed` between
   two polls, so single-step adjacency checks applied to polled samples will flag healthy peers. Only
   an event stream can be held to adjacency. A spec that defines a state machine without saying which
   observation channels promise which guarantees leaves every implementer to rediscover this; this
   implementation encodes the distinction directly in the client.
2. **Task creation is not idempotent unless you make it so.** A created task plus a lost response plus
   a client retry equals two tasks doing the same work — billed twice, side effects twice. Nothing in
   the protocol shape forces dedup, so the implementation makes creation idempotent via `client_ref`.
3. **Hang and slow are indistinguishable on the wire.** A `working` task with no progress signal could
   be seconds from done or dead forever. Without a heartbeat field the only sound policy is a hard
   deadline plus remote cancel, which also ends legitimately slow tasks. A `last_progress_at` field
   would let clients cancel on *stall* instead of *duration*.
4. **Cancellation is a race by construction.** The client may receive `completed` for a task it
   canceled a millisecond earlier. That is workable — but then "who observed what" governs side
   effects, and the protocol is silent on it.
5. **Partial artifacts on failure are undefined.** When a task fails after producing artifacts, are
   they usable? This implementation keeps them and lets the caller decide, because nothing in the
   protocol marks artifacts complete, partial or poisoned.
6. **The discovery card is a trust boundary with no teeth.** It is unauthenticated by necessity (it
   advertises the auth scheme) and unsigned, so everything it claims is unverified until first use. A
   card that misrepresents itself surfaces only at task time as `rejected` or `failed` — which the
   client handles as a defined outcome rather than an unbounded wait.
