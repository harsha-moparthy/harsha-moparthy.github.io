---
title: Legacy MCP
track: fde
order: 18
group: Legacy modernization
kind: Integration layer
repo: harsha-moparthy/legacy-mcp
description: >-
  A governed MCP tool layer over an authentically awful legacy stand-in — a SOAP service fronting
  cryptic stored procedures — where a scripted generic agent completes 0/6 realistic tasks against
  the raw interface and 6/6 through the wrapper, protected by a rate cap and circuit breaker whose
  behavior is measured against a live degraded backend.
stack: [Python, MCP SDK, FastAPI, httpx, SQLite]
highlights:
  - value: "0/6 → 6/6"
    label: task success, raw interface vs wrapped, end-state checkers
  - value: "4 calls"
    label: total backend contact while circuit-breaking a 2s-slow backend
  - value: "0/25 vs 20/25"
    label: SYSTEM BUSY faults, paced wrapper vs unthrottled caller
  - value: "33/33"
    label: tests passing
---

## Why this project exists

Enterprises run on decades-old systems — SOAP services, stored-procedure databases, screens nobody
has re-designed since the aughts. The current wave of forward-deployed work is making those systems
usable by AI agents *without replacing them*: wrapping legacy interfaces in governed, modern tool
layers. The craft is not the MCP part. It is the archaeology (what does `PROC_UPD_47` actually do?),
the safe-write patterns on a backend with no cross-call transactions, and the duty of care toward
infrastructure that falls over if you hammer it.

This project builds the legacy system *and* the wrapper, so every claim is checkable end to end.

## The legacy stand-in, faithfully awful

A wholesale order-management backend reachable only through a SOAP-style XML endpoint fronting
stored procedures:

- tables `T_CST` / `T_ITM` / `T_ORD_H` / `T_ORD_L`; `C_STS CHAR(1)` with magic letters, money in
  integer cents, dates as `YYYYMMDD` integers
- positional parameters (`<P1>`, `<P2>`, …) and faults like `ERR-3007 CONSTRAINT VIOLATION SEGMENT 4`
- **no cross-call transactions**: order entry is a three-procedure protocol (header → lines →
  finalize); die in the middle and an incomplete header is stranded forever — the seed data ships
  with one such orphan as the exhibit
- **undocumented side effects**: `PROC_UPD_47` "sets customer status" but also recalculates the
  credit-block flag from open exposure, so releasing a hold does not necessarily unblock the customer
- **fragility**: above ~5 calls/s it faults `ERR-9999 SYSTEM BUSY`

The wrapper never imports the database — it speaks the XML wire only, exactly like a real engagement.

## What the wrapper adds

**A semantic data dictionary** (the archaeology deliverable): every table, column, status letter,
procedure contract, error code, and landmine, with how each was recovered. The code's `semantics.py`
is its executable form, and tests pin the two to each other.

**Business-operation tools, not endpoints**: `place_order`, `get_customer_credit`, `release_hold`,
`cleanup_incomplete_orders` — statuses are words, money is decimal, dates are ISO. Every failure is
translated into meaning plus remediation plus the raw code for humans.

**Compensation for transactionless writes**: `place_order` drives the three-call protocol and, on
any mid-protocol failure, deletes the incomplete order and says so. Tested down to "no orphan rows,
stock untouched."

**Load protection**: every legacy call passes a token bucket (throttle by waiting, not shedding) and
a circuit breaker (open on consecutive infrastructure failures, half-open probe to recover; business
faults never count against it).

## Measured results

### Before/after capability

Six realistic tasks, judged purely by end-state database checkers — no graders. The raw arm is a
scripted *generic-competence* operator (parses XML, retries once, makes sensible guesses); what it
lacks is tribal knowledge, which is precisely what the wrapper packages.

| task | raw interface | MCP tools |
|---|---|---|
| place a simple order | FAIL — stranded incomplete (nothing advertises the finalize call) | PASS |
| explain a blocked order | FAIL — cannot decode `ERR-3007` | PASS — hold **and** over-limit, release won't fix |
| failed order leaves no debris | FAIL — orphan header left behind | PASS — compensated |
| cancel and confirm restock | FAIL — guesses the wrong status code | PASS — restock observed |
| find stuck orders | FAIL — `I` is just a letter | PASS — orphan found and removed |
| credit headroom in currency | FAIL — computes from cents and wrong statuses | PASS — exact |

**Raw 0/6 — wrapped 6/6.** The strict test fails in both directions: if the raw operator starts
passing, the stand-in got too easy; if the wrapped one slips, the wrapper regressed.

### Protection under a degraded backend (real sockets)

Against a backend slowed to 2s/call (wrapper timeout 0.5s, breaker threshold 3): three timed-out
probes opened the circuit, five subsequent agent calls fast-failed in ~0ms with an actionable
"backend degraded, retry in Ns", and a half-open probe closed the circuit after recovery — **4 total
backend calls** across the whole episode.

Against the 5-calls/s SYSTEM BUSY ceiling, 25 reads: an unthrottled caller burned **20/25** requests
into faults in 0.02s; the wrapper paced the same workload to **0/25** faults, spending 5.95s
deliberately waiting instead of hammering. The first bucket sizing (burst 4 + 4/s) still produced
2 faults because burst plus refill exceeded the backend's ceiling in the first second — the fix and
the lesson (size the bucket to the backend's measured capacity, not a round number) are kept in the
code.

## Honesty notes

The raw operator is scripted, not an LLM; its generic competence and its ignorance are both explicit
in code, and the suite measures what the *interface* affords. The legacy stand-in is self-built, so
its awfulness is curated rather than accreted — but every quirk is documented from real systems:
transactionless multi-call writes, overloaded error codes, side-effecting status procedures,
cents-and-YYYYMMDD encodings, SYSTEM BUSY ceilings. Protection numbers come from real sockets and
real timeouts; the deterministic breaker unit tests use a simulated transport and say so.
