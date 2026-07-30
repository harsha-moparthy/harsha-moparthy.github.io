---
title: "Systems goldmines: concurrency, memory, and the CPU"
date: 2026-07-30 10:30:00 +0530
categories: [Resources, Systems]
tags: [concurrency, cpu, performance, goldmines]
description: >-
  The under-known heavyweights of low-level systems: McKenney's perfbook,
  Drepper's memory paper, Agner Fog's manuals, Bakhvalov's free performance
  book, 1024cores, Preshing, and the linker essays.
---

TLPI is the known god-tier book for Linux. This list is its peers that somehow stayed obscure —
each one written by the person who actually built or maintains the thing it explains.

## Concurrency, from the kernel's parallelism maintainer

- **[Is Parallel Programming Hard, And, If So, What Can You Do About It?](https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html)**
  — Paul McKenney, free, continuously updated. The author maintains RCU in the Linux kernel; this
  is four decades of parallel-programming scar tissue in one book: counting (harder than you
  think), locking honestly appraised, memory ordering, RCU itself. If you read one thing on this
  list, read this.
- **[The Little Book of Semaphores](https://greenteapress.com/wp/semaphores/)** — Allen Downey,
  free. A problem book: classic synchronization puzzles (readers-writers, dining philosophers,
  the unlikely-sounding ones like "the sushi bar") posed *before* their solutions. Working
  through it is the difference between recognizing concurrency patterns and deriving them.
- **[1024cores](https://www.1024cores.net/)** — Dmitry Vyukov (author of Go's race detector and
  the MPSC queues everyone copies). Lock-free algorithms, memory models, and synchronization laid
  out by someone who ships them. His bounded MPMC queue writeup is the canonical one.
- **[Preshing on Programming](https://preshing.com/)** — the gentlest correct introduction to
  memory ordering that exists: acquire/release semantics, weak vs strong models, lock-free
  fundamentals, each post with diagrams that make the reorderings visible.
- **[What every systems programmer should know about concurrency](https://assets.bitbashing.io/papers/concurrency-primer.pdf)**
  — Matt Kline. Sixteen pages; the ideal first read before the two books above.

## Memory and the microarchitecture

- **[What Every Programmer Should Know About Memory](https://akkadia.org/drepper/cpumemory.pdf)**
  — Ulrich Drepper (glibc maintainer at the time). 114 pages on caches, TLBs, NUMA, and
  prefetching. From 2007 and still the reference — the constants changed, the model didn't.
- **[Agner Fog's optimization manuals](https://www.agner.org/optimize/)** — five free manuals,
  maintained for over two decades: C++ optimization, assembly, microarchitecture of every x86
  generation, and the instruction tables (latency/throughput for every instruction on every
  CPU). When people say "check Agner," this is what they mean.
- **[Performance Analysis and Tuning on Modern CPUs](https://easyperf.net/my_book/)** — Denis
  Bakhvalov. Free, open-source ([PDF on GitHub](https://github.com/dendibakh/perf-book)); the
  second edition adds ARM and a chapter of case studies. The bridge between Gregg's system-level
  view and Agner's instruction-level one: top-down analysis, PMU counters, and what to actually
  do about the bottleneck you found. His [easyperf blog](https://easyperf.net/) is the ongoing
  serial.
- **[Understanding Software Dynamics](https://www.oreilly.com/library/view/understanding-software-dynamics/9780137589692/)**
  — Richard Sites (co-designer of the DEC Alpha). The book on finding the *missing time* in live
  systems — where did those 50ms go — built around tracing rather than sampling. Nothing else
  covers this territory.
- **[Putting the "You" in CPU](https://cpu.land/)** — Lexi Mattick. A free short book answering
  "what actually happens when you run a program" — syscalls, ELF, scheduling, forking — with the
  energy of someone who just found out and *has to tell you*. The best on-ramp to everything
  above.

## The dark art nobody teaches: linking

- **[Ian Lance Taylor's 20-part linker essays](https://www.airs.com/blog/archives/38)** — the
  author of gold explaining symbols, relocations, TLS, and shared libraries from first
  principles. Linking is where "it compiles" meets reality, and this is the only complete
  treatment written by a linker author.
- **[Linkers and Loaders](https://www.iecc.com/linker/)** — John Levine's book, free online. The
  book-length companion: object formats, dynamic linking, position-independent code.

## The blogs that go with them

- **[Chris Wellons (nullprogram)](https://nullprogram.com/)** — C and systems craftsmanship;
  arena allocators, fuzzing, writing libraries with zero dependencies.
- **[Paul Khuong](https://pvk.ca/)** — the deep end: SBCL internals, cache-efficient data
  structures, and numerical tricks measured properly.
- **[John Regehr](https://blog.regehr.org/)** — undefined behavior, compiler testing, and why
  your C program is lying to you. The
  [UB guide](https://blog.regehr.org/archives/213) should be required reading.

Every entry here rewards the same habit: read with `perf`, a compiler explorer tab, or a test
program open. These authors all wrote from experiments; the material only transfers the same way.
