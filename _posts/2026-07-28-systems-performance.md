---
title: "Systems performance: measuring before believing"
date: 2026-07-28 10:00:00 +0530
categories: [Resources, Systems]
tags: [performance, profiling, benchmarking, brendan-gregg]
description: >-
  The performance canon: Brendan Gregg's book and methods, napkin math,
  latency numbers, and the discipline of benchmarking honestly.
---

Every project on this site ships with a measurement harness, and this reading list is why.
Performance work is where wrong beliefs are most expensive and most common — the canon below is
about replacing belief with measurement.

## The canon

- **[Systems Performance](https://www.brendangregg.com/systems-performance-2nd-edition-book.html)**
  (2nd ed.) — Brendan Gregg. The reference: CPUs, memory, filesystems, disks, networks, and the
  methodologies that keep you from drowning in tools. The
  [USE method](https://www.brendangregg.com/usemethod.html) (utilization, saturation, errors, per
  resource) is the single most reusable idea — it turns "it's slow" into a checklist.
- **[BPF Performance Tools](https://www.brendangregg.com/bpf-performance-tools-book.html)** — Gregg
  again; the modern observability toolbox. Even just knowing what `off-CPU analysis` and
  [flame graphs](https://www.brendangregg.com/flamegraphs.html) can show changes what questions
  you ask.
- **[Napkin math](https://github.com/sirupsen/napkin-math)** — Simon Eskildsen's numbers and
  drills for order-of-magnitude estimation, plus
  [the latency numbers every programmer should know](https://colin-scott.github.io/personal_website/research/interactive_latency.html).
  Being able to say "that's 10x more than physics allows" *before* profiling is a superpower, and
  it's learnable.

## Benchmarking without fooling yourself

- **[How NOT to Measure Latency](https://www.youtube.com/watch?v=lJ8ydIuPFeU)** — Gil Tene. The
  talk that ruins bad benchmarks forever: coordinated omission, why averages lie, why p99 of a
  load generator is not p99 of a user. Watch it before publishing any latency number.
- **["Producing Wrong Data Without Doing Anything Obviously Wrong!"](https://users.cs.northwestern.edu/~robby/courses/322-2013-spring/mytkowicz-wrong-data.pdf)**
  (Mytkowicz et al.) — measurement bias from link order and environment size can exceed the effect
  you're studying. The paper behind my habit of running baselines and treatments in the same
  harness, interleaved.
- The working rules I hold myself to, all learned from the above the hard way: state the
  hardware; commit the harness with the numbers; report the distribution, not the mean; and keep
  the losing rows in the table — a benchmark that can't embarrass you can't inform you either.

## Where it shows up in practice

The KV-cache study on this site found configurations where perplexity stayed identical while task
accuracy fell 67 points — the measurement-selection lesson in miniature. The serving engine keeps
the row where Hugging Face's static batching beats it on raw throughput, because that row sizes
the remaining kernel-level headroom. Both habits trace directly to this reading list: the number
you don't report is the one that would have taught you the most.
