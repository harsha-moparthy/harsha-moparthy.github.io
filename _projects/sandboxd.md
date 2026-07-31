---
title: Sandboxd
track: sde
order: 30
group: Sandboxing and isolation
kind: Execution service
repo: harsha-moparthy/sandboxd
description: >-
  A code-execution service for AI agents, built twice — on gVisor and on Firecracker microVMs — so the
  isolation and latency claims are measured and compared rather than asserted. 16/16 hostile payloads
  contained on both backends, and a warm pool that cuts Firecracker latency 44x, from 3.7 s cold to 83 ms.
stack: [Rust, tokio, axum, gVisor, Firecracker, cgroup v2]
highlights:
  - value: "16/16"
    label: hostile payloads contained, both backends
  - value: "44x"
    label: "Firecracker: 3665 ms cold to 83 ms warm"
  - value: "23.5 ms"
    label: warm-pool p50 on gVisor
  - value: "~60 ms"
    label: warm cost of a hardware boundary
---

## Why this project exists

AI agents write and run code constantly, and running machine-generated code on shared infrastructure
is dangerous. A whole product category (E2B, Modal, Daytona) exists to do one thing: execute untrusted
code fast and safely. The two halves of that sentence fight each other — the strongest isolation
boundary is a separate kernel, and booting a kernel takes seconds while an agent waits synchronously
on the other end of an HTTP request. This service builds both halves and measures what each one costs.

Any sandbox project can print "16/16 tests passed." The question is what would have made them fail.
Two design moves address that. Containment is asserted on kernel counters — `pids.events:max`
incremented, `memory.events:max` incremented, the payload observing its own `ENOSPC` — not on "it
didn't crash"; a payload that merely exits non-zero does not count as contained, and a meta-test
rejects any payload whose expectation can never fail. And the same suite runs against two different
isolation boundaries behind one `Backend`/`Sandbox` trait, so when the backends disagreed, that was a
finding. It happened three times.

## What it does

- Executes Python or shell submissions behind a choice of isolation boundary: gVisor (`runsc`
  user-space kernel) or Firecracker (KVM microVM with its own guest kernel)
- Enforces CPU, memory, process-count, disk, and network caps through kernel mechanisms — cgroup v2,
  `RLIMIT_*`, size-bounded ext4 loop images, namespaces with no interface — not supervisor-side timers
- Keeps a warm pool of pre-created sandboxes and never reuses one across tenants: a used sandbox is
  destroyed, not cleaned
- Serves an HTTP API with per-tenant quotas (concurrency plus a rolling CPU budget), cap clamping,
  and 429-with-`Retry-After` rather than silent queueing
- Reports a latency decomposition per execution (acquire / setup / run / teardown), so "the service
  is slow" can be attributed to a layer
- Runs a 16-payload hostile suite — fork bombs, memory bombs, disk fill, escape attempts, `/proc` and
  `/sys` probes, network exfiltration, and an ordered cross-tenant residue probe — as a CI gate

## Measured results

Host: Apple M4 Pro, macOS → Lima `vz` VM with nested virtualization, Ubuntu 24.04 aarch64. Latency is
service overhead (acquire + setup + teardown, payload runtime excluded), n=10 per mode, 0 failures
across all 7 modes.

| Evidence | Result |
|---|---|
| Hostile suite, gVisor | **16/16 contained**, asserted on kernel counters |
| Hostile suite, Firecracker | **16/16 contained**, same payloads, same verifier |
| gVisor warm pool | **p50 23.5 ms**, p95 27.5 ms |
| gVisor cold start | p50 71.1 ms |
| Firecracker cold boot | p50 3665 ms |
| Firecracker warm pool | **p50 83.1 ms** — a 44x reduction over cold |
| Firecracker snapshot restore | p50 844 ms — 4.3x faster than cold, 10x slower than warm |
| Hardware boundary premium when warm | ~60 ms (83 ms vs 23.5 ms) — the price of a separate kernel |
| Unit tests / lint | 47 pass; `clippy -D warnings` and `cargo fmt --check` clean |
| Resource-leak audit after suites and demos | 0 leaked processes, cgroups, mounts, or bundle dirs |

Measurement, not assumption, produced the interesting findings: the host `pids` cgroup does not stop
a fork bomb under gVisor (a shell bomb hit 5000 guest processes while the host saw 32 threads — the
binding limit is `RLIMIT_NPROC` inside the sandbox); Firecracker's cumulative `cpu.stat` over-reported
per-execution CPU by ~78x until charged as a delta; and three hostile payloads initially did not test
what they claimed. Each mistake is documented at the code that fixes it.

## Tech stack

| Component | Choice |
|---|---|
| Language | Rust 2021, tokio — the supervisor is latency-sensitive |
| API | axum: `POST /v1/executions`, `/health`, `/metrics` |
| Isolation A | gVisor `runsc` (systrap), hand-written OCI spec |
| Isolation B | Firecracker v1.16.1, guest kernel 6.1.141, vsock guest agent |
| Enforcement | cgroup v2 + `RLIMIT_*`, counters read back as containment evidence |
| Guest agent | Python stdlib only, runs in a stock rootfs unchanged |
| Host / CI | Lima `vz` with nested virt; GitHub Actions runs the gVisor suite as a gate |
