---
title: "Probability and statistics: the load-bearing layer under ML"
date: 2026-07-30 09:00:00 +0530
categories: [Resources, Machine Learning]
tags: [probability, statistics, blitzstein, wasserman]
description: >-
  Where to actually learn probability and statistics: Stat 110, Wasserman's
  All of Statistics, and the applied habits — intervals, bootstraps, and
  paired tests — that every honest benchmark depends on.
---

Every eval, benchmark, and A/B comparison is a statistics problem wearing a systems costume. This
is the layer that decides whether your numbers mean anything.

## Learn probability properly

- **[Introduction to Probability](https://projects.iq.harvard.edu/stat110/home)** — Blitzstein &
  Hwang, with the complete
  [Stat 110 lectures](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)
  free on YouTube. The best intuition-first treatment: stories and problems, conditioning as the
  soul of statistics. The book's problems are the point — do them.
- **[Probability Theory: The Logic of Science](https://bayes.wustl.edu/etj/prob/book.pdf)** —
  E.T. Jaynes. Opinionated, occasionally cranky, and the deepest answer to *why* probability is
  the right calculus for reasoning under uncertainty. Read after Blitzstein, not before.

## Statistics for people who ship

- **[All of Statistics](https://link.springer.com/book/10.1007/978-0-387-21736-9)** — Larry
  Wasserman. Exactly what the title promises: the whole field's skeleton (estimation, confidence
  sets, testing, bootstrap, regression) in brisk, honest chapters. The right book for engineers
  who need working command fast.
- **[Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/)** — Richard McElreath,
  with [free lectures](https://www.youtube.com/playlist?list=PLDcUM9US4XdPz-KxHM4XHt7uUVGWWVSus).
  The best applied Bayesian course: builds models from scratch and is ruthless about what
  inference does and doesn't license.
- **[An Introduction to the Bootstrap](https://www.taylorfrancis.com/books/mono/10.1201/9780429246593/introduction-bootstrap-bradley-efron-tibshirani)**
  — Efron & Tibshirani. The bootstrap is the workhorse of practical uncertainty; knowing its
  assumptions (and where resampling structure matters) pays off constantly.

## The applied habits, learned from the above

These are the specific practices this reading installed, all visible in the projects here:

- **Wilson intervals over Wald** for small-n success rates — Wald produces bounds outside [0,1]
  exactly where evals live (rates near 0 and 1, n under 50).
- **Cluster/paired bootstrap** — resample *tasks*, keeping each task's runs together; run-level
  resampling understates between-task variance, which is usually the dominant term.
- **Paired designs and McNemar's test** for comparing two systems on the same items — the RAG
  study's headline claims rest on exact McNemar p-values, not eyeballed deltas.
- **A/A tests before A/B claims** — the trajectory-eval harness measures its own false-alarm rate
  (6%) before claiming any regression detection; calibration first, claims second.
- **State n, always.** A percentage without its denominator is decoration.

If you only do one thing from this post: next time you report an eval number, attach an interval
and the n. The discipline that follows from that one habit pulls the rest of this reading in
behind it.
