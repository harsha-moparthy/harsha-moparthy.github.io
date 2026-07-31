---
title: Permission-Aware RAG
track: fde
order: 28
group: Governed data access
kind: Governed retrieval
repo: harsha-moparthy/permission-aware-rag
description: >-
  Enterprise RAG where the access decision happens inside retrieval and is re-verified against the
  source of truth before any text reaches a generator. Zero leaks across 20 adversarial probes and
  three leak surfaces while all 17 entitled questions are answered — and the suite mutates
  permissions mid-flight, because two of the four unsafe control designs are byte-identical to the
  correct one until something changes.
stack: [Python, SQLite, BM25, Ollama, GitHub Actions]
highlights:
  - value: "0"
    label: leaks across 20 probes and 3 surfaces
  - value: "17/17"
    label: positive controls answered, citing the gold chunk
  - value: "0 vs 6"
    label: stale-version citations, with vs without the freshness guard
  - value: "13.1 ms"
    label: p95 permission propagation at sweep cadence 1
---

## Why this project exists

"No data leaked" is the least falsifiable claim in enterprise AI, usually supported by an
architecture diagram. Three things here make it support itself. The corpus is built to punish
plausible implementations: an intern seconded to finance, a document everyone may read whose
pricing appendix is exec-only, groups that contain each other, and eleven canary markers so a leak
is a string match rather than a judgement call. Zero leaks is checked against cheating — a system
that refuses everything leaks nothing, so 17 positive controls require the right answer citing the
right chunk. And permissions are mutated mid-flight, because the failures that matter live in the
interval between an administrator clicking revoke and the indexer catching up.

## What it does

- Enforces chunk-level ACLs before scoring, re-verifies survivors against the authoritative store,
  and drops anything the index holds at a superseded version.
- Runs four alternative designs as controls, each differing in exactly one respect — post-filtering,
  document-level ACLs, trusting the index snapshot, cached group membership — so every leak is
  attributable. The two racy arms return byte-identical context to the correct arm at rest and are
  only caught by revoking and asking immediately.
- Makes revocation immediate by construction (the final check reads the authoritative store) while
  grants wait for the next index sweep — an availability gap, not a leak, and the correct direction
  to be wrong in.
- Withholds rather than quotes a chunk the store has superseded, and reports the price: 4 answers
  withheld pending reindex against 6 confidently out-of-date answers in the unguarded arms.
- Refuses without becoming an existence oracle: "nothing you can read is relevant" and "the part
  that answers this is withheld" are byte-identical sentences to the user, asserted by a test, with
  reason codes kept separate in telemetry.
- Measures the retrieval cost of post-filtering separately: ~15% of the top-k budget is spent on
  chunks that will be thrown away.

## Measured results

| Evidence | Result |
|---|---|
| Adversarial leaks, strict arm | 0 across all three surfaces (context, citation, canary) |
| Forbidden probes refused | 20/20 |
| Positive controls (answered and citing the gold chunk) | 17/17 |
| Same question, different askers | 9 questions answered for one user and refused for another |
| Unsafe arms caught | 4/4, each by the failure it exists to demonstrate |
| Revocation window | closed — the query lands with the revoke still unswept, refuses anyway |
| Answers citing a superseded version | 0 with the freshness guard, 6 without |
| Propagation latency | p95 13.1 ms at sweep cadence 1, 22.9 ms at cadence 8 |
| Per-tier answer rate | 1.00 in all 7 tiers, on 6–16 visible chunks each |
| Test suite / mutation check | 53 passed; 8/8 mutants caught by a named test |

The central finding arrived as a broken test: a static suite passes two of the four wrong
implementations without comment. Without race tests, half the wrong designs get a clean bill of
health.

## Tech stack

| Component | Choice |
|---|---|
| Stores | authoritative store and index snapshot, deliberately separate, over SQLite |
| ACL resolution | transitive group resolution, cycle-safe; deny beats allow |
| Retrieval | BM25 with five enforcement arms; the decision happens inside retrieval |
| Indexer | watermark sweep with propagation-latency instrumentation |
| Answerer | extractive with a coverage floor and a single refusal vocabulary |
| Optional model arm | Ollama answering arm, harvested outside CI |
