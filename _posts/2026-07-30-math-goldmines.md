---
title: "Math goldmines: the free books that carry CS"
date: 2026-07-30 12:30:00 +0530
categories: [Resources, Books]
tags: [math, linear-algebra, cryptography, goldmines]
description: >-
  The freely available math that punches far above its fame: Evan Chen's
  Napkin, MIT's Mathematics for CS, Linear Algebra Done Wrong, and the
  Boneh–Shoup cryptography book with cryptopals as its gym.
---

Math resources have the worst discovery problem: the famous books are gates, and the actual
on-ramps are free PDFs passed around like samizdat. Here are the ones worth the hype they never
got.

## The on-ramps

- **[An Infinitely Large Napkin](https://web.evanchen.cc/napkin.html)** — Evan Chen. A free
  ~1000-page tour of university math (groups through Galois theory, topology, measure,
  category theory) written for people who want the *ideas* fast, with honest signposts about
  what's being skipped. There is nothing else like it: it optimizes for "what is this field and
  why," which is exactly what an engineer raiding math needs.
- **[Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)**
  — Lehman, Leighton, Meyer (MIT 6.042, free book + lectures). Proofs, induction, number theory,
  graphs, counting, probability — the discrete foundation under algorithms, taught with CS
  examples throughout. The proofs chapters alone fix the "I can code it but can't prove it" gap.
- **[Linear Algebra Done Wrong](https://www.math.brown.edu/streil/papers/LADW/LADW.html)** —
  Sergei Treil, free. The title jokes at Axler's famous book: this one *keeps* determinants and
  matrices front and center, which is the version computer people actually use. Rigorous, terse,
  and free forever.

## Interactive and reference

- **[Seeing Theory](https://seeing-theory.brown.edu/)** — Brown's interactive probability
  visualizations. Twenty minutes here fixes more intuition about distributions and inference than
  a week of slides.
- **[The Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)** and
  **[matrixcalculus.org](https://www.matrixcalculus.org/)** — the identity reference and the
  derivative calculator. Between them, matrix calculus stops being a hazing ritual.

## Applied math in disguise: cryptography

- **[A Graduate Course in Applied Cryptography
](https://toc.cryptobook.us/)** — Dan Boneh and
  Victor Shoup, free. The definitive modern crypto text: security definitions and proofs done
  properly, from ciphers through zero-knowledge. It's the book Stanford's famous course grew
  into, and it costs nothing.
- **[Cryptopals](https://cryptopals.com/)** — the gym for the book above: 48+ challenges where
  you *break* real crypto (ECB cut-and-paste, CBC padding oracles, nonce reuse) with nothing but
  code. The single most effective "learn by attacking" curriculum in any field; finishing set 3
  changes how you read every security adv
isory forever.

## How to raid math as an engineer

Don't read linearly; raid with a purpose. Napkin to scout a field, 6.042 when proofs feel shaky,
Treil when linear algebra needs rebuilding under ML, Boneh–Shoup plus
cryptopals when you want the math to fight back. A theorem you used beats ten you highlighted.
