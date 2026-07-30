---
title: "Operating systems: from OSTEP to the kernel"
date: 2026-07-24 10:00:00 +0530
categories: [Resources, Systems]
tags: [operating-systems, ostep, xv6, linux]
description: >-
  The OS path: OSTEP as the spine, xv6 and MIT 6.1810 for building, TLPI for
  the Linux interface, and where kernel-adjacent engineering knowledge pays off.
---

Operating systems knowledge compounds better than almost anything else in the stack: schedulers,
virtual memory, and file systems reappear as thread pools, caches, and storage engines in every
system you'll ever build. Two projects on this site — a paged KV cache and a continuous-batching
scheduler — are OS ideas transplanted into LLM serving, which is exactly the point.

## The spine

- **[Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/)** (OSTEP) —
  Remzi and Andrea Arpaci-Dusseau. Free online, and the best-written textbook in systems:
  virtualization, concurrency, persistence, one honest chapter at a time with real homework. If
  you read one OS book, it's this one.
- **[xv6](https://pdos.csail.mit.edu/6.1810/2025/xv6.html)** — MIT's teaching kernel: a complete
  Unix-like OS in ~10k lines of readable C with
  [a commentary book](https://pdos.csail.mit.edu/6.1810/2025/xv6/book-riscv-rev5.pdf). Reading a
  whole kernel end to end demystifies the machine like nothing else.
- **[MIT 6.1810](https://pdos.csail.mit.edu/6.1810/)** (formerly 6.S081) — the labs that go with
  xv6: implement page tables, traps, copy-on-write fork, and a file system. All materials public.
  Doing three or four of these labs is worth more than reading any five books.

## The Linux layer

- **[The Linux Programming Interface](https://man7.org/tlpi/)** — Michael Kerrisk. 1,500 pages and
  worth its shelf space: the definitive reference on syscalls, processes, signals, and IPC, by the
  maintainer of the man-pages project. Use it as an encyclopedia.
- **[Linux Kernel Development](https://www.oreilly.com/library/view/linux-kernel-development/9780768696974/)**
  — Robert Love. Dated in specifics, still the friendliest guided tour of how the scheduler, memory
  management, and interrupts hang together.
- **[LWN.net](https://lwn.net/)** — where kernel development is actually documented. The kernel
  index and merge-window summaries are how you stay current after the books.

## The practical layer

- **[Julia Evans' zines and blog](https://jvns.ca/)** — strace, /proc, signals, containers —
  short, precise, and immediately usable. The fastest route from "book knowledge" to "debugging a
  live process at 2am."
- **[Brendan Gregg's site](https://www.brendangregg.com/)** — covered fully in the systems
  performance post, but his [Linux performance page](https://www.brendangregg.com/linuxperf.html)
  belongs here too: the diagram of observability tools per subsystem is the map.

## A path that works

OSTEP cover to cover with homework → xv6 book alongside the source → two or three 6.1810 labs →
TLPI as reference forever after. Six months of evenings, and the payoff is permanent: every
"mysterious" production behavior — a hung process, a memory blow-up, a slow fsync — becomes a
question you know how to decompose.
