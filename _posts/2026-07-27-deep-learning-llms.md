---
title: "Deep learning and LLMs: learn it by building it"
date: 2026-07-27 10:00:00 +0530
categories: [Resources, Machine Learning]
tags: [deep-learning, llms, karpathy, transformers]
description: >-
  The build-first path into modern deep learning: Karpathy's Zero to Hero,
  nanoGPT, the papers that are actually worth reading, and the engineering
  layer around LLMs.
---

For classical foundations, see the ML foundations post. This is the modern half — and here the
best pedagogy is build-first.

## Build it from scratch

- **[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)** — Andrej Karpathy.
  The best deep-learning pedagogy in existence: backprop from raw scalars (micrograd), through
  language models, to
  [building GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY) and
  [reproducing GPT-2](https://github.com/karpathy/build-nanogpt). Type every line yourself; the
  typing is the learning.
- **[nanoGPT](https://github.com/karpathy/nanoGPT)** — the ~600-line training codebase that
  demystifies the whole stack. Reading it end to end kills the illusion that LLM training is
  exotic.
- **[Dive into Deep Learning](https://d2l.ai/)** — free, runnable-notebook textbook; the best
  bridge between Karpathy's intuition and Bishop's formality.

## The papers actually worth reading

The field produces thousands of papers a year; these are the ones whose ideas you'll use weekly:

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — read *after* building a
  transformer, when every design choice suddenly makes sense.
- [Scaling laws (Kaplan et al.)](https://arxiv.org/abs/2001.08361) and
  [Chinchilla](https://arxiv.org/abs/2203.15556) — why model/data/compute ratios dominate
  architecture cleverness.
- [InstructGPT](https://arxiv.org/abs/2203.02155), [DPO](https://arxiv.org/abs/2305.18290), and
  [GRPO (DeepSeekMath)](https://arxiv.org/abs/2402.03300) — the post-training lineage. I
  implemented DPO and GRPO from scratch for the Toolcall DPO project, and the papers only fully
  clicked at that point — the loss functions are two dozen lines each, and every subtlety lives in
  the data and the reference model.
- [FlashAttention](https://arxiv.org/abs/2205.14135) and the
  [vLLM/PagedAttention paper](https://arxiv.org/abs/2309.06180) — where systems thinking meets
  attention; PagedAttention is an OS idea, which is why I built PageServe.
- **[Lilian Weng's blog](https://lilianweng.github.io/)** — the survey layer: her posts on
  attention, RLHF, and agents are the best-maintained maps of each subfield.

## The engineering layer

- **[AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)** and
  [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning-systems/9781098107956/)
  — Chip Huyen. The production reality: evals, data flywheels, serving, drift.
- **[Hugging Face courses](https://huggingface.co/learn)** — the practical toolchain
  (transformers, PEFT, TRL) with runnable notebooks.

## The loop that works

Watch one Karpathy video → rebuild it without the video → read the corresponding paper → then
attach a measurement harness and make a claim you can defend with numbers. That last step is the
difference between following the field and doing the work — every ML project on this site is that
step, repeated.
