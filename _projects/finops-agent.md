---
title: FinOps Agent
track: fde
order: 26
group: Analysis copilots
kind: Cost analysis agent
repo: harsha-moparthy/finops-agent
description: >-
  A cloud cost analysis agent that reads two months of billing, finds waste across four classes at
  1.00 precision and recall on planted scenarios, and drafts a reviewable remediation for each
  finding — never auto-applied, graded by execution on a mock cloud. A savings-verification loop
  grades its own projections against the next month's bill: 11/12 verified, portfolio 4.3% off, and
  the one engineered shortfall flagged at a 61% miss.
stack: [Python, SQLite, Bash, Terraform, Ollama]
highlights:
  - value: "1.00 / 1.00"
    label: detection precision and recall, 4 waste classes
  - value: "4.3%"
    label: portfolio projection error, $1,462.97 vs $1,399.52
  - value: "11/12"
    label: savings verified; the 12th flagged at a 61% miss, by design
  - value: "12/12"
    label: remediations reach the intended end state on the mock cloud
---

## Why this project exists

Cloud bills are large and opaque, and "we found $X of waste" is a claim nobody believes without
evidence. Savings are the rare applied-AI output that is objectively measurable after the fact, so
the project is built around three things that make the number trustworthy: waste planted alongside
look-alikes that punish a naive detector, projections verified against an independent
counterfactual of what the bill actually became, and remediations graded by execution rather than
by looks. A verifier that passed everything would prove nothing, so one planted case is engineered
to fall short.

## What it does

- Detects four waste classes — idle compute, oversized instances, unattached volumes, missing
  lifecycle policies — from observable signals only: billing, utilization, inventory, and S3 access
  analytics. A structural test asserts detectors never read the ground-truth tables.
- Survives the traps: idle is judged on the CPU distribution, not the mean, so a spiky nightly
  batch is not flagged; a downsize must leave headroom and a workload trending up is left alone; a
  3-day-old instance is not judged; a bucket that already has a lifecycle policy is skipped.
- Defers oversized to idle so a resource never gets two findings.
- Projects a monthly saving for every finding from period 1, then verifies against period 2 —
  generated independently — inside a ±15% band wide enough for rate drift and tight enough to
  reject a 61% miss.
- Drafts each fix as a bash script or Terraform diff carrying a machine-checkable intent. A mock
  cloud applies it and diffs the end state — it enforces that `modify-instance-attribute` requires
  a stopped instance, so a script that forgets to stop first fails.
- Never touches a real cloud: drafting produces text, and a test confirms it does not mutate even
  the corpus.

## Measured results

| Evidence | Result |
|---|---|
| Detection precision / recall on planted scenarios | 1.00 / 1.00 — 12 TP, 0 FP, 0 FN |
| Waste classes exercised | idle ×4, oversized ×3, unattached ×3, lifecycle ×2 |
| Look-alike traps flagged | 0 (spiky batch, maxed-out, growing, new, attached volume, hot and managed buckets) |
| Savings verification (±15% band) | 11/12 verified; portfolio projected $1,462.97 vs realized $1,399.52 — 4.3% off |
| The negative control | not verified — 61% miss, exactly as designed |
| Remediation execution, fake arm | 12/12 reach the intended end state |
| Mutation check | 9/9 mutants caught by a specific test |
| Test suite | 35 passed |
| Corpus | 87 resources, 6,201 billing lines, two periods, one seed |

The negative control is the point: its projection is honest — stopping an idle instance recovers
its full bill — but the fix landed on day 18 of the period, so only 40% of the month's savings
realized. A loop that rubber-stamped it would also rubber-stamp a genuinely wrong projection.

## Tech stack

| Component | Choice |
|---|---|
| Corpus | deterministic two-period generator, CUR-shaped billing over SQLite |
| Detectors | four rule-based detectors with independently load-bearing guards |
| Remediations | bash scripts and Terraform diffs, each with a machine-checkable intent |
| Grading | in-memory mock cloud that applies artifacts and diffs end state |
| Optional model arm | Ollama drafter, harvested separately from CI |
| Verification | mutation check (9 mutants) and CI steps parsed from the workflow YAML |
