---
title: "Machine learning foundations: Murphy and the load-bearing books"
date: 2026-07-26 10:00:00 +0530
categories: [Resources, Machine Learning]
tags: [machine-learning, murphy, statistics, textbooks]
description: >-
  The ML bookshelf that holds weight: Kevin Murphy's Probabilistic Machine
  Learning volumes as the spine, with ESL, Bishop, and the math that makes
  them readable.
---

Most ML content optimizes for feeling productive. Textbooks optimize for being right. This is the
short list that holds weight, with Kevin Murphy's two volumes as the spine.

## The spine: Murphy

- **[Probabilistic Machine Learning: An Introduction](https://probml.github.io/pml-book/book1.html)**
  (2022) — Kevin Murphy. The modern replacement for a whole shelf: probability, linear models,
  deep networks, trees, kernels — all in one consistent probabilistic voice, with
  [free draft PDF and code](https://github.com/probml/pyprobml) online. When a concept is fuzzy,
  this is where I check my understanding against something rigorous.
- **[Probabilistic Machine Learning: Advanced Topics](https://probml.github.io/pml-book/book2.html)**
  (2023) — the second volume: inference, generative models, causality. Not a
  first read — it is the reference you grow into, and having it visible on the shelf is a good
  reminder of how deep the field actually goes.

Murphy's precision is the point. After reading his treatment of, say, variational inference, you
know exactly which assumptions you're making — which is the difference between using a method and
gesturing at it.

## The rest of the shelf

- **[The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)** — Hastie,
  Tibshirani, Friedman. Free PDF. Still the sharpest treatment of the classical core:
  bias–variance, regularization, boosting, model selection. When a deep model underperforms
  gradient boosting on tabular data — which still happens constantly — this book explains why.
  Start with [An Introduction to Statistical Learning](https://www.statlearning.com/) if ESL's
  math is a wall.
- **[Deep Learning: Foundations and Concepts](https://www.bishopbook.com/)** (2024) — Bishop &
  Bishop. The successor to PRML, rebuilt for the transformer era; free to read online. The
  cleanest mathematical presentation of modern architectures.
- **[Mathematics for Machine Learning](https://mml-book.github.io/)** — Deisenroth, Faisal, Ong.
  Free PDF. The gap-filler: exactly the linear algebra, calculus, and probability the other books
  assume, and nothing more.
- **[Introduction to Probability](https://projects.iq.harvard.edu/stat110/home)** — Blitzstein &
  Hwang, with the Stat 110 lectures free online. If probability is shaky, everything above is
  built on sand; fix it here first.

## How to read them

Textbooks reward a different mode than blogs: slowly, with a notebook, doing derivations by hand
and reproducing at least one figure per chapter in code. One chapter of Murphy done that way beats
ten survey posts — I keep relearning this. And read with a project in hand: theory anchored to a
system you're building (an eval harness, a router, a fine-tune) sticks; theory read in the
abstract evaporates in weeks.
