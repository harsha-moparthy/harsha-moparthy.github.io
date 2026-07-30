---
title: "GPU and ML-performance goldmines: making it go fast"
date: 2026-07-30 12:00:00 +0530
categories: [Resources, Machine Learning]
tags: [gpu, cuda, ml-performance, goldmines]
description: >-
  Where the GPU-performance knowledge actually lives: PMPP, GPU MODE, Simon
  Boehm's matmul worklog, Horace He's brrrr essay, the Ultra-Scale Playbook,
  and Stas Bekman's open ML-engineering book.
---

ML performance knowledge lives in a strange place: too systems-y for ML courses, too ML-y for
systems courses. The result is a set of goldmines almost nobody assigns.

## The mental model

- **[Making Deep Learning Go Brrrr From First Principles](https://horace.io/brrr_intro.html)** —
  Horace He (torch.compile). The single most clarifying essay in the field: every workload is
  compute-bound, memory-bandwidth-bound, or overhead-bound, and each regime has different fixes.
  Read this before touching a profiler; it tells you what the profiler will mean.
- **[The Little Book of Deep Learning](https://fleuret.org/public/lbdl.pdf)** — François Fleuret.
  Free, 160 phone-formatted pages: the whole conceptual core of DL with unusual precision-per-
  page. The companion when
 you need the concept, not the survey.

## The craft, learned by watching

- **[Programming Massively Parallel Processors](https://www.sciencedirect.com/book/9780323912310/programming-massively-parallel-processors)**
  (4th ed., Hwu, Kirk, El Hajj) — "the PMPP book": still the canonical CUDA text — memory
  coalescing, tiling, occupancy — and the shared vocabulary of everyone doing kernel work.
- **[GPU MODE](https://www.youtube.com/@GPUMODE)** — the community (lectures + Discord) where
  working kernel engineers teach: profiling lectures, Triton, quantization, ring attention. The
  live-coding sessions are the apprenticeship the field never had.
- **[How to Optimize a CUDA Matmul Kernel](https://siboehm.com/articles/22/CUDA-MMM)** — Simon
  Boehm (now Anthropic). One kernel taken through ten optimization stages from 1% to ~94% of
  cuBLAS, with the reasoning and the dead ends preserved. The single best worked example of
  performance engineering on the internet, GPU or otherwise.
- **[The Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook)** —
  Hugging Face's nanotron team. Free, interactive, built on 4,000+ real scaling experiments:
  data/tensor/pipeline parallelism, ZeRO, and overlap, from one GPU to thousands. The distributed-
  training knowledge that used to live only inside big labs.
- **[ML Engineering Open Book](https://github.com/stas00/ml-engineering)** — Stas Bekman (BLOOM
  training). The operator's notebook: debugging NCCL hangs, node-failure playbooks, storage
  throughput, the "how it actually goes wrong at 3am" layer no paper covers.

## The references you'll keep open

- **[Understanding Deep Learning](https://udlbook.github.io/udlbook/)** — Simon Prince. Free,
  and the best-illustrated DL textbook in existence; the figures alone repair more misconceptions
  than most courses.
- **[The Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)** — every
  matrix identity and derivative you'll ever need, in one PDF. Not reading material; keep it
  within reach whenever deriving gradients.
- **[What Are Embeddings](https://vickiboykis.com/what_are_embeddings/)** — Vicki Boykis. A free
  book-length answer to a question everyone pretends they've fully internalized — from one-hot to
  transformers, with the engineering context most explanations drop.

## The connecting thread

PageServe and the KV-cache study on this site are downstream of exactly this reading: paging,
bandwidth-vs-compute reasoning, and profile-before-believing. The material transfers because GPU
performance *is* systems performance — same discipline, hotter chip.
