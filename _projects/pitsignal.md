---
title: PitSignal
track: hft
order: 51
group: Prediction and research
kind: Signal pipeline
repo: harsha-moparthy/pitsignal
description: >-
  A point-in-time LLM signal pipeline over 255 real SEC 8-K earnings filings where PIT discipline
  is enforced by the type system and every evaluation is bracketed by controls: a planted arm that
  must fire (t = 15.8) and a shuffled arm that must stay silent (t = 0.55). The naive filing-date
  join places 94 of 255 fills before the document existed; the honest event study, clustered by
  issuer, says the naive text signal is not significant.
stack: [Python, Ollama, SEC EDGAR, Yahoo Finance, pytest, uv]
highlights:
  - value: "t = 15.8"
    label: planted control fires — the study can see signal
  - value: "t = 0.55"
    label: shuffled control silent — no manufactured significance
  - value: "94/255"
    label: naive-join fills placed before publication
  - value: "34/255"
    label: wrong EDGAR timestamps caught, 4-5 hours early
---

## Why this project exists

Trading firms run LLMs over filings and earnings calls to extract signals humans cannot read fast
enough. The graveyard failure is temporal leakage — an ordinary indexing mistake that happens to be
extremely profitable on paper: a filing accepted at 20:30 ET joined to that day's close return
collects the overnight earnings gap for free. "Be careful with timestamps" does not prevent this,
because the leaky join is the natural thing to write. Here the care is structural, and the honesty
is enforced by controls that fail loudly.

## What it does

- Point-in-time as a type: prices are reachable only through an `AsOfView` that raises `LeakError`
  on any read of a not-yet-public bar, enforced per field; forward reads require a `ForwardWindow`
  with a stated purpose, recorded in an audit ledger a test checks no scorer ever appears in
- Two controls bracket every result — planted (score copied from the realised return sign) and
  shuffled (real score distribution, pairing destroyed) — computed first; the pipeline refuses to
  report if either fails its gate
- A market-model event study: abnormal returns are residuals of a regression fit strictly before
  each event, with significance reported cross-sectionally and clustered by issuer
- Corpus of 255 real item-2.02 8-K earnings releases across 24 large-cap issuers, each publication
  instant read from its authoritative EDGAR header rather than the JSON index
- A deterministic finance-lexicon scorer runs the whole pipeline offline; a live Ollama LLM arm
  plus entity masking measures the model-recall leakage channel
- A three-entry-rule leakage study quantifies exactly what the naive filing-date-close join does,
  stratified by publication regime

## Measured results

| Evidence | Result |
|---|---|
| Planted (positive) control | **t = 15.76** against a required threshold of 4 |
| Shuffled (negative) control | **t = 0.55** against a required ceiling of 2 |
| Naive lexicon signal, clustered by issuer (1/3/5 sessions) | t = -1.83 / -1.93 / -1.81 — **not significant**; the honest answer is no |
| Naive filing-date-close entry rule | **94 of 255 fills placed before the document existed** |
| Honest entry rule (first open after acceptance) | 0 of 253 pre-publication fills |
| Same naive join on a corpus with a real planted signal | inflates the measured spread **2.85x** |
| EDGAR timestamp audit | **34 of 255** filings carry a wrong UTC suffix (actually Eastern time, 4-5 h early); all 255 re-verified to the second, 0 mismatches |
| Tests | **142**, fully offline, no network, no secrets |

The timestamp bug is the story: read literally, the wrong stamps place publication hours earlier
than it happened — the same direction and magnitude as the leak the project exists to measure, and
some are undetectable from the value alone.

## Tech stack

- Python with a typed PIT barrier (`AsOfView`, `ForwardWindow`, audit ledger)
- SEC EDGAR ingestion with authoritative per-filing header timestamps
- Yahoo daily bars with provenance; market-model event study with issuer-clustered t-statistics
- Ollama (local qwen3 8B) for the live LLM arm; a deterministic lexicon arm for CI and baselines
- Latency reported as two numbers so neither misleads: sub-millisecond p50 scoring vs the market's
  own p50 3.2-hour publication-to-open wait
