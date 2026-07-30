---
title: "Database goldmines: internals without the folklore"
date: 2026-07-30 11:00:00 +0530
categories: [Resources, Systems]
tags: [databases, sql, storage, goldmines]
description: >-
  The database-internals material practitioners actually learn from: Use The
  Index Luke, CMU 15-445/721, Database Internals, the Red Book, and the blogs
  where people build storage engines in public.
---

Databases are the rare field where the best material is genuinely free and genuinely deep — and
still most engineers never get past ORM folklore. This is the path through.

## The one every backend engineer should have read

- **[Use The Index, Luke](https://use-the-index-luke.com/)** — Markus Winand. A free book-length
  site on exactly one thing: how SQL indexing actually works (B-trees, composite index column
  order, index-only scans, why `LIKE '%x'` can't use an index) across Postgres, MySQL, Oracle,
  and SQL Server. The highest ratio of "queries fixed per page read" of anything on this site.
  His [Modern SQL](https://modern-sql.com/) covers what SQL grew after 1992 — window functions,
  lateral joins, `FILTER` — that most people still write application code to avoid.

## The courses that replaced the textbook

- **[CMU 15-445: Database Systems](https://15445.courses.cs.cmu.edu/)** — Andy Pavlo. Every
  lecture on YouTube, every project public: build a buffer pool, a B+tree, query executors, and
  concurrency control inside a real storage manager (BusTub). This is *the* modern internals
  course.
- **[CMU 15-721: Advanced Database Systems](https://15721.courses.cs.cmu.edu/)** — the graduate
  sequel: vectorized execution, query compilation, MVCC variants, modern OLAP architecture, taught
  through the papers that defined each.

## The books

- **[Database Internals](https://www.databass.dev/)** — Alex Petrov. The book for the layer the
  courses build: storage engines (B-trees in anger, LSM trees) in the first half, distributed
  consensus and replication in the second. Reads like a guided tour of the source code of every
  database you use.
- **[Readings in Database Systems](http://www.redbook.io/)** ("the Red Book") — Bailis,
  Hellerstein, Stonebraker. Free: the field's judgment layer — which papers mattered and *why*,
  with Stonebraker's opinions attached. Read it to acquire taste, not facts.
- **[Architecture of a Database System](https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf)**
  — Hellerstein, Stonebraker, Hamilton. An 80-page paper that is secretly the best systems-design
  document ever written: process models, admission control, and how the pieces of a DBMS fit.

## Build-one-in-public blogs

- **[Phil Eaton](https://eatonphil.com/)** — databases from scratch, in public: write-ahead logs,
  MVCC, io_uring, Raft — each post a working implementation plus honest notes. Also runs
  [/r/databasedevelopment's reading ecosystem](https://eatonphil.com/database-books.html)-adjacent
  lists that are better curated than any official syllabus.
- **[build-your-own.org](https://build-your-own.org/)** — James Smith's free books: build a Redis,
  a database, a compiler, from empty file to working system in small verified steps. The database
  one is the fastest route from "read about B-trees" to "wrote one."
- **[transactional.blog](https://transactional.blog/)** — Alex Miller (FoundationDB). The deepest
  public writing on transaction internals and distributed correctness testing — the
  ["simulation testing"](https://transactional.blog/simulation/) series explains the technique
  FoundationDB used to become the most trusted codebase in databases.
- **[Jamie Brandon](https://www.scattered-thoughts.net/)** — query languages and incremental
  computation; ["Internal consistency in streaming systems"](https://www.scattered-thoughts.net/writing/internal-consistency-in-streaming-systems/)
  will change how you look at every streaming pipeline demo.

## How to use this layer

Pick the pairing that matches your gap: queries slow → Winand this week; want internals → 15-445
projects with Petrov as the reference; designing systems → the Red Book and the Hellerstein paper.
And one habit from all of them: `EXPLAIN ANALYZE` before believing anything — the planner is the
territory, everything else is map.
