---
title: ITCH-RTL
track: hft
order: 47
group: Tick-to-trade and matching
kind: Hardware feed parser
repo: harsha-moparthy/itch-rtl
description: >-
  A SystemVerilog ITCH 5.0 feed parser verified bit-identically against a software golden model
  over 5,000,000 messages — 0 mismatching bytes — at a fixed 1-cycle latency for all five message
  types. Yosys estimates 447 LUTs and 832 flip-flops on Xilinx 7-series; a 400-fault malformed-input
  suite checks that every rejection fires by the exact expected reject code.
stack: [SystemVerilog, Verilator, Yosys, C++, Python]
highlights:
  - value: "5M"
    label: messages diffed, 0 mismatching bytes
  - value: "1 cycle"
    label: fixed latency, min equals max for all 5 types
  - value: "447/832"
    label: LUTs and FFs, Yosys 7-series estimate
  - value: "400/400"
    label: injected faults caught by the exact reject code
---

## Why this project exists

The fastest trading firms parse market data in hardware: an FPGA turns packet bytes into decoded
fields in nanoseconds where software takes microseconds. The usual blocker for demonstrating the
skill is five-figure hardware — but what actually matters is demonstrable in cycle-accurate
simulation: thinking in fixed pipeline stages instead of loops and allocations, a framing state
machine that survives a corrupt wire, and above all proving the thing correct. The verification is
the deliverable, not the parser.

## What it does

- SystemVerilog ITCH 5.0 parser: byte-serial framing FSM (length prefix, body, decode), fixed field
  offsets wired as bit slices out of a fixed 44-byte body buffer — no allocation, no pointer walking
- Emits a packed 56-byte canonical record with a per-type field mask, so a zeroed field cannot
  compare equal vacuously
- C++ golden model diffed via `memcmp` over all 56 bytes — one wrong bit fails the run and names
  the byte offset
- The golden model is itself audited against a third, table-driven Python implementation before it
  is trusted; a shared spec misreading would have to happen three times independently
- Malformed-input suite that distinguishes recoverable corruptions (unknown type, bad length) from
  desync faults no parser can recover, since ITCH framing has no sync marker
- Yosys synthesis flow with `-noiopad` for an honest resource number

## Measured results

| Evidence | Result |
|---|---|
| Bit-identical diff vs software reference | **5,000,000 messages, 168.8 MB, 0 mismatching records, 0 mismatching bytes** |
| Cycle latency, per message type (A/F/E/X/P) | fixed **1 cycle**; min == max asserted per type, run fails otherwise |
| Latency with injected input gaps (stall every 2-3 bytes) | unchanged — the measurement is anchored to byte acceptance |
| Resource estimate (Yosys, Xilinx 7-series, `-noiopad`) | **447 LUTs, 832 FFs, 346 estimated LCs**, 1,343 total cells |
| Recoverable fault injection | **400/400 detected**, each by the exact expected reject code — wrong-reason rejection counts as failure |
| Resynchronization after recoverable faults | 1,332 subsequent records bit-identical, **0 fabricated** |
| Desync stream (corrupted length prefixes) | liveness 67,636/67,636 bytes consumed, 0 fabricated of 11 emitted — resync is honestly claimed impossible |
| Assumed-clock throughput at 200 MHz | 200 MB/s, ~5.9M messages/s on the stream's 33.8-byte mean frame — labelled as assumed, since Yosys does no timing analysis |

Bugs the harness caught: a registered verdict read one cycle too early (message 0 of every stream
vanished — caught by the diff on its first run), a latency of zero measured through a two-register
pipeline (the determinism assertion flagged it), and a green test that examined 0.5% of its input
before declaring success.

## Tech stack

- SystemVerilog RTL: framing FSM plus fixed-offset decode, lint-clean under Verilator `-Wall` with
  no waivers
- Verilator 5 for cycle-accurate simulation, with C++ testbenches for equivalence and robustness
- Yosys for the synthesis estimate (Xilinx 7-series mapping)
- Python tooling: a seeded spec-accurate ITCH generator, a catalogued fault injector, and the
  third implementation used to audit the golden model
- The 168 MB test stream is reproducible from the committed seed, so no capture is tracked
