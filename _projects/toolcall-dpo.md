---
title: Toolcall DPO
track: ml
order: 15
group: Data and post-training
kind: Post-training
repo: harsha-moparthy/toolcall-dpo
description: >-
  Post-training a small model for tool calling: DPO and GRPO written from scratch with
  verifier-graded rewards, decomposed evaluation and pair-quality ablations. DPO lifts held-out
  accuracy 16.1% → 21.5% with the second trained skill held at 100%, and the decomposed evaluation
  isolates GRPO reward hacking that a validity-only metric would have scored as a win.
stack: [Python, PyTorch, DPO, GRPO, TRL export]
highlights:
  - value: "16.1% → 21.5%"
    label: held-out composite after DPO
  - value: "reward ↑, exactness ↓"
    label: GRPO reward hacking, isolated by decomposed eval
  - value: "48 > 92"
    label: near-miss pairs beat twice as many mixed
  - value: "17 / 17"
    label: tests passing
---

## Why this project exists

Small open models are cheap to run and mediocre at the exact skill agents need: emitting correct,
well-formed tool calls. Post-training on preference data for that one skill is the current practical
answer — and the *machinery* matters more than the scale: preference pairs graded by programmatic
verifiers, the DPO loss and its reference anchor, group-relative rewards, and an evaluation that
separates what *kind* of wrong a call is.

So everything here is implemented from scratch — roughly 50 lines each for DPO and GRPO — and the whole
experiment runs deterministically in about 40 seconds per seed on a laptop CPU. A ~600k-parameter
transformer is genuinely SFT-trained, genuinely sampled, genuinely improved by DPO, and the reward
hacking GRPO produces is measured on the same harness. Nothing is mocked.

## The setup

A closed tool-calling DSL: six functions with typed, enumerable parameters, and requests generated from
five phrasing templates per function.

```
prompt:   ASK what is the weather in tokyo in celsius SEP
response: CALL get_weather ( city = tokyo , units = celsius ) END
```

**Split isolation is what makes the numbers mean anything.** Templates are partitioned so a gain has to
transfer across phrasings rather than being memorised:

| split | templates | role |
|---|---|---|
| SFT (330) + val (50) | 0–2 | training; val is for hyperparameter selection only |
| pair / GRPO prompts (158) | **4 only** | preference data |
| held-out (110) | **3 only** | never seen by SFT, pairs or GRPO; disjoint value combos |
| describe (12) | — | a second trained skill: the regression check |

**Verifiers, not a judge model.** A strict parser grades every sample into an ordered scale —
`INVALID` < `WRONG_FUNCTION` < `WRONG_ARGS` < `CORRECT` — which is what makes the preference pairs
objective and the reward computable.

**The base model is deliberately under-trained.** SFT runs for exactly 14 epochs, an operating point
chosen by scanning: enough correct samples to build pairs, far from ceiling, describe skill fully
learned. The scan also established that held-out validity *falls* after ~18 epochs as the model
memorises templates, so the low operating point earns its place twice.

## Measured results

Three fully independent runs — data splits, model init, sampling and training order all reseeded.

| arm | composite mean | range | validity mean | describe (regression) |
|---|---|---|---|---|
| base (SFT only) | 16.1% | [10.9%, 20.0%] | 47.6% | 100.0% |
| **DPO (iterative, near-miss pairs)** | **21.5%** | [16.4%, 28.2%] | 51.8% | 100.0% |
| GRPO (verifier rewards) | 13.3% | [10.9%, 15.5%] | 67.0% | 100.0% |

DPO improved composite on seeds 7 and 8 (+5.5pp, +10.9pp) and was exactly neutral on seed 9 — it never
regressed. The describe skill held at **100% in every arm on every seed**: the KL and reference
anchoring did their job, which is the "minimal capability regression" criterion in miniature.

### The GRPO finding: reward up, exactness down

GRPO's mean verifier reward rose within every run (0.37 → 0.49 on seed 9) while held-out composite
landed below base. The mechanism is visible in the decomposition: the graded reward pays 0.25 for mere
well-formedness, and that is the easiest credit to farm. The policy shifted mass toward "any valid
call" — validity jumped from 47.6% to 67.0% (82.7% on seed 7) while function selection and argument
binding degraded.

**The reward was optimised exactly as written; what was written was not exactly the goal.** That is a
clean small-scale demonstration of reward-shaping risk, and it is reported as a primary finding. It is
also the reason the evaluation decomposes into validity / selection / arguments instead of reporting one
accuracy number — a single metric would have scored this as a validity *win*.

### Pair-quality ablation

Same DPO recipe, different pairs:

| tier | pairs (mean) | composite mean |
|---|---|---|
| **near_miss** (rejected = plausible-but-wrong) | 48 | **21.5%** |
| all failure classes | 92 | 19.1% |
| gross (rejected = invalid junk) | 48 | 15.2% |
| random pairing (control) | 158 | 13.9% |

The hard-negatives hypothesis, measured: near-miss pairs — right shape, wrong binding — beat **twice as
many** mixed pairs. Gross pairs teach little the model doesn't already know. And random pairing, the
"are the verifiers doing anything at all" control, comes last despite being by far the largest set. That
control is what separates a working preference pipeline from one that would look fine on a loss curve.

### Hyperparameter sensitivity, located by measurement

At `lr=1e-4` both methods over-optimise against the frozen reference and give up accuracy on the
pre-isolation splits — the classic post-training failure mode, located by measurement rather than
assumed away.

All final hyperparameters (`beta=0.3, lr=3e-5, 2 epochs` for DPO; `kl=0.2, lr=3e-5, 2 iterations` for
GRPO) were selected on the **val split only**. The held-out set was evaluated once per arm, after
everything was locked.

## Scope and next steps

The GRPO implementation samples fresh completions each iteration and takes one gradient step per group,
so the PPO clipped ratio is identically 1 and is omitted — the on-policy special case, documented in the
module docstring. Zero-variance groups carry no gradient signal and are skipped, which makes GRPO's
known data inefficiency explicit in the code path. The describe-skill check is the capability-regression
analogue available at this scale.

## Scaling the recipe

The implementations are miniature; the recipe is model-agnostic. `toolpost export-trl` writes the pairs
as `{"prompt", "chosen", "rejected"}` JSONL for TRL's `DPOTrainer`, so the same verifier-graded pipeline
drives a real 3–8B model with LoRA on a 24 GB GPU. The from-scratch code is the evidence that step's
knobs — beta, reference anchoring, pair quality — are understood rather than cargo-culted.
