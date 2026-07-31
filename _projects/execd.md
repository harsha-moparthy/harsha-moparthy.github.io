---
title: Execd
track: backend
order: 65
group: Durable execution and sandboxing
kind: Execution API
repo: harsha-moparthy/execd
description: >-
  A multi-tenant sandboxed code-execution API in zero-dependency Go, in the shape of what E2B and
  Modal sell to AI teams. Tenant-tagged warm pools with a structural cross-tenant reboot gate
  showed 0 leaks across 7 attack categories, warm exec runs at p50 0.16 ms against 192 ms cold
  boot, and 288 ledger entries reconcile exactly against the independent usage log.
stack: [Go, Python, net/http, JSONL, Process sandboxing]
highlights:
  - value: "0 leaks"
    label: 7 attack categories, reboot gate
  - value: "0.16 ms"
    label: warm exec p50 vs 192 ms cold boot
  - value: "288/288"
    label: ledger vs usage log, exact reconcile
  - value: "1 of 30"
    label: flood requests admitted at cap 1, victims unharmed
---

## Why this project exists

Every AI product that lets an agent "run code" needs this backend, and the hard part is not
executing Python; it is multiplexing a warm pool across tenants without cross-contamination,
keeping one tenant's flood from degrading everyone else, and producing billing records you can
prove correct. Those three claims are exactly what this repo tests and measures.

## What it does

- Serves `POST /v1/exec` for one-shot runs plus persistent sessions (state survives between
  calls, idle-reaped, capped per tenant), with every refusal typed and machine-actionable
  (`QUOTA_*`, `POOL_EXHAUSTED`, `EXEC_TIMEOUT`, with `retry_after_ms`).
- Recycles sandboxes with tenant-aware rules: same-tenant handoff is direct, fresh sandboxes need
  no gate, and cross-tenant reuse is never ungated — the default gate destroys the interpreter
  and boots a fresh process, so isolation is structural rather than checked.
- Documents the cheaper alternative honestly: reset-verify re-probes in-guest at ~200x lower cost
  but provably misses stdlib attribute mutations, so the test asserts the leak so the limitation
  cannot silently rot.
- Admits requests through per-tenant concurrency gates and CPU-ms windows before they can touch
  the pool, so a flood is contained at admission.
- Writes two independent books — an API ledger and a metering usage log, produced by different
  components at different call sites — and reconciles them, because reconciling a log against
  itself proves nothing.

## Measured results

M4 Pro, darwin/arm64, go1.26.5, full stack over in-process HTTP; reproduce with
`go run ./cmd/bench`.

| Evidence | Result |
|---|---|
| Residue probe suite: 7 attack categories (globals, files, env, module state, daemon-thread re-planter, stdlib mutation, builtins mutation), planted as tenant A, probed as tenant B | reboot gate: 0 leaks, every category, every round; reset-verify: 6/7, stdlib mutation leaks by design and is asserted |
| Warm pool | cold boot p50 192 ms; warm exec p50 0.16 ms (~1,180×); cross-tenant reboot handoff p50 153 ms vs 0.76 ms reset-verify |
| Skewed multi-tenant mix (288 requests, 16 tenants, pool of 16) | enterprise 87.5% warm-hit at 2.2 ms p50; free tier 19.2% warm-hit at 163 ms p50 |
| Free-tier flood, 30 concurrent at concurrency cap 1 | exactly 1 admitted, 29 typed 429s; a pro tenant alongside sees p50 0.48 ms vs 0.43 ms baseline, zero errors |
| Metering | 288 ledger entries vs 288 usage events, all matched on exec_id, tenant, ok, cpu_ms; timeouts billed at the full wall deadline |
| Test suite | 44 tests, race-detector clean, including quota exactness under racing admissions |

The isolation unit is a process, not a VM, and the README says so: the claims are about
cross-tenant contamination through the pooling layer, the part E2B-style products layer on top of
microVMs.

## Tech stack

| Component | Choice |
|---|---|
| Language | Go, zero external dependencies, plus a stdlib-only Python guest runner |
| Sandbox | One python3 process per sandbox, own process group, length-prefixed JSON over pipes, host-owned timeouts |
| Pool | Warm, tenant-tagged recycling with reserve-fresh slots for churn-heavy tiers |
| Quotas | Per-tenant concurrency gate plus CPU-ms window, enforced before body decode |
| Metering | Two independent JSONL books joined by a reconciler |
| Isolation unit | A process, stated honestly — production would swap in Firecracker/gVisor and keep the pool, quota, and metering logic |
