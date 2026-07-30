---
title: "Compiler and interpreter goldmines: build the language"
date: 2026-07-30 11:30:00 +0530
categories: [Resources, Systems]
tags: [compilers, interpreters, parsing, goldmines]
description: >-
  The language-implementation canon that actually gets read: Crafting
  Interpreters, Russ Cox's essays, Eli Bendersky's archive, matklad, and the
  Architecture of Open Source Applications.
---

Nothing demystifies computing like implementing a language — and the field quietly produced some
of the best-written technical material anywhere. These are the entries worth your evenings.

## The modern classic

- **[Crafting Interpreters](https://craftinginterpreters.com/)** — Bob Nystrom. Free online, and
  simply one of the best technical books ever written: a complete tree-walking interpreter in
  Java, then a bytecode VM with GC in C, every single line of both in the book. The prose is so
  good it hides how much you're learning. If "compilers" ever felt like a graduate gate, this is
  the counter-evidence.
- **[Game Programming Patterns](https://gameprogrammingpatterns.com/)** — Nystrom's other free
  book. Not compilers, but the chapters on bytecode, object pools, and data locality are systems
  design education disguised as game dev.

## The essays

- **[Russ Cox: research.swtch.com](https://research.swtch.com/)** — the Go co-lead's essay
  archive. The [regular expression series](https://research.swtch.com/implementing-regular-expressions)
  (why Thompson NFA beats backtracking, how RE2 works) is the single best compiler-adjacent read
  on the internet; the ["Zip files all the way down"](https://research.swtch.com/zip) and version
  -selection essays show what rigorous engineering writing looks like.
- **[Eli Bendersky](https://eli.thegreenplace.net/)** — twenty years of patient deep dives:
  parsing (his [recursive descent and Pratt parsing posts](https://eli.thegreenplace.net/tag/recursive-descent-parsing)
  are the standard references), LLVM internals, Go assembly, CPython internals. The archive
  rewards systematic raiding.
- **[matklad](https://matklad.github.io/)** — Alex Kladov, rust-analyzer's original author.
  ["Simple but Powerful Pratt Parsing"](https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html)
  finally made operator precedence click for a generation; the posts on IDE-grade incremental
  analysis, testing strategy, and code architecture generalize far beyond compilers.

## Reading real codebases

- **[The Architecture of Open Source Applications](https://aosabook.org/)** + **500 Lines or
  Less** — free volumes where maintainers explain their own systems' architecture (LLVM, nginx,
  SQLite chapters are standouts), and then build small complete systems in under 500 lines. The
  missing genre: how software is *actually* structured, written by the people who structured it.
- **[Writing an Interpreter in Go](https://interpreterbook.com/)** /
  **[Writing a Compiler in Go](https://compilerbook.com/)** — Thorsten Ball. The
  test-driven companion path to Nystrom: everything built via TDD, which doubles as a masterclass
  in testing language tooling.

## Why this is on a systems-portfolio site

Language implementation is transfer learning for everything else: parsers are protocol decoders
(the SOAP wrapper project), bytecode VMs are schedulers with opinions, and GC is cache
management wearing a costume. The habit these books build — hold the whole pipeline in your head,
from characters to behavior — is the systems habit.
