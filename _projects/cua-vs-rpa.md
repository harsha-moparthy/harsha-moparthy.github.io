---
title: CUA vs RPA
track: fde
order: 22
group: Agent operations
kind: Automation study
repo: harsha-moparthy/cua-vs-rpa
description: >-
  A computer-use agent, a scripted RPA bot, and a script-first/agent-on-failure hybrid, run
  head-to-head on the same invoice-entry workflow across five levels of UI drift — 750 measured
  episodes scored by reading the app's stored state. The script holds 100% through cosmetic change
  and falls to 0% the moment structure drifts; the agent and the hybrid hold 100% at every level.
stack: [Python, Playwright, Chromium, uv, GitHub Actions]
highlights:
  - value: "750"
    label: episodes, 0 harness faults
  - value: "100%"
    label: agent success at every drift level, one code path
  - value: "0%"
    label: script success at L2–L4; breaks, never miswrites
  - value: "334x"
    label: margin on the hybrid-beats-script conclusion
---

## Why this project exists

Enterprises spent a decade scripting robotic process automation against legacy GUIs, and every UI
change breaks the scripts. Vision-based agents promise resilience to exactly that drift, but nobody
quite trusts them yet. The evidence that settles the argument is not a demo of an agent clicking a
button — it is a fair, repeatable head-to-head on the same tasks with the same success test, where
the script is allowed to win on the axes it actually wins on (speed, cost) and the agent has to
earn its keep on the one that matters: surviving drift.

## What it does

- A dated-looking invoice-entry web app (VENDOPAY 2000) is driven by three arms across five
  mutation levels: baseline, cosmetic changes, renamed ids and labels, structural reordering with
  decoy fields, and interstitial notices plus a confirmation page.
- Every episode gets a cookie-isolated workspace and is scored by reading the app's stored invoice:
  right vendor, number, date, every line and amount, the computed total, and no decoy field filled.
  Partial credit does not exist in accounts payable.
- The script is the median real RPA artifact, not a strawman — hardcoded selectors recorded against
  the baseline, a fixed action sequence, no recovery — and it is genuinely fast and free per run.
- The agent is a deterministic semantic matcher standing in for a VLM's grounding at exactly the
  interface a VLM agent uses, which makes 750 episodes reproducible with no API key. Dollar figures
  are modeled from measured step counts and labeled as modeled everywhere they appear.
- The hybrid runs the script first and wakes the agent on exactly the 150 episodes where the script
  broke, never otherwise.
- Harness faults are quarantined, not counted as arm behavior: a run refuses to publish and exits
  non-zero if any episode measured the harness instead of an arm.

## Measured results

| Evidence | Result |
|---|---|
| Full grid: 3 arms × 5 levels × 50 tasks | 750 episodes, 0 harness faults |
| Script under drift | 100% at L0/L1, 0% at L2–L4 — and it breaks rather than miswriting |
| Agent under drift | 100% at every level, one code path, never shown a mutation |
| Hybrid | 100% at every level; agent takeover on exactly 50/50 episodes per drifted level |
| Script failure mode | all 150 failures are a missing selector with no write attempted |
| Latency, stable UI | script ~0.15 s and $0.0000; agent ~0.4 s and $0.0030–0.0050 (modeled) |
| Latency, drifted UI | script pays a 1.5 s timeout to detect the break, then stops |
| Hybrid-beats-script margin | $0.0050 vs $1.67 per stranded task — ~334x, independent of every cost assumption |
| Break-even for agent-only vs hybrid | ~36,900 tasks/month under the stated assumptions |
| Test suite | 43 passed |

The decision framework separates the two conclusions. The hybrid strictly dominating script-only
needs no cost assumptions: re-record costs cancel, and what remains is whether stranded tasks are
handled at the modeled agent rate or by hand. Agent-only beating the hybrid depends on volume, and
at a worked 2,000 tasks/month it is $10 against $180 against $262 for script-only.

## Tech stack

| Component | Choice |
|---|---|
| Target app | VENDOPAY 2000, a deliberately dated invoice-entry web app with five mutation levels |
| Browser automation | Playwright driving Chromium |
| Agent arm | deterministic semantic matcher at the observe-page/choose-action interface |
| Scoring | app state read through a test endpoint, exact-match success |
| Config | every knob (tasks, seed, modeled prices, assumptions) in `.env` |
| CI | GitHub Actions: full test suite plus a quick grid on every push |
