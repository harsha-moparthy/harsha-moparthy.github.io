# Large Language Models: Exhaustive Topic → Subtopic Index

> **Scope:** Language-model theory, data, architecture, pretraining, midtraining, post-training, reasoning, alignment, inference and serving, retrieval, agents, multimodality, evaluation, security, research, and hands-on engineering.
> **Snapshot:** 9 November 2026. This is a broad working taxonomy, not a claim that every new paper or technique can be enumerated permanently.

**Coverage:** **60 major topics · 204 subtopic groups · 1,240 atomic learning concepts.**

**How to use:** Open the topic or subtopic link below to jump to the detailed checklist. Check off concepts as you understand them. The three resource columns now contain discovered Medium article candidates ranked by topical relevance and recency. Engagement/clap totals remain unverified; see the ranking notice above the table.

## A. Major-topic index

| # | Topic | Subtopics | Concepts |
|---:|---|---:|---:|
| 01 | [LLM landscape, concepts, and lifecycle](#01-llm-landscape-concepts-and-lifecycle) | 3 | 23 |
| 02 | [Mathematical foundations for LLMs](#02-mathematical-foundations-for-llms) | 4 | 26 |
| 03 | [Machine-learning and deep-learning prerequisites](#03-machine-learning-and-deep-learning-prerequisites) | 3 | 18 |
| 04 | [NLP and language-model evolution](#04-nlp-and-language-model-evolution) | 3 | 17 |
| 05 | [Pretraining corpora, sources, and dataset design](#05-pretraining-corpora-sources-and-dataset-design) | 3 | 19 |
| 06 | [Data processing, quality filtering, and synthesis](#06-data-processing-quality-filtering-and-synthesis) | 4 | 24 |
| 07 | [Tokenization and text representation](#07-tokenization-and-text-representation) | 3 | 18 |
| 08 | [Embeddings and representation geometry](#08-embeddings-and-representation-geometry) | 3 | 18 |
| 09 | [Transformer architecture fundamentals](#09-transformer-architecture-fundamentals) | 3 | 19 |
| 10 | [Attention mechanisms and variants](#10-attention-mechanisms-and-variants) | 3 | 18 |
| 11 | [Positional information and context length](#11-positional-information-and-context-length) | 3 | 20 |
| 12 | [Transformer blocks, normalization, and activation design](#12-transformer-blocks-normalization-and-activation-design) | 3 | 17 |
| 13 | [Architecture families beyond standard decoder-only LLMs](#13-architecture-families-beyond-standard-decoder-only-llms) | 3 | 18 |
| 14 | [Mixture-of-experts (MoE) and sparsity](#14-mixture-of-experts-moe-and-sparsity) | 3 | 18 |
| 15 | [Scaling laws, compute, and model design](#15-scaling-laws-compute-and-model-design) | 3 | 18 |
| 16 | [Pretraining objectives and objectives beyond next-token prediction](#16-pretraining-objectives-and-objectives-beyond-next-token-prediction) | 3 | 18 |
| 17 | [Pretraining optimization and experimental practice](#17-pretraining-optimization-and-experimental-practice) | 3 | 18 |
| 18 | [Training hardware and distributed systems](#18-training-hardware-and-distributed-systems) | 4 | 25 |
| 19 | [Fine-tuning, adaptation, and transfer learning](#19-fine-tuning-adaptation-and-transfer-learning) | 4 | 24 |
| 20 | [Instruction tuning and supervised post-training (SFT)](#20-instruction-tuning-and-supervised-post-training-sft) | 3 | 18 |
| 21 | [Preference learning, reward modeling, and RLHF](#21-preference-learning-reward-modeling-and-rlhf) | 5 | 30 |
| 22 | [Reinforcement learning for reasoning and verifiable tasks](#22-reinforcement-learning-for-reasoning-and-verifiable-tasks) | 5 | 30 |
| 23 | [Reasoning, planning, and test-time computation](#23-reasoning-planning-and-test-time-computation) | 5 | 30 |
| 24 | [Autoregressive generation and decoding](#24-autoregressive-generation-and-decoding) | 4 | 24 |
| 25 | [Prompt engineering and context engineering](#25-prompt-engineering-and-context-engineering) | 4 | 24 |
| 26 | [Long-context systems, compression, and persistent context](#26-long-context-systems-compression-and-persistent-context) | 3 | 18 |
| 27 | [KV cache and inference memory management](#27-kv-cache-and-inference-memory-management) | 4 | 24 |
| 28 | [Efficient attention kernels and GPU optimization](#28-efficient-attention-kernels-and-gpu-optimization) | 3 | 18 |
| 29 | [Quantization, pruning, sparsity, and distillation](#29-quantization-pruning-sparsity-and-distillation) | 4 | 25 |
| 30 | [LLM inference execution and throughput optimization](#30-llm-inference-execution-and-throughput-optimization) | 4 | 24 |
| 31 | [Model serving engines and deployment stacks](#31-model-serving-engines-and-deployment-stacks) | 3 | 18 |
| 32 | [LLM APIs, protocols, and application integration](#32-llm-apis-protocols-and-application-integration) | 3 | 18 |
| 33 | [Retrieval, search, ranking, and embedding systems](#33-retrieval-search-ranking-and-embedding-systems) | 3 | 18 |
| 34 | [Retrieval-augmented generation (RAG)](#34-retrieval-augmented-generation-rag) | 4 | 24 |
| 35 | [Tool use, function calling, and external computation](#35-tool-use-function-calling-and-external-computation) | 3 | 18 |
| 36 | [LLM agents and workflow architectures](#36-llm-agents-and-workflow-architectures) | 3 | 18 |
| 37 | [Multi-agent systems, coordination, and protocols](#37-multi-agent-systems-coordination-and-protocols) | 3 | 18 |
| 38 | [Agent memory, state, and long-horizon autonomy](#38-agent-memory-state-and-long-horizon-autonomy) | 3 | 18 |
| 39 | [Multimodal LLM fundamentals](#39-multimodal-llm-fundamentals) | 3 | 18 |
| 40 | [Vision-language models (VLMs) and documents](#40-vision-language-models-vlms-and-documents) | 3 | 18 |
| 41 | [Audio, speech, music, and spoken language models](#41-audio-speech-music-and-spoken-language-models) | 3 | 18 |
| 42 | [Video, real-time multimodal systems, and embodied agents](#42-video-real-time-multimodal-systems-and-embodied-agents) | 3 | 18 |
| 43 | [Code language models and software-engineering agents](#43-code-language-models-and-software-engineering-agents) | 3 | 18 |
| 44 | [Domain-specific and multilingual LLMs](#44-domain-specific-and-multilingual-llms) | 3 | 18 |
| 45 | [Evaluation methodology and benchmark engineering](#45-evaluation-methodology-and-benchmark-engineering) | 5 | 31 |
| 46 | [Factuality, uncertainty, calibration, and robustness](#46-factuality-uncertainty-calibration-and-robustness) | 3 | 18 |
| 47 | [Interpretability, mechanistic analysis, and model editing](#47-interpretability-mechanistic-analysis-and-model-editing) | 3 | 18 |
| 48 | [Alignment, model behavior, and responsible AI](#48-alignment-model-behavior-and-responsible-ai) | 3 | 18 |
| 49 | [LLM security, prompt injection, and adversarial ML](#49-llm-security-prompt-injection-and-adversarial-ml) | 4 | 27 |
| 50 | [Privacy, intellectual property, governance, and compliance](#50-privacy-intellectual-property-governance-and-compliance) | 3 | 18 |
| 51 | [Synthetic training loops, self-improvement, and knowledge distillation](#51-synthetic-training-loops-self-improvement-and-knowledge-distillation) | 3 | 18 |
| 52 | [LLMOps, observability, testing, and production lifecycle](#52-llmops-observability-testing-and-production-lifecycle) | 3 | 18 |
| 53 | [Cost, latency, architecture, and product optimization](#53-cost-latency-architecture-and-product-optimization) | 4 | 24 |
| 54 | [Research frontiers and unresolved questions](#54-research-frontiers-and-unresolved-questions) | 4 | 24 |
| 55 | [Hands-on implementations and capstone projects](#55-hands-on-implementations-and-capstone-projects) | 5 | 31 |
| 56 | [Developer tools, libraries, ecosystems, and workflows](#56-developer-tools-libraries-ecosystems-and-workflows) | 4 | 24 |
| 57 | [In-context learning, meta-learning, and capability theory](#57-in-context-learning-meta-learning-and-capability-theory) | 3 | 18 |
| 58 | [Diffusion and non-autoregressive language models](#58-diffusion-and-non-autoregressive-language-models) | 3 | 18 |
| 59 | [Midtraining, annealing, and specialization recipes](#59-midtraining-annealing-and-specialization-recipes) | 3 | 18 |
| 60 | [Computer-use, browser, and GUI agents](#60-computer-use-browser-and-gui-agents) | 3 | 18 |

> **Medium article ranking — 9 November 2026 (qualified).** These are **curated relevant article candidates**, in recommended reading order, for each of the 204 subtopics. All linked articles were discovered as concrete Medium pages in live web searches. The **year** is sourced from publication metadata when available (some year-only dates are approximate); **clap/like counts could not be reliably extracted from the accessible Medium pages**. Medium uses *claps*, not a conventional like count. Therefore, **the ordinal ranks are based on topical fit, technical depth, and recency — NOT an audited popularity or clap ranking.** No invented engagement figures have been added. Articles may repeat across closely related subtopics because one strong deep dive can cover several concepts. An em dash means fewer than three grounded links were available.

**Ranking intended once clap data are available:** First discard irrelevant or factually weak articles, then compute `score = 0.55 × normalized(log(1 + claps)) + 0.30 × recency(2026 snapshot) + 0.15 × topic-fit`, rerank within each row. Currently every clap value is **unverified / NA** and the score has **not** been executed. Publication date is not a substitute for likes.

## B. Topic → subtopic table

| Topic | Subtopic | Concepts | Medium #1 | Medium #2 | Medium #3 |
|---|---|---:|---|---|---|
| [LLM landscape, concepts, and lifecycle](#01-llm-landscape-concepts-and-lifecycle) | [01.1 — Definitions and model taxonomy](#011-definitions-and-model-taxonomy) | 8 | [#1: Building and Deploying LLMs: A Full Lifecycle (2025)](https://medium.com/%40hkabhi916/building-and-deploying-large-language-models-llms-a-full-lifecycle-with-python-aws-8edde0229869) | [#2: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [LLM landscape, concepts, and lifecycle](#01-llm-landscape-concepts-and-lifecycle) | [01.2 — End-to-end lifecycle](#012-end-to-end-lifecycle) | 8 | [#1: Building and Deploying LLMs: A Full Lifecycle (2025)](https://medium.com/%40hkabhi916/building-and-deploying-large-language-models-llms-a-full-lifecycle-with-python-aws-8edde0229869) | [#2: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [LLM landscape, concepts, and lifecycle](#01-llm-landscape-concepts-and-lifecycle) | [01.3 — Research and industry landscape](#013-research-and-industry-landscape) | 7 | [#1: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#2: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#3: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) |
| [Mathematical foundations for LLMs](#02-mathematical-foundations-for-llms) | [02.1 — Linear algebra and tensors](#021-linear-algebra-and-tensors) | 7 | [#1: Math for AI: A Visual Series (2026)](https://medium.com/%40manjeet981203kumar/math-for-ai-a-visual-series-437bc209ece7) | [#2: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#3: Learn and Code MHA MQA and GQA (2025)](https://medium.com/%40r9644360/learn-and-code-mha-mqa-and-gqa-a-guide-to-efficient-attention-mechanisms-in-transformers-ff621fe76680) |
| [Mathematical foundations for LLMs](#02-mathematical-foundations-for-llms) | [02.2 — Probability and information theory](#022-probability-and-information-theory) | 7 | [#1: Math for AI: A Visual Series (2026)](https://medium.com/%40manjeet981203kumar/math-for-ai-a-visual-series-437bc209ece7) | [#2: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) | [#3: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) |
| [Mathematical foundations for LLMs](#02-mathematical-foundations-for-llms) | [02.3 — Calculus and numerical methods](#023-calculus-and-numerical-methods) | 6 | [#1: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#2: Backpropagation (2026)](https://medium.com/%40EleventhHourEnthusiast/backpropagation-15a69ce6b365) | [#3: Math for AI: A Visual Series (2026)](https://medium.com/%40manjeet981203kumar/math-for-ai-a-visual-series-437bc209ece7) |
| [Mathematical foundations for LLMs](#02-mathematical-foundations-for-llms) | [02.4 — Optimization and scaling mathematics](#024-optimization-and-scaling-mathematics) | 6 | [#1: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) | [#2: Why Transformers Scale: The Math of Scaling Laws (2026)](https://medium.com/%40ppp.mishra124/why-transformers-scale-the-math-of-scaling-laws-02c045509186) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [Machine-learning and deep-learning prerequisites](#03-machine-learning-and-deep-learning-prerequisites) | [03.1 — Core learning concepts](#031-core-learning-concepts) | 6 | [#1: Math for AI: A Visual Series (2026)](https://medium.com/%40manjeet981203kumar/math-for-ai-a-visual-series-437bc209ece7) | [#2: Backpropagation (2026)](https://medium.com/%40EleventhHourEnthusiast/backpropagation-15a69ce6b365) | [#3: LSTM Explained (2026)](https://medium.com/data-science-collective/lstm-explained-c78dd92ecf85) |
| [Machine-learning and deep-learning prerequisites](#03-machine-learning-and-deep-learning-prerequisites) | [03.2 — Neural-network foundations](#032-neural-network-foundations) | 6 | [#1: Backpropagation (2026)](https://medium.com/%40EleventhHourEnthusiast/backpropagation-15a69ce6b365) | [#2: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#3: Residual Connections and Normalization in Transformers (2026)](https://medium.com/%40wasowski.jarek/a-decade-of-misplaced-sacred-cows-in-neural-networks-residuals-norms-1a4f85749a0d) |
| [Machine-learning and deep-learning prerequisites](#03-machine-learning-and-deep-learning-prerequisites) | [03.3 — Learning objectives and transfer](#033-learning-objectives-and-transfer) | 6 | [#1: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#2: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [NLP and language-model evolution](#04-nlp-and-language-model-evolution) | [04.1 — Language and classical NLP](#041-language-and-classical-nlp) | 6 | [#1: Attention Is All You Need: From RNNs to Transformers (2025)](https://medium.com/%40ftech/attention-is-all-you-need-the-evolution-from-rnns-to-transformers-ba81e12899d7) | [#2: LSTM Explained (2026)](https://medium.com/data-science-collective/lstm-explained-c78dd92ecf85) | [#3: BPE vs WordPiece vs SentencePiece (2025)](https://medium.com/%40dhiyaadli/bpe-vs-wordpiece-vs-sentencepiece-a-beginner-friendly-guide-to-subword-tokenization-8047b39d82e0) |
| [NLP and language-model evolution](#04-nlp-and-language-model-evolution) | [04.2 — Sequence modeling before transformers](#042-sequence-modeling-before-transformers) | 6 | [#1: LSTM Explained (2026)](https://medium.com/data-science-collective/lstm-explained-c78dd92ecf85) | [#2: Attention Is All You Need: From RNNs to Transformers (2025)](https://medium.com/%40ftech/attention-is-all-you-need-the-evolution-from-rnns-to-transformers-ba81e12899d7) | [#3: Beyond Attention: Mamba (2025)](https://medium.com/correll-lab/beyond-attention-mamba-as-a-replacement-for-transformers-5483b6e23a6e) |
| [NLP and language-model evolution](#04-nlp-and-language-model-evolution) | [04.3 — Foundation-model history](#043-foundation-model-history) | 5 | [#1: Attention Is All You Need: From RNNs to Transformers (2025)](https://medium.com/%40ftech/attention-is-all-you-need-the-evolution-from-rnns-to-transformers-ba81e12899d7) | [#2: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Pretraining corpora, sources, and dataset design](#05-pretraining-corpora-sources-and-dataset-design) | [05.1 — Data sources and composition](#051-data-sources-and-composition) | 7 | [#1: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#2: Papers Explained: Falcon (2023)](https://medium.com/dair-ai/papers-explained-59-falcon-26831087247f) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Pretraining corpora, sources, and dataset design](#05-pretraining-corpora-sources-and-dataset-design) | [05.2 — Dataset provenance and governance](#052-dataset-provenance-and-governance) | 6 | [#1: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#2: Papers Explained: Falcon (2023)](https://medium.com/dair-ai/papers-explained-59-falcon-26831087247f) | [#3: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) |
| [Pretraining corpora, sources, and dataset design](#05-pretraining-corpora-sources-and-dataset-design) | [05.3 — Mixture construction](#053-mixture-construction) | 6 | [#1: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#2: Papers Explained: Falcon (2023)](https://medium.com/dair-ai/papers-explained-59-falcon-26831087247f) | [#3: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) |
| [Data processing, quality filtering, and synthesis](#06-data-processing-quality-filtering-and-synthesis) | [06.1 — Extraction and normalization](#061-extraction-and-normalization) | 6 | [#1: Papers Explained: Falcon (2023)](https://medium.com/dair-ai/papers-explained-59-falcon-26831087247f) | [#2: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Data processing, quality filtering, and synthesis](#06-data-processing-quality-filtering-and-synthesis) | [06.2 — Deduplication and contamination](#062-deduplication-and-contamination) | 6 | [#1: Papers Explained: Falcon (2023)](https://medium.com/dair-ai/papers-explained-59-falcon-26831087247f) | [#2: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#3: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) |
| [Data processing, quality filtering, and synthesis](#06-data-processing-quality-filtering-and-synthesis) | [06.3 — Filtering and quality estimation](#063-filtering-and-quality-estimation) | 6 | [#1: Papers Explained: Falcon (2023)](https://medium.com/dair-ai/papers-explained-59-falcon-26831087247f) | [#2: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Data processing, quality filtering, and synthesis](#06-data-processing-quality-filtering-and-synthesis) | [06.4 — Synthetic data and augmentation](#064-synthetic-data-and-augmentation) | 6 | [#1: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#2: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#3: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) |
| [Tokenization and text representation](#07-tokenization-and-text-representation) | [07.1 — Tokenizer algorithms](#071-tokenizer-algorithms) | 6 | [#1: Tokenization Part 2: Algorithms (2026)](https://medium.com/from-tokens-to-agents/tokenization-part-2-the-algorithms-behind-every-token-03745b385438) | [#2: Byte Pair Encoding from Scratch (2026)](https://medium.com/%40dakshrathi/byte-pair-encoding-bpe-from-data-compression-to-gpt-2-tokenization-44e35be2fd58) | [#3: BPE vs WordPiece vs SentencePiece (2025)](https://medium.com/%40dhiyaadli/bpe-vs-wordpiece-vs-sentencepiece-a-beginner-friendly-guide-to-subword-tokenization-8047b39d82e0) |
| [Tokenization and text representation](#07-tokenization-and-text-representation) | [07.2 — Vocabulary and token semantics](#072-vocabulary-and-token-semantics) | 6 | [#1: BPE vs WordPiece vs SentencePiece (2025)](https://medium.com/%40dhiyaadli/bpe-vs-wordpiece-vs-sentencepiece-a-beginner-friendly-guide-to-subword-tokenization-8047b39d82e0) | [#2: Tokenization Part 2: Algorithms (2026)](https://medium.com/from-tokens-to-agents/tokenization-part-2-the-algorithms-behind-every-token-03745b385438) | [#3: SentencePiece Tokenizer Demystified (2020)](https://medium.com/data-science/sentencepiece-tokenizer-demystified-d0a3aac19b15) |
| [Tokenization and text representation](#07-tokenization-and-text-representation) | [07.3 — Tokenization engineering](#073-tokenization-engineering) | 6 | [#1: Byte Pair Encoding from Scratch (2026)](https://medium.com/%40dakshrathi/byte-pair-encoding-bpe-from-data-compression-to-gpt-2-tokenization-44e35be2fd58) | [#2: Tokenization Part 2: Algorithms (2026)](https://medium.com/from-tokens-to-agents/tokenization-part-2-the-algorithms-behind-every-token-03745b385438) | [#3: SentencePiece Tokenizer Demystified (2020)](https://medium.com/data-science/sentencepiece-tokenizer-demystified-d0a3aac19b15) |
| [Embeddings and representation geometry](#08-embeddings-and-representation-geometry) | [08.1 — Input and output representations](#081-input-and-output-representations) | 6 | [#1: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#2: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) | [#3: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) |
| [Embeddings and representation geometry](#08-embeddings-and-representation-geometry) | [08.2 — Sentence and document embeddings](#082-sentence-and-document-embeddings) | 6 | [#1: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) | [#2: LLM Coding Interview: Retrieval Augmented Generation (2026)](https://medium.com/models-to-systems/llm-coding-interview-series-18-30-retrieval-augmented-generation-rag-00864084fcf8) | [#3: Beyond the Embedding: How LLMs Learned to See (2026)](https://medium.com/data-science-collective/beyond-the-embedding-how-llms-learned-to-see-ba74dae187ee) |
| [Embeddings and representation geometry](#08-embeddings-and-representation-geometry) | [08.3 — Representation analysis and retrieval](#083-representation-analysis-and-retrieval) | 6 | [#1: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) | [#2: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) | [#3: LLM Coding Interview: Retrieval Augmented Generation (2026)](https://medium.com/models-to-systems/llm-coding-interview-series-18-30-retrieval-augmented-generation-rag-00864084fcf8) |
| [Transformer architecture fundamentals](#09-transformer-architecture-fundamentals) | [09.1 — Transformer computation graph](#091-transformer-computation-graph) | 6 | [#1: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#2: Learn and Code MHA MQA and GQA (2025)](https://medium.com/%40r9644360/learn-and-code-mha-mqa-and-gqa-a-guide-to-efficient-attention-mechanisms-in-transformers-ff621fe76680) | [#3: Residual Connections and Normalization in Transformers (2026)](https://medium.com/%40wasowski.jarek/a-decade-of-misplaced-sacred-cows-in-neural-networks-residuals-norms-1a4f85749a0d) |
| [Transformer architecture fundamentals](#09-transformer-architecture-fundamentals) | [09.2 — Attention math](#092-attention-math) | 7 | [#1: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#2: Learn and Code MHA MQA and GQA (2025)](https://medium.com/%40r9644360/learn-and-code-mha-mqa-and-gqa-a-guide-to-efficient-attention-mechanisms-in-transformers-ff621fe76680) | [#3: Positional Encoding: Sinusoidal to RoPE to ALiBi (2026)](https://medium.com/data-science-collective/positional-encoding-from-sinusoidal-to-rope-to-alibi-02774e73a6a8) |
| [Transformer architecture fundamentals](#09-transformer-architecture-fundamentals) | [09.3 — Training versus autoregressive inference](#093-training-versus-autoregressive-inference) | 6 | [#1: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#2: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [Attention mechanisms and variants](#10-attention-mechanisms-and-variants) | [10.1 — Head organization](#101-head-organization) | 6 | [#1: Learn and Code MHA MQA and GQA (2025)](https://medium.com/%40r9644360/learn-and-code-mha-mqa-and-gqa-a-guide-to-efficient-attention-mechanisms-in-transformers-ff621fe76680) | [#2: LLM Inference Engineering: Problems and Solutions (2026)](https://medium.com/%40amitshekhar/llm-inference-engineering-problem-and-solution-8111b1919145) | [#3: Mixture of Experts from Router Up (2026)](https://medium.com/%40cosmicray001/mixture-of-experts-from-the-router-up-5c70caf9ea4b) |
| [Attention mechanisms and variants](#10-attention-mechanisms-and-variants) | [10.2 — Attention pattern variants](#102-attention-pattern-variants) | 6 | [#1: Learn and Code MHA MQA and GQA (2025)](https://medium.com/%40r9644360/learn-and-code-mha-mqa-and-gqa-a-guide-to-efficient-attention-mechanisms-in-transformers-ff621fe76680) | [#2: Positional Encoding: Sinusoidal to RoPE to ALiBi (2026)](https://medium.com/data-science-collective/positional-encoding-from-sinusoidal-to-rope-to-alibi-02774e73a6a8) | [#3: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) |
| [Attention mechanisms and variants](#10-attention-mechanisms-and-variants) | [10.3 — Novel and hybrid attention ideas](#103-novel-and-hybrid-attention-ideas) | 6 | [#1: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) | [#2: Beyond Attention: Mamba (2025)](https://medium.com/correll-lab/beyond-attention-mamba-as-a-replacement-for-transformers-5483b6e23a6e) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Positional information and context length](#11-positional-information-and-context-length) | [11.1 — Position encoding families](#111-position-encoding-families) | 7 | [#1: Positional Encoding: Sinusoidal to RoPE to ALiBi (2026)](https://medium.com/data-science-collective/positional-encoding-from-sinusoidal-to-rope-to-alibi-02774e73a6a8) | [#2: RoPE Explained: Intuition Behind Rotation (2026)](https://medium.com/data-science-collective/rope-explained-intuition-behind-why-rotation-is-better-than-addition-951e06091a7c) | [#3: RoPE: Rotary Positional Embedding (2026)](https://lzhangstat.medium.com/rope-rotary-positional-embedding-bcc631b5b88f) |
| [Positional information and context length](#11-positional-information-and-context-length) | [11.2 — RoPE and extrapolation details](#112-rope-and-extrapolation-details) | 6 | [#1: RoPE: Rotary Positional Embedding (2026)](https://lzhangstat.medium.com/rope-rotary-positional-embedding-bcc631b5b88f) | [#2: RoPE Explained: Intuition Behind Rotation (2026)](https://medium.com/data-science-collective/rope-explained-intuition-behind-why-rotation-is-better-than-addition-951e06091a7c) | [#3: Positional Encoding: Sinusoidal to RoPE to ALiBi (2026)](https://medium.com/data-science-collective/positional-encoding-from-sinusoidal-to-rope-to-alibi-02774e73a6a8) |
| [Positional information and context length](#11-positional-information-and-context-length) | [11.3 — Long-context learning](#113-long-context-learning) | 7 | [#1: Positional Encoding: Sinusoidal to RoPE to ALiBi (2026)](https://medium.com/data-science-collective/positional-encoding-from-sinusoidal-to-rope-to-alibi-02774e73a6a8) | [#2: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) | [#3: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) |
| [Transformer blocks, normalization, and activation design](#12-transformer-blocks-normalization-and-activation-design) | [12.1 — Feed-forward network design](#121-feed-forward-network-design) | 5 | [#1: Residual Connections and Normalization in Transformers (2026)](https://medium.com/%40wasowski.jarek/a-decade-of-misplaced-sacred-cows-in-neural-networks-residuals-norms-1a4f85749a0d) | [#2: Mixture of Experts from Router Up (2026)](https://medium.com/%40cosmicray001/mixture-of-experts-from-the-router-up-5c70caf9ea4b) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [Transformer blocks, normalization, and activation design](#12-transformer-blocks-normalization-and-activation-design) | [12.2 — Normalization and residual topology](#122-normalization-and-residual-topology) | 6 | [#1: Residual Connections and Normalization in Transformers (2026)](https://medium.com/%40wasowski.jarek/a-decade-of-misplaced-sacred-cows-in-neural-networks-residuals-norms-1a4f85749a0d) | [#2: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [Transformer blocks, normalization, and activation design](#12-transformer-blocks-normalization-and-activation-design) | [12.3 — Structural design choices](#123-structural-design-choices) | 6 | [#1: Residual Connections and Normalization in Transformers (2026)](https://medium.com/%40wasowski.jarek/a-decade-of-misplaced-sacred-cows-in-neural-networks-residuals-norms-1a4f85749a0d) | [#2: Learn and Code MHA MQA and GQA (2025)](https://medium.com/%40r9644360/learn-and-code-mha-mqa-and-gqa-a-guide-to-efficient-attention-mechanisms-in-transformers-ff621fe76680) | [#3: Beyond Attention: Mamba (2025)](https://medium.com/correll-lab/beyond-attention-mamba-as-a-replacement-for-transformers-5483b6e23a6e) |
| [Architecture families beyond standard decoder-only LLMs](#13-architecture-families-beyond-standard-decoder-only-llms) | [13.1 — Transformer family variants](#131-transformer-family-variants) | 6 | [#1: Attention Is All You Need: From RNNs to Transformers (2025)](https://medium.com/%40ftech/attention-is-all-you-need-the-evolution-from-rnns-to-transformers-ba81e12899d7) | [#2: Beyond Attention: Mamba (2025)](https://medium.com/correll-lab/beyond-attention-mamba-as-a-replacement-for-transformers-5483b6e23a6e) | [#3: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) |
| [Architecture families beyond standard decoder-only LLMs](#13-architecture-families-beyond-standard-decoder-only-llms) | [13.2 — Recurrence and state-space alternatives](#132-recurrence-and-state-space-alternatives) | 6 | [#1: Beyond Attention: Mamba (2025)](https://medium.com/correll-lab/beyond-attention-mamba-as-a-replacement-for-transformers-5483b6e23a6e) | [#2: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) | [#3: Attention Is All You Need: From RNNs to Transformers (2025)](https://medium.com/%40ftech/attention-is-all-you-need-the-evolution-from-rnns-to-transformers-ba81e12899d7) |
| [Architecture families beyond standard decoder-only LLMs](#13-architecture-families-beyond-standard-decoder-only-llms) | [13.3 — Hybrid and adaptive computation](#133-hybrid-and-adaptive-computation) | 6 | [#1: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) | [#2: Beyond Attention: Mamba (2025)](https://medium.com/correll-lab/beyond-attention-mamba-as-a-replacement-for-transformers-5483b6e23a6e) | [#3: Mixture of Experts from Router Up (2026)](https://medium.com/%40cosmicray001/mixture-of-experts-from-the-router-up-5c70caf9ea4b) |
| [Mixture-of-experts (MoE) and sparsity](#14-mixture-of-experts-moe-and-sparsity) | [14.1 — MoE fundamentals](#141-moe-fundamentals) | 6 | [#1: Mixture of Experts from Router Up (2026)](https://medium.com/%40cosmicray001/mixture-of-experts-from-the-router-up-5c70caf9ea4b) | [#2: MoE: Routing as Active Research (2026)](https://medium.com/models-to-systems/mixture-of-experts-why-routing-is-the-active-research-surface-explained-for-everyone-e4f9f5e8c07e) | [#3: Auxiliary-Loss-Free Load Balancing for MoE (2026)](https://medium.com/mlwithdev/deepseek-series-auxiliary-loss-free-load-balancing-for-mixture-of-experts-5dbd4e983bba) |
| [Mixture-of-experts (MoE) and sparsity](#14-mixture-of-experts-moe-and-sparsity) | [14.2 — Training and routing mechanics](#142-training-and-routing-mechanics) | 6 | [#1: Auxiliary-Loss-Free Load Balancing for MoE (2026)](https://medium.com/mlwithdev/deepseek-series-auxiliary-loss-free-load-balancing-for-mixture-of-experts-5dbd4e983bba) | [#2: Mixture of Experts from Router Up (2026)](https://medium.com/%40cosmicray001/mixture-of-experts-from-the-router-up-5c70caf9ea4b) | [#3: MoE: Routing as Active Research (2026)](https://medium.com/models-to-systems/mixture-of-experts-why-routing-is-the-active-research-surface-explained-for-everyone-e4f9f5e8c07e) |
| [Mixture-of-experts (MoE) and sparsity](#14-mixture-of-experts-moe-and-sparsity) | [14.3 — MoE inference and adaptation](#143-moe-inference-and-adaptation) | 6 | [#1: Mixture of Experts from Router Up (2026)](https://medium.com/%40cosmicray001/mixture-of-experts-from-the-router-up-5c70caf9ea4b) | [#2: MoE: Routing as Active Research (2026)](https://medium.com/models-to-systems/mixture-of-experts-why-routing-is-the-active-research-surface-explained-for-everyone-e4f9f5e8c07e) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Scaling laws, compute, and model design](#15-scaling-laws-compute-and-model-design) | [15.1 — Empirical scaling behavior](#151-empirical-scaling-behavior) | 6 | [#1: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) | [#2: Why Transformers Scale: The Math of Scaling Laws (2026)](https://medium.com/%40ppp.mishra124/why-transformers-scale-the-math-of-scaling-laws-02c045509186) | [#3: AI Scaling Laws: Bigger Is Not Always Better (2026)](https://medium.com/%40ardacikgoz9/ai-scaling-laws-why-bigger-isnt-always-better-and-when-it-is-c95be4d84c3a) |
| [Scaling laws, compute, and model design](#15-scaling-laws-compute-and-model-design) | [15.2 — Model and compute budgeting](#152-model-and-compute-budgeting) | 6 | [#1: Why Transformers Scale: The Math of Scaling Laws (2026)](https://medium.com/%40ppp.mishra124/why-transformers-scale-the-math-of-scaling-laws-02c045509186) | [#2: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) | [#3: AI Scaling Laws: Bigger Is Not Always Better (2026)](https://medium.com/%40ardacikgoz9/ai-scaling-laws-why-bigger-isnt-always-better-and-when-it-is-c95be4d84c3a) |
| [Scaling laws, compute, and model design](#15-scaling-laws-compute-and-model-design) | [15.3 — Research design questions](#153-research-design-questions) | 6 | [#1: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) | [#2: Why Transformers Scale: The Math of Scaling Laws (2026)](https://medium.com/%40ppp.mishra124/why-transformers-scale-the-math-of-scaling-laws-02c045509186) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Pretraining objectives and objectives beyond next-token prediction](#16-pretraining-objectives-and-objectives-beyond-next-token-prediction) | [16.1 — Core LM objectives](#161-core-lm-objectives) | 6 | [#1: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#2: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Pretraining objectives and objectives beyond next-token prediction](#16-pretraining-objectives-and-objectives-beyond-next-token-prediction) | [16.2 — Specialized and auxiliary objectives](#162-specialized-and-auxiliary-objectives) | 6 | [#1: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#2: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#3: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) |
| [Pretraining objectives and objectives beyond next-token prediction](#16-pretraining-objectives-and-objectives-beyond-next-token-prediction) | [16.3 — Objective mechanics](#163-objective-mechanics) | 6 | [#1: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#2: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#3: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) |
| [Pretraining optimization and experimental practice](#17-pretraining-optimization-and-experimental-practice) | [17.1 — Training-loop implementation](#171-training-loop-implementation) | 6 | [#1: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#2: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Pretraining optimization and experimental practice](#17-pretraining-optimization-and-experimental-practice) | [17.2 — Stability and debugging](#172-stability-and-debugging) | 6 | [#1: I Traced Every Gradient Through Attention (2026)](https://medium.com/data-and-beyond/i-traced-every-gradient-through-attention-here-they-all-are-d284e494623a) | [#2: Residual Connections and Normalization in Transformers (2026)](https://medium.com/%40wasowski.jarek/a-decade-of-misplaced-sacred-cows-in-neural-networks-residuals-norms-1a4f85749a0d) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [Pretraining optimization and experimental practice](#17-pretraining-optimization-and-experimental-practice) | [17.3 — Training stages and checkpoints](#173-training-stages-and-checkpoints) | 6 | [#1: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#2: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#3: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) |
| [Training hardware and distributed systems](#18-training-hardware-and-distributed-systems) | [18.1 — Accelerator and memory fundamentals](#181-accelerator-and-memory-fundamentals) | 6 | [#1: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#2: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [Training hardware and distributed systems](#18-training-hardware-and-distributed-systems) | [18.2 — Parallelism strategies](#182-parallelism-strategies) | 7 | [#1: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#2: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Training hardware and distributed systems](#18-training-hardware-and-distributed-systems) | [18.3 — Memory and runtime optimization](#183-memory-and-runtime-optimization) | 6 | [#1: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#2: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Training hardware and distributed systems](#18-training-hardware-and-distributed-systems) | [18.4 — Operational training infrastructure](#184-operational-training-infrastructure) | 6 | [#1: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#2: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#3: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) |
| [Fine-tuning, adaptation, and transfer learning](#19-fine-tuning-adaptation-and-transfer-learning) | [19.1 — Fine-tuning paradigms](#191-fine-tuning-paradigms) | 6 | [#1: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) |
| [Fine-tuning, adaptation, and transfer learning](#19-fine-tuning-adaptation-and-transfer-learning) | [19.2 — Parameter-efficient fine-tuning (PEFT)](#192-parameter-efficient-fine-tuning-peft) | 6 | [#1: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: Fine Tuning VaultGemma with Differential Privacy (2025)](https://medium.com/%40rubenszimbres/fine-tuning-vaultgemma-with-differential-privacy-using-a-colab-runtime-in-vscode-2a01d39d2821) |
| [Fine-tuning, adaptation, and transfer learning](#19-fine-tuning-adaptation-and-transfer-learning) | [19.3 — Adapter composition and deployment](#193-adapter-composition-and-deployment) | 6 | [#1: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) |
| [Fine-tuning, adaptation, and transfer learning](#19-fine-tuning-adaptation-and-transfer-learning) | [19.4 — Fine-tuning quality controls](#194-fine-tuning-quality-controls) | 6 | [#1: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#2: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#3: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) |
| [Instruction tuning and supervised post-training (SFT)](#20-instruction-tuning-and-supervised-post-training-sft) | [20.1 — Instruction datasets](#201-instruction-datasets) | 6 | [#1: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#2: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#3: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) |
| [Instruction tuning and supervised post-training (SFT)](#20-instruction-tuning-and-supervised-post-training-sft) | [20.2 — SFT objectives and methods](#202-sft-objectives-and-methods) | 6 | [#1: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#2: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#3: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) |
| [Instruction tuning and supervised post-training (SFT)](#20-instruction-tuning-and-supervised-post-training-sft) | [20.3 — SFT failure modes and evaluation](#203-sft-failure-modes-and-evaluation) | 6 | [#1: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) |
| [Preference learning, reward modeling, and RLHF](#21-preference-learning-reward-modeling-and-rlhf) | [21.1 — Human preference data](#211-human-preference-data) | 6 | [#1: Beyond RLHF: Direct Preference Optimization (2026)](https://medium.com/data-science-collective/beyond-rlhf-aligning-llms-with-direct-preference-optimization-dpo-79f968c9177f) | [#2: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) | [#3: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) |
| [Preference learning, reward modeling, and RLHF](#21-preference-learning-reward-modeling-and-rlhf) | [21.2 — Reward-model training](#212-reward-model-training) | 6 | [#1: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#2: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) | [#3: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) |
| [Preference learning, reward modeling, and RLHF](#21-preference-learning-reward-modeling-and-rlhf) | [21.3 — Classical RLHF pipeline](#213-classical-rlhf-pipeline) | 6 | [#1: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) |
| [Preference learning, reward modeling, and RLHF](#21-preference-learning-reward-modeling-and-rlhf) | [21.4 — Offline and direct preference objectives](#214-offline-and-direct-preference-objectives) | 6 | [#1: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) | [#2: Beyond RLHF: Direct Preference Optimization (2026)](https://medium.com/data-science-collective/beyond-rlhf-aligning-llms-with-direct-preference-optimization-dpo-79f968c9177f) | [#3: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) |
| [Preference learning, reward modeling, and RLHF](#21-preference-learning-reward-modeling-and-rlhf) | [21.5 — Alignment feedback sources](#215-alignment-feedback-sources) | 6 | [#1: Beyond RLHF: Direct Preference Optimization (2026)](https://medium.com/data-science-collective/beyond-rlhf-aligning-llms-with-direct-preference-optimization-dpo-79f968c9177f) | [#2: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) | [#3: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) |
| [Reinforcement learning for reasoning and verifiable tasks](#22-reinforcement-learning-for-reasoning-and-verifiable-tasks) | [22.1 — RL foundations applied to LLMs](#221-rl-foundations-applied-to-llms) | 6 | [#1: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) | [#2: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#3: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) |
| [Reinforcement learning for reasoning and verifiable tasks](#22-reinforcement-learning-for-reasoning-and-verifiable-tasks) | [22.2 — LLM-centric RL objectives](#222-llm-centric-rl-objectives) | 6 | [#1: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#2: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) | [#3: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) |
| [Reinforcement learning for reasoning and verifiable tasks](#22-reinforcement-learning-for-reasoning-and-verifiable-tasks) | [22.3 — Training with verifiers and environments](#223-training-with-verifiers-and-environments) | 6 | [#1: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#2: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#3: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) |
| [Reinforcement learning for reasoning and verifiable tasks](#22-reinforcement-learning-for-reasoning-and-verifiable-tasks) | [22.4 — Reasoning-RL pathologies](#224-reasoning-rl-pathologies) | 6 | [#1: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) | [#2: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#3: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) |
| [Reinforcement learning for reasoning and verifiable tasks](#22-reinforcement-learning-for-reasoning-and-verifiable-tasks) | [22.5 — Online RL engineering](#225-online-rl-engineering) | 6 | [#1: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#2: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) | [#3: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) |
| [Reasoning, planning, and test-time computation](#23-reasoning-planning-and-test-time-computation) | [23.1 — Reasoning behaviors](#231-reasoning-behaviors) | 6 | [#1: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) | [#2: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#3: In Context Learning: Induction Head (2025)](https://medium.com/%40madhuriagarwal723/in-context-learning-induction-head-1279b36934fb) |
| [Reasoning, planning, and test-time computation](#23-reasoning-planning-and-test-time-computation) | [23.2 — Prompt-level reasoning strategies](#232-prompt-level-reasoning-strategies) | 6 | [#1: Prompt Engineering 2026: Introduction (2026)](https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433) | [#2: In Context Learning: Induction Head (2025)](https://medium.com/%40madhuriagarwal723/in-context-learning-induction-head-1279b36934fb) | [#3: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) |
| [Reasoning, planning, and test-time computation](#23-reasoning-planning-and-test-time-computation) | [23.3 — Search and inference-time algorithms](#233-search-and-inference-time-algorithms) | 6 | [#1: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) | [#2: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#3: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) |
| [Reasoning, planning, and test-time computation](#23-reasoning-planning-and-test-time-computation) | [23.4 — Advanced reasoning paradigms](#234-advanced-reasoning-paradigms) | 6 | [#1: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) | [#2: Prompt Engineering 2026: Introduction (2026)](https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433) | [#3: In Context Learning: Induction Head (2025)](https://medium.com/%40madhuriagarwal723/in-context-learning-induction-head-1279b36934fb) |
| [Reasoning, planning, and test-time computation](#23-reasoning-planning-and-test-time-computation) | [23.5 — Math and formal reasoning](#235-math-and-formal-reasoning) | 6 | [#1: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) | [#2: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#3: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) |
| [Autoregressive generation and decoding](#24-autoregressive-generation-and-decoding) | [24.1 — Logits to output tokens](#241-logits-to-output-tokens) | 6 | [#1: Top P vs Top K vs Temperature (2026)](https://harshitdawar.medium.com/top-p-vs-top-k-vs-temperature-60494480b9d5) | [#2: Decoding the Decoder: Top k Top p Beam Search (2025)](https://medium.com/%40ayushyajnik2/decoding-the-decoder-top-k-top-p-temperature-beam-search-hallucinations-in-llms-e54963eb3de7) | [#3: Choosing between Top K Top P Temperature (2025)](https://medium.com/%40CyberGee/choosing-between-top-k-top-p-temperature-53fa89f71ae5) |
| [Autoregressive generation and decoding](#24-autoregressive-generation-and-decoding) | [24.2 — Search and multiple candidates](#242-search-and-multiple-candidates) | 6 | [#1: Decoding the Decoder: Top k Top p Beam Search (2025)](https://medium.com/%40ayushyajnik2/decoding-the-decoder-top-k-top-p-temperature-beam-search-hallucinations-in-llms-e54963eb3de7) | [#2: Top P vs Top K vs Temperature (2026)](https://harshitdawar.medium.com/top-p-vs-top-k-vs-temperature-60494480b9d5) | [#3: Choosing between Top K Top P Temperature (2025)](https://medium.com/%40CyberGee/choosing-between-top-k-top-p-temperature-53fa89f71ae5) |
| [Autoregressive generation and decoding](#24-autoregressive-generation-and-decoding) | [24.3 — Structured and constrained generation](#243-structured-and-constrained-generation) | 6 | [#1: Decoding the Decoder: Top k Top p Beam Search (2025)](https://medium.com/%40ayushyajnik2/decoding-the-decoder-top-k-top-p-temperature-beam-search-hallucinations-in-llms-e54963eb3de7) | [#2: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Autoregressive generation and decoding](#24-autoregressive-generation-and-decoding) | [24.4 — Decoding pitfalls](#244-decoding-pitfalls) | 6 | [#1: Decoding the Decoder: Top k Top p Beam Search (2025)](https://medium.com/%40ayushyajnik2/decoding-the-decoder-top-k-top-p-temperature-beam-search-hallucinations-in-llms-e54963eb3de7) | [#2: Top P vs Top K vs Temperature (2026)](https://harshitdawar.medium.com/top-p-vs-top-k-vs-temperature-60494480b9d5) | [#3: Choosing between Top K Top P Temperature (2025)](https://medium.com/%40CyberGee/choosing-between-top-k-top-p-temperature-53fa89f71ae5) |
| [Prompt engineering and context engineering](#25-prompt-engineering-and-context-engineering) | [25.1 — Prompt construction](#251-prompt-construction) | 6 | [#1: Prompt Engineering 2026: Introduction (2026)](https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433) | [#2: Prompt Engineering vs Context Engineering: Research (2026)](https://medium.com/beyond-the-algorithm/prompt-engineering-vs-context-engineering-what-the-research-actually-says-c4637e46c98b) | [#3: Context Engineering Is the New Prompt Engineering (2026)](https://medium.com/data-science-collective/context-engineering-is-the-new-prompt-engineering-and-most-people-are-doing-it-wrong-79698a7698f6) |
| [Prompt engineering and context engineering](#25-prompt-engineering-and-context-engineering) | [25.2 — Advanced prompt techniques](#252-advanced-prompt-techniques) | 6 | [#1: Prompt Engineering 2026: Introduction (2026)](https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433) | [#2: Prompt Engineering vs Context Engineering: Research (2026)](https://medium.com/beyond-the-algorithm/prompt-engineering-vs-context-engineering-what-the-research-actually-says-c4637e46c98b) | [#3: Context Engineering Is the New Prompt Engineering (2026)](https://medium.com/data-science-collective/context-engineering-is-the-new-prompt-engineering-and-most-people-are-doing-it-wrong-79698a7698f6) |
| [Prompt engineering and context engineering](#25-prompt-engineering-and-context-engineering) | [25.3 — Context assembly](#253-context-assembly) | 6 | [#1: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#2: Prompt Engineering vs Context Engineering: Research (2026)](https://medium.com/beyond-the-algorithm/prompt-engineering-vs-context-engineering-what-the-research-actually-says-c4637e46c98b) | [#3: Context Engineering Is the New Prompt Engineering (2026)](https://medium.com/data-science-collective/context-engineering-is-the-new-prompt-engineering-and-most-people-are-doing-it-wrong-79698a7698f6) |
| [Prompt engineering and context engineering](#25-prompt-engineering-and-context-engineering) | [25.4 — Prompt reliability and measurement](#254-prompt-reliability-and-measurement) | 6 | [#1: Prompt Engineering vs Context Engineering: Research (2026)](https://medium.com/beyond-the-algorithm/prompt-engineering-vs-context-engineering-what-the-research-actually-says-c4637e46c98b) | [#2: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#3: Prompt Engineering 2026: Introduction (2026)](https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433) |
| [Long-context systems, compression, and persistent context](#26-long-context-systems-compression-and-persistent-context) | [26.1 — Long-context use cases](#261-long-context-use-cases) | 6 | [#1: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) | [#2: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#3: Prompt Engineering vs Context Engineering: Research (2026)](https://medium.com/beyond-the-algorithm/prompt-engineering-vs-context-engineering-what-the-research-actually-says-c4637e46c98b) |
| [Long-context systems, compression, and persistent context](#26-long-context-systems-compression-and-persistent-context) | [26.2 — Context-reduction strategies](#262-context-reduction-strategies) | 6 | [#1: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#2: Prompt Engineering vs Context Engineering: Research (2026)](https://medium.com/beyond-the-algorithm/prompt-engineering-vs-context-engineering-what-the-research-actually-says-c4637e46c98b) | [#3: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) |
| [Long-context systems, compression, and persistent context](#26-long-context-systems-compression-and-persistent-context) | [26.3 — Memory integration](#263-memory-integration) | 6 | [#1: Agent Memory Frameworks: Mem0 Zep Letta Cognee (2026)](https://medium.com/data-science-collective/agent-memory-frameworks-showdown-cognee-vs-mem0-vs-zep-vs-letta-0f439b56f282) | [#2: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#3: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) |
| [KV cache and inference memory management](#27-kv-cache-and-inference-memory-management) | [27.1 — KV cache mathematics and layout](#271-kv-cache-mathematics-and-layout) | 6 | [#1: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#2: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) | [#3: Learn and Code MHA MQA and GQA (2025)](https://medium.com/%40r9644360/learn-and-code-mha-mqa-and-gqa-a-guide-to-efficient-attention-mechanisms-in-transformers-ff621fe76680) |
| [KV cache and inference memory management](#27-kv-cache-and-inference-memory-management) | [27.2 — Cache memory architectures](#272-cache-memory-architectures) | 6 | [#1: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) | [#2: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#3: vLLM Explained (2026)](https://medium.com/mlworks/vllm-explained-how-it-makes-llm-inference-faster-044da99542cf) |
| [KV cache and inference memory management](#27-kv-cache-and-inference-memory-management) | [27.3 — KV compression and advanced caching](#273-kv-compression-and-advanced-caching) | 6 | [#1: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#2: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) | [#3: vLLM Explained (2026)](https://medium.com/mlworks/vllm-explained-how-it-makes-llm-inference-faster-044da99542cf) |
| [KV cache and inference memory management](#27-kv-cache-and-inference-memory-management) | [27.4 — Cache performance and validation](#274-cache-performance-and-validation) | 6 | [#1: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) | [#2: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) | [#3: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) |
| [Efficient attention kernels and GPU optimization](#28-efficient-attention-kernels-and-gpu-optimization) | [28.1 — IO-aware attention](#281-io-aware-attention) | 6 | [#1: Kernel Case Study: Flash Attention (2025)](https://arunjitha.medium.com/kernel-case-study-flash-attention-5d63a3875c2d) | [#2: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) | [#3: LLM Inference Engineering: Problems and Solutions (2026)](https://medium.com/%40amitshekhar/llm-inference-engineering-problem-and-solution-8111b1919145) |
| [Efficient attention kernels and GPU optimization](#28-efficient-attention-kernels-and-gpu-optimization) | [28.2 — GPU kernel engineering](#282-gpu-kernel-engineering) | 6 | [#1: Kernel Case Study: Flash Attention (2025)](https://arunjitha.medium.com/kernel-case-study-flash-attention-5d63a3875c2d) | [#2: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) | [#3: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) |
| [Efficient attention kernels and GPU optimization](#28-efficient-attention-kernels-and-gpu-optimization) | [28.3 — Attention alternatives and benchmarking](#283-attention-alternatives-and-benchmarking) | 6 | [#1: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) | [#2: Kernel Case Study: Flash Attention (2025)](https://arunjitha.medium.com/kernel-case-study-flash-attention-5d63a3875c2d) | [#3: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) |
| [Quantization, pruning, sparsity, and distillation](#29-quantization-pruning-sparsity-and-distillation) | [29.1 — Numeric formats and quantization basics](#291-numeric-formats-and-quantization-basics) | 6 | [#1: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) | [#2: LLM Inference Engineering: Problems and Solutions (2026)](https://medium.com/%40amitshekhar/llm-inference-engineering-problem-and-solution-8111b1919145) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Quantization, pruning, sparsity, and distillation](#29-quantization-pruning-sparsity-and-distillation) | [29.2 — Weight and activation quantization](#292-weight-and-activation-quantization) | 7 | [#1: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) | [#2: LLM Inference Engineering: Problems and Solutions (2026)](https://medium.com/%40amitshekhar/llm-inference-engineering-problem-and-solution-8111b1919145) | [#3: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) |
| [Quantization, pruning, sparsity, and distillation](#29-quantization-pruning-sparsity-and-distillation) | [29.3 — Inference-oriented compression](#293-inference-oriented-compression) | 6 | [#1: LLM Inference Engineering: Problems and Solutions (2026)](https://medium.com/%40amitshekhar/llm-inference-engineering-problem-and-solution-8111b1919145) | [#2: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Quantization, pruning, sparsity, and distillation](#29-quantization-pruning-sparsity-and-distillation) | [29.4 — Distillation and compact modeling](#294-distillation-and-compact-modeling) | 6 | [#1: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: LLM Inference Engineering: Problems and Solutions (2026)](https://medium.com/%40amitshekhar/llm-inference-engineering-problem-and-solution-8111b1919145) |
| [LLM inference execution and throughput optimization](#30-llm-inference-execution-and-throughput-optimization) | [30.1 — Prefill/decode computational regimes](#301-prefilldecode-computational-regimes) | 6 | [#1: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#2: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) | [#3: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) |
| [LLM inference execution and throughput optimization](#30-llm-inference-execution-and-throughput-optimization) | [30.2 — Batching and request scheduling](#302-batching-and-request-scheduling) | 6 | [#1: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) | [#2: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#3: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) |
| [LLM inference execution and throughput optimization](#30-llm-inference-execution-and-throughput-optimization) | [30.3 — Speculative and parallel generation](#303-speculative-and-parallel-generation) | 6 | [#1: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) | [#2: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) | [#3: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) |
| [LLM inference execution and throughput optimization](#30-llm-inference-execution-and-throughput-optimization) | [30.4 — Distributed inference architecture](#304-distributed-inference-architecture) | 6 | [#1: LLM Inference Stack in 2026 (2026)](https://medium.com/%40charan.panthangi/the-llm-inference-stack-in-2026-vllm-sglang-tensorrt-llm-semantic-routing-and-the-combination-d9df1a16f93f) | [#2: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) | [#3: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) |
| [Model serving engines and deployment stacks](#31-model-serving-engines-and-deployment-stacks) | [31.1 — Open and commercial inference runtimes](#311-open-and-commercial-inference-runtimes) | 6 | [#1: LLM Inference Stack in 2026 (2026)](https://medium.com/%40charan.panthangi/the-llm-inference-stack-in-2026-vllm-sglang-tensorrt-llm-semantic-routing-and-the-combination-d9df1a16f93f) | [#2: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) | [#3: vLLM Explained (2026)](https://medium.com/mlworks/vllm-explained-how-it-makes-llm-inference-faster-044da99542cf) |
| [Model serving engines and deployment stacks](#31-model-serving-engines-and-deployment-stacks) | [31.2 — Serving design](#312-serving-design) | 6 | [#1: LLM Inference Stack in 2026 (2026)](https://medium.com/%40charan.panthangi/the-llm-inference-stack-in-2026-vllm-sglang-tensorrt-llm-semantic-routing-and-the-combination-d9df1a16f93f) | [#2: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#3: vLLM Explained (2026)](https://medium.com/mlworks/vllm-explained-how-it-makes-llm-inference-faster-044da99542cf) |
| [Model serving engines and deployment stacks](#31-model-serving-engines-and-deployment-stacks) | [31.3 — Production performance](#313-production-performance) | 6 | [#1: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) | [#2: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) | [#3: LLM Inference Stack in 2026 (2026)](https://medium.com/%40charan.panthangi/the-llm-inference-stack-in-2026-vllm-sglang-tensorrt-llm-semantic-routing-and-the-combination-d9df1a16f93f) |
| [LLM APIs, protocols, and application integration](#32-llm-apis-protocols-and-application-integration) | [32.1 — API fundamentals](#321-api-fundamentals) | 6 | [#1: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#2: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) | [#3: Tools in 2026: Action Selection (2026)](https://medium.com/%40Micheal-Lanham/tools-in-2026-why-picking-the-right-action-is-the-new-planning-problem-d28d8443bf3f) |
| [LLM APIs, protocols, and application integration](#32-llm-apis-protocols-and-application-integration) | [32.2 — Structured interfaces](#322-structured-interfaces) | 6 | [#1: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#2: Tools in 2026: Action Selection (2026)](https://medium.com/%40Micheal-Lanham/tools-in-2026-why-picking-the-right-action-is-the-new-planning-problem-d28d8443bf3f) | [#3: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) |
| [LLM APIs, protocols, and application integration](#32-llm-apis-protocols-and-application-integration) | [32.3 — System integration](#323-system-integration) | 6 | [#1: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#2: Tools in 2026: Action Selection (2026)](https://medium.com/%40Micheal-Lanham/tools-in-2026-why-picking-the-right-action-is-the-new-planning-problem-d28d8443bf3f) | [#3: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) |
| [Retrieval, search, ranking, and embedding systems](#33-retrieval-search-ranking-and-embedding-systems) | [33.1 — Search paradigms](#331-search-paradigms) | 6 | [#1: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) | [#2: LLM Coding Interview: Retrieval Augmented Generation (2026)](https://medium.com/models-to-systems/llm-coding-interview-series-18-30-retrieval-augmented-generation-rag-00864084fcf8) | [#3: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) |
| [Retrieval, search, ranking, and embedding systems](#33-retrieval-search-ranking-and-embedding-systems) | [33.2 — Indexing and vector databases](#332-indexing-and-vector-databases) | 6 | [#1: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) | [#2: LLM Coding Interview: Retrieval Augmented Generation (2026)](https://medium.com/models-to-systems/llm-coding-interview-series-18-30-retrieval-augmented-generation-rag-00864084fcf8) | [#3: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) |
| [Retrieval, search, ranking, and embedding systems](#33-retrieval-search-ranking-and-embedding-systems) | [33.3 — Retrieval training and metrics](#333-retrieval-training-and-metrics) | 6 | [#1: RAG Evaluation Metrics: Retrieval Generation E2E (2026)](https://medium.com/operations-research-bit/evaluation-metrics-for-rag-measure-retrieval-generation-and-end-to-end-quality-with-numbers-that-f80d3f14f889) | [#2: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) | [#3: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) |
| [Retrieval-augmented generation (RAG)](#34-retrieval-augmented-generation-rag) | [34.1 — Document ingestion and chunking](#341-document-ingestion-and-chunking) | 6 | [#1: LLM Coding Interview: Retrieval Augmented Generation (2026)](https://medium.com/models-to-systems/llm-coding-interview-series-18-30-retrieval-augmented-generation-rag-00864084fcf8) | [#2: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) | [#3: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) |
| [Retrieval-augmented generation (RAG)](#34-retrieval-augmented-generation-rag) | [34.2 — RAG query pipeline](#342-rag-query-pipeline) | 6 | [#1: LLM Coding Interview: Retrieval Augmented Generation (2026)](https://medium.com/models-to-systems/llm-coding-interview-series-18-30-retrieval-augmented-generation-rag-00864084fcf8) | [#2: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) | [#3: 10 RAG Shifts in Production AI (2026)](https://medium.com/microsoft/10-rag-shifts-redefining-production-ai-in-2026-7acbdd66076c) |
| [Retrieval-augmented generation (RAG)](#34-retrieval-augmented-generation-rag) | [34.3 — Advanced RAG strategies](#343-advanced-rag-strategies) | 6 | [#1: 10 RAG Shifts in Production AI (2026)](https://medium.com/microsoft/10-rag-shifts-redefining-production-ai-in-2026-7acbdd66076c) | [#2: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) | [#3: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) |
| [Retrieval-augmented generation (RAG)](#34-retrieval-augmented-generation-rag) | [34.4 — RAG evaluation and optimization](#344-rag-evaluation-and-optimization) | 6 | [#1: RAG Evaluation Metrics: Retrieval Generation E2E (2026)](https://medium.com/operations-research-bit/evaluation-metrics-for-rag-measure-retrieval-generation-and-end-to-end-quality-with-numbers-that-f80d3f14f889) | [#2: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) | [#3: Dense vs Hybrid Retrieval Measured (2026)](https://medium.com/adi-insights-innovations-collective/dense-vs-hybrid-retrieval-measuring-what-each-layer-adds-f372e69d08e7) |
| [Tool use, function calling, and external computation](#35-tool-use-function-calling-and-external-computation) | [35.1 — Tool-use fundamentals](#351-tool-use-fundamentals) | 6 | [#1: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#2: Tools in 2026: Action Selection (2026)](https://medium.com/%40Micheal-Lanham/tools-in-2026-why-picking-the-right-action-is-the-new-planning-problem-d28d8443bf3f) | [#3: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) |
| [Tool use, function calling, and external computation](#35-tool-use-function-calling-and-external-computation) | [35.2 — Tool-use categories](#352-tool-use-categories) | 6 | [#1: Tools in 2026: Action Selection (2026)](https://medium.com/%40Micheal-Lanham/tools-in-2026-why-picking-the-right-action-is-the-new-planning-problem-d28d8443bf3f) | [#2: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#3: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) |
| [Tool use, function calling, and external computation](#35-tool-use-function-calling-and-external-computation) | [35.3 — Tool-use reliability and safety](#353-tool-use-reliability-and-safety) | 6 | [#1: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#2: Tools in 2026: Action Selection (2026)](https://medium.com/%40Micheal-Lanham/tools-in-2026-why-picking-the-right-action-is-the-new-planning-problem-d28d8443bf3f) | [#3: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) |
| [LLM agents and workflow architectures](#36-llm-agents-and-workflow-architectures) | [36.1 — Agent fundamentals](#361-agent-fundamentals) | 6 | [#1: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#2: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) | [#3: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) |
| [LLM agents and workflow architectures](#36-llm-agents-and-workflow-architectures) | [36.2 — Agent patterns](#362-agent-patterns) | 6 | [#1: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) | [#2: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) | [#3: Tools in 2026: Action Selection (2026)](https://medium.com/%40Micheal-Lanham/tools-in-2026-why-picking-the-right-action-is-the-new-planning-problem-d28d8443bf3f) |
| [LLM agents and workflow architectures](#36-llm-agents-and-workflow-architectures) | [36.3 — Reliability and governance](#363-reliability-and-governance) | 6 | [#1: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#2: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#3: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) |
| [Multi-agent systems, coordination, and protocols](#37-multi-agent-systems-coordination-and-protocols) | [37.1 — Multi-agent coordination](#371-multi-agent-coordination) | 6 | [#1: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) | [#2: A2A Joins AAIF (2026)](https://medium.com/google-cloud/a2a-joins-aaif-90047ccdf731) | [#3: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) |
| [Multi-agent systems, coordination, and protocols](#37-multi-agent-systems-coordination-and-protocols) | [37.2 — Agent communication and interoperability](#372-agent-communication-and-interoperability) | 6 | [#1: A2A Joins AAIF (2026)](https://medium.com/google-cloud/a2a-joins-aaif-90047ccdf731) | [#2: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) | [#3: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) |
| [Multi-agent systems, coordination, and protocols](#37-multi-agent-systems-coordination-and-protocols) | [37.3 — Agent evaluation and optimization](#373-agent-evaluation-and-optimization) | 6 | [#1: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#2: Token Cost of Routing Agent Intents (2026)](https://medium.com/google-cloud/routing-160-telco-intents-in-gecx-can-we-use-systemone-thinking-models-6f4eaf3dc0cf) | [#3: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) |
| [Agent memory, state, and long-horizon autonomy](#38-agent-memory-state-and-long-horizon-autonomy) | [38.1 — Memory taxonomies](#381-memory-taxonomies) | 6 | [#1: Agent Memory Frameworks: Mem0 Zep Letta Cognee (2026)](https://medium.com/data-science-collective/agent-memory-frameworks-showdown-cognee-vs-mem0-vs-zep-vs-letta-0f439b56f282) | [#2: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#3: Prompt Engineering vs Context Engineering: Research (2026)](https://medium.com/beyond-the-algorithm/prompt-engineering-vs-context-engineering-what-the-research-actually-says-c4637e46c98b) |
| [Agent memory, state, and long-horizon autonomy](#38-agent-memory-state-and-long-horizon-autonomy) | [38.2 — Memory operations](#382-memory-operations) | 6 | [#1: Agent Memory Frameworks: Mem0 Zep Letta Cognee (2026)](https://medium.com/data-science-collective/agent-memory-frameworks-showdown-cognee-vs-mem0-vs-zep-vs-letta-0f439b56f282) | [#2: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#3: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) |
| [Agent memory, state, and long-horizon autonomy](#38-agent-memory-state-and-long-horizon-autonomy) | [38.3 — Long-horizon execution](#383-long-horizon-execution) | 6 | [#1: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) | [#2: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) | [#3: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) |
| [Multimodal LLM fundamentals](#39-multimodal-llm-fundamentals) | [39.1 — Multimodal representations](#391-multimodal-representations) | 6 | [#1: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#2: Beyond the Embedding: How LLMs Learned to See (2026)](https://medium.com/data-science-collective/beyond-the-embedding-how-llms-learned-to-see-ba74dae187ee) | [#3: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) |
| [Multimodal LLM fundamentals](#39-multimodal-llm-fundamentals) | [39.2 — Multimodal training](#392-multimodal-training) | 6 | [#1: Beyond the Embedding: How LLMs Learned to See (2026)](https://medium.com/data-science-collective/beyond-the-embedding-how-llms-learned-to-see-ba74dae187ee) | [#2: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#3: Robot Foundation Models: A Technical Survey (2026)](https://medium.com/%40adnanmasood/robot-foundation-models-a-complete-technical-survey-5bf9add22d1c) |
| [Multimodal LLM fundamentals](#39-multimodal-llm-fundamentals) | [39.3 — Evaluation and integration](#393-evaluation-and-integration) | 6 | [#1: Sharp Attention Is a Lie in VLMs (2026)](https://medium.com/%40loganmann_98349/sharp-attention-is-a-lie-what-actually-predicts-when-a-vision-language-model-is-right-8ea4b0abfa98) | [#2: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#3: Advanced RAG Long Context and Multimodal (2026)](https://billtcheng2013.medium.com/retrieval-augmented-generation-advanced-6ebcc4fa4914) |
| [Vision-language models (VLMs) and documents](#40-vision-language-models-vlms-and-documents) | [40.1 — Vision encoders and alignment](#401-vision-encoders-and-alignment) | 6 | [#1: Beyond the Embedding: How LLMs Learned to See (2026)](https://medium.com/data-science-collective/beyond-the-embedding-how-llms-learned-to-see-ba74dae187ee) | [#2: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#3: Sharp Attention Is a Lie in VLMs (2026)](https://medium.com/%40loganmann_98349/sharp-attention-is-a-lie-what-actually-predicts-when-a-vision-language-model-is-right-8ea4b0abfa98) |
| [Vision-language models (VLMs) and documents](#40-vision-language-models-vlms-and-documents) | [40.2 — VLM capabilities](#402-vlm-capabilities) | 6 | [#1: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#2: Beyond the Embedding: How LLMs Learned to See (2026)](https://medium.com/data-science-collective/beyond-the-embedding-how-llms-learned-to-see-ba74dae187ee) | [#3: Sharp Attention Is a Lie in VLMs (2026)](https://medium.com/%40loganmann_98349/sharp-attention-is-a-lie-what-actually-predicts-when-a-vision-language-model-is-right-8ea4b0abfa98) |
| [Vision-language models (VLMs) and documents](#40-vision-language-models-vlms-and-documents) | [40.3 — Vision-specific limitations](#403-vision-specific-limitations) | 6 | [#1: Sharp Attention Is a Lie in VLMs (2026)](https://medium.com/%40loganmann_98349/sharp-attention-is-a-lie-what-actually-predicts-when-a-vision-language-model-is-right-8ea4b0abfa98) | [#2: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#3: Beyond the Embedding: How LLMs Learned to See (2026)](https://medium.com/data-science-collective/beyond-the-embedding-how-llms-learned-to-see-ba74dae187ee) |
| [Audio, speech, music, and spoken language models](#41-audio-speech-music-and-spoken-language-models) | [41.1 — Audio foundations](#411-audio-foundations) | 6 | [#1: Can a Language Model Hear? Technical Tour of Audio and Music Understanding (2026)](https://medium.com/%40aminfadaeinejad.edu/15-can-a-language-model-hear-a-technical-tour-of-audio-music-understanding-llms-826fdd8a13c6) | [#2: How Voice Models Work: From Whisper to Conversational AI (2026)](https://medium.com/%40adnanmasood/how-voice-models-work-from-whisper-to-conversational-ai-cb4b0a8ab20f) | [#3: Best Speech to Text APIs 2026 (2026)](https://medium.com/%40lukeocodes/best-speech-to-text-apis-july-2026-0fd1d024b4f7) |
| [Audio, speech, music, and spoken language models](#41-audio-speech-music-and-spoken-language-models) | [41.2 — Speech tasks and models](#412-speech-tasks-and-models) | 6 | [#1: How Voice Models Work: From Whisper to Conversational AI (2026)](https://medium.com/%40adnanmasood/how-voice-models-work-from-whisper-to-conversational-ai-cb4b0a8ab20f) | [#2: Your Voice Agent Transcribes the Wrong Person (2026)](https://medium.com/data-science-collective/your-voice-agent-transcribes-the-wrong-person-i-measured-it-40ada71f9a46) | [#3: Best Speech to Text APIs 2026 (2026)](https://medium.com/%40lukeocodes/best-speech-to-text-apis-july-2026-0fd1d024b4f7) |
| [Audio, speech, music, and spoken language models](#41-audio-speech-music-and-spoken-language-models) | [41.3 — Real-time voice systems](#413-real-time-voice-systems) | 6 | [#1: Building a Production AI Voice Agent: Architectures Patterns and Problems (2026)](https://medium.com/data-science-collective/building-a-production-ai-voice-agent-architecture-patterns-and-the-hard-problems-48c880870527) | [#2: The Four-Layer Voice Agent Latency Stack (2026)](https://medium.com/%40marcus.chen_88321/the-4-layer-voice-agent-latency-stack-traced-with-otel-spans-3a8e53894920) | [#3: Build a Real-Time Voice Agent with 1.3s Replies (2026)](https://medium.com/%40f.alberto.sg/how-i-built-a-cascade-real-time-voice-agent-that-replies-in-1-3-seconds-732d272fed7e) |
| [Video, real-time multimodal systems, and embodied agents](#42-video-real-time-multimodal-systems-and-embodied-agents) | [42.1 — Video representation](#421-video-representation) | 6 | [#1: Inside Qwen3-VL: Vision and Video Tokens (2026)](https://medium.com/%40hyunjicha397/inside-qwen3-vl-a-deep-dive-into-the-architecture-behind-qwens-vision-language-model-18117d27482f) | [#2: Robot Foundation Models: A Technical Survey (2026)](https://medium.com/%40adnanmasood/robot-foundation-models-a-complete-technical-survey-5bf9add22d1c) | [#3: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) |
| [Video, real-time multimodal systems, and embodied agents](#42-video-real-time-multimodal-systems-and-embodied-agents) | [42.2 — Real-time multimodal interaction](#422-real-time-multimodal-interaction) | 6 | [#1: Visualising Vision Language Models (2025)](https://medium.com/advanced-deep-learning/how-ai-sees-and-reads-visualising-vision-language-models-5903c0fab0ab) | [#2: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) | [#3: Robot Foundation Models: A Technical Survey (2026)](https://medium.com/%40adnanmasood/robot-foundation-models-a-complete-technical-survey-5bf9add22d1c) |
| [Video, real-time multimodal systems, and embodied agents](#42-video-real-time-multimodal-systems-and-embodied-agents) | [42.3 — Action and embodied language models](#423-action-and-embodied-language-models) | 6 | [#1: Robot Foundation Models: A Technical Survey (2026)](https://medium.com/%40adnanmasood/robot-foundation-models-a-complete-technical-survey-5bf9add22d1c) | [#2: What is a Vision Language Action Model? (2026)](https://vizuara.medium.com/what-exactly-is-a-vision-language-action-vla-model-08b689df3406) | [#3: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) |
| [Code language models and software-engineering agents](#43-code-language-models-and-software-engineering-agents) | [43.1 — Code modeling](#431-code-modeling) | 6 | [#1: Papers Explained: Code Llama and Fill-in-the-Middle (2023)](https://medium.com/dair-ai/papers-explained-62-code-llama-ee266bfa495f) | [#2: Code Generation and Repository-Level Benchmarks (2026)](https://medium.com/%40adnanmasood/code-generation-repository-level-software-engineering-benchmarks-a-field-guide-to-llm-benchmarks-330bc3015d80) | [#3: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) |
| [Code language models and software-engineering agents](#43-code-language-models-and-software-engineering-agents) | [43.2 — Code reasoning and verification](#432-code-reasoning-and-verification) | 6 | [#1: Code Generation and Repository-Level Benchmarks (2026)](https://medium.com/%40adnanmasood/code-generation-repository-level-software-engineering-benchmarks-a-field-guide-to-llm-benchmarks-330bc3015d80) | [#2: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#3: Think Your Coding Agent Is Good? Try Real-SWE (2026)](https://agentnativedev.medium.com/think-your-coding-agent-is-good-try-real-swe-0115294550ba) |
| [Code language models and software-engineering agents](#43-code-language-models-and-software-engineering-agents) | [43.3 — Software-engineering agents](#433-software-engineering-agents) | 6 | [#1: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) | [#2: Think Your Coding Agent Is Good? Try Real-SWE (2026)](https://agentnativedev.medium.com/think-your-coding-agent-is-good-try-real-swe-0115294550ba) | [#3: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) |
| [Domain-specific and multilingual LLMs](#44-domain-specific-and-multilingual-llms) | [44.1 — Domain adaptation](#441-domain-adaptation) | 6 | [#1: India-First LLMs: Sarvam and Param2 (2026)](https://medium.com/%40indiai/india-first-llms-on-indian-languages-sarvam-30b-and-param2-17b-6676b637f3ab) | [#2: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#3: Fine Tuning VaultGemma with Differential Privacy (2025)](https://medium.com/%40rubenszimbres/fine-tuning-vaultgemma-with-differential-privacy-using-a-colab-runtime-in-vscode-2a01d39d2821) |
| [Domain-specific and multilingual LLMs](#44-domain-specific-and-multilingual-llms) | [44.2 — Multilingual and cross-lingual learning](#442-multilingual-and-cross-lingual-learning) | 6 | [#1: India-First LLMs: Sarvam and Param2 (2026)](https://medium.com/%40indiai/india-first-llms-on-indian-languages-sarvam-30b-and-param2-17b-6676b637f3ab) | [#2: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#3: BPE vs WordPiece vs SentencePiece (2025)](https://medium.com/%40dhiyaadli/bpe-vs-wordpiece-vs-sentencepiece-a-beginner-friendly-guide-to-subword-tokenization-8047b39d82e0) |
| [Domain-specific and multilingual LLMs](#44-domain-specific-and-multilingual-llms) | [44.3 — Specialized model families](#443-specialized-model-families) | 6 | [#1: The Best Open Models Fine-Tuned for Specialized Industries (2026)](https://medium.com/aimonks/the-best-open-source-and-open-weight-fine-tuned-ai-models-for-different-industries-in-2026-40bdcef22037) | [#2: LexiMini: A Legal LLM for India From Scratch (2026)](https://medium.com/google-developer-experts/%EF%B8%8F-leximini-how-i-built-an-ai-legal-assistant-for-india-from-scratch-on-a-tpu-f8354e20cbc9) | [#3: Specialized Fine-Tuning and RAG Datasets in 2026 (2026)](https://odsc.medium.com/15-specialized-fine-tuning-rag-datasets-for-domain-specific-ai-in-2026-ea290dde0c79) |
| [Evaluation methodology and benchmark engineering](#45-evaluation-methodology-and-benchmark-engineering) | [45.1 — Offline evaluation basics](#451-offline-evaluation-basics) | 6 | [#1: LLM Benchmarks Field Guide (2026)](https://ananno.medium.com/series-llm-benchmarks-field-guide-14371fdd406b) | [#2: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) | [#3: LLM Benchmarks Simplified: MMLU to GPQA (2026)](https://medium.com/%40dibyajyoti_20397/llm-benchmarks-simplified-from-mmlu-to-gpqa-7e88b6a83c0c) |
| [Evaluation methodology and benchmark engineering](#45-evaluation-methodology-and-benchmark-engineering) | [45.2 — Capability benchmark families](#452-capability-benchmark-families) | 7 | [#1: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) | [#2: LLM Benchmarks Simplified: MMLU to GPQA (2026)](https://medium.com/%40dibyajyoti_20397/llm-benchmarks-simplified-from-mmlu-to-gpqa-7e88b6a83c0c) | [#3: LLM Benchmarks Field Guide (2026)](https://ananno.medium.com/series-llm-benchmarks-field-guide-14371fdd406b) |
| [Evaluation methodology and benchmark engineering](#45-evaluation-methodology-and-benchmark-engineering) | [45.3 — Specialized benchmarking](#453-specialized-benchmarking) | 6 | [#1: Code Generation and Repository-Level Benchmarks (2026)](https://medium.com/%40adnanmasood/code-generation-repository-level-software-engineering-benchmarks-a-field-guide-to-llm-benchmarks-330bc3015d80) | [#2: RAG Evaluation Metrics: Retrieval Generation E2E (2026)](https://medium.com/operations-research-bit/evaluation-metrics-for-rag-measure-retrieval-generation-and-end-to-end-quality-with-numbers-that-f80d3f14f889) | [#3: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) |
| [Evaluation methodology and benchmark engineering](#45-evaluation-methodology-and-benchmark-engineering) | [45.4 — Evaluation reliability](#454-evaluation-reliability) | 6 | [#1: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#2: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) | [#3: LLM Benchmarks Field Guide (2026)](https://ananno.medium.com/series-llm-benchmarks-field-guide-14371fdd406b) |
| [Evaluation methodology and benchmark engineering](#45-evaluation-methodology-and-benchmark-engineering) | [45.5 — Online and product evaluation](#455-online-and-product-evaluation) | 6 | [#1: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#2: RAG Evaluation Metrics: Retrieval Generation E2E (2026)](https://medium.com/operations-research-bit/evaluation-metrics-for-rag-measure-retrieval-generation-and-end-to-end-quality-with-numbers-that-f80d3f14f889) | [#3: LLMOps Observability Comparison (2026)](https://medium.com/%40kanerika/llmops-observability-langsmith-vs-arize-vs-langfuse-vs-w-b-f1baeabd1bbf) |
| [Factuality, uncertainty, calibration, and robustness](#46-factuality-uncertainty-calibration-and-robustness) | [46.1 — Hallucinations and factual errors](#461-hallucinations-and-factual-errors) | 6 | [#1: Sharp Attention Is a Lie in VLMs (2026)](https://medium.com/%40loganmann_98349/sharp-attention-is-a-lie-what-actually-predicts-when-a-vision-language-model-is-right-8ea4b0abfa98) | [#2: RAG Evaluation Metrics: Retrieval Generation E2E (2026)](https://medium.com/operations-research-bit/evaluation-metrics-for-rag-measure-retrieval-generation-and-end-to-end-quality-with-numbers-that-f80d3f14f889) | [#3: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) |
| [Factuality, uncertainty, calibration, and robustness](#46-factuality-uncertainty-calibration-and-robustness) | [46.2 — Uncertainty and calibration](#462-uncertainty-and-calibration) | 6 | [#1: Sharp Attention Is a Lie in VLMs (2026)](https://medium.com/%40loganmann_98349/sharp-attention-is-a-lie-what-actually-predicts-when-a-vision-language-model-is-right-8ea4b0abfa98) | [#2: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) | [#3: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) |
| [Factuality, uncertainty, calibration, and robustness](#46-factuality-uncertainty-calibration-and-robustness) | [46.3 — Robustness and stress testing](#463-robustness-and-stress-testing) | 6 | [#1: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#2: Sharp Attention Is a Lie in VLMs (2026)](https://medium.com/%40loganmann_98349/sharp-attention-is-a-lie-what-actually-predicts-when-a-vision-language-model-is-right-8ea4b0abfa98) | [#3: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) |
| [Interpretability, mechanistic analysis, and model editing](#47-interpretability-mechanistic-analysis-and-model-editing) | [47.1 — Black-box interpretability](#471-black-box-interpretability) | 6 | [#1: Mechanistic Interpretability Explained (2026)](https://medium.com/%40adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72) | [#2: Getting Started with Mechanistic Interpretability (2026)](https://medium.com/%40adnanmasood/getting-started-with-mechanistic-interpretability-part-0-why-mech-interp-and-why-now-30693e952064) | [#3: In Context Learning: Induction Head (2025)](https://medium.com/%40madhuriagarwal723/in-context-learning-induction-head-1279b36934fb) |
| [Interpretability, mechanistic analysis, and model editing](#47-interpretability-mechanistic-analysis-and-model-editing) | [47.2 — Mechanistic interpretability](#472-mechanistic-interpretability) | 6 | [#1: Sparse Autoencoders and Polysemanticity (2026)](https://medium.com/%40izzetcansorna/sparse-autoencoders-and-the-polysemanticity-problem-a-deep-dive-into-mechanistic-interpretability-71d3c3dc2b73) | [#2: Getting Started with Mechanistic Interpretability (2026)](https://medium.com/%40adnanmasood/getting-started-with-mechanistic-interpretability-part-0-why-mech-interp-and-why-now-30693e952064) | [#3: Mechanistic Interpretability Explained (2026)](https://medium.com/%40adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72) |
| [Interpretability, mechanistic analysis, and model editing](#47-interpretability-mechanistic-analysis-and-model-editing) | [47.3 — Model editing and steering](#473-model-editing-and-steering) | 6 | [#1: Mechanistic Interpretability Explained (2026)](https://medium.com/%40adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72) | [#2: Sparse Autoencoders and Polysemanticity (2026)](https://medium.com/%40izzetcansorna/sparse-autoencoders-and-the-polysemanticity-problem-a-deep-dive-into-mechanistic-interpretability-71d3c3dc2b73) | [#3: Building a Sparse Autoencoder from Scratch (2026)](https://medium.com/%40divyanshpandey0108/building-a-sparse-autoencoder-on-gpt-2-from-scratch-a-mechanistic-interpretability-investigation-2aa3f81e2e67) |
| [Alignment, model behavior, and responsible AI](#48-alignment-model-behavior-and-responsible-ai) | [48.1 — Alignment objectives](#481-alignment-objectives) | 6 | [#1: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) | [#2: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) | [#3: Mechanistic Interpretability Explained (2026)](https://medium.com/%40adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72) |
| [Alignment, model behavior, and responsible AI](#48-alignment-model-behavior-and-responsible-ai) | [48.2 — Safety post-training](#482-safety-post-training) | 6 | [#1: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) | [#2: Length Bias in Reward Models DPO GRPO (2026)](https://medium.com/%40sarathc225/why-does-rlhf-make-models-verbose-length-bias-in-reward-models-dpo-and-grpo-ac4a4c8c07d6) | [#3: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) |
| [Alignment, model behavior, and responsible AI](#48-alignment-model-behavior-and-responsible-ai) | [48.3 — Fairness and societal impacts](#483-fairness-and-societal-impacts) | 6 | [#1: When Fairness and Language Model Quality Conflict (2026)](https://medium.com/supportiv/part-3-the-ablation-when-fairness-and-language-model-quality-conflict-59f8f0834185) | [#2: LLMs as Judges: Measuring Bias and Hinting Effects (2026)](https://medium.com/google-developer-experts/llms-as-judges-measuring-bias-hinting-effects-and-tier-preferences-8096a9114433) | [#3: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) |
| [LLM security, prompt injection, and adversarial ML](#49-llm-security-prompt-injection-and-adversarial-ml) | [49.1 — Threat modeling](#491-threat-modeling) | 6 | [#1: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) | [#2: OWASP Top 10: Attack Surface (2026)](https://medium.com/%40derickjohnson/owasp-llm-top-10-part-1-when-the-model-becomes-the-attack-surface-2188a2a672fc) | [#3: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) |
| [LLM security, prompt injection, and adversarial ML](#49-llm-security-prompt-injection-and-adversarial-ml) | [49.2 — Attack classes](#492-attack-classes) | 8 | [#1: OWASP Top 10: Attack Surface (2026)](https://medium.com/%40derickjohnson/owasp-llm-top-10-part-1-when-the-model-becomes-the-attack-surface-2188a2a672fc) | [#2: LLM01 Prompt Injection (2026)](https://erdemstar.medium.com/llm01-prompt-injection-c3b77be7157c) | [#3: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) |
| [LLM security, prompt injection, and adversarial ML](#49-llm-security-prompt-injection-and-adversarial-ml) | [49.3 — Defenses and secure architecture](#493-defenses-and-secure-architecture) | 7 | [#1: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) | [#2: LLM01 Prompt Injection (2026)](https://erdemstar.medium.com/llm01-prompt-injection-c3b77be7157c) | [#3: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) |
| [LLM security, prompt injection, and adversarial ML](#49-llm-security-prompt-injection-and-adversarial-ml) | [49.4 — Security standards and research](#494-security-standards-and-research) | 6 | [#1: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) | [#2: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) | [#3: OWASP Top 10: Attack Surface (2026)](https://medium.com/%40derickjohnson/owasp-llm-top-10-part-1-when-the-model-becomes-the-attack-surface-2188a2a672fc) |
| [Privacy, intellectual property, governance, and compliance](#50-privacy-intellectual-property-governance-and-compliance) | [50.1 — Privacy-preserving learning](#501-privacy-preserving-learning) | 6 | [#1: Differential Privacy and DP-SGD in Language Models (2026)](https://medium.com/%40izzetcansorna/differential-privacy-and-dp-sgd-mathematically-bounding-what-a-model-can-leak-about-its-training-4fe414d294a9) | [#2: Federated Fine-Tuning in LLMs and Privacy (2026)](https://medium.com/%40mohantaastha/federated-fine-tuning-in-llms-why-the-future-of-ai-privacy-starts-here-a0de34f8c613) | [#3: Fine Tuning VaultGemma with Differential Privacy (2025)](https://medium.com/%40rubenszimbres/fine-tuning-vaultgemma-with-differential-privacy-using-a-colab-runtime-in-vscode-2a01d39d2821) |
| [Privacy, intellectual property, governance, and compliance](#50-privacy-intellectual-property-governance-and-compliance) | [50.2 — Intellectual property and provenance](#502-intellectual-property-and-provenance) | 6 | [#1: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#2: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) | [#3: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) |
| [Privacy, intellectual property, governance, and compliance](#50-privacy-intellectual-property-governance-and-compliance) | [50.3 — Governance and operational controls](#503-governance-and-operational-controls) | 6 | [#1: AI Security Reading List: OWASP MITRE NIST AI RMF EU AI Act (2026)](https://medium.com/%40techalisa/ai-security-reading-list-2026-owasp-top-10-llm-agentic-apps-mitre-atlas-nist-ai-rmf-eu-ai-act-5bc484f12608) | [#2: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) | [#3: Fine Tuning VaultGemma with Differential Privacy (2025)](https://medium.com/%40rubenszimbres/fine-tuning-vaultgemma-with-differential-privacy-using-a-colab-runtime-in-vscode-2a01d39d2821) |
| [Synthetic training loops, self-improvement, and knowledge distillation](#51-synthetic-training-loops-self-improvement-and-knowledge-distillation) | [51.1 — Synthetic instruction and reasoning data](#511-synthetic-instruction-and-reasoning-data) | 6 | [#1: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#2: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#3: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) |
| [Synthetic training loops, self-improvement, and knowledge distillation](#51-synthetic-training-loops-self-improvement-and-knowledge-distillation) | [51.2 — Self-improvement strategies](#512-self-improvement-strategies) | 6 | [#1: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) |
| [Synthetic training loops, self-improvement, and knowledge distillation](#51-synthetic-training-loops-self-improvement-and-knowledge-distillation) | [51.3 — Distillation and transfer mechanics](#513-distillation-and-transfer-mechanics) | 6 | [#1: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) |
| [LLMOps, observability, testing, and production lifecycle](#52-llmops-observability-testing-and-production-lifecycle) | [52.1 — Experiment management](#521-experiment-management) | 6 | [#1: LLMOps Stack Nobody Tells You About (2026)](https://medium.com/%40Manjunath-Hanmantgad/the-llmops-stack-nobody-tells-you-about-53b07317dff8) | [#2: Top LLMOps Tools (2026)](https://medium.com/devops-ai-decoded/top-10-llmops-tools-for-managing-ai-models-in-production-d3c18f70b328) | [#3: LLMOps Observability Comparison (2026)](https://medium.com/%40kanerika/llmops-observability-langsmith-vs-arize-vs-langfuse-vs-w-b-f1baeabd1bbf) |
| [LLMOps, observability, testing, and production lifecycle](#52-llmops-observability-testing-and-production-lifecycle) | [52.2 — Inference and agent observability](#522-inference-and-agent-observability) | 6 | [#1: LLM Observability: Traces Tokens Costs (2026)](https://medium.com/%40khwajakhan/llm-observability-traces-tokens-and-cost-on-a-frozen-agentic-app-e0a3b9e2c790) | [#2: LLMOps Observability Comparison (2026)](https://medium.com/%40kanerika/llmops-observability-langsmith-vs-arize-vs-langfuse-vs-w-b-f1baeabd1bbf) | [#3: Top LLMOps Tools (2026)](https://medium.com/devops-ai-decoded/top-10-llmops-tools-for-managing-ai-models-in-production-d3c18f70b328) |
| [LLMOps, observability, testing, and production lifecycle](#52-llmops-observability-testing-and-production-lifecycle) | [52.3 — Reliability operations](#523-reliability-operations) | 6 | [#1: LLMOps Observability Comparison (2026)](https://medium.com/%40kanerika/llmops-observability-langsmith-vs-arize-vs-langfuse-vs-w-b-f1baeabd1bbf) | [#2: LLM Observability: Traces Tokens Costs (2026)](https://medium.com/%40khwajakhan/llm-observability-traces-tokens-and-cost-on-a-frozen-agentic-app-e0a3b9e2c790) | [#3: LLMOps Stack Nobody Tells You About (2026)](https://medium.com/%40Manjunath-Hanmantgad/the-llmops-stack-nobody-tells-you-about-53b07317dff8) |
| [Cost, latency, architecture, and product optimization](#53-cost-latency-architecture-and-product-optimization) | [53.1 — Token economics](#531-token-economics) | 6 | [#1: Token Cost of Routing Agent Intents (2026)](https://medium.com/google-cloud/routing-160-telco-intents-in-gecx-can-we-use-systemone-thinking-models-6f4eaf3dc0cf) | [#2: LLM Observability: Traces Tokens Costs (2026)](https://medium.com/%40khwajakhan/llm-observability-traces-tokens-and-cost-on-a-frozen-agentic-app-e0a3b9e2c790) | [#3: LLM Inference Stack in 2026 (2026)](https://medium.com/%40charan.panthangi/the-llm-inference-stack-in-2026-vllm-sglang-tensorrt-llm-semantic-routing-and-the-combination-d9df1a16f93f) |
| [Cost, latency, architecture, and product optimization](#53-cost-latency-architecture-and-product-optimization) | [53.2 — System architecture choices](#532-system-architecture-choices) | 6 | [#1: LLM Inference Stack in 2026 (2026)](https://medium.com/%40charan.panthangi/the-llm-inference-stack-in-2026-vllm-sglang-tensorrt-llm-semantic-routing-and-the-combination-d9df1a16f93f) | [#2: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) | [#3: Token Cost of Routing Agent Intents (2026)](https://medium.com/google-cloud/routing-160-telco-intents-in-gecx-can-we-use-systemone-thinking-models-6f4eaf3dc0cf) |
| [Cost, latency, architecture, and product optimization](#53-cost-latency-architecture-and-product-optimization) | [53.3 — Performance engineering](#533-performance-engineering) | 6 | [#1: What Really Limits LLM Inference Performance (2026)](https://medium.com/data-science-collective/what-really-limits-llm-inference-performance-3d04ae41fe3e) | [#2: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Cost, latency, architecture, and product optimization](#53-cost-latency-architecture-and-product-optimization) | [53.4 — Product and UX design](#534-product-and-ux-design) | 6 | [#1: Token Cost of Routing Agent Intents (2026)](https://medium.com/google-cloud/routing-160-telco-intents-in-gecx-can-we-use-systemone-thinking-models-6f4eaf3dc0cf) | [#2: Context Engineering: Four Operations (2026)](https://medium.com/oracledevs/what-is-context-engineering-the-four-operations-that-decide-whether-your-agent-survives-production-e803bb8ddf17) | [#3: LLM Observability: Traces Tokens Costs (2026)](https://medium.com/%40khwajakhan/llm-observability-traces-tokens-and-cost-on-a-frozen-agentic-app-e0a3b9e2c790) |
| [Research frontiers and unresolved questions](#54-research-frontiers-and-unresolved-questions) | [54.1 — Capability and scaling frontiers](#541-capability-and-scaling-frontiers) | 6 | [#1: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) | [#2: Why Transformers Scale: The Math of Scaling Laws (2026)](https://medium.com/%40ppp.mishra124/why-transformers-scale-the-math-of-scaling-laws-02c045509186) | [#3: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) |
| [Research frontiers and unresolved questions](#54-research-frontiers-and-unresolved-questions) | [54.2 — Architecture frontiers](#542-architecture-frontiers) | 6 | [#1: Beyond Attention: Mamba (2025)](https://medium.com/correll-lab/beyond-attention-mamba-as-a-replacement-for-transformers-5483b6e23a6e) | [#2: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) | [#3: Diffusion Language Models: Throughput and Benchmark Tradeoffs (2026)](https://medium.com/fandhe/diffusion-language-models-1-479-tok-s-behind-on-gpqa-ab47fe9a2544) |
| [Research frontiers and unresolved questions](#54-research-frontiers-and-unresolved-questions) | [54.3 — Learning and alignment frontiers](#543-learning-and-alignment-frontiers) | 6 | [#1: MoE: Routing as Active Research (2026)](https://medium.com/models-to-systems/mixture-of-experts-why-routing-is-the-active-research-surface-explained-for-everyone-e4f9f5e8c07e) | [#2: GRPO vs PPO vs DAPO for Reasoning Models (2026)](https://medium.com/%40sarathc225/grpo-vs-ppo-vs-dapo-which-rl-algorithm-should-you-use-to-train-a-reasoning-model-41dae134e141) | [#3: Mechanistic Interpretability Explained (2026)](https://medium.com/%40adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72) |
| [Research frontiers and unresolved questions](#54-research-frontiers-and-unresolved-questions) | [54.4 — Research methodology](#544-research-methodology) | 6 | [#1: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#2: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#3: Mechanistic Interpretability Explained (2026)](https://medium.com/%40adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72) |
| [Hands-on implementations and capstone projects](#55-hands-on-implementations-and-capstone-projects) | [55.1 — From-scratch components](#551-from-scratch-components) | 6 | [#1: Byte Pair Encoding from Scratch (2026)](https://medium.com/%40dakshrathi/byte-pair-encoding-bpe-from-data-compression-to-gpt-2-tokenization-44e35be2fd58) | [#2: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#3: Kernel Case Study: Flash Attention (2025)](https://arunjitha.medium.com/kernel-case-study-flash-attention-5d63a3875c2d) |
| [Hands-on implementations and capstone projects](#55-hands-on-implementations-and-capstone-projects) | [55.2 — Training and post-training projects](#552-training-and-post-training-projects) | 6 | [#1: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#2: Implementing DPO from Scratch (2026)](https://medium.com/%40brayannjoroge259/implementing-direct-preference-optimization-dpo-149360bd2e9b) | [#3: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) |
| [Hands-on implementations and capstone projects](#55-hands-on-implementations-and-capstone-projects) | [55.3 — Inference and serving projects](#553-inference-and-serving-projects) | 7 | [#1: Kernel Case Study: Flash Attention (2025)](https://arunjitha.medium.com/kernel-case-study-flash-attention-5d63a3875c2d) | [#2: LLM Inference on a GPU from Scratch (2026)](https://medium.com/%40ar.taneja/llm-inference-on-a-gpu-explained-from-scratch-b8a478924687) | [#3: LLM Inference vLLM vs SGLang vs TensorRT-LLM L40S (2026)](https://medium.com/%40wojdylak.michal/llm-inference-benchmarks-vllm-vs-sglang-vs-tensorrt-llm-on-a-single-l40s-8976d46a7ef3) |
| [Hands-on implementations and capstone projects](#55-hands-on-implementations-and-capstone-projects) | [55.4 — RAG and agent projects](#554-rag-and-agent-projects) | 6 | [#1: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) | [#2: Building an Agent with Google ADK A2A and MCP (2026)](https://medium.com/google-cloud/building-a-financial-ai-agent-with-google-adk-a2a-and-mcp-084f5937f1e8) | [#3: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) |
| [Hands-on implementations and capstone projects](#55-hands-on-implementations-and-capstone-projects) | [55.5 — Research replication and security projects](#555-research-replication-and-security-projects) | 6 | [#1: Building a Sparse Autoencoder from Scratch (2026)](https://medium.com/%40divyanshpandey0108/building-a-sparse-autoencoder-on-gpt-2-from-scratch-a-mechanistic-interpretability-investigation-2aa3f81e2e67) | [#2: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#3: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) |
| [Developer tools, libraries, ecosystems, and workflows](#56-developer-tools-libraries-ecosystems-and-workflows) | [56.1 — Model development libraries](#561-model-development-libraries) | 6 | [#1: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#2: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#3: LoRA QLoRA and DoRA Parameter Efficient Fine Tuning (2026)](https://medium.com/%40izzetcansorna/parameter-efficient-fine-tuning-how-lora-qlora-and-dora-made-large-models-adaptable-d9835411f1c2) |
| [Developer tools, libraries, ecosystems, and workflows](#56-developer-tools-libraries-ecosystems-and-workflows) | [56.2 — Model inference and optimization libraries](#562-model-inference-and-optimization-libraries) | 6 | [#1: LLM Inference Stack in 2026 (2026)](https://medium.com/%40charan.panthangi/the-llm-inference-stack-in-2026-vllm-sglang-tensorrt-llm-semantic-routing-and-the-combination-d9df1a16f93f) | [#2: vLLM Explained (2026)](https://medium.com/mlworks/vllm-explained-how-it-makes-llm-inference-faster-044da99542cf) | [#3: How LLM Serving Gets Fast (2026)](https://medium.com/data-science-collective/how-llm-serving-gets-fast-flashattention-pagedattention-continuous-batching-speculative-cd980096daf2) |
| [Developer tools, libraries, ecosystems, and workflows](#56-developer-tools-libraries-ecosystems-and-workflows) | [56.3 — Retrieval, orchestration, and evaluation tools](#563-retrieval-orchestration-and-evaluation-tools) | 6 | [#1: Top LLMOps Tools (2026)](https://medium.com/devops-ai-decoded/top-10-llmops-tools-for-managing-ai-models-in-production-d3c18f70b328) | [#2: Four Enterprise RAG Architectures Compared (2026)](https://medium.com/%40Chioma_Kamalu/i-tested-four-enterprise-rag-architectures-was-the-most-complex-one-worth-it-c33fe82a54ca) | [#3: Agent Memory Frameworks: Mem0 Zep Letta Cognee (2026)](https://medium.com/data-science-collective/agent-memory-frameworks-showdown-cognee-vs-mem0-vs-zep-vs-letta-0f439b56f282) |
| [Developer tools, libraries, ecosystems, and workflows](#56-developer-tools-libraries-ecosystems-and-workflows) | [56.4 — Scientific reading and implementation workflow](#564-scientific-reading-and-implementation-workflow) | 6 | [#1: The CS336 Resource List for LLM Training Inference Evaluation (2026)](https://medium.com/%40punitvara/the-ultimate-cs336-resource-list-for-llms-training-inference-and-evaluation-3dfbd0f88b29) | [#2: LLM Benchmarks Field Guide (2026)](https://ananno.medium.com/series-llm-benchmarks-field-guide-14371fdd406b) | [#3: Built a Cloud Coding Agent Tested on SWE-bench (2026)](https://medium.com/%40thimayarohit/how-i-built-a-devin-style-cloud-coding-agent-and-tested-it-on-swe-bench-a1581cef47fa) |
| [In-context learning, meta-learning, and capability theory](#57-in-context-learning-meta-learning-and-capability-theory) | [57.1 — In-context learning behavior](#571-in-context-learning-behavior) | 6 | [#1: In Context Learning: Induction Head (2025)](https://medium.com/%40madhuriagarwal723/in-context-learning-induction-head-1279b36934fb) | [#2: Getting Started with Mechanistic Interpretability (2026)](https://medium.com/%40adnanmasood/getting-started-with-mechanistic-interpretability-part-0-why-mech-interp-and-why-now-30693e952064) | [#3: Prompt Engineering 2026: Introduction (2026)](https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433) |
| [In-context learning, meta-learning, and capability theory](#57-in-context-learning-meta-learning-and-capability-theory) | [57.2 — Emergence and capability analysis](#572-emergence-and-capability-analysis) | 6 | [#1: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) | [#2: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) | [#3: In Context Learning: Induction Head (2025)](https://medium.com/%40madhuriagarwal723/in-context-learning-induction-head-1279b36934fb) |
| [In-context learning, meta-learning, and capability theory](#57-in-context-learning-meta-learning-and-capability-theory) | [57.3 — Inference-time adaptation](#573-inference-time-adaptation) | 6 | [#1: In Context Learning: Induction Head (2025)](https://medium.com/%40madhuriagarwal723/in-context-learning-induction-head-1279b36934fb) | [#2: PPO and GRPO: Improving a Policy (2026)](https://medium.com/%40can.demir/ppo-and-grpo-why-improving-a-policy-is-mostly-about-not-ruining-it-0d41386b3515) | [#3: Prompt Engineering 2026: Introduction (2026)](https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433) |
| [Diffusion and non-autoregressive language models](#58-diffusion-and-non-autoregressive-language-models) | [58.1 — Alternative generative modeling paradigms](#581-alternative-generative-modeling-paradigms) | 6 | [#1: What Exactly is a Diffusion Language Model? (2026)](https://vizuara.medium.com/what-exactly-is-a-diffusion-language-model-6015cc06de2d) | [#2: Diffusion Language Models: Throughput and Benchmark Tradeoffs (2026)](https://medium.com/fandhe/diffusion-language-models-1-479-tok-s-behind-on-gpqa-ab47fe9a2544) | [#3: Mamba Hyena and RWKV Beyond Attention (2025)](https://medium.com/%40cenghanbayram35/attention-isnt-all-you-need-beating-the-o-n%C2%B2-wall-with-mamba-hyena-and-rwkv-602d9b1466f7) |
| [Diffusion and non-autoregressive language models](#58-diffusion-and-non-autoregressive-language-models) | [58.2 — Training and generation](#582-training-and-generation) | 6 | [#1: What Exactly is a Diffusion Language Model? (2026)](https://vizuara.medium.com/what-exactly-is-a-diffusion-language-model-6015cc06de2d) | [#2: Diffusion Language Models: Throughput and Benchmark Tradeoffs (2026)](https://medium.com/fandhe/diffusion-language-models-1-479-tok-s-behind-on-gpqa-ab47fe9a2544) | [#3: Mercury 3 and the Rise of Diffusion Language Models (2026)](https://medium.com/%40peeyushkmisra_79926/this-ai-doesnt-write-left-to-right-mercury-3-and-the-rise-of-diffusion-language-models-682c4245c964) |
| [Diffusion and non-autoregressive language models](#58-diffusion-and-non-autoregressive-language-models) | [58.3 — Models and research questions](#583-models-and-research-questions) | 6 | [#1: Metastate: Giving Diffusion Language Models Working Memory (2026)](https://medium.com/models-to-systems/metastate-giving-diffusion-language-models-a-working-memory-5fe59cd79284) | [#2: Mercury 3 and the Rise of Diffusion Language Models (2026)](https://medium.com/%40peeyushkmisra_79926/this-ai-doesnt-write-left-to-right-mercury-3-and-the-rise-of-diffusion-language-models-682c4245c964) | [#3: Diffusion Language Models: Throughput and Benchmark Tradeoffs (2026)](https://medium.com/fandhe/diffusion-language-models-1-479-tok-s-behind-on-gpqa-ab47fe9a2544) |
| [Midtraining, annealing, and specialization recipes](#59-midtraining-annealing-and-specialization-recipes) | [59.1 — Training-stage distinctions](#591-training-stage-distinctions) | 6 | [#1: Pretraining vs Post-training phases (2025)](https://medium.com/%40adnanmasood/an-ontological-examination-of-pre-training-and-post-training-phases-in-transformer-based-language-7c7fb786d805) | [#2: Modern Fine Tuning Strategies from SFT to GRPO (2026)](https://maciejzalwert.medium.com/modern-fine-tuning-strategies-for-large-language-models-from-sft-to-grpo-with-explanation-and-f00b54ce2133) | [#3: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) |
| [Midtraining, annealing, and specialization recipes](#59-midtraining-annealing-and-specialization-recipes) | [59.2 — Data-mixture and optimization schedules](#592-data-mixture-and-optimization-schedules) | 6 | [#1: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#2: What Large Language Models Are Trained On (2026)](https://dataman-ai.medium.com/what-large-language-models-are-trained-on-c57901349b57) | [#3: Scaling Laws: Why Bigger Reliably Means Better (2026)](https://medium.com/%40charan.panthangi/scaling-laws-why-bigger-reliably-means-better-75dcc5b114a3) |
| [Midtraining, annealing, and specialization recipes](#59-midtraining-annealing-and-specialization-recipes) | [59.3 — Evaluation of staged training](#593-evaluation-of-staged-training) | 6 | [#1: Training the Tiny Transformer Properly (2025)](https://medium.com/%40gourish.deshpande/training-the-tiny-transformer-properly-7dfafb712f9a) | [#2: Higher Reward Not Necessarily Better Answers (2026)](https://medium.com/%40shahnawaz43778/when-an-ai-model-gets-a-higher-reward-score-is-it-actually-getting-better-68672d39db25) | [#3: General Knowledge and Reasoning Benchmarks Field Guide (2026)](https://medium.com/%40adnanmasood/general-knowledge-and-reasoning-a-field-guide-to-llm-benchmarks-b9ec02dea520) |
| [Computer-use, browser, and GUI agents](#60-computer-use-browser-and-gui-agents) | [60.1 — Perception and action interfaces](#601-perception-and-action-interfaces) | 6 | [#1: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) | [#2: The GUI Just Got a Second User (2026)](https://medium.com/postmcp-ai/the-gui-isnt-dying-it-just-got-a-second-user-and-your-site-is-failing-it-6b22dbe5d014) | [#3: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) |
| [Computer-use, browser, and GUI agents](#60-computer-use-browser-and-gui-agents) | [60.2 — Reliability and evaluation](#602-reliability-and-evaluation) | 6 | [#1: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) | [#2: How to Build an Agent Eval You Can Trust (2026)](https://medium.com/data-science-collective/how-to-build-an-agent-eval-you-can-trust-b306940b02f2) | [#3: The GUI Just Got a Second User (2026)](https://medium.com/postmcp-ai/the-gui-isnt-dying-it-just-got-a-second-user-and-your-site-is-failing-it-6b22dbe5d014) |
| [Computer-use, browser, and GUI agents](#60-computer-use-browser-and-gui-agents) | [60.3 — Security and production architecture](#603-security-and-production-architecture) | 6 | [#1: The State of Computer Use Agents (2026)](https://medium.com/%40adnanmasood/the-hardest-easy-problem-in-ai-the-state-of-computer-use-agents-a7e3aea7fa3a) | [#2: OWASP Top 10 for LLM Applications 2026 (2026)](https://medium.com/%40Rakeshjoshi7/owasp-top-10-for-llm-applications-the-complete-2026-guide-c4b5dd95575a) | [#3: AI Agent Tool Calling: MCP Function Calling A2A (2026)](https://medium.com/ai-agent-engineering/what-is-ai-agent-tool-calling-84e17decfe14) |
## C. Complete hierarchical checklist

Every checklist line is a separate learning concept; the subtopic heading is the natural unit for attaching one high-quality article or paper.

## 01. LLM landscape, concepts, and lifecycle
### 01.1 Definitions and model taxonomy
- [ ] Language models versus large language models versus foundation models
- [ ] Base, pretrained, instruct, chat, reasoning, tool-use, and agentic models
- [ ] Encoder-only, decoder-only, and encoder–decoder architectures
- [ ] Open-weight versus open-source versus proprietary API models
- [ ] Dense, mixture-of-experts, recurrent, hybrid, and multimodal models
- [ ] General-purpose, domain-specialized, small, on-device, and frontier models
- [ ] Parameters, active parameters, tokens, context window, and modalities
- [ ] Training compute, inference compute, latency, throughput, and quality
### 01.2 End-to-end lifecycle
- [ ] Raw data collection and licensing
- [ ] Data cleaning, deduplication, tokenization, and mixture design
- [ ] Architecture design and compute budgeting
- [ ] Pretraining and continued pretraining
- [ ] Supervised fine-tuning and instruction tuning
- [ ] Preference optimization and reinforcement learning
- [ ] Model evaluation, red-teaming, and release
- [ ] Deployment, monitoring, adaptation, and retirement
### 01.3 Research and industry landscape
- [ ] Landmark model families and their architectural choices
- [ ] Model cards, technical reports, and benchmark caveats
- [ ] Open-weight ecosystems and model hubs
- [ ] Small language models versus frontier-scale models
- [ ] Training-time versus test-time scaling
- [ ] Model capabilities versus system capabilities
- [ ] Generalization, memorization, emergence, and limitations

## 02. Mathematical foundations for LLMs
### 02.1 Linear algebra and tensors
- [ ] Vectors, matrices, tensors, shapes, broadcasting, and Einstein notation
- [ ] Matrix multiplication, batched matmul, transpose, and contractions
- [ ] Dot product, cosine similarity, norms, and normalization
- [ ] Eigenvalues, eigenvectors, SVD, matrix rank, and low-rank approximation
- [ ] Orthogonality, projections, subspaces, and condition number
- [ ] Jacobians, Hessians, and vector–Jacobian products
- [ ] Tensor layouts, strides, contiguity, and memory views
### 02.2 Probability and information theory
- [ ] Conditional, joint, and marginal distributions
- [ ] Bayes' theorem, likelihood, and maximum likelihood estimation
- [ ] Categorical distributions, sampling, and Monte Carlo estimates
- [ ] Entropy, cross-entropy, KL divergence, and Jensen–Shannon divergence
- [ ] Mutual information, perplexity, and bits per token/byte
- [ ] Calibration, uncertainty, expected values, and variance
- [ ] Importance sampling, rejection sampling, and distribution shift
### 02.3 Calculus and numerical methods
- [ ] Chain rule, automatic differentiation, backpropagation, and computation graphs
- [ ] Gradients of softmax, cross-entropy, and layer normalization
- [ ] Log-sum-exp trick and stable softmax
- [ ] Gradient clipping and exploding/vanishing gradients
- [ ] Floating-point rounding, underflow, overflow, and loss scaling
- [ ] Numerical stability, reduction errors, and reproducibility
### 02.4 Optimization and scaling mathematics
- [ ] SGD, momentum, Adam, AdamW, and adaptive optimizers
- [ ] Learning-rate schedules, warmup, and cosine decay
- [ ] Weight decay versus L2 regularization
- [ ] Bias–variance, overfitting, generalization, and regularization
- [ ] Gradient noise scale, batch size, and effective batch size
- [ ] FLOPs, memory complexity, bandwidth, and arithmetic intensity

## 03. Machine-learning and deep-learning prerequisites
### 03.1 Core learning concepts
- [ ] Supervised, self-supervised, unsupervised, and reinforcement learning
- [ ] Training/validation/test split, leakage, and cross-validation
- [ ] Empirical risk, surrogate losses, and generalization error
- [ ] Distribution shift, out-of-distribution detection, and robustness
- [ ] Feature learning versus manually engineered features
- [ ] Representation learning and transfer learning
### 03.2 Neural-network foundations
- [ ] MLPs, nonlinear activations, and universal approximation
- [ ] Residual networks and skip connections
- [ ] Layer normalization, RMS normalization, and batch normalization
- [ ] Initialization, parameter sharing, and weight tying
- [ ] Dropout, stochastic depth, and other regularizers
- [ ] Autograd debugging and gradient checks
### 03.3 Learning objectives and transfer
- [ ] Classification, ranking, contrastive, and generative objectives
- [ ] Contrastive representation learning and negative sampling
- [ ] Knowledge transfer, multitask learning, and curriculum learning
- [ ] Data augmentation and invariance
- [ ] Domain adaptation and catastrophic forgetting
- [ ] Calibration and uncertainty-aware decisions

## 04. NLP and language-model evolution
### 04.1 Language and classical NLP
- [ ] Morphology, syntax, semantics, pragmatics, and discourse
- [ ] Language ambiguity, coreference, and compositionality
- [ ] Unicode, normalization, multilingual scripts, and text processing
- [ ] N-gram language models, smoothing, and backoff
- [ ] Bag of words, TF–IDF, and traditional sparse retrieval
- [ ] Word2Vec, CBOW, skip-gram, GloVe, and fastText
### 04.2 Sequence modeling before transformers
- [ ] Feed-forward neural language models
- [ ] RNN, LSTM, and GRU sequence models
- [ ] Teacher forcing and exposure bias
- [ ] Encoder–decoder sequence-to-sequence learning
- [ ] Additive and multiplicative attention
- [ ] Beam search in classical seq2seq systems
### 04.3 Foundation-model history
- [ ] ELMo, ULMFiT, and contextual embeddings
- [ ] Transformer, BERT, GPT, T5, and BART paradigms
- [ ] Masked, causal, prefix, and span-corruption objectives
- [ ] Instruction-tuned and chat-oriented models
- [ ] Scaling of language models and multimodal extension

## 05. Pretraining corpora, sources, and dataset design
### 05.1 Data sources and composition
- [ ] Web crawls and Common Crawl-style corpora
- [ ] Books, encyclopedias, academic papers, and educational text
- [ ] Source code, documentation, repositories, and issue trackers
- [ ] Question–answer, dialog, instructional, and tool-use traces
- [ ] Mathematics, proofs, equations, and structured reasoning corpora
- [ ] Multilingual and low-resource language corpora
- [ ] Multimodal text–image–audio–video paired data
### 05.2 Dataset provenance and governance
- [ ] Licenses, terms, consent, and provenance metadata
- [ ] Personally identifiable information and sensitive data
- [ ] Copyrighted content and opt-out handling
- [ ] Data retention, deletion, and audit logs
- [ ] Contamination risk and benchmark overlap
- [ ] Geographic, linguistic, temporal, and demographic coverage
### 05.3 Mixture construction
- [ ] Dataset sampling weights and source balancing
- [ ] Temperature sampling and domain reweighting
- [ ] Data quality versus data quantity
- [ ] Repeated-token exposure and epoch accounting
- [ ] Data curriculum, staged mixtures, and annealing
- [ ] General-domain versus specialist data trade-offs

## 06. Data processing, quality filtering, and synthesis
### 06.1 Extraction and normalization
- [ ] HTML parsing, boilerplate removal, and document segmentation
- [ ] PDF extraction, tables, equations, and layout-aware parsing
- [ ] Unicode normalization, whitespace, and text encoding
- [ ] Language identification and script detection
- [ ] Line, paragraph, document, and conversation boundaries
- [ ] Broken-text, encoding-error, and malformed-markup detection
### 06.2 Deduplication and contamination
- [ ] Exact hashes, near-duplicate detection, and MinHash/LSH
- [ ] Semantic deduplication and embedding-based clustering
- [ ] Repetition and template spam detection
- [ ] Train–validation–test overlap detection
- [ ] Benchmark contamination and decontamination
- [ ] Time-aware splits and leakage diagnostics
### 06.3 Filtering and quality estimation
- [ ] Heuristic, classifier-based, and LLM-based quality filters
- [ ] Toxicity, unsafe content, profanity, and sensitive-data screening
- [ ] Educational-value and reasoning-quality scoring
- [ ] Code compilability, unit tests, and license filtering
- [ ] Multilingual quality scoring and language balance
- [ ] Quality–diversity trade-offs, coverage, and bias
### 06.4 Synthetic data and augmentation
- [ ] Self-instruct and instruction generation
- [ ] Paraphrasing, translation, back-translation, and perturbations
- [ ] Synthetic chain-of-thought and solution traces
- [ ] Verifier-based filtering and answer checking
- [ ] Self-play, simulation, and adversarial data generation
- [ ] Model collapse, synthetic-data feedback loops, and diversity controls

## 07. Tokenization and text representation
### 07.1 Tokenizer algorithms
- [ ] Character, word, subword, byte, and byte-level tokenization
- [ ] Byte Pair Encoding (BPE) and byte-level BPE
- [ ] WordPiece and Unigram language-model tokenization
- [ ] SentencePiece and whitespace-agnostic processing
- [ ] tiktoken-style vocabulary design and byte fallback
- [ ] Morphology-aware and multilingual tokenizer design
### 07.2 Vocabulary and token semantics
- [ ] Vocabulary size, token frequency, and fertility
- [ ] Special tokens: BOS, EOS, PAD, UNK, MASK, SEP
- [ ] Chat delimiters, role tokens, tool-call tokens, and turn endings
- [ ] FIM/infill tokens and multimodal sentinel tokens
- [ ] Added tokens, token collisions, and reserved IDs
- [ ] Whitespace, capitalization, numerals, emojis, and Unicode edge cases
### 07.3 Tokenization engineering
- [ ] Tokenizer training, normalization, pretokenization, and decoding
- [ ] Offsets, token-to-character alignment, and spans
- [ ] Padding, truncation, packing, and padding side
- [ ] Attention masks, loss masks, and shifted labels
- [ ] Tokenizer migration, embedding resize, and compatibility
- [ ] Token counting, API costs, and tokenizer attack surface

## 08. Embeddings and representation geometry
### 08.1 Input and output representations
- [ ] Token embedding lookup and learned embedding matrices
- [ ] Weight tying between embeddings and LM head
- [ ] Embedding scaling and initialization
- [ ] Hidden states, layerwise representations, and anisotropy
- [ ] Contextual versus static embeddings
- [ ] Output logits, vocabulary projection, and logit lens
### 08.2 Sentence and document embeddings
- [ ] Mean, CLS, last-token, and weighted pooling
- [ ] Bi-encoders and dual-encoder training
- [ ] Contrastive losses: InfoNCE, triplet, and multiple negatives
- [ ] Embedding normalization and similarity functions
- [ ] Instruction-aware and query/document asymmetric embeddings
- [ ] Multilingual and multimodal embedding spaces
### 08.3 Representation analysis and retrieval
- [ ] Cosine, dot product, and Euclidean distance
- [ ] Nearest-neighbor search and approximate nearest neighbors
- [ ] Embedding dimensions, truncation, and Matryoshka representations
- [ ] Embedding drift, domain shift, and recalibration
- [ ] Embedding evaluation (retrieval, classification, clustering)
- [ ] Semantic similarity versus relevance versus factual entailment

## 09. Transformer architecture fundamentals
### 09.1 Transformer computation graph
- [ ] Encoder block versus decoder block
- [ ] Input embeddings, positional information, and residual stream
- [ ] Self-attention, cross-attention, and feed-forward sublayers
- [ ] Pre-norm versus post-norm and normalization order
- [ ] Residual connections and layer stacking
- [ ] Vocabulary projection, logits, and language-model loss
### 09.2 Attention math
- [ ] Queries, keys, values, and learned projections
- [ ] Scaled dot-product attention and 1/sqrt(d_k) scaling
- [ ] Attention scores, masking, and softmax
- [ ] Causal, bidirectional, padding, and cross-attention masks
- [ ] Multi-head splitting, reshaping, concatenation, and output projection
- [ ] Tensor-shape derivations for B × T × d
- [ ] Computational and memory complexity of attention
### 09.3 Training versus autoregressive inference
- [ ] Parallel teacher-forced training and shifted targets
- [ ] Autoregressive next-token generation
- [ ] Prefill versus decode computation
- [ ] Causal masks with variable sequence lengths
- [ ] Attention KV reuse and incremental decoding
- [ ] Sequence packing and document boundary isolation

## 10. Attention mechanisms and variants
### 10.1 Head organization
- [ ] Multi-head attention (MHA)
- [ ] Multi-query attention (MQA)
- [ ] Grouped-query attention (GQA)
- [ ] Multi-head latent attention (MLA)
- [ ] Multi-scale, multi-granular, and heterogeneous heads
- [ ] Head dimensions, KV-head counts, and head pruning
### 10.2 Attention pattern variants
- [ ] Local, sliding-window, and dilated attention
- [ ] Block-sparse and global–local attention
- [ ] BigBird, Longformer, and sparse transformer patterns
- [ ] Sink tokens, attention sinks, and global memory tokens
- [ ] Linearized/kernel attention and approximation limits
- [ ] Cross-attention and bidirectional conditioning
### 10.3 Novel and hybrid attention ideas
- [ ] Differential attention and attention-score modifications
- [ ] Talking-heads and gated attention
- [ ] Multi-latent and compressed attention representations
- [ ] Multi-dimensional and grouped-query attention trade-offs
- [ ] Attention-free and recurrent alternatives
- [ ] Combining full attention with local/recurrent layers

## 11. Positional information and context length
### 11.1 Position encoding families
- [ ] Absolute learned positional embeddings
- [ ] Sinusoidal positional encodings
- [ ] Relative positional encodings and relative biases
- [ ] ALiBi and attention-bias methods
- [ ] Rotary positional embeddings (RoPE)
- [ ] Complex-number and rotation-matrix view of RoPE
- [ ] Multi-axis and multimodal positional encoding
### 11.2 RoPE and extrapolation details
- [ ] Base frequencies, theta, wavelength, and head dimension
- [ ] Rotation on Q and K and relative-position identity
- [ ] RoPE scaling and position interpolation
- [ ] NTK-aware scaling, YaRN, and LongRoPE approaches
- [ ] Extrapolation versus interpolation and failure modes
- [ ] Position-ID offsets, packed sequences, and KV-cache compatibility
### 11.3 Long-context learning
- [ ] Context extension by continued training
- [ ] Long-sequence data synthesis and packing
- [ ] Lost-in-the-middle and positional bias
- [ ] Needle-in-a-haystack versus multi-hop long-context retrieval
- [ ] Effective context window versus advertised context length
- [ ] Long-context attention alternatives and segment recurrence
- [ ] Long-context evaluation and memory–compute bottlenecks

## 12. Transformer blocks, normalization, and activation design
### 12.1 Feed-forward network design
- [ ] Positionwise MLP/FFN expansion and contraction
- [ ] ReLU, GELU, SiLU/Swish, and gated activations
- [ ] GLU, GEGLU, and SwiGLU
- [ ] FFN expansion ratio and parameter budgeting
- [ ] Weight tying, factorization, and depth/width trade-offs
### 12.2 Normalization and residual topology
- [ ] LayerNorm versus RMSNorm
- [ ] Pre-LN, Post-LN, and sandwich normalization
- [ ] Residual scaling and deep-network stability
- [ ] QK normalization and attention logit control
- [ ] Bias-free and bias-containing projections
- [ ] Initialization and stabilization of very deep transformers
### 12.3 Structural design choices
- [ ] Parallel versus sequential attention/FFN blocks
- [ ] Shared versus separate input/output embeddings
- [ ] Weight sharing across layers and recurrent depth
- [ ] Layer dropping, early exits, and adaptive depth
- [ ] Multi-token prediction heads and auxiliary losses
- [ ] Memory tokens and architectural conditioning

## 13. Architecture families beyond standard decoder-only LLMs
### 13.1 Transformer family variants
- [ ] Decoder-only causal LMs
- [ ] Encoder-only masked language models
- [ ] Encoder–decoder text-to-text models
- [ ] Prefix language models and infilling architectures
- [ ] Retrieval-augmented language-model architectures
- [ ] Prefix conditioning and multimodal decoder variants
### 13.2 Recurrence and state-space alternatives
- [ ] Recurrent language models and persistent hidden state
- [ ] State-space models and selective state spaces (Mamba family)
- [ ] RWKV and attention-free recurrent variants
- [ ] Retention and RetNet-style mechanisms
- [ ] xLSTM and gated recurrent alternatives
- [ ] Convolutional/long-filter sequence models
### 13.3 Hybrid and adaptive computation
- [ ] Transformer–SSM and attention–recurrence hybrids
- [ ] Mixture of depths and adaptive computation time
- [ ] Dynamic layer skipping and early exit
- [ ] Token pruning, token merging, and token routing
- [ ] Recurrent memory and compressed context models
- [ ] Architecture search and train–serve co-design

## 14. Mixture-of-experts (MoE) and sparsity
### 14.1 MoE fundamentals
- [ ] Dense FFN versus sparse expert FFNs
- [ ] Token-choice routing and top-k expert selection
- [ ] Router logits, softmax, and gating gradients
- [ ] Shared experts versus routed experts
- [ ] Active parameters versus total parameters
- [ ] Capacity factors, dropped tokens, and overflow handling
### 14.2 Training and routing mechanics
- [ ] Load-balancing auxiliary losses
- [ ] Router entropy, z-loss, and stability
- [ ] Expert specialization, redundancy, and collapse
- [ ] Expert-choice routing and alternative assignment schemes
- [ ] Fine-grained expert segmentation and expert grouping
- [ ] Noisy routing, token dispatch, and expert parallelism
### 14.3 MoE inference and adaptation
- [ ] All-to-all communication and load imbalance
- [ ] Expert caching, offloading, and hot-expert placement
- [ ] Expert quantization and heterogeneous precision
- [ ] Expert parallel deployment and batch utilization
- [ ] Expert merging, pruning, and distillation
- [ ] Multi-LoRA expert mixtures and task-conditioned routing

## 15. Scaling laws, compute, and model design
### 15.1 Empirical scaling behavior
- [ ] Parameter, data, and compute scaling laws
- [ ] Compute-optimal training and Chinchilla-style trade-offs
- [ ] Kaplan-style loss scaling and data regimes
- [ ] Scaling versus downstream task performance
- [ ] Test-time scaling and inference budget allocation
- [ ] Diminishing returns and benchmark saturation
### 15.2 Model and compute budgeting
- [ ] Parameters and training FLOP estimators
- [ ] Tokens per parameter and repeated epochs
- [ ] Effective batch size and sequence length trade-offs
- [ ] Dense versus MoE compute/quality trade-offs
- [ ] Training from scratch versus continued pretraining
- [ ] GPU utilization, MFU, throughput, and wall-clock cost
### 15.3 Research design questions
- [ ] Model size, depth, width, and head-count selection
- [ ] Context length versus attention cost
- [ ] Data diversity versus extra training tokens
- [ ] Longer training versus post-training investment
- [ ] Smaller specialized models versus larger general models
- [ ] Scaling failures, emergent behavior claims, and causal confounders

## 16. Pretraining objectives and objectives beyond next-token prediction
### 16.1 Core LM objectives
- [ ] Autoregressive causal language modeling
- [ ] Masked language modeling
- [ ] Span corruption and denoising autoencoding
- [ ] Prefix language modeling
- [ ] Sequence-to-sequence denoising objectives
- [ ] Fill-in-the-middle (FIM) and code infilling
### 16.2 Specialized and auxiliary objectives
- [ ] Multi-token prediction and multiple prediction heads
- [ ] Contrastive and discriminative auxiliary objectives
- [ ] Document coherence and next-segment objectives
- [ ] Retrieval or grounded-generation auxiliary tasks
- [ ] Instruction-aware continued pretraining
- [ ] Multimodal next-token and joint-token prediction
### 16.3 Objective mechanics
- [ ] Teacher forcing and exposure bias
- [ ] Shifted labels and ignore-index masks
- [ ] Cross-entropy, label smoothing, and loss weighting
- [ ] Packing-aware per-token versus per-document normalization
- [ ] Vocabulary loss and rare-token learning
- [ ] Perplexity interpretation across tokenizers

## 17. Pretraining optimization and experimental practice
### 17.1 Training-loop implementation
- [ ] Forward, loss, backward, optimizer step, and scheduler step
- [ ] Gradient accumulation and microbatching
- [ ] AdamW settings, betas, epsilon, and weight decay
- [ ] Learning-rate warmup, decay, and cooldown
- [ ] Gradient norm monitoring, clipping, and anomaly detection
- [ ] Dropout, regularization, and mixed-precision training
### 17.2 Stability and debugging
- [ ] Loss spikes, gradient explosions, and divergence
- [ ] NaNs, infinities, overflow, and optimizer-state corruption
- [ ] Activation statistics and initialization sensitivity
- [ ] Batch-size changes and optimization rescaling
- [ ] Data-quality anomalies and anomalous batches
- [ ] Seed control, determinism, and reproducibility
### 17.3 Training stages and checkpoints
- [ ] Warmup, steady-state training, and cooldown
- [ ] Stagewise data-mixture changes
- [ ] Continued pretraining and domain-adaptive pretraining
- [ ] Checkpoint frequency, retention, and restart
- [ ] Optimizer-state checkpointing and resumption fidelity
- [ ] Intermediate evaluation and checkpoint selection

## 18. Training hardware and distributed systems
### 18.1 Accelerator and memory fundamentals
- [ ] GPUs, TPUs, NPUs, and accelerator memory hierarchies
- [ ] HBM, cache, PCIe, NVLink, InfiniBand, and network topology
- [ ] Compute-bound versus memory-bandwidth-bound kernels
- [ ] GPU occupancy, warp execution, and kernel launch overhead
- [ ] BF16, FP16, FP8, and lower-precision training
- [ ] Activation, parameter, gradient, and optimizer-state memory
### 18.2 Parallelism strategies
- [ ] Data parallelism and distributed data parallel (DDP)
- [ ] Tensor parallelism
- [ ] Pipeline parallelism and pipeline bubbles
- [ ] Sequence parallelism and context parallelism
- [ ] Expert parallelism for MoE
- [ ] ZeRO optimizer stages and FSDP sharding
- [ ] 3D/4D/5D parallelism combinations
### 18.3 Memory and runtime optimization
- [ ] Gradient checkpointing / activation recomputation
- [ ] CPU/NVMe optimizer and parameter offloading
- [ ] FlashAttention and fused training kernels
- [ ] Sequence packing, bucketing, and dynamic batching
- [ ] Fused optimizers, fused normalization, and fused MLPs
- [ ] Distributed checkpointing and sharded state
### 18.4 Operational training infrastructure
- [ ] PyTorch distributed, DeepSpeed, Megatron, FSDP, and JAX ecosystems
- [ ] Cluster scheduling, job orchestration, and preemption
- [ ] Fault tolerance, elastic training, and restart strategies
- [ ] Data-loader throughput and streaming data pipelines
- [ ] Performance profiling, traces, and bottleneck diagnosis
- [ ] Energy usage, utilization, cost, and carbon accounting

## 19. Fine-tuning, adaptation, and transfer learning
### 19.1 Fine-tuning paradigms
- [ ] Full-parameter fine-tuning
- [ ] Continued pretraining versus task fine-tuning
- [ ] Instruction fine-tuning and conversational adaptation
- [ ] Domain-adaptive and task-adaptive fine-tuning
- [ ] Multitask fine-tuning and dataset mixtures
- [ ] Continual learning, catastrophic forgetting, and replay
### 19.2 Parameter-efficient fine-tuning (PEFT)
- [ ] Low-rank adaptation (LoRA) mathematics
- [ ] LoRA rank, scaling alpha, target modules, and dropout
- [ ] QLoRA and quantized frozen backbones
- [ ] DoRA, AdaLoRA, rsLoRA, and low-rank variants
- [ ] IA3, adapters, prefix tuning, and prompt tuning
- [ ] BitFit, selective fine-tuning, and layer freezing
### 19.3 Adapter composition and deployment
- [ ] LoRA merging and unmerging
- [ ] Multi-adapter serving and adapter hot swapping
- [ ] Task arithmetic and model merging
- [ ] TIES, DARE, and merging conflicts
- [ ] Mixtures of adapters, gating, and routing
- [ ] Adapter interpolation, transfer, and interference
### 19.4 Fine-tuning quality controls
- [ ] Chat template and tokenizer consistency
- [ ] Loss masking on user/system versus assistant tokens
- [ ] Response-only versus full-conversation loss
- [ ] Packing, truncation, and EOS correctness
- [ ] Overfitting, forgetting, and generality regression tests
- [ ] Fine-tuning hyperparameter sweeps and reproducibility

## 20. Instruction tuning and supervised post-training (SFT)
### 20.1 Instruction datasets
- [ ] Instruction–response pairs and multi-turn conversations
- [ ] System, developer, user, assistant, and tool-message roles
- [ ] Chat templates and message serialization
- [ ] Task diversity, difficulty, and data balancing
- [ ] Human-written versus synthetic demonstrations
- [ ] Refusal, safety, format-following, and tool-call examples
### 20.2 SFT objectives and methods
- [ ] Token-level negative log likelihood
- [ ] Assistant-response loss masking
- [ ] Full-sequence versus completion-only SFT
- [ ] Multi-turn context windows and conversational packing
- [ ] Curriculum and quality-weighted SFT
- [ ] Multi-objective SFT and auxiliary losses
### 20.3 SFT failure modes and evaluation
- [ ] Style imitation versus genuine capability gain
- [ ] Hallucinations induced by weak demonstrations
- [ ] Over-refusal and under-refusal
- [ ] Instruction hierarchy confusion
- [ ] Catastrophic forgetting of pretrained capabilities
- [ ] Distribution mismatch between training and usage

## 21. Preference learning, reward modeling, and RLHF
### 21.1 Human preference data
- [ ] Pairwise chosen–rejected responses
- [ ] Preference annotation rubrics and inter-rater agreement
- [ ] Bradley–Terry and pairwise choice models
- [ ] Helpfulness, harmlessness, honesty, and task-specific rewards
- [ ] Preference noise, position bias, and annotator disagreement
- [ ] Online versus offline preference collection
### 21.2 Reward-model training
- [ ] Scalar reward models and pairwise ranking loss
- [ ] Process reward models versus outcome reward models
- [ ] Verifiable rewards versus learned rewards
- [ ] Reward-model calibration and uncertainty
- [ ] Reward hacking, specification gaming, and overoptimization
- [ ] Reward ensemble models and disagreement detection
### 21.3 Classical RLHF pipeline
- [ ] SFT initialization, reward model, and policy optimization
- [ ] PPO objective, advantage estimation, and clipping
- [ ] KL penalty to a reference policy
- [ ] Policy–value model roles and critic training
- [ ] Rollouts, generation sampling, and sequence rewards
- [ ] Credit assignment for token-level decisions
### 21.4 Offline and direct preference objectives
- [ ] Direct Preference Optimization (DPO)
- [ ] IPO and DPO variants
- [ ] ORPO, SimPO, and reference-free approaches
- [ ] KTO and unpaired preference learning
- [ ] CPO, RLOO, online DPO, and related methods
- [ ] DPO beta, margin, data quality, and instability
### 21.5 Alignment feedback sources
- [ ] RLHF versus RLAIF and AI-generated critiques
- [ ] Constitutional AI and rule-guided feedback
- [ ] Human-written versus model-generated reward rubrics
- [ ] Multi-objective reward trade-offs
- [ ] Personalized preference modeling and pluralistic alignment
- [ ] Preference drift and iterative alignment updates

## 22. Reinforcement learning for reasoning and verifiable tasks
### 22.1 RL foundations applied to LLMs
- [ ] Markov decision process view of token generation
- [ ] Trajectories, actions, returns, and episodic rewards
- [ ] REINFORCE and policy-gradient estimators
- [ ] Baselines, advantages, and variance reduction
- [ ] Importance ratios and on-policy versus off-policy sampling
- [ ] Exploration, entropy bonuses, and reward sparsity
### 22.2 LLM-centric RL objectives
- [ ] GRPO and group-relative advantages
- [ ] RLOO and leave-one-out baselines
- [ ] DAPO and dynamic sampling/optimization choices
- [ ] GSPO and sequence-level policy optimization
- [ ] REINFORCE++ and critic-free variants
- [ ] PPO versus GRPO versus DPO conceptual comparisons
### 22.3 Training with verifiers and environments
- [ ] Exact-match and programmatic reward functions
- [ ] Math answer verification and symbolic checks
- [ ] Unit-test and compiler-based code rewards
- [ ] Tool-call outcomes and environment feedback
- [ ] Process-level and step-level rewards
- [ ] Reward shaping and sparse terminal rewards
### 22.4 Reasoning-RL pathologies
- [ ] Reward hacking and exploitable verifiers
- [ ] Long-response bias and length normalization
- [ ] Entropy collapse, mode collapse, and exploration failure
- [ ] KL drift, policy lag, and stale rollouts
- [ ] Incorrect answer extraction and false negatives
- [ ] Goodhart's law and benchmark-specific overfitting
### 22.5 Online RL engineering
- [ ] Rollout generation versus gradient-update workers
- [ ] Asynchronous rollouts and policy staleness
- [ ] Actor–learner architecture and inference–training coupling
- [ ] Reward service scaling and sandboxed evaluation
- [ ] vLLM/SGLang-backed rollouts and distributed training
- [ ] Reproducible seeds, reward logging, and checkpoint analysis

## 23. Reasoning, planning, and test-time computation
### 23.1 Reasoning behaviors
- [ ] Arithmetic, symbolic, causal, spatial, and temporal reasoning
- [ ] Multi-hop and compositional reasoning
- [ ] Deduction, induction, abduction, and analogy
- [ ] Formal proofs versus natural-language explanations
- [ ] Planning and search versus pattern completion
- [ ] Reasoning faithfulness and unfaithful explanations
### 23.2 Prompt-level reasoning strategies
- [ ] Zero-shot and few-shot reasoning prompts
- [ ] Chain-of-thought as a prompting paradigm
- [ ] Least-to-most and decomposition prompting
- [ ] Self-consistency and majority voting
- [ ] ReAct-style interleaved reasoning and actions
- [ ] Debate, critique, and self-refinement
### 23.3 Search and inference-time algorithms
- [ ] Best-of-N and rejection sampling
- [ ] Tree of Thoughts and branching search
- [ ] Beam search with verifier scoring
- [ ] Monte Carlo tree search for language tasks
- [ ] Process reward guided search
- [ ] Dynamic compute budgets and early stopping
### 23.4 Advanced reasoning paradigms
- [ ] Latent-space versus verbalized reasoning
- [ ] Hidden reasoning tokens and intermediate computation
- [ ] Deliberation models and fast/slow modes
- [ ] Parallel versus sequential thinking
- [ ] Verifier–generator systems and proof checking
- [ ] Test-time training and adaptation
### 23.5 Math and formal reasoning
- [ ] Symbolic algebra and numerical tool augmentation
- [ ] Formal theorem provers and proof assistants
- [ ] Program synthesis and executable reasoning
- [ ] Constraint solving and SAT/SMT integration
- [ ] Robustness to superficial math perturbations
- [ ] Measuring reasoning depth and out-of-distribution transfer

## 24. Autoregressive generation and decoding
### 24.1 Logits to output tokens
- [ ] Temperature scaling and categorical sampling
- [ ] Greedy decoding
- [ ] Top-k sampling and nucleus (top-p) sampling
- [ ] Min-p, typical sampling, and alternative truncation rules
- [ ] Repetition, frequency, and presence penalties
- [ ] Logit bias, bad-token masks, and stop sequences
### 24.2 Search and multiple candidates
- [ ] Beam search and length penalties
- [ ] Diverse beam search and constrained beam search
- [ ] Best-of-N sampling and candidate reranking
- [ ] Contrastive search and contrastive decoding
- [ ] Diverse generations and stochastic seed control
- [ ] Confidence-aware stopping and stopping criteria
### 24.3 Structured and constrained generation
- [ ] JSON schema-constrained generation
- [ ] Regex, grammars, and finite-state decoders
- [ ] Tool-call argument constrained decoding
- [ ] Format validation and repair loops
- [ ] Handling partial JSON and incremental streaming parsers
- [ ] Decoder-level versus prompt-only format guarantees
### 24.4 Decoding pitfalls
- [ ] Degeneration, loops, and repetition
- [ ] Temperature versus entropy and diversity
- [ ] Length bias and EOS behavior
- [ ] Sampling-induced variability and nondeterminism
- [ ] Label smoothing and logit calibration
- [ ] Exposure bias and long-horizon error propagation

## 25. Prompt engineering and context engineering
### 25.1 Prompt construction
- [ ] Instruction clarity, task specification, and success criteria
- [ ] System versus developer versus user instructions
- [ ] Prompt templates and reusable prompt components
- [ ] Zero-shot, one-shot, and few-shot examples
- [ ] Positive/negative exemplars and edge cases
- [ ] Delimiters, quoted content, and role separation
### 25.2 Advanced prompt techniques
- [ ] Decomposition and stepwise task organization
- [ ] Self-critique, refinement, and verification prompts
- [ ] Role/persona conditioning and its limitations
- [ ] Prompt chaining and prompt programs
- [ ] Structured output and tool-calling prompts
- [ ] Multi-modal prompting with images/audio/video
### 25.3 Context assembly
- [ ] Relevant context selection and ordering
- [ ] Lost-in-the-middle and position effects
- [ ] Context compression, summarization, and trimming
- [ ] Source attribution and explicit uncertainty handling
- [ ] Retrieval-aware prompt design
- [ ] Token-budget allocation among instructions, data, and output
### 25.4 Prompt reliability and measurement
- [ ] Prompt injection versus legitimate instructions
- [ ] Evaluating prompt variants on held-out cases
- [ ] Prompt overfitting and prompt sensitivity
- [ ] Perturbation testing and consistency checks
- [ ] Template version control and regression testing
- [ ] Prompt optimization using search or automated optimizers

## 26. Long-context systems, compression, and persistent context
### 26.1 Long-context use cases
- [ ] Full-document analysis and multi-document synthesis
- [ ] Repository-scale code analysis
- [ ] Multi-hour meeting/conversation analysis
- [ ] Long-horizon agents and ongoing tasks
- [ ] Long-context extraction and structured query answering
- [ ] Long-range dependencies and cross-document references
### 26.2 Context-reduction strategies
- [ ] Sliding-window history and message trimming
- [ ] Hierarchical document summaries
- [ ] Query-aware compression and contextual compression
- [ ] Extractive versus abstractive compression
- [ ] Semantic chunk selection and salience scoring
- [ ] Lossy compression, forgetting, and summary drift
### 26.3 Memory integration
- [ ] External long-term memory versus model weights
- [ ] Episodic, semantic, and procedural memory
- [ ] Retrieval over user history and project state
- [ ] Memory consolidation, expiration, and contradiction handling
- [ ] Persistent notes, knowledge graphs, and structured memories
- [ ] Privacy-aware memory boundaries and deletion

## 27. KV cache and inference memory management
### 27.1 KV cache mathematics and layout
- [ ] Deriving key/value tensor shapes per layer
- [ ] KV cache versus query recomputation
- [ ] KV size as function of B, T, H_kv, d_head, layers, and dtype
- [ ] Effect of MHA, MQA, GQA, and MLA on KV storage
- [ ] Cache indexing, RoPE positions, and attention masks
- [ ] Prefill-created versus decode-appended KV entries
### 27.2 Cache memory architectures
- [ ] Contiguous cache allocation versus paged cache
- [ ] PagedAttention block tables and indirection
- [ ] Prefix caching and shared prompt blocks
- [ ] Copy-on-write and forked sequence caches
- [ ] Cache eviction, swapping, and compaction
- [ ] Host/device offload and hierarchical KV storage
### 27.3 KV compression and advanced caching
- [ ] KV quantization and per-head quantization
- [ ] Sliding-window and sink-token retention
- [ ] Selective token eviction and importance-based pruning
- [ ] Cache pooling, low-rank compression, and latent cache
- [ ] Cross-request cache reuse and cache correctness
- [ ] Distributed KV transfers and prefill–decode disaggregation
### 27.4 Cache performance and validation
- [ ] Cache-aware scheduling and fragmentation
- [ ] KV bandwidth versus attention compute cost
- [ ] Cache pollution, tenant isolation, and leakage
- [ ] Long-context cache stress tests
- [ ] Speculative decoding cache rollback
- [ ] Memory profiler calculations and capacity planning

## 28. Efficient attention kernels and GPU optimization
### 28.1 IO-aware attention
- [ ] Standard attention's intermediate attention matrix
- [ ] FlashAttention intuition and tile-based softmax
- [ ] Online softmax and numerical equivalence
- [ ] FlashAttention variants and backward recomputation
- [ ] FlashDecoding and incremental attention
- [ ] Memory traffic analysis and arithmetic intensity
### 28.2 GPU kernel engineering
- [ ] Triton and CUDA kernel fundamentals
- [ ] Shared-memory tiling and register pressure
- [ ] Fused RMSNorm, RoPE, MLP, and softmax kernels
- [ ] GEMM layouts, tensor cores, and precision selection
- [ ] CUDA graphs and launch-overhead elimination
- [ ] Kernel autotuning and architecture-specific optimization
### 28.3 Attention alternatives and benchmarking
- [ ] FlashInfer and attention backend selection
- [ ] Sparse attention kernel efficiency
- [ ] MLA-specific kernels and cache representations
- [ ] Chunked attention and context parallelism
- [ ] Kernel correctness under different masks and shapes
- [ ] Roofline analysis, throughput, and memory profiling

## 29. Quantization, pruning, sparsity, and distillation
### 29.1 Numeric formats and quantization basics
- [ ] FP32, TF32, BF16, FP16, FP8, and FP4
- [ ] Integer formats INT8, INT4, and mixed precision
- [ ] Symmetric versus asymmetric quantization
- [ ] Per-tensor, per-channel, and per-group scales
- [ ] Zero points, clipping, and calibration
- [ ] Quantization error and outlier activation distributions
### 29.2 Weight and activation quantization
- [ ] Post-training quantization (PTQ)
- [ ] Quantization-aware training (QAT)
- [ ] GPTQ and Hessian-aware quantization
- [ ] AWQ and activation-aware quantization
- [ ] SmoothQuant and activation smoothing
- [ ] GGUF/GGML ecosystem and portable formats
- [ ] NF4 and double quantization in QLoRA
### 29.3 Inference-oriented compression
- [ ] Weight-only versus weight–activation quantization
- [ ] KV cache quantization
- [ ] Dynamic versus static activation quantization
- [ ] Mixed-bit and layer-sensitive quantization
- [ ] Structured/unstructured pruning and N:M sparsity
- [ ] Low-rank factorization and neural compression
### 29.4 Distillation and compact modeling
- [ ] Teacher–student distillation and soft labels
- [ ] Logit-level versus feature-level distillation
- [ ] Sequence-level and on-policy distillation
- [ ] Reasoning-trace and tool-use distillation
- [ ] Distillation from ensembles or verifier-filtered samples
- [ ] Compression quality–latency–memory Pareto frontiers

## 30. LLM inference execution and throughput optimization
### 30.1 Prefill/decode computational regimes
- [ ] Prefill compute profile and first-token latency
- [ ] Decode memory-bandwidth profile and tokens/sec
- [ ] Time to first token (TTFT) versus inter-token latency (ITL)
- [ ] Throughput, goodput, and tail-latency definitions
- [ ] Arithmetic intensity and roofline model
- [ ] Latency–batch size and concurrency trade-offs
### 30.2 Batching and request scheduling
- [ ] Static batching versus continuous batching
- [ ] Dynamic batching, request admission, and waiting queues
- [ ] Chunked prefill and prefill–decode interleaving
- [ ] Prefix sharing and response-length prediction
- [ ] Fairness, priority, deadlines, and preemption
- [ ] Head-of-line blocking and straggler requests
### 30.3 Speculative and parallel generation
- [ ] Draft-model speculative decoding and acceptance/rejection
- [ ] Self-speculative decoding and early-exit drafts
- [ ] N-gram and suffix speculation
- [ ] EAGLE-style draft heads and verification
- [ ] Multi-token prediction for inference
- [ ] Parallel decoding and tree verification
### 30.4 Distributed inference architecture
- [ ] Tensor parallelism versus pipeline parallelism
- [ ] Expert parallelism for MoE serving
- [ ] Context parallelism and long-sequence inference
- [ ] Disaggregated prefill, decode, and encode
- [ ] Multi-node KV transfer and remote cache access
- [ ] Elastic scaling and heterogeneous accelerator fleets

## 31. Model serving engines and deployment stacks
### 31.1 Open and commercial inference runtimes
- [ ] Hugging Face Transformers generation API
- [ ] vLLM engine and OpenAI-compatible APIs
- [ ] SGLang runtime and structured generation
- [ ] TensorRT-LLM and compiler-driven inference
- [ ] llama.cpp, GGUF, and CPU/local inference
- [ ] MLX, ONNX Runtime, TGI, and alternate runtimes
### 31.2 Serving design
- [ ] Model loading, warmup, and weight distribution
- [ ] Multi-model placement, routing, and autoscaling
- [ ] Multi-LoRA adapter hosting
- [ ] Streaming responses and SSE/WebSocket transport
- [ ] Multi-tenant isolation, quotas, and rate limits
- [ ] Offline batch processing versus low-latency serving
### 31.3 Production performance
- [ ] End-to-end latency decomposition
- [ ] Token throughput and GPU utilization dashboards
- [ ] Prefix caching and cache-hit metrics
- [ ] Model replicas, scaling policies, and queue saturation
- [ ] Tail latency, retries, and overload protection
- [ ] Benchmarking representative workloads and capacity planning

## 32. LLM APIs, protocols, and application integration
### 32.1 API fundamentals
- [ ] Chat-completion versus response-oriented APIs
- [ ] Message roles, content parts, and output modalities
- [ ] Tokens, usage accounting, and token budgets
- [ ] Streaming token events and incremental output handling
- [ ] Retries, backoff, idempotency, and timeouts
- [ ] Version pinning, model deprecation, and compatibility
### 32.2 Structured interfaces
- [ ] Tool/function-call schemas and validation
- [ ] JSON schema, XML, and grammar-constrained output
- [ ] Parallel tool calls and tool-result correlation
- [ ] Schema evolution and backward compatibility
- [ ] Function-calling failure recovery and argument repair
- [ ] Multimodal message payload representation
### 32.3 System integration
- [ ] Queues, background workers, and orchestration
- [ ] REST, gRPC, WebSockets, and event streams
- [ ] Authentication, authorization, and secrets management
- [ ] Provider abstraction, fallbacks, and model routing
- [ ] Cost governance and usage observability
- [ ] API privacy, retention, and regional hosting controls

## 33. Retrieval, search, ranking, and embedding systems
### 33.1 Search paradigms
- [ ] Lexical search, BM25, and inverted indexes
- [ ] Dense vector retrieval
- [ ] Hybrid sparse–dense search
- [ ] Cross-encoder reranking
- [ ] Late-interaction retrieval such as ColBERT
- [ ] Learned sparse retrieval and SPLADE-style methods
### 33.2 Indexing and vector databases
- [ ] Exact nearest-neighbor search
- [ ] ANN techniques: IVF, HNSW, and product quantization
- [ ] FAISS internals and GPU indexing
- [ ] Vector databases and metadata filtering
- [ ] Index build/update/delete, sharding, and replication
- [ ] Embedding version migration and reindexing
### 33.3 Retrieval training and metrics
- [ ] Contrastive learning for query/document matching
- [ ] Hard negatives, in-batch negatives, and false negatives
- [ ] Recall@k, precision@k, MRR, MAP, and nDCG
- [ ] Retrieval query understanding and expansion
- [ ] Domain-specific embeddings and rerankers
- [ ] Calibration, freshness, and retrieval drift

## 34. Retrieval-augmented generation (RAG)
### 34.1 Document ingestion and chunking
- [ ] PDF, HTML, DOCX, Markdown, table, and code ingestion
- [ ] Fixed-size, semantic, structure-aware, and recursive chunking
- [ ] Overlap sizing and parent–child chunk linkage
- [ ] Metadata, citations, provenance, and document versioning
- [ ] Table/image extraction and multimodal document parsing
- [ ] ACL-aware indexing and content redaction
### 34.2 RAG query pipeline
- [ ] Query rewriting, decomposition, and multi-query search
- [ ] Hybrid retrieval, filtering, and reranking
- [ ] Context assembly and answer grounding
- [ ] Citation spans and source verification
- [ ] Query routing and retrieval-depth selection
- [ ] Handling no-answer and low-retrieval-confidence cases
### 34.3 Advanced RAG strategies
- [ ] Agentic RAG and iterative retrieval
- [ ] GraphRAG and entity/relation retrieval
- [ ] Hierarchical and long-document RAG
- [ ] Corrective, adaptive, and self-reflective RAG
- [ ] Multimodal RAG and vision-based page retrieval
- [ ] Knowledge graph plus vector-store hybrids
### 34.4 RAG evaluation and optimization
- [ ] Retrieval relevance versus answer faithfulness
- [ ] Context precision, context recall, and citation correctness
- [ ] Groundedness, answer completeness, and abstention
- [ ] RAGAS-style and task-specific eval frameworks
- [ ] Dataset construction and synthetic QA pairs
- [ ] Latency–accuracy–cost trade-offs and caching

## 35. Tool use, function calling, and external computation
### 35.1 Tool-use fundamentals
- [ ] Tool descriptions, schemas, and capability boundaries
- [ ] Tool selection and argument generation
- [ ] Parallel versus sequential tool invocation
- [ ] Tool observations and result incorporation
- [ ] Errors, retries, timeouts, and partial failures
- [ ] Human approval before consequential tool actions
### 35.2 Tool-use categories
- [ ] Search/browser tools and source retrieval
- [ ] Code execution, calculators, and sandboxes
- [ ] SQL querying and database connectors
- [ ] Filesystem and document operations
- [ ] Scheduling, messaging, and third-party actions
- [ ] Scientific tools, symbolic solvers, and APIs
### 35.3 Tool-use reliability and safety
- [ ] Tool-output injection and untrusted content
- [ ] Least-privilege permissions and scoped credentials
- [ ] Side-effect isolation and idempotency
- [ ] Tool-call trace auditing and replay
- [ ] Transaction boundaries and compensation actions
- [ ] Tool-call benchmark design and pass/fail criteria

## 36. LLM agents and workflow architectures
### 36.1 Agent fundamentals
- [ ] LLM as planner/controller versus LLM as component
- [ ] Perception, planning, action, observation, and feedback
- [ ] ReAct loops and state machines
- [ ] Workflow orchestration versus autonomous agents
- [ ] Tool-augmented execution and environment interaction
- [ ] Task completion, stopping conditions, and verification
### 36.2 Agent patterns
- [ ] Plan-and-execute agents
- [ ] ReAct and iterative observation-action agents
- [ ] Reflection and critique loops
- [ ] Supervisor–worker and hierarchical orchestration
- [ ] Event-driven agents and durable workflows
- [ ] Graph-based state-machine orchestrators
### 36.3 Reliability and governance
- [ ] State persistence, checkpoints, and resumability
- [ ] Max-step controls, budgets, and termination criteria
- [ ] Retry handling, idempotency, and compensating actions
- [ ] Human-in-the-loop review and escalation
- [ ] Agent evaluation by trajectory, outcome, and cost
- [ ] Agent sandboxing and permission boundaries

## 37. Multi-agent systems, coordination, and protocols
### 37.1 Multi-agent coordination
- [ ] Role-specialized agent teams
- [ ] Manager–worker and planner–executor patterns
- [ ] Debate, voting, and critique ensembles
- [ ] Collaborative blackboard and shared-memory systems
- [ ] Negotiation, delegation, and task decomposition
- [ ] Coordination overhead and emergent failure modes
### 37.2 Agent communication and interoperability
- [ ] Agent-to-agent message schemas and contracts
- [ ] Model Context Protocol (MCP) concepts and tool/resources interfaces
- [ ] Agent-to-Agent (A2A) communication concepts
- [ ] Tool discovery and capability registries
- [ ] Stateful handoffs, provenance, and correlation IDs
- [ ] Trust boundaries and authenticated inter-agent messaging
### 37.3 Agent evaluation and optimization
- [ ] Single-agent versus multi-agent baselines
- [ ] Task success, communication cost, and latency
- [ ] Credit assignment across agents
- [ ] Redundant work, conflicts, and deadlock avoidance
- [ ] Trace-level analysis and root-cause attribution
- [ ] Failover, human override, and orchestration policies

## 38. Agent memory, state, and long-horizon autonomy
### 38.1 Memory taxonomies
- [ ] Working memory, short-term history, and long-term memory
- [ ] Episodic memories of events and interactions
- [ ] Semantic memory and structured facts
- [ ] Procedural memory, learned skills, and reusable workflows
- [ ] Model-internal knowledge versus external storage
- [ ] Shared versus per-agent memories
### 38.2 Memory operations
- [ ] Memory write policy and salience selection
- [ ] Retrieval and relevance scoring
- [ ] Consolidation, summarization, and conflict resolution
- [ ] Temporal decay, forgetting, and memory expiration
- [ ] Attribution, provenance, and uncertainty metadata
- [ ] User correction, deletion, and memory access control
### 38.3 Long-horizon execution
- [ ] Durable plans and hierarchical task tracking
- [ ] Resuming work after context loss
- [ ] State snapshots, event sourcing, and action replay
- [ ] Subgoal decomposition and progress verification
- [ ] Stuck-agent detection and recovery
- [ ] Memory poisoning defenses and permissioned recall

## 39. Multimodal LLM fundamentals
### 39.1 Multimodal representations
- [ ] Text, image, audio, video, and spatial tokens
- [ ] Modality encoders, adapters, projectors, and decoders
- [ ] Early, middle, and late fusion
- [ ] Cross-attention versus token-concatenation fusion
- [ ] Shared embedding spaces and contrastive alignment
- [ ] Modality-specific preprocessing and patching
### 39.2 Multimodal training
- [ ] Image–text and audio–text paired data
- [ ] Captioning, contrastive, and generative objectives
- [ ] Instruction tuning with multimodal conversations
- [ ] Interleaved text–image and text–audio sequences
- [ ] Cross-modal grounding and hallucination mitigation
- [ ] Multimodal preference optimization and reward modeling
### 39.3 Evaluation and integration
- [ ] Modalities in a shared context window
- [ ] Modality-specific token cost and memory footprints
- [ ] Cross-modal consistency and grounding
- [ ] Accessibility and alternative text generation
- [ ] Robustness to low-quality input and missing modalities
- [ ] Multimodal safety and privacy evaluation

## 40. Vision-language models (VLMs) and documents
### 40.1 Vision encoders and alignment
- [ ] CNN versus Vision Transformer (ViT) image encoders
- [ ] CLIP-style contrastive vision–language alignment
- [ ] Image patches, resolution, tiling, and crops
- [ ] Visual projector and Q-Former-style adapters
- [ ] Perceiver resampling and token compression
- [ ] Variable-resolution and dynamic visual tokens
### 40.2 VLM capabilities
- [ ] Image captioning and visual question answering
- [ ] OCR, scene text, and handwriting interpretation
- [ ] Charts, tables, diagrams, and document QA
- [ ] Spatial grounding, localization, and referring expressions
- [ ] Multi-image comparison and visual reasoning
- [ ] GUI/screen understanding and screenshot-based agents
### 40.3 Vision-specific limitations
- [ ] Object counting and spatial relation failures
- [ ] Fine-detail recognition and resolution bottlenecks
- [ ] Visual hallucinations and grounding errors
- [ ] OCR/layout confusion and page ordering
- [ ] Adversarial image and embedded-text injection
- [ ] Evaluation of vision reasoning and document accuracy

## 41. Audio, speech, music, and spoken language models
### 41.1 Audio foundations
- [ ] Waveforms, sample rates, spectrograms, and mel features
- [ ] Audio codecs, discrete acoustic tokens, and neural quantizers
- [ ] Streaming chunks, timestamps, and speaker diarization
- [ ] Speech activity detection and noise robustness
- [ ] Audio embeddings and speech encoders
- [ ] Cross-modal audio–text alignment
### 41.2 Speech tasks and models
- [ ] Automatic speech recognition (ASR)
- [ ] Speech translation and multilingual transcription
- [ ] Text-to-speech (TTS) and speech generation
- [ ] Speech-to-speech and simultaneous translation
- [ ] Voice activity and turn-taking prediction
- [ ] Speaker identification, diarization, and separation
### 41.3 Real-time voice systems
- [ ] Cascaded ASR→LLM→TTS versus end-to-end audio models
- [ ] Streaming speech input and output generation
- [ ] Barge-in, interruption, and full-duplex conversation
- [ ] End-of-turn detection and latency budgeting
- [ ] Prosody, emotion, and voice consistency
- [ ] Audio safety, spoofing, and voice consent

## 42. Video, real-time multimodal systems, and embodied agents
### 42.1 Video representation
- [ ] Frames, clips, timestamps, and temporal sampling
- [ ] Video tokenization and temporal compression
- [ ] Spatiotemporal positional encodings
- [ ] Event recognition and temporal localization
- [ ] Long-video summarization and retrieval
- [ ] Audio–video synchronization
### 42.2 Real-time multimodal interaction
- [ ] Streaming visual and audio observations
- [ ] Incremental perception and state updates
- [ ] Live multimodal conversation and event triggers
- [ ] Time-aligned memory and synchronized outputs
- [ ] Latency management under continuous perception
- [ ] Multimodal hallucination and temporal grounding
### 42.3 Action and embodied language models
- [ ] Vision-language-action (VLA) models
- [ ] Action tokenization and trajectory prediction
- [ ] Robotics instruction following and manipulation
- [ ] World models and predictive latent states
- [ ] Affordance learning and spatial planning
- [ ] Sim-to-real transfer, safety, and closed-loop evaluation

## 43. Code language models and software-engineering agents
### 43.1 Code modeling
- [ ] Programming-language tokenization and syntax patterns
- [ ] Repository pretraining, licensing, and decontamination
- [ ] Fill-in-the-middle code completion
- [ ] Code generation, translation, and refactoring
- [ ] Static analysis, ASTs, and type information
- [ ] Multi-file and repository-level code understanding
### 43.2 Code reasoning and verification
- [ ] Program synthesis and algorithmic reasoning
- [ ] Test-case generation and property-based testing
- [ ] Compiler and interpreter feedback
- [ ] Execution traces, stack traces, and debugging
- [ ] Patch generation, code editing, and differential testing
- [ ] Secure coding and vulnerability detection
### 43.3 Software-engineering agents
- [ ] Repository search, code navigation, and dependency mapping
- [ ] Issue localization and root-cause analysis
- [ ] Tool-driven edit–test–debug loops
- [ ] CI integration and test execution sandboxes
- [ ] PR generation, review, and merge-conflict resolution
- [ ] SWE-bench-style evaluation and leakage controls

## 44. Domain-specific and multilingual LLMs
### 44.1 Domain adaptation
- [ ] Medical, scientific, legal, financial, and educational LLMs
- [ ] Domain vocabulary and specialist tokenization
- [ ] Domain-adaptive continued pretraining
- [ ] Domain-specific SFT and preference optimization
- [ ] Domain-specific retrieval and knowledge bases
- [ ] Validation with domain experts and external standards
### 44.2 Multilingual and cross-lingual learning
- [ ] Language-balanced pretraining and sampling
- [ ] Cross-lingual transfer and zero-shot transfer
- [ ] Translation-based augmentation and evaluation
- [ ] Code-switching, transliteration, and mixed scripts
- [ ] Morphologically rich and low-resource languages
- [ ] Regional language safety and cultural context
### 44.3 Specialized model families
- [ ] Mathematical reasoning models
- [ ] Scientific and symbolic reasoning models
- [ ] Legal document reasoning models
- [ ] Financial and time-series language models
- [ ] Biology/chemistry/protein-sequence foundation models
- [ ] Tabular, database, and structured-data language models

## 45. Evaluation methodology and benchmark engineering
### 45.1 Offline evaluation basics
- [ ] Held-out testing and dataset stratification
- [ ] Perplexity, loss, exact match, F1, and task accuracy
- [ ] Human evaluation and annotation rubrics
- [ ] Pairwise preference and win-rate evaluation
- [ ] Statistical confidence intervals and significance testing
- [ ] Variance across prompts, seeds, and decoding settings
### 45.2 Capability benchmark families
- [ ] General knowledge and MMLU-style evaluation
- [ ] Graduate knowledge and GPQA-style evaluation
- [ ] Math benchmarks and verifiable problem solving
- [ ] Code benchmarks: HumanEval, MBPP, LiveCodeBench
- [ ] Software-agent benchmarks: SWE-bench and terminal tasks
- [ ] Long-context benchmarks: LongBench, RULER, needle tests
- [ ] Instruction following and IFEval-style tests
### 45.3 Specialized benchmarking
- [ ] Tool calling and function argument correctness
- [ ] RAG factuality, retrieval, and citation benchmarks
- [ ] Embedding and retrieval evaluation (MTEB-style)
- [ ] VLM, audio, video, and multimodal reasoning benchmarks
- [ ] Safety, bias, jailbreak, and refusal testing
- [ ] Multilingual and low-resource benchmarks
### 45.4 Evaluation reliability
- [ ] Data contamination, leaderboard overfitting, and test leakage
- [ ] Static versus rolling/private test sets
- [ ] LLM-as-a-judge strengths and position/style bias
- [ ] Judge calibration, reference checks, and rubric design
- [ ] Goodhart's law and benchmark gaming
- [ ] Reproducible harnesses, versions, and environment control
### 45.5 Online and product evaluation
- [ ] A/B tests and interleaving experiments
- [ ] User satisfaction, task success, and downstream outcomes
- [ ] Latency, cost, availability, and quality trade-offs
- [ ] Human escalation and error-severity metrics
- [ ] Shadow evaluation and canary model releases
- [ ] Longitudinal drift and regression monitoring

## 46. Factuality, uncertainty, calibration, and robustness
### 46.1 Hallucinations and factual errors
- [ ] Intrinsic versus extrinsic hallucination
- [ ] Unsupported claims, fabricated citations, and invented entities
- [ ] Retrieval failure versus generation failure
- [ ] Knowledge cutoff and temporal staleness
- [ ] Multi-hop fact composition and contradiction
- [ ] Grounded generation and evidence attribution
### 46.2 Uncertainty and calibration
- [ ] Token probability versus answer correctness
- [ ] Predictive entropy and confidence aggregation
- [ ] Verbal confidence and confidence elicitation
- [ ] Temperature scaling and post-hoc calibration
- [ ] Selective prediction and abstention
- [ ] Conformal prediction and uncertainty sets
### 46.3 Robustness and stress testing
- [ ] Paraphrase and formatting sensitivity
- [ ] Long context and distractor robustness
- [ ] Out-of-distribution and distribution-shift tests
- [ ] Contradictory evidence and adversarial examples
- [ ] Tool error robustness and API schema drift
- [ ] Reliability under nondeterminism and sampling changes

## 47. Interpretability, mechanistic analysis, and model editing
### 47.1 Black-box interpretability
- [ ] Probing classifiers and representation similarity
- [ ] Layerwise behavior and intermediate activations
- [ ] Attention visualization and its limitations
- [ ] Logit lens and tuned lens
- [ ] Model behavior attribution and counterfactual tests
- [ ] Feature visualization and activation statistics
### 47.2 Mechanistic interpretability
- [ ] Residual-stream decomposition and circuit hypotheses
- [ ] Induction heads and in-context copying circuits
- [ ] Activation patching and causal tracing
- [ ] Path patching, ablation, and causal mediation
- [ ] Sparse autoencoders (SAEs) and feature dictionaries
- [ ] Superposition, polysemanticity, and feature geometry
### 47.3 Model editing and steering
- [ ] Knowledge editing and targeted factual updates
- [ ] Rank-one and locate-and-edit approaches
- [ ] Representation steering and activation addition
- [ ] Steering vectors and inference-time control
- [ ] Unlearning, concept erasure, and side effects
- [ ] Evaluating edit specificity, locality, and persistence

## 48. Alignment, model behavior, and responsible AI
### 48.1 Alignment objectives
- [ ] Helpful, honest, harmless, and user-intent-aligned behavior
- [ ] Instruction hierarchy and authorized directives
- [ ] Corrigibility and appropriate human oversight
- [ ] Moral uncertainty and pluralistic values
- [ ] Reward–objective mismatch and specification gaming
- [ ] Alignment tax and capability–safety trade-offs
### 48.2 Safety post-training
- [ ] Safety-specific SFT and preference data
- [ ] Refusal policies and safe-completion strategies
- [ ] Rule-based, classifier-based, and model-based guardrails
- [ ] Safety evaluation before and after fine-tuning
- [ ] Robustness to indirect and multi-turn attacks
- [ ] Escalation, tool action gating, and high-stakes domains
### 48.3 Fairness and societal impacts
- [ ] Stereotypes, representational harms, and disparate performance
- [ ] Cultural and multilingual fairness evaluations
- [ ] Toxicity, bias amplification, and content moderation
- [ ] Accessibility and inclusive interaction design
- [ ] Transparency, explainability, and affected-user recourse
- [ ] Environmental and workforce effects of deployment

## 49. LLM security, prompt injection, and adversarial ML
### 49.1 Threat modeling
- [ ] Assets, trust boundaries, attackers, and attack surfaces
- [ ] Model, prompt, tool, retrieval, and data supply chains
- [ ] Direct versus indirect prompt injection
- [ ] Jailbreaks versus application-level security failures
- [ ] Attacker-controlled documents, websites, and tool results
- [ ] Agent authority boundaries and privilege escalation
### 49.2 Attack classes
- [ ] Prompt injection and instruction override attempts
- [ ] Sensitive-data disclosure and hidden-context exposure
- [ ] Excessive agency and unauthorized tool actions
- [ ] Data poisoning, model poisoning, and backdoors
- [ ] Model extraction, membership inference, and inversion
- [ ] Tool-output misuse and insecure output handling
- [ ] Vector/embedding store poisoning and retrieval hijacking
- [ ] Unbounded consumption and denial-of-wallet attacks
### 49.3 Defenses and secure architecture
- [ ] Treating retrieved text and tool output as untrusted data
- [ ] Instruction hierarchy enforcement and role separation
- [ ] Tool allowlists, schema validation, and permission checks
- [ ] Sandboxed execution and network/file-system isolation
- [ ] Secret minimization and least-privilege service accounts
- [ ] Rate limiting, monitoring, audit trails, and kill switches
- [ ] Continuous red teaming and attack regression suites
### 49.4 Security standards and research
- [ ] OWASP Top 10 for LLM Applications (2026)
- [ ] OWASP agentic security threat categories
- [ ] MITRE ATLAS and adversarial ML mapping
- [ ] Threat-model-driven evaluations and incident response
- [ ] AI supply-chain integrity, model artifact signing, and provenance
- [ ] Security–utility trade-offs and defense-in-depth limits

## 50. Privacy, intellectual property, governance, and compliance
### 50.1 Privacy-preserving learning
- [ ] Differential privacy definitions and epsilon/delta accounting
- [ ] DP-SGD and privacy–utility trade-offs
- [ ] Private fine-tuning and privacy budgets
- [ ] Data minimization and retention windows
- [ ] Federated/distributed privacy-preserving adaptation
- [ ] Memorization, extraction, and training-data leakage
### 50.2 Intellectual property and provenance
- [ ] Copyright and licensing of model weights and datasets
- [ ] Open-source license compatibility
- [ ] Dataset and model provenance tracking
- [ ] Memorized passages and verbatim reproduction risk
- [ ] Output ownership and commercial-use constraints
- [ ] Watermarking, content credentials, and provenance metadata
### 50.3 Governance and operational controls
- [ ] Model cards, dataset cards, and risk documentation
- [ ] Model release evaluations and risk acceptance
- [ ] Audit trails, incident reporting, and access reviews
- [ ] Regional data residency and cross-border data flows
- [ ] Sector-specific standards and regulatory checks
- [ ] Monitoring policy changes over time

## 51. Synthetic training loops, self-improvement, and knowledge distillation
### 51.1 Synthetic instruction and reasoning data
- [ ] Self-instruct pipelines
- [ ] Teacher-generated demonstrations and explanations
- [ ] Multi-sample solution generation with verification
- [ ] Curriculum and difficulty selection
- [ ] Error-driven counterexample generation
- [ ] Diversity and coverage validation
### 51.2 Self-improvement strategies
- [ ] Rejection sampling fine-tuning (RFT)
- [ ] Iterative SFT and preference optimization cycles
- [ ] Self-play and competitive training setups
- [ ] Critique–revise–verify pipelines
- [ ] Online feedback and data flywheel design
- [ ] Guarding against reward gaming and distribution collapse
### 51.3 Distillation and transfer mechanics
- [ ] Sequence-level distillation from a stronger teacher
- [ ] On-policy versus offline distillation
- [ ] Hidden-state/feature distillation
- [ ] Reasoning compression and short-answer distillation
- [ ] Specialist-to-generalist and generalist-to-specialist transfer
- [ ] Maintaining diversity and avoiding brittle imitation

## 52. LLMOps, observability, testing, and production lifecycle
### 52.1 Experiment management
- [ ] Dataset, prompt, tokenizer, and weight versioning
- [ ] Experiment tracking and artifact registries
- [ ] Reproducibility manifests and environment locking
- [ ] Model cards and evaluation reports
- [ ] CI/CD for prompts, agents, and models
- [ ] Offline eval gates and canary releases
### 52.2 Inference and agent observability
- [ ] Request/response tracing and span correlation
- [ ] Prompt, retrieval, tool, and model-step traces
- [ ] Token usage, TTFT, ITL, throughput, and error rates
- [ ] Quality regression, hallucination, and safety metrics
- [ ] User feedback and annotation queues
- [ ] PII-safe logging, sampling, and redaction
### 52.3 Reliability operations
- [ ] SLIs, SLOs, and service-level agreements
- [ ] Capacity planning, autoscaling, and fallback routing
- [ ] Circuit breakers, timeouts, retries, and graceful degradation
- [ ] Prompt/model drift and scheduled regression tests
- [ ] Postmortems and root-cause analysis
- [ ] Rollback plans and model lifecycle management

## 53. Cost, latency, architecture, and product optimization
### 53.1 Token economics
- [ ] Input, output, cached, and reasoning-token billing
- [ ] Batch discounts and prompt caching
- [ ] Cost per task versus cost per million tokens
- [ ] Context window expansion and hidden cost
- [ ] Model routing and small-model-first cascades
- [ ] Cost–quality–latency Pareto optimization
### 53.2 System architecture choices
- [ ] API-hosted versus self-hosted models
- [ ] On-device, edge, single-GPU, and distributed deployment
- [ ] RAG versus fine-tuning versus long-context prompting
- [ ] Dense versus MoE model choice
- [ ] Multi-model routing, verifier ensembles, and fallbacks
- [ ] Constrained decoding versus prompt-only formatting
### 53.3 Performance engineering
- [ ] Prompt/prefix caching and semantic caching
- [ ] Request coalescing and deduplication
- [ ] GPU memory budget and effective concurrency
- [ ] Tail latency optimization and queuing behavior
- [ ] Speculative decoding and batching ROI
- [ ] Quality validation for quantized/optimized models
### 53.4 Product and UX design
- [ ] Streaming interface and partial-output management
- [ ] Cited answers and source provenance UX
- [ ] Human verification for consequential actions
- [ ] Feedback collection and evaluation loop
- [ ] Failure messaging and trustworthy uncertainty
- [ ] Accessibility, multilingual UX, and interaction modalities

## 54. Research frontiers and unresolved questions
### 54.1 Capability and scaling frontiers
- [ ] Scaling pretraining data and high-quality data scarcity
- [ ] Test-time compute allocation and adaptive deliberation
- [ ] Long-horizon planning and coherent execution
- [ ] Continual learning without catastrophic forgetting
- [ ] Robust out-of-distribution generalization
- [ ] Knowledge updating without full retraining
### 54.2 Architecture frontiers
- [ ] Efficient long-sequence and near-linear attention alternatives
- [ ] Recurrent memory and persistent-state architectures
- [ ] Sparse computation, dynamic routing, and MoE scaling
- [ ] Latent reasoning and nonverbal intermediate representations
- [ ] Native multimodal token/action spaces
- [ ] Hardware-aware architecture co-design
### 54.3 Learning and alignment frontiers
- [ ] Better process supervision and verifier reliability
- [ ] RL with real-world, delayed, or noisy rewards
- [ ] Exploration in long-horizon environments
- [ ] Scalable oversight and automated interpretability
- [ ] Reliable uncertainty estimation and calibrated abstention
- [ ] Secure tool-using autonomy and agentic evaluations
### 54.4 Research methodology
- [ ] Reading model technical reports and paper appendices
- [ ] Separating empirical claims from theoretical claims
- [ ] Identifying baselines, confounders, and ablation requirements
- [ ] Reproduction with limited compute
- [ ] Benchmark construction with contamination controls
- [ ] Reporting variance, confidence intervals, and negative results

## 55. Hands-on implementations and capstone projects
### 55.1 From-scratch components
- [ ] Implement BPE or Unigram tokenizer on a text corpus
- [ ] Implement token embeddings and a causal attention mask
- [ ] Implement MHA, GQA, and RoPE with shape tests
- [ ] Implement LayerNorm/RMSNorm and SwiGLU
- [ ] Build a small decoder-only transformer in PyTorch
- [ ] Train a toy causal LM and monitor perplexity
### 55.2 Training and post-training projects
- [ ] Pretrain a tiny model with packing and mixed precision
- [ ] Implement LoRA and compare with full fine-tuning
- [ ] Run QLoRA SFT on a small instruct dataset
- [ ] Train a pairwise reward model
- [ ] Reproduce DPO on a preference dataset
- [ ] Run a tiny verifiable-reward RL/GRPO experiment
### 55.3 Inference and serving projects
- [ ] Implement naive autoregressive generation
- [ ] Add per-layer KV caching and compare decode speed
- [ ] Derive KV memory for MHA versus GQA versus MLA
- [ ] Serve a model with vLLM or SGLang
- [ ] Benchmark continuous batching and prefix caching
- [ ] Compare FP16, FP8, and INT4 memory/performance
- [ ] Implement and evaluate speculative decoding
### 55.4 RAG and agent projects
- [ ] Build BM25, dense, hybrid, and reranked retrieval baselines
- [ ] Build a citation-grounded document RAG application
- [ ] Evaluate retrieval quality separately from answer quality
- [ ] Build a tool-calling agent with permission checks
- [ ] Implement durable agent state and memory updates
- [ ] Benchmark an agent with deterministic task environments
### 55.5 Research replication and security projects
- [ ] Replicate a positional encoding or attention paper
- [ ] Compare dense versus MoE under controlled compute
- [ ] Audit a benchmark for contamination
- [ ] Analyze reasoning trace faithfulness and verifier failures
- [ ] Build a prompt-injection test corpus and defensive regression suite
- [ ] Profile GPU memory, kernel runtime, and service latency

## 56. Developer tools, libraries, ecosystems, and workflows
### 56.1 Model development libraries
- [ ] PyTorch and torch.compile
- [ ] Hugging Face Transformers, Tokenizers, and Datasets
- [ ] Accelerate, PEFT, and TRL
- [ ] DeepSpeed, FSDP, and Megatron frameworks
- [ ] JAX/Flax and alternate training frameworks
- [ ] Model hubs, safetensors, and checkpoint formats
### 56.2 Model inference and optimization libraries
- [ ] vLLM, SGLang, TensorRT-LLM, and TGI
- [ ] llama.cpp, MLX, ONNX Runtime, and local model tools
- [ ] FlashAttention, FlashInfer, Triton, and kernel tooling
- [ ] GPTQ/AWQ/quantization toolchains
- [ ] Benchmarking and profiling suites
- [ ] Deployment containers and orchestration platforms
### 56.3 Retrieval, orchestration, and evaluation tools
- [ ] FAISS and vector-search libraries
- [ ] OpenSearch/Elasticsearch and hybrid search engines
- [ ] Agent orchestration frameworks and state graphs
- [ ] MCP-compatible tool and resource servers
- [ ] lm-evaluation-harness and custom evaluation runners
- [ ] Tracing, experiment tracking, and quality-monitoring tools
### 56.4 Scientific reading and implementation workflow
- [ ] Original papers versus secondary blog explanations
- [ ] Inspecting official source implementations
- [ ] Minimal reproducible experiments and unit tests
- [ ] Ablation tables and per-experiment hypotheses
- [ ] Version-pinned code, environments, and datasets
- [ ] Maintaining a personal concept index and revision questions

## 57. In-context learning, meta-learning, and capability theory
### 57.1 In-context learning behavior
- [ ] Few-shot learning without weight updates
- [ ] Demonstration selection, order, and label bias
- [ ] Task induction versus pattern matching
- [ ] In-context linear regression and Bayesian interpretations
- [ ] In-context algorithm learning and implicit optimization
- [ ] Context length, example diversity, and generalization
### 57.2 Emergence and capability analysis
- [ ] Induction heads and sequence copying
- [ ] Task vectors and latent task representations
- [ ] Compositional generalization and systematicity
- [ ] Grokking, memorization, and circuit formation
- [ ] Phase transitions and metric-dependent emergence claims
- [ ] Model scaling, data composition, and reasoning transfer
### 57.3 Inference-time adaptation
- [ ] Retrieval as non-parametric adaptation
- [ ] In-context demonstration optimization
- [ ] Test-time training and gradient-based updates
- [ ] Activation steering and temporary state changes
- [ ] Personalization without fine-tuning
- [ ] When to choose ICL versus RAG versus PEFT

## 58. Diffusion and non-autoregressive language models
### 58.1 Alternative generative modeling paradigms
- [ ] Autoregressive versus non-autoregressive text generation
- [ ] Masked token denoising and iterative refinement
- [ ] Discrete diffusion and categorical noising processes
- [ ] Absorbing/mask-state diffusion objectives
- [ ] Continuous-latent diffusion for text and hybrid approaches
- [ ] Diffusion versus causal language-model likelihoods
### 58.2 Training and generation
- [ ] Noise schedules, transition kernels, and denoising losses
- [ ] Iterative unmasking and confidence-based token updates
- [ ] Remasking, blockwise refinement, and parallel token decoding
- [ ] Variable iteration budgets and quality–latency trade-offs
- [ ] Conditioning, infilling, and constrained editing
- [ ] Diffusion-model serving and cache challenges
### 58.3 Models and research questions
- [ ] D3PM and theoretical foundations of discrete diffusion
- [ ] LLaDA/Dream-style masked diffusion language modeling
- [ ] Block diffusion and hybrid autoregressive–diffusion designs
- [ ] Reasoning and planning with iterative denoising
- [ ] Comparisons on throughput, quality, and controllability
- [ ] Evaluation pitfalls and emerging scaling laws

## 59. Midtraining, annealing, and specialization recipes
### 59.1 Training-stage distinctions
- [ ] General pretraining versus midtraining versus post-training
- [ ] Domain upsampling and curated high-quality mixtures
- [ ] Knowledge acquisition versus instruction following
- [ ] Context extension as an intermediate training stage
- [ ] Code/math/reasoning-focused continued pretraining
- [ ] Risk of forgetting general capabilities during specialization
### 59.2 Data-mixture and optimization schedules
- [ ] Data annealing and late-stage high-quality data
- [ ] Token-budget allocation by domain and stage
- [ ] Learning-rate restart versus continued schedule
- [ ] Replay of general data during specialist adaptation
- [ ] Dynamic mixture adjustment by validation loss
- [ ] Checkpoint selection across training transitions
### 59.3 Evaluation of staged training
- [ ] Pretrained base versus midtrained versus aligned checkpoints
- [ ] General and domain-specific capability trade-offs
- [ ] Knowledge retention and transfer benchmarks
- [ ] Measuring gains from curation versus extra compute
- [ ] Stage-ablation experiments and train–serve outcomes
- [ ] Decontamination and time-aware held-out tests

## 60. Computer-use, browser, and GUI agents
### 60.1 Perception and action interfaces
- [ ] Screenshot-based UI grounding
- [ ] DOM/accessibility tree versus visual observations
- [ ] Mouse, keyboard, scroll, and touch action spaces
- [ ] Element localization, coordinate grounding, and scaling
- [ ] Multi-step interaction plans and state tracking
- [ ] Browser sessions, authentication, and isolated execution
### 60.2 Reliability and evaluation
- [ ] Visual state-change detection and action verification
- [ ] Waiting for page loads and asynchronous UI changes
- [ ] Handling popups, captchas, errors, and dynamic layouts
- [ ] Benchmarking web and desktop task completion
- [ ] Recovery from misplaced clicks and navigation errors
- [ ] Human approval for irreversible or sensitive actions
### 60.3 Security and production architecture
- [ ] Web content as untrusted instructions
- [ ] Session sandboxing and permissions
- [ ] Credential handling and secret isolation
- [ ] Auditable interaction traces and replay
- [ ] Rate limits, policy constraints, and termination controls
- [ ] Cross-application workflow design and failure boundaries

---

## D. Reference documentation and coverage checks

These are **taxonomy cross-check sources**, not a requirement to read every page; they help keep the index current. Blog/article rankings can be filled into the table above later.

- [Hugging Face Transformers documentation](https://huggingface.co/docs/transformers/index) — model architectures, preprocessing, generation, training, multimodal support.
- [Hugging Face TRL documentation](https://huggingface.co/docs/trl/index) — SFT, DPO, GRPO, reward models, and other post-training methods.
- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/index) — adapters, LoRA, and parameter-efficient specialization.
- [vLLM documentation](https://docs.vllm.ai/en/latest/) — KV caching, speculative decoding, quantization, scheduling, distributed inference.
- [NVIDIA Megatron Core parallelism guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html) — DP, TP, PP, CP, EP, and sharding.
- [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — standardized LLM benchmark harness.
- [OpenAI Agents SDK guidance](https://developers.openai.com/api/docs/guides/agents/sdk) — agents, state, tools, handoffs, tracing, and approvals.
- [OWASP Top 10 for LLM Applications, 2026](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10) — prompt injection, supply chain, excessive agency, retrieval and data attacks.
- [Discrete diffusion language modeling survey, 2026](https://link.springer.com/article/10.1007/s44336-026-00040-5) — alternatives to causal autoregressive decoding.

## E. Scope boundaries

- This index includes the **LLM-relevant** parts of mathematics, classical ML/NLP, vision, speech, reinforcement learning, distributed systems, and security; it is not a replacement for full standalone curricula in those subjects.
- Named method lists are representative of major approaches, not an endorsement or an exhaustive catalog of every variant/preprint.
- Regulatory and security standards evolve; check the current primary source when applying them.


## F. Medium curation audit

- **Source index:** Entries were manually transcribed from live Medium search results retrieved 9 November 2026. Titles and URLs correspond to result pages; no article URLs were synthetically generated.
- **Clap availability:** Unavailable in the accessible article text for the pages searched, so the proposed 55% clap weighting was not applied. Do not represent #1/#2/#3 as popularity rankings until clap data are measured.
- **Date availability:** Years represent available article publication information; if a year/date is not reliable or a result has crawl-date ambiguity, recheck Medium before citing it academically.
- **Coverage:** All 204 subtopic rows now contain three candidate articles. For specialized areas, the ranking may reuse an appropriate cross-cutting article and should be inspected for exact scope before study.
- **Repetition guard:** Overlap is intentional across adjacent subtopics; do not read an article multiple times.
- **Important:** These are learning-resource recommendations, not fact-checked endorsements of every technical claim made by independent authors. Cross-check math, benchmarks and model specifications with primary papers and documentation.
