---
title: BomSquad
track: sde
order: 44
group: Supply-chain security
kind: Supply-chain security
repo: harsha-moparthy/bomsquad
description: >-
  A supply-chain security toolkit for npm and PyPI: CycloneDX SBOMs from lockfiles, sigstore/SLSA
  provenance verified down to the lockfile digest, and a typosquat plus hallucinated-import scanner.
  Name rules detect 28/54 documented historical attacks, and two-stage exoneration leaves 2 flags
  across 6,517 packages from real clean trees — a 0.031% false-positive rate.
stack: [Python, CycloneDX, sigstore, in-toto, pypi-attestations]
highlights:
  - value: "28/54"
    label: documented historical squat attacks detected
  - value: "0.031%"
    label: FP rate — 2 flags in 6,517 real packages
  - value: "98.4%"
    label: PyPI malware census caught with registry state
  - value: "106/479"
    label: real direct deps cryptographically verified
---

## Why this project exists

Attackers stopped attacking your code and started attacking your `package-lock.json`: typosquatted
names one edit from something popular, hijacked maintainer accounts, tampered build pipelines, and —
newest — AI assistants confidently importing packages that do not exist, whose names get registered
by whoever moves first. Regulators and enterprise buyers now ask for SBOMs and provenance proofs, and
the tooling answering them is mostly vibes: scanners with unreported false-positive rates and
"provenance" checks that never bind a signature to the bytes you actually install.

Two design moves keep this honest: every detector ships with its measured miss rate (evaluated
against 54 cited historical attacks and seeded samples of the entire OSV malicious-package census),
and false positives are counted on real dependency trees, by name, with every flag listed in the
results JSON.

## What it does

- `bomsquad sbom` — CycloneDX 1.5 SBOMs from `package-lock.json` (v2/v3, workspace-aware), `uv.lock`,
  and pinned `requirements.txt`, with full dependency graph and artifact hashes; schema-validated in
  the test suite and deterministic so SBOMs diff cleanly in CI
- `bomsquad verify` — real cryptographic verification: npm sigstore bundles (Fulcio chain, SCT, Rekor
  inclusion, DSSE signature) under a CI-issuer policy, then the in-toto subject digest is required to
  equal the tarball hash in your lockfile — binding "built on CI" to "the bytes npm will install";
  PyPI PEP 740 attestations verified against their trusted publisher
- `bomsquad scan` — a two-stage risk engine: offline Damerau-Levenshtein typosquat rules against
  vendored popularity lists (10k npm / 15k PyPI), separator/confusable/affix rules, stdlib-shadow
  detection, and lockfile hygiene; stage 2 spends network only on candidates and downgrades name
  flags on packages with long registry history — which is what keeps the FP rate tolerable
- `bomsquad check-imports` — the hallucinated-import checker: does this AI-suggested package exist,
  and is installing this name what the import means (`pip install cv2` is not `opencv-python`)
- A 404 is a finding, not an error: a lockfile referencing a package gone from the registry is
  exactly what a pulled malicious package looks like — treated as CRITICAL

## Measured results

All numbers produced by the committed eval scripts with fixed seeds and cited corpora.

| Evidence | Result |
|---|---|
| 54 documented historical squat attacks, name rules only | **28/54 (51.9%)** — npm 19/41, PyPI 9/13; every miss listed with its citation |
| OSV malicious census (8,000 sampled names per ecosystem), name rules alone | 0.4% npm / 11.7% PyPI — the honest, unflattering number: most modern registry malware is dependency-confusion spam no name rule should flag |
| Census with registry state (250-name live subsample) | **66.4% npm / 98.4% PyPI**, with the caveat printed that these signals detect known, already-removed malware |
| False positives, 6,517 packages from 8 real projects | stage 1: 38 flags (0.58%); after exoneration: **2 flags (0.031%)** — both under a year old, one edit from a popular name, exactly what a human should inspect |
| Provenance tamper controls | flip one byte of the signed statement — `invalid`; validly signed attestation with the wrong tarball digest — `invalid` |
| Provenance survey over 479 real direct dependencies | **106 verified** (each naming the exact source repo the attestation binds to), 243 unsigned, 128 unverifiable, 2 unsupported, **0 invalid** |
| Test suite | 35 tests, including schema validation and tamper cases |

The reporting vocabulary is deliberate: `invalid` means cryptography failed and nothing else — a
tooling gap reports `unsupported`, and a lockfile with no hashes to bind against reports
`unverifiable`, because a report that calls a tooling gap a forgery is lying to you.

## Tech stack

| Component | Choice |
|---|---|
| SBOM | CycloneDX 1.5 emitter, validated against the official schema, deterministic output |
| Provenance | sigstore bundle verification, in-toto digest binding, PEP 740 via pypi-attestations |
| Risk engine | Damerau-Levenshtein plus rule-based squat detection, two-stage registry exoneration |
| Registry client | Cached; offline mode replays the cache byte-for-byte |
| Evaluation | OSV MAL-* census samples, vendored popularity snapshots, 8 real clean lockfiles |
| CI | GitHub Actions: bomsquad gates its own dependency tree and uploads its own SBOM |
