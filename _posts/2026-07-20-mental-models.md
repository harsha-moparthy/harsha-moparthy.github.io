---
title: "Mental models: building the latticework"
date: 2026-07-20 10:00:00 +0530
categories: [Resources, Clear Thinking]
tags: [mental-models, munger, farnam-street]
description: >-
  Where to actually learn mental models — the books, the one speech that started
  it all, and the handful of models that earn their keep in engineering work.
---

"You've got to have models in your head... and you've got to array your experience — both
vicarious and direct — on this latticework of models." That's Charlie Munger in
[*A Lesson on Elementary, Worldly Wisdom*](https://fs.blog/great-talks/a-lesson-on-worldly-wisdom/)
(USC, 1994), the talk that started the whole genre. Read it before any book on the subject — it is
the primary source and still the best.

## The canon

- **[The Great Mental Models](https://fs.blog/tgmm/), volumes 1–4** (Farnam Street / Portfolio) —
  the most systematic treatment: general thinking concepts, then models from physics, chemistry,
  biology, systems, math, economics. One model per chapter, each with failure modes — which is what
  separates it from listicles. Volume 1 is the right entry point.
- **[Poor Charlie's Almanack](https://www.stripe.press/poor-charlies-almanack)** — the latticework
  demonstrated rather than described, across decades of talks.
- **[Seeking Wisdom](https://www.amazon.com/Seeking-Wisdom-Darwin-Munger-3rd/dp/1578644283)** by
  Peter Bevelin — drier than the others but the most complete inventory of misjudgment, drawn from
  Darwin, Munger, and Feynman.
- **[The FS mental models index](https://fs.blog/mental-models/)** — the free reference. Bookmark
  it; use it as a checklist when a decision feels stuck, not as reading material.

## The models that earn their keep in engineering

A model you can't apply is trivia. These are the ones I reach for weekly:

- **Inversion** — debug by asking what would *have* to be true for this failure to occur.
- **Second-order effects** — every cache, retry, and fallback you add has behavior *under failure*
  that is the real design question.
- **Margin of safety** — from engineering via Graham: the interesting question is never the
  expected load, it's the load at which things break and what happens then.
- **Base rates** — "how often does this kind of project ship on time" beats any amount of
  inside-view planning detail.
- **Map is not the territory** — dashboards, benchmarks, and evals are maps. Every project I've
  built has found at least one place where the map lied.
- **Circle of competence** — the honest edge of what you know. The practical version: write down
  what you'd bet on vs. what you'd merely argue for.

## How to actually internalize them

Reading produces recognition, not fluency. What worked for me: after any significant decision or
postmortem, name the model that applied (or would have helped) in one line. A model you have used
five times on real problems is worth fifty you can define.
