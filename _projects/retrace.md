---
title: Retrace
track: sde
order: 35
group: Coding-agent infrastructure
kind: Replay debugger
repo: harsha-moparthy/retrace
description: >-
  A record/replay/diff debugger for AI agents: 19/19 committed sessions replay byte-identically with
  every boundary mocked, and a validated trajectory aligner (2000/2000 planted-divergence trials)
  pinpoints the first divergence — including run pairs where both give the right answer while the
  drifted one silently ignores its own tools.
stack: [Python, Typer, Ollama, http.server, GitHub Actions]
highlights:
  - value: "19/19"
    label: sessions replay byte-identically
  - value: "2000/2000"
    label: planted divergences recovered, kind + index
  - value: "4/4"
    label: negative controls correctly fail
  - value: "~75 B"
    label: dedup break-even, measured by sweep
---

## Why this project exists

When an agent does something strange, today's answer is scrolling logs. For ordinary bugs we have
better tools: record the process, replay it deterministically, diff two runs to see where they parted
company. For agents that tooling barely exists, and the reason is specific: replay requires capturing
every source of nondeterminism (model output, tool results, time, randomness), and diffing is not
line-diffing — two runs fork at a decision point and everything after shifts.

The most useful output was what the diff showed on real recordings. In one pair, a drifted tool
returned 37 instead of 30; the model's tools computed 111 — and it answered 90 anyway, the right
answer it already knew, directly contradicting the tool result it had just received. Both runs emit
90, so pass/fail on the answer is identical. The agent looks perfect at exactly the moment it stopped
believing the tools it exists to orchestrate, and no assertion on the output can see it.

## What it does

- Records every boundary crossing — model completions, tool calls, wall-clock reads, RNG draws —
  through a single interception object; an agent reads nondeterminism only through it, so replay
  determinism is true by construction
- Replays byte-identically with every boundary mocked: no model, no network, no clock, verified as a
  CI gate over the committed recordings
- Drift-checks replay rather than serving responses positionally: if the replayed agent asks a
  different question than when recorded, it stops with the exact event index — and drift is recorded
  stickily, so a broad `except` cannot swallow it into a false PASS
- Diffs two runs structurally: byte-identical common prefix, first divergence classified by cause
  (`response` vs `request`), remainder aligned with Needleman-Wunsch so re-convergence is visible
- Stores sessions content-addressed (canonical JSON + SHA-256), with the dedup crossover measured
  rather than asserted
- Serves a zero-dependency web UI for side-by-side inspection

## Measured results

Host: Apple M4 Pro; live recordings harvested from Ollama `gemma4:31b-it-qat`. Replay, diff, and
storage need no model or network. A CI script re-derives every README number from committed
artifacts, so a stale figure fails the build.

| Evidence | Result |
|---|---|
| Committed recordings replaying byte-identically | **19/19** |
| Negative controls that correctly fail | **4/4** — over-consumption, wrong request, under-consumption, reordering |
| Aligner validation, planted divergences | **2000/2000** across response / request / insert / delete perturbations |
| Swallowed-drift fuzz (pre-fix bug class) | 3000/3000 recordings produced a false `identical=True`; the sticky-drift fix closes it |
| Real divergent pairs, labeled by cause | 8 pairs from live runs, plus one honest non-divergent counter-example |
| Storage dedup on the committed data | **0.79x** — dedup loses on ~100-byte bodies, reported as measured |
| Dedup sweep | break-even ~75-byte bodies; 3.16x at 3200 bytes — kilobyte completions sit in the paying regime |
| Test suite | 60 tests; 10 of 12 replay tests are controls that must fail |

The committed recordings double as a regression suite for the agent's own code: a one-character regex
relaxation in the agent changes its behavior, and a test asserts the replay fails at the exact
divergent event.

## Tech stack

| Component | Choice |
|---|---|
| Language | Python 3.12 — replay, diff, and storage need no third-party code |
| CLI | Typer |
| Live model | Ollama `gemma4:31b-it-qat`, touched only by the harvester |
| Storage | Filesystem + JSON, content-addressed with canonical JSON + SHA-256 |
| Alignment | Common prefix + divergence taxonomy + Needleman-Wunsch |
| Web UI | `http.server` plus one static page, no framework |
| CI | GitHub Actions: replay-fidelity gate plus README claim checker |
