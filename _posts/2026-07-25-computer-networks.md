---
title: "Computer networks: from Kurose to packets on the wire"
date: 2026-07-25 10:00:00 +0530
categories: [Resources, Systems]
tags: [networking, tcp, http, protocols]
description: >-
  The networking path: Kurose & Ross for the map, Beej for sockets, TCP/IP
  Illustrated for the wire, High Performance Browser Networking for the web,
  and the blogs where protocol engineering happens in public.
---

Networking is the layer engineers most often treat as magic — until a latency budget, a hung
connection, or a TLS handshake failure forces the issue. The path below goes from map to wire.

## The map

- **[Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/)** — Kurose &
  Ross. The standard for a reason: it starts at HTTP where your intuition lives and descends to
  the link layer. The authors keep
  [free lecture videos and interactive material](https://gaia.cs.umass.edu/kurose_ross/online_lectures.htm)
  on the same page. Read the application, transport, and network chapters carefully; skim the rest
  on first pass.
- **[Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)** — free, funny, and still
  the fastest route to actually writing socket code. An afternoon with Beej teaches more than a
  month of diagrams, because `bind`, `listen`, and `EWOULDBLOCK` stop being abstract.

## The wire

- **[TCP/IP Illustrated, Volume 1](https://www.informit.com/store/tcp-ip-illustrated-volume-1-the-protocols-9780321336316)**
  (2nd ed., Fall & Stevens) — the classic that teaches by *showing packet traces* rather than
  telling. Read it with [Wireshark](https://www.wireshark.org/) open and reproduce the captures;
  that habit — look at the actual packets — is the entire skill.
- **[High Performance Browser Networking](https://hpbn.co/)** — Ilya Grigorik, free online. The
  best single text on what latency actually costs and where it hides: TCP slow start, TLS
  handshakes, HTTP/2 multiplexing, WebSockets, WebRTC. Chapter 1's "latency is the bottleneck"
  argument should be mandatory for anyone building APIs.

## Staying current: protocols keep moving

- **[Cloudflare's blog](https://blog.cloudflare.com/tag/deep-dive/)** — the best running source of
  production protocol engineering: QUIC and HTTP/3 rollouts, BBR congestion control, DDoS
  anatomy, TLS internals. Their explainers (e.g.
  [HTTP/3 explained](https://blog.cloudflare.com/http3-the-past-present-and-future/)) are how I'd
  learn any post-2018 protocol.
- **[RFC 9293 (TCP)](https://www.rfc-editor.org/rfc/rfc9293)** and
  **[RFC 9000 (QUIC)](https://www.rfc-editor.org/rfc/rfc9000)** — reading one RFC end to end is a
  rite of passage worth doing once: you learn that the primary sources are readable and that blog
  summaries routinely flatten the interesting corners.

## Making it stick

Three exercises that convert reading into skill: capture and annotate one full TCP handshake +
TLS negotiation + HTTP exchange in Wireshark; write an HTTP/1.1 client with raw sockets from Beej
(no libraries) until keep-alive and chunked encoding work; and trace one real production timeout
all the way down (app → connection pool → kernel → wire) writing down every layer you cross. The
third one is the job.
