---
title: SpecForge
track: sde
order: 34
group: Coding-agent infrastructure
kind: Dev toolchain
repo: harsha-moparthy/specforge
description: >-
  A spec-driven dev toolchain: machine-readable feature specs compile deterministically to pytest
  suites that gate sandboxed coding agents, plus an ambiguity linter. On a 20-feature benchmark with a
  local 31B model, detailed specs solved 20/20 on the first attempt; terse prose solved 17/20 at 1.7x
  the attempts and 1.7x the wall time.
stack: [Python, pytest, YAML, Ollama, uv]
highlights:
  - value: "20/20"
    label: detailed specs solved, 100% first-attempt
  - value: "17/20"
    label: terse prose, at 1.70 mean attempts
  - value: "308 s"
    label: mean wall per feature, vs 515 s terse
  - value: "109"
    label: tests, all 20 benchmark features CI-verified
---

## Why this project exists

As agents write more of the code, the scarce human skill shifts to specifying what to build.
SpecForge makes the spec the contract: tests are generated deterministically from acceptance criteria
(and traced back to them for human review), the agent never sees the tests, and a verdict is produced
by running the suite in an isolated sandbox. That measures whether the spec carried the intent, not
whether the model can pattern-match asserts.

Three design choices carry the weight. Test generation is a deterministic compilation of
acceptance-criterion examples — no LLM in the loop that could silently drift from the spec, and every
generated test maps to the criterion it encodes in a review manifest. The agent sees only the spec
prose plus the interface contract, and on failure a truncated report. And ambiguities are surfaced,
not papered over: a linter flags vague terms ("robust", "properly"), hedges ("etc.", "as needed"),
criteria with no examples, the same call with two expected outcomes, and specs with no error-path
criterion at all.

## What it does

- Loads strict YAML specs — user stories, interface signature, non-goals, acceptance criteria with
  `given/when/then` and executable examples; every `call` and `expect` is syntax-checked at load time
- `specforge lint` runs the deterministic ambiguity linter over a spec
- `specforge compile` emits a pytest suite plus a review manifest tracing every test to its criterion
- `specforge run` drives an agent loop: prompt from the spec, implementation executed in a sandbox
  (fresh tmpdir, scrubbed env, CPU rlimit, wall timeout, network blocked), results parsed from JUnit
  XML, compact failure reports fed back with bounded retries
- `specforge eval` runs the 20-feature terse-vs-detailed benchmark and writes reports
- Backends: local Ollama models or any OpenAI-compatible endpoint
- Every benchmark feature is verified in CI: a reference solution must pass its generated suite in
  the sandbox, so the eval rests on suites known to be satisfiable

## Measured results

Benchmark: 20 small features, each with one canonical structured spec (compiling to the one fixed
test suite — the yardstick) and a deliberately terse prose variant of the kind found in real tickets.
The suite to pass is identical in both arms, so spec quality is the only variable. Model: local
`gemma4:31b-it-qat` via Ollama, 3 attempts max with failure feedback between attempts.

| Evidence | Result |
|---|---|
| Detailed spec arm | **20/20 solved (100%)**, mean 1.00 attempts — every run first-attempt |
| Terse prose arm | **17/20 solved (85%)**, mean 1.70 attempts |
| Wall time per feature | 308 s detailed vs 515 s terse |
| Retries under terse specs | needed on 10/20 features, never recovered on 3 |
| The 3 unrecovered losses | all unstated error-path contracts ("be robust", "validate as needed") — exactly what the ambiguity linter flags |
| Test suite | **109 tests**, including sandboxed verification of all 20 reference solutions |

The failure analysis is the point: every feature the terse arm permanently lost came down to an
implicit error-path contract the prose never stated, which is precisely the class of ambiguity the
linter is built to catch before an agent ever runs.

## Tech stack

| Component | Choice |
|---|---|
| Spec format | Strict YAML dataclasses with load-time validation |
| Test generation | Deterministic criteria-to-pytest compilation plus review manifest |
| Linter | Deterministic ambiguity rules — vague terms, hedges, untestable or conflicting criteria |
| Sandbox | Isolated subprocess: rlimits, scrubbed env, no network, JUnit parsing |
| Agent backends | Ollama, OpenAI-compatible endpoints, scripted (for tests) |
| Tooling | Python 3.12+, uv, pytest, ruff |
