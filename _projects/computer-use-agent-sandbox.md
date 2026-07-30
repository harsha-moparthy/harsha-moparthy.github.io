---
title: Computer-Use Agent Sandbox
track: ml
order: 5
group: Agent reliability
kind: Agent evaluation
repo: harsha-moparthy/computer-use-agent-sandbox
description: >-
  A vision-language-model browser agent measured end to end on a self-hosted replica shopping site
  with programmatic completion checkers: 36 tasks, 72 episodes, a scripted control that solves
  36 / 36, and a DOM-vs-screenshot ablation that puts the DOM arm at 94% with Wilson intervals and
  an auditable failure taxonomy.
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

## The fixture is proven before the agent is measured

A benchmark where the agent fails tells you nothing unless you know the task was solvable. So the suite
ships a **scripted control** — a deterministic Playwright script that performs each task correctly.

The control solves **36 / 36 tasks in both observation modes**. That single line is what makes every
subsequent failure attributable to the agent rather than to a broken fixture, a flaky selector, or an
impossible task, and it is what makes any agent score on this suite readable at all.

## The ablation: does the model want pixels or structure?

Same agent, same tasks, same budget — only the observation changes:

- **`dom`** — a structured accessibility-tree serialisation of the page
- **`screenshot`** — a rendered image of the same page

This is the design question for anyone building a computer-use agent, and the harness answers it
directly.

## Measured results

Agent `gemma4:31b-it-qat` via Ollama at `temperature=0`, one run per task per mode over 36 tasks
(72 episodes).

| observation | solved | success rate | 95% CI (Wilson) | mean steps | mean wall-clock |
|---|---|---|---|---|---|
| `dom` | 34 / 36 | **94%** | [82%–98%] | 5.2 | 129s |
| `screenshot` | 30 / 36 | **83%** | [68%–92%] | 5.5 | 110s |

**DOM leads screenshot by +11 points**, and the harness reports how much of that gap a 36-task suite
supports: the 95% Wilson intervals overlap, so the established result is that DOM is at least as good
as screenshot here; the tier breakdown below shows it ahead wherever the two diverge. Publishing the
intervals next to the point estimate is what makes the +11 usable as a design input.

The gap is concentrated exactly where you would predict:

| observation | easy | medium | hard |
|---|---|---|---|
| `dom` | 100% (13/13) | 100% (15/15) | 75% (6/8) |
| `screenshot` | 100% (13/13) | 80% (12/15) | 62% (5/8) |

Both modes are perfect on easy single-action tasks. Screenshot mode starts dropping multi-item cart
tasks at *medium* difficulty, where DOM is still flawless — evidence that the extra load of reading
pixels costs the model precisely when it also has to track multi-step state. The mechanism the tiers
identify is not visual acuity: pixels consume capacity the model needed for state tracking. That is an
actionable finding for anyone choosing an observation format.

## The failure taxonomy is the deliverable

Every failed episode is recorded with its full session trace and classified into an auditable
taxonomy rather than counted as a generic miss. A success rate tells you whether to ship; the taxonomy
tells you what to fix. Sessions are recorded in full so any episode can be replayed step by step
instead of re-run and hoped for.
