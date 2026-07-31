---
title: ToolGate
track: sde
order: 37
group: Governed tool layers
kind: Policy engine
repo: harsha-moparthy/toolgate
description: >-
  IAM for coding agents: declarative YAML policies compile to decision functions that gate every tool
  call outside the model, with an escalation queue and a hash-chained audit log. The balanced policy
  blocks 93/93 bypass attempts while allowing 38/38 benign operations, deciding in p50 210 µs against
  a 5 ms budget.
stack: [Python, YAML, JSONL, uv, pytest]
highlights:
  - value: "93/93"
    label: bypass attempts blocked, balanced policy
  - value: "38/38"
    label: benign operations allowed, same policy
  - value: "210 µs"
    label: p50 decision latency, p99 0.67 ms
  - value: "306"
    label: tests; bypass suite gates CI
---

## Why this project exists

Today the control surface for coding agents is a choice between "ask the human every time" and
"allow everything". The missing middle is fine-grained, declarative rules about what an agent may do.
ToolGate is that middle: policies describe command classes, filesystem scopes, and network
destinations, and the engine enforces them outside the model, in a hook process that runs after the
model has already chosen its arguments. No prompt text can talk its way past it.

Most "command allowlists" match on the string an agent submitted, which fails immediately because the
same action has unbounded spellings: `env -i /bin/cat /etc/passwd`, `bash -c 'cat /etc/shadow'`,
`cd /etc && cat passwd`, a path in a variable, a symlink out of the workspace, or
`curl --data-binary @.env` as exfiltration. ToolGate parses instead of pattern-matching.

## What it does

- Answers three questions per request: what would actually run (tokenize, split on shell operators,
  recursively unwrap `env`, `sudo`, `timeout`, `xargs`, `uv run`, `sh -c`); which paths and how
  (including redirection targets and upload operands, expanded and `realpath`-resolved after any
  `cd`, so symlinks are judged where they land); and what could not be worked out
- Anything unknowable statically — `$(...)` substitution, inline `python -c`, an overridden `PATH` —
  becomes an opaque reason the policy matches on; fail-closed is an explicit policy choice, not a
  silent parser default
- Effect precedence, not file order: deny beats escalate beats allow, so adding a rule can only make
  a policy stricter for the requests it matches
- Path matchers name their quantifier (`paths_within` = every path inside; `writes_outside` = any
  write lands outside) because `cp /etc/hosts ./local` has a read outside and a write inside
- Escalations go to a file-backed human approval queue with TTL expiry (expiry = deny); every
  decision, allows included, lands in a hash-chained JSONL audit log with credential redaction
- Strict policy loading (unknown keys, duplicate ids, undefined variables are hard errors) plus a
  `policy lint` that reports fail-open smells
- Hooks into agent CLIs with the standard contract: JSON on stdin, exit 0 proceed, exit 2 block,
  optional "ask" body

## Measured results

Bypass suite: 93 attack cases. Benign suite: 38 legitimate operations. Both run against a workspace
staged per-run in a temp directory, including the symlink that escapes the scope.

| Evidence | Result |
|---|---|
| `balanced` policy vs bypass suite | **93/93 blocked** (41 denied, 52 escalated) |
| `balanced` policy vs benign suite | **38/38 allowed** |
| `strict` policy | 93/93 blocked, but only 16/38 benign allowed — blocking everything is trivial; the pair is the interesting number |
| `permissive` policy | 41/93 blocked — fail-open by design, guardrails for things outside the sandbox kept |
| Decision latency, balanced (22 rules) | **p50 210 µs, p99 0.67 ms** against a 5 ms budget, measured on a busy laptop (load average 15) |
| Test suite | **306 tests**; CI also runs the bypass suite against both enforcing policies, so a parser change that opens a hole fails the build |
| Audit verification | edited or removed lines detected with line numbers |

The two suites are reported together on purpose: blocking 93/93 attacks is trivial for a policy that
denies everything — `strict` does exactly that and pays by refusing 22 of 38 legitimate operations.

## Tech stack

| Component | Choice |
|---|---|
| Engine | Python: request → facts → compiled rules → effect, with effect precedence |
| Shell analysis | Tokenizer + wrapper unwrapping + command classification + path extraction |
| Path scoping | Variable expansion, symlink-safe `realpath` resolution, containment checks |
| Network scoping | URL canonicalization: numeric hosts, IPv6-mapped addresses, userinfo tricks |
| Policies | Strict YAML with matcher compilation and lint; strict / balanced / permissive ship |
| Escalation and audit | File-backed queue with TTL, hash-chained JSONL log with redaction |
