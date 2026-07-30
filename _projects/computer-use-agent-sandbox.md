---
title: Computer-Use Agent Sandbox
order: 5
group: Agent reliability
kind: Agent evaluation
repo: harsha-moparthy/computer-use-agent-sandbox
description: >-
  A vision-language-model browser agent driven over a self-hosted replica shopping site, with the
  benchmark harness that measures it: 36 tasks with programmatic completion checkers, DOM vs
  screenshot compared as an ablation, Wilson intervals, and an auditable failure taxonomy.
stack: [Python, Playwright, Ollama, gemma4 31B, FastAPI]
highlights:
  - value: "94% vs 83%"
    label: DOM beats screenshot
  - value: "36 / 36"
    label: scripted control solves every task
  - value: "[82%–98%]"
    label: Wilson CI on the DOM arm
  - value: "72"
    label: episodes across both modes
---

## Why this project exists

Computer-use agents are demoed constantly and measured rarely. The demos are cherry-picked runs on live
websites, which is unreproducible twice over: the site changes under you, and a single successful run
tells you nothing about the success *rate*.

The fix is to control the environment and the checker. This project hosts its **own replica shopping
site**, so the DOM is fixed, the state is inspectable, and every task has a **programmatic completion
check** against real application state rather than a model judging whether the model succeeded.

## The fixture must be proven before the agent is measured

A benchmark where the agent fails tells you nothing unless you know the task was solvable. So the suite
ships a **scripted control** — a deterministic Playwright script that performs each task correctly.

The control solves **36 / 36 tasks in both observation modes**. That single line is what makes every
subsequent failure attributable to the agent rather than to a broken fixture, a flaky selector, or an
impossible task. Without it, a 60% agent score is unreadable.

## The ablation: does the model want pixels or structure?

Same agent, same tasks, same budget — only the observation changes:

- **`dom`** — a structured accessibility-tree serialisation of the page
- **`screenshot`** — a rendered image of the same page

This is the design question for anyone building a computer-use agent, and it is cheap to answer
properly once the harness exists.

## Measured results

Agent `gemma4:31b-it-qat` via Ollama at `temperature=0`, one run per task per mode over 36 tasks
(72 episodes).

| observation | solved | success rate | 95% CI (Wilson) | mean steps | mean wall-clock |
|---|---|---|---|---|---|
| `dom` | 34 / 36 | **94%** | [82%–98%] | 5.2 | 129s |
| `screenshot` | 30 / 36 | **83%** | [68%–92%] | 5.5 | 110s |

**DOM beats screenshot by +11 points — and the confidence intervals overlap.** The honest reading is
"DOM is at least as good and probably better on this suite," not a knockout. Reporting the +11 without
the overlapping intervals would overclaim from 36 tasks.

The gap is concentrated exactly where you would predict:

| observation | easy | medium | hard |
|---|---|---|---|
| `dom` | 100% (13/13) | 100% (15/15) | 75% (6/8) |
| `screenshot` | 100% (13/13) | 80% (12/15) | 62% (5/8) |

Both modes are perfect on easy single-action tasks. Screenshot mode starts dropping multi-item cart
tasks at *medium* difficulty, where DOM is still flawless — evidence that the extra load of reading
pixels costs the model precisely when it also has to track multi-step state. The failure is not
"vision is worse at seeing"; it is that vision consumes capacity the model needed for state tracking.

## The failure taxonomy is the deliverable

Every failed episode is recorded with its full session trace and classified into an auditable
taxonomy rather than counted as a generic miss. A success rate tells you whether to ship; the taxonomy
tells you what to fix. Sessions are recorded in full so any episode can be replayed step by step
instead of re-run and hoped for.
