---
title: "Distributed systems: DDIA, 6.824, and Jepsen"
date: 2026-07-29 10:00:00 +0530
categories: [Resources, Systems]
tags: [distributed-systems, ddia, raft, consensus]
description: >-
  The distributed-systems path: Kleppmann's DDIA as the map, MIT 6.824 labs as
  the practice, Jepsen as the reality check, and the five papers worth reading
  in full.
---

Distributed systems is where intuition goes to die: the network partitions, the clock lies, and
the "impossible" interleaving ships to production. The materials below are the ones that build
correct instincts.

## The map

- **[Designing Data-Intensive Applications](https://dataintensive.net/)** — Martin Kleppmann.
  The best systems book of the last decade: replication, partitioning, transactions, consistency
  models, and stream processing, each with its failure modes attached. Chapters 5–9 are the core;
  read them twice. His
  [distributed systems lecture series](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB)
  (Cambridge) is the free video companion.

## The practice

- **[MIT 6.824 / 6.5840](https://pdos.csail.mit.edu/6.824/)** — all lectures and labs public.
  Implementing Raft (lab 2) is the rite of passage: nothing else teaches what "the leader might
  not know it's been deposed" *feels* like. Budget real weeks; the labs' test suites are
  adversarial in exactly the way networks are.
- **[Raft](https://raft.github.io/raft.pdf)** — read the paper alongside the lab, and use
  [the visualization](https://thesecretlivesofdata.com/raft/) when the paper's figure 2 stops
  making sense at 1am.

## The reality check

- **[Jepsen](https://jepsen.io/analyses)** — Kyle Kingsbury's distributed-systems testing
  analyses: real databases, real partitions, real violated guarantees, written up with unusual
  rigor and wit. Reading five Jepsen reports recalibrates how much you trust vendor consistency
  claims — permanently. The companion
  [consistency models map](https://jepsen.io/consistency) is the clearest reference on what
  linearizable/sequential/snapshot actually promise.
- **[Aphyr's "Strong consistency models"](https://aphyr.com/posts/313-strong-consistency-models)**
  — the essay version, worth reading before the map.

## Five papers worth reading in full

- [Time, Clocks, and the Ordering of Events](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) — Lamport, 1978. Still the foundation.
- [The Google File System](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) and
  [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) — how the modern data stack started.
- [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) — the
  availability-first design whose ideas (consistent hashing, hinted handoff, vector clocks) are
  everywhere.
- [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf) —
  the opposite bet: global strong consistency via TrueTime.

## Why it's on this list

The durable-agents project on this site is a distributed-systems problem wearing an AI costume:
checkpointing, exactly-once side effects under `kill -9`, idempotency keys. The concepts
transferred one-for-one from this reading — which is the argument for learning the foundations
even if you never build a database.
