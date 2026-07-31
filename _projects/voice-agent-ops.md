---
title: Voice Agent Ops
track: fde
order: 21
group: Agent operations
kind: Voice operations
repo: harsha-moparthy/voice-agent-ops
description: >-
  A phone-line voice agent for a service shop — booking, rescheduling, cancelling, status —
  evaluated by a simulated-caller harness that drives real 8 kHz audio through the full stack under
  seven failure conditions, with every claimed outcome verified against the backend database.
  Confirming every high-stakes slot takes wrong bookings from 17% to 0%, and p95 turn latency holds
  at 929 ms.
stack: [Python, NumPy, SQLite, Typer, Rich]
highlights:
  - value: "17% -> 0%"
    label: wrong bookings, no-confirm vs confirm-everything
  - value: "929 ms"
    label: p95 turn latency, 0 of 559 turns over budget
  - value: "98 ms"
    label: barge-in overlap, vs 1,971 ms unhandled
  - value: "593"
    label: tests in ~72 s, fully offline
---

## Why this project exists

A transcript-level metric would score the no-confirmation arm as almost entirely successful — the
agent said "you're all set" on every one of those calls. Reading the database instead finds 21
wrong bookings out of 126: wrong day, wrong time, wrong phone number. That gap is the whole reason
this project verifies backend effects rather than conversations, and why the evaluation runs 126
calls per arm, 504 per full report, seeded from one integer with no API keys and no network.

## What it does

- Synthesizes real PCM at 8 kHz in 20 ms frames, mixes noise to a requested speech-active SNR, and
  estimates the SNR back out with a streaming energy VAD — the recognizer never sees the condition
  label, only samples.
- Runs a dialogue state machine over a SQLite service calendar where double-booking is prevented by
  a partial unique index in the schema, so it holds even against a raw INSERT.
- Tests three confirmation policies (off, confidence-gated, confirm-everything) as a designed
  experiment. The honest result is negative: gating catches 81% of preventable wrong effects but
  pays 82% of the full readback cost, so the recommendation is confirm every high-stakes slot.
- Evaluates seven named conditions as separate failure mechanisms — clean, mild and heavy noise,
  accented speech, barge-in, corrections, and calls that must be escalated to a human.
- Scores escalation against a three-valued ground truth (required, forbidden, permitted), earned at
  runtime rather than read from the script, and grades the handoff packet a human receives.
- Handles duplex audio: stopping playback on detected barge-in cuts overlap from 1,971 ms to 98 ms
  and takes word error rate on those turns from 0.17 to 0.02.

## Measured results

| Evidence | Result |
|---|---|
| Task completion, cooperative conditions | 69% (74/108, CI 59–77%) |
| Wrong backend effects — no confirmation | 17% (21/126) |
| Wrong backend effects — confidence-gated | 3% (4/126) |
| Wrong backend effects — confirm everything | 0% (0/126) |
| p95 turn latency | 929 ms, 0 of 559 turns over the 1,200 ms budget |
| Endpointing in heavy noise (5 dB) | 29% of turns truncated — a correctness failure, not a latency one |
| Escalation precision / recall (88 decidable calls) | 85% / 94%, F1 0.89 |
| Escalation reason correct | 100% (17/17) |
| Barge-in overlap, handled vs unhandled | 98 ms vs 1,971 ms (WER 0.02 vs 0.17) |
| Test suite | 593 passing in ~72 s |

Heavy noise breaks endpointing, not latency: p95 stayed inside budget in every condition, but at
5 dB the voice-activity detector cut 29% of turns off before the caller finished. The 6% completion
there is honest — 17 of 18 calls ended in a transfer to a human, which is the correct behaviour on
a line that bad.

## Tech stack

| Component | Choice |
|---|---|
| Audio | real 8 kHz PCM synthesis, pink noise, SNR-targeted mixing (NumPy) |
| Endpointing and barge-in | streaming energy VAD, measured from frames |
| ASR / TTS | provider interfaces with declared offline stand-ins; confidence never peeks at outcomes |
| Backend | SQLite service calendar, constraints in the schema |
| Dialogue | state machine with decidable invariants, not a prompt |
| CLI and reports | Typer + Rich; Wilson intervals on every rate |
