---
title: Surveil
track: hft
order: 56
group: Risk and surveillance
kind: Surveillance
repo: harsha-moparthy/surveil
description: >-
  Streaming market-manipulation surveillance — spoofing, layering, wash trading, momentum ignition —
  measured against injected ground truth on a 4.6M-event stream: the learned scorer detects 100% of
  200 injected episodes at 2.15 false positives per hour versus 81% at 5.85 for hand-tuned rules.
  The gap is widest on subtle manipulation, where rules catch 42.5% and the learned model catches
  all of it.
stack: [Python, pytest, discrete-event simulation, streaming features]
highlights:
  - value: "100%"
    label: detection, 200/200 injected episodes
  - value: "2.15/hr"
    label: false positives vs 5.85 for the rule baseline
  - value: "381 ms"
    label: p50 detection latency vs 1126 ms for rules
  - value: "4.6M"
    label: events, 6.5-hour session, single core
---

## Why this project exists

Exchanges and regulators run surveillance systems that flag manipulation in real time. The
detection problem is a clean streaming-analytics challenge with a nasty twist: the patterns are
behavioural, not single-event — no individual order is a spoof; a spoof is a large order posted,
the imbalance it creates, its cancellation, and the trade on the other side it set up. Whether a
system is usable comes down to a precision/recall trade-off measured against ground truth you had
to create yourself. The measurement is the deliverable, not the detector.

## What it does

- Ground truth by injection: manipulation episodes are inserted through the same matching engine as
  everything else, each tagged with an episode id; detectors receive a view that strips the labels,
  so "the detector never sees ground truth" is enforced by construction and asserted by a test
- Each pattern is parameterized by an aggressiveness in [0, 1] — the study's independent variable,
  because a system that only catches the blatant is easy to evade
- A background population built to cause false positives on purpose: market makers with genuinely
  >95% cancel ratios, large orders legitimately cancelled after adverse moves, institutions slicing
  parent orders, retail noise
- Causal, O(1)-per-event sliding-window features (monotonic-deque maxima); a rule-based baseline
  and a learned multi-class scorer trained and evaluated on disjoint seeds
- An attribution harness that does not flatter itself: an alert detects an episode only if it names
  a participating account, fires in the window, and names the correct pattern — misclassifications
  are counted separately from detections and false positives

## Measured results

| Evidence | Result |
|---|---|
| Session scale | **4,636,199 events**, 6.5 hours, 21 accounts, 200 injected episodes, Apple M4 single core |
| Detection rate | learned **100.0% (200/200)** vs rules 81.0% (162/200) |
| False positives per hour | learned **2.15** vs rules 5.85 |
| Pattern-precision (exact label) | learned **93.0%** vs rules 52.9% |
| Detection latency, p50 | learned **381 ms** vs rules 1126 ms |
| Subtle manipulation (aggressiveness 0.1) | learned **100%** vs rules 42.5% |
| Throughput, one core | rules 192k events/s; learned 65k events/s |
| The real discriminator | `reversal_ratio` separates manipulation from legitimate flow by **~20x** with no overlap — while "fast cancels" points at market makers, the inverse of intuition |

Bugs the methodology caught: the reconstructed book silently crossed until a diff against the
exchange's own book pinned it exactly, and wash detection drowned in false positives until the
self-match graph required price concentration — a ~16x reduction.

## Tech stack

- Python, seeded end to end: the same arguments reproduce the same event stream and results
- A price-time-priority matching engine where every state change emits a labelled event
- Monotonic-deque sliding-window features, causal and O(1) per event
- Rule detectors plus a learned multi-class scorer over the same features; pytest invariant suite
  gates CI (labels never leak, detection rises with aggressiveness)
- The rules remain the explainable baseline the model has to beat — writing them is what forced
  each pattern's behavioural definition to be explicit
