---
title: "Competitive programming goldmines: Halim and the deep archive"
date: 2026-07-30 10:00:00 +0530
categories: [Resources, Competitive Programming]
tags: [competitive-programming, halim, goldmines]
description: >-
  The CP resources serious competitors use that rarely make beginner lists:
  Steven Halim's CP4 and Methods to Solve, VisuAlgo, Sannemo's free book,
  KACTL, and the Codeforces Catalog.
---

The starter resources (CPH, CSES, USACO Guide) are in my earlier CP post. This is the layer
beneath — the material strong competitors actually keep open, which almost never appears on
beginner lists.

## The Halim universe

- **[Competitive Programming 4](https://cpbook.net/)** — Steven Halim, Felix Halim, Suhendry
  Effendy. Subtitled "the lower bound of programming contests in the 2020s," and that's the right
  frame: two volumes that are less a tutorial than a *map of everything examinable*, with
  thousands of classified problems. Where CPH teaches you techniques, CP4 tells you what exists —
  its taxonomy is how you discover that your gap is, say, DP on broken profiles before a contest
  exposes it.
- **[Methods to Solve](https://www.comp.nus.edu.sg/~stevenha/methodstosolve.html)** — Halim's
  companion site: thousands of judge problems, each labeled with the technique that solves it.
  Reverse it for training: pick a technique, solve five problems *knowing* the tag, then five
  mixed ones where you must recognize it cold. Recognition is the contest skill.
- **[VisuAlgo](https://visualgo.net/)** — Halim's algorithm visualizations: segment trees, max
  flow, suffix arrays, animated step by step with your own inputs. The fastest way to repair a
  wrong mental model — watching lazy propagation actually propagate beats re-reading any proof.

## The free book nobody assigns

- **[Principles of Algorithmic Problem Solving](https://heap.link/)** — Johan Sannemo. Free PDF,
  written by an IOI/ICPC coach, and unusual in the best way: it teaches the *problem-solving
  process* (simplify, look for invariants, solve a smaller case) as explicitly as the algorithms
  themselves. The chapters between "intro" and "here's a segment tree" — the ones most books skip
  — are the reason to read it.

## The reference layer

- **[KACTL](https://github.com/kth-competitive-programming/kactl)** — KTH's ICPC team notebook:
  the most battle-tested algorithm library in the community, every routine fuzz-tested, sized to
  the 25-page ICPC limit. Read it even if you never compete in teams — seeing HLD or min-cost
  flow expressed in 40 tight, correct lines recalibrates what implementations should look like.
- **[cp-algorithms](https://cp-algorithms.com/)** — already in my starter post, but it belongs in
  any goldmine list too: the translated-and-maintained e-maxx wiki is still the single best
  technique reference.
- **[Codeforces Catalog](https://codeforces.com/catalog)** — the curated index over fifteen years
  of community blogs. The best explanations of advanced techniques (slope trick, Aliens trick,
  suffix automata) were never written as articles anywhere else — they're Codeforces blogs, and
  this is how you find them.

## The masterclass tier

- **[Petr Mitrichev's blog](https://petr-mitrichev.blogspot.com/)** — a legend's contest diaries,
  going back to 2009. The value isn't solutions; it's watching how one of the strongest solvers
  alive *narrates his own reasoning*, including the wrong turns. Read the posts where he struggles.
- **[The AtCoder DP contest](https://atcoder.jp/contests/dp)** plus
  [Errichto's](https://www.youtube.com/c/Errichto) and
  [Colin Galen's](https://www.youtube.com/c/ColinGalen) deep-dive videos — the modern oral
  tradition. Watching a strong solver think in real time is deliberate-practice feedback you
  cannot get from editorials.

The pattern across all of these: the goldmines aren't hidden because they're obscure — they're
hidden because they sit one layer past where most people stop.
