# LLM Atlas: Curated Reading Guide

Updated 2026-11-11. 60 of 204 subtopics curated.

Read each list in order: orientation, explanation, implementation, or deeper theory. These are editorial learning paths, not popularity rankings. Sources were inspected through publisher pages or search excerpts; this is not a claim that every technical statement was independently reproduced. Older articles remain where they explain durable foundations. No claim of exhaustive concept coverage is made. Original Medium candidates are retained in the source index, not endorsed by this guide.

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

1. [LLM Course: Introduction](https://huggingface.co/learn/llm-course/chapter1/1) — Hugging Face · Overview. Orient yourself among NLP tasks, model families, and the training workflow.
2. [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — Jay Alammar · Visual guide. Follow tokens through a decoder-only model and understand how next-token predictions are produced.
3. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar · Visual guide. Build intuition for encoder-decoder architecture, attention, positional information, and output probabilities.
4. [On the Opportunities and Risks of Foundation Models](https://crfm.stanford.edu/report.html) — Stanford CRFM · Research overview. Understand the foundation-model framing, adaptation opportunities, and systemic limitations.

### 01.2 End-to-end lifecycle

- [ ] Raw data collection and licensing
- [ ] Data cleaning, deduplication, tokenization, and mixture design
- [ ] Architecture design and compute budgeting
- [ ] Pretraining and continued pretraining
- [ ] Supervised fine-tuning and instruction tuning
- [ ] Preference optimization and reinforcement learning
- [ ] Model evaluation, red-teaming, and release
- [ ] Deployment, monitoring, adaptation, and retirement

1. [LLM Course: Introduction](https://huggingface.co/learn/llm-course/chapter1/1) — Hugging Face · Overview. Orient yourself among NLP tasks, model families, and the training workflow.
2. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.
3. [Building LLM applications for production](https://huyenchip.com/2023/04/11/llm-engineering.html) — Chip Huyen · Engineering article. Connect model capabilities to evaluation, latency, cost, tools, and application design.

### 01.3 Research and industry landscape

- [ ] Landmark model families and their architectural choices
- [ ] Model cards, technical reports, and benchmark caveats
- [ ] Open-weight ecosystems and model hubs
- [ ] Small language models versus frontier-scale models
- [ ] Training-time versus test-time scaling
- [ ] Model capabilities versus system capabilities
- [ ] Generalization, memorization, emergence, and limitations

1. [On the Opportunities and Risks of Foundation Models](https://crfm.stanford.edu/report.html) — Stanford CRFM · Research overview. Understand the foundation-model framing, adaptation opportunities, and systemic limitations.
2. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.
3. [Building LLM applications for production](https://huyenchip.com/2023/04/11/llm-engineering.html) — Chip Huyen · Engineering article. Connect model capabilities to evaluation, latency, cost, tools, and application design.

## 02. Mathematical foundations for LLMs

### 02.1 Linear algebra and tensors

- [ ] Vectors, matrices, tensors, shapes, broadcasting, and Einstein notation
- [ ] Matrix multiplication, batched matmul, transpose, and contractions
- [ ] Dot product, cosine similarity, norms, and normalization
- [ ] Eigenvalues, eigenvectors, SVD, matrix rank, and low-rank approximation
- [ ] Orthogonality, projections, subspaces, and condition number
- [ ] Jacobians, Hessians, and vector–Jacobian products
- [ ] Tensor layouts, strides, contiguity, and memory views

1. [Vectors, Matrices, and Linear Maps](https://www.theorempath.com/topics/vectors-matrices-and-linear-maps) — TheoremPath · Theory. Connect vector spaces, linear transformations, bases, and rank to matrix computations.
2. [Linear Algebra](https://d2l.ai/chapter_preliminaries/linear-algebra.html) — Dive into Deep Learning · Hands-on chapter. Practice tensor shapes, matrix operations, reductions, dot products, and norms in code.
3. [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) — Jay Alammar · Visual guide. Understand learned embeddings, similarity, context prediction, and negative sampling.

### 02.2 Probability and information theory

- [ ] Conditional, joint, and marginal distributions
- [ ] Bayes' theorem, likelihood, and maximum likelihood estimation
- [ ] Categorical distributions, sampling, and Monte Carlo estimates
- [ ] Entropy, cross-entropy, KL divergence, and Jensen–Shannon divergence
- [ ] Mutual information, perplexity, and bits per token/byte
- [ ] Calibration, uncertainty, expected values, and variance
- [ ] Importance sampling, rejection sampling, and distribution shift

1. [Probability and Statistics](https://d2l.ai/chapter_preliminaries/probability.html) — Dive into Deep Learning · Hands-on chapter. Work through random variables, conditional probabilities, expectations, and sampling.
2. [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) — Christopher Olah · Visual guide. Understand entropy, cross-entropy, and KL divergence through probability diagrams.
3. [Generalization](https://d2l.ai/chapter_linear-regression/generalization.html) — Dive into Deep Learning · Theory and practice. Separate training fit from generalization and reason about model capacity and data.

### 02.3 Calculus and numerical methods

- [ ] Chain rule, automatic differentiation, backpropagation, and computation graphs
- [ ] Gradients of softmax, cross-entropy, and layer normalization
- [ ] Log-sum-exp trick and stable softmax
- [ ] Gradient clipping and exploding/vanishing gradients
- [ ] Floating-point rounding, underflow, overflow, and loss scaling
- [ ] Numerical stability, reduction errors, and reproducibility

1. [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/) — Christopher Olah · Visual guide. See why reverse-mode differentiation efficiently accumulates derivatives through a computation graph.
2. [Backpropagation, Intuitions](https://cs231n.github.io/optimization-2/) — Stanford CS231n · Worked tutorial. Trace gradients through scalar and vector operations and implement the chain rule.
3. [Linear Algebra](https://d2l.ai/chapter_preliminaries/linear-algebra.html) — Dive into Deep Learning · Hands-on chapter. Practice tensor shapes, matrix operations, reductions, dot products, and norms in code.

### 02.4 Optimization and scaling mathematics

- [ ] SGD, momentum, Adam, AdamW, and adaptive optimizers
- [ ] Learning-rate schedules, warmup, and cosine decay
- [ ] Weight decay versus L2 regularization
- [ ] Bias–variance, overfitting, generalization, and regularization
- [ ] Gradient noise scale, batch size, and effective batch size
- [ ] FLOPs, memory complexity, bandwidth, and arithmetic intensity

1. [Why Momentum Really Works](https://distill.pub/2017/momentum/) — Gabriel Goh / Distill · Interactive article. Explore how curvature, learning rate, and momentum change optimization trajectories.
2. [An overview of gradient descent optimization algorithms](https://www.ruder.io/optimizing-gradient-descent/) — Sebastian Ruder · Technical article. Compare SGD, momentum, adaptive optimizers, and practical optimization difficulties.
3. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.

## 03. Machine-learning and deep-learning prerequisites

### 03.1 Core learning concepts

- [ ] Supervised, self-supervised, unsupervised, and reinforcement learning
- [ ] Training/validation/test split, leakage, and cross-validation
- [ ] Empirical risk, surrogate losses, and generalization error
- [ ] Distribution shift, out-of-distribution detection, and robustness
- [ ] Feature learning versus manually engineered features
- [ ] Representation learning and transfer learning

1. [Generalization](https://d2l.ai/chapter_linear-regression/generalization.html) — Dive into Deep Learning · Theory and practice. Separate training fit from generalization and reason about model capacity and data.
2. [Neural Networks, Part 2](https://cs231n.github.io/neural-networks-2/) — Stanford CS231n · Practical tutorial. Connect preprocessing, initialization, regularization, and loss functions to training behavior.
3. [Probability and Statistics](https://d2l.ai/chapter_preliminaries/probability.html) — Dive into Deep Learning · Hands-on chapter. Work through random variables, conditional probabilities, expectations, and sampling.

### 03.2 Neural-network foundations

- [ ] MLPs, nonlinear activations, and universal approximation
- [ ] Residual networks and skip connections
- [ ] Layer normalization, RMS normalization, and batch normalization
- [ ] Initialization, parameter sharing, and weight tying
- [ ] Dropout, stochastic depth, and other regularizers
- [ ] Autograd debugging and gradient checks

1. [But what is a Neural Network?](https://www.3blue1brown.com/lessons/neural-networks/) — 3Blue1Brown · Interactive lesson. Build intuition for weights, activations, layers, and learned representations.
2. [Neural Networks, Part 1](https://cs231n.github.io/neural-networks-1/) — Stanford CS231n · Technical tutorial. Understand activations, feed-forward computation, network depth, and representational capacity.
3. [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/) — Christopher Olah · Visual guide. See why reverse-mode differentiation efficiently accumulates derivatives through a computation graph.
4. [Backpropagation, Intuitions](https://cs231n.github.io/optimization-2/) — Stanford CS231n · Worked tutorial. Trace gradients through scalar and vector operations and implement the chain rule.

### 03.3 Learning objectives and transfer

- [ ] Classification, ranking, contrastive, and generative objectives
- [ ] Contrastive representation learning and negative sampling
- [ ] Knowledge transfer, multitask learning, and curriculum learning
- [ ] Data augmentation and invariance
- [ ] Domain adaptation and catastrophic forgetting
- [ ] Calibration and uncertainty-aware decisions

1. [Transfer Learning](https://cs231n.github.io/transfer-learning/) — Stanford CS231n · Practical tutorial. Distinguish frozen feature extraction from fine-tuning; examples use vision networks.
2. [Neural Networks, Part 2](https://cs231n.github.io/neural-networks-2/) — Stanford CS231n · Practical tutorial. Connect preprocessing, initialization, regularization, and loss functions to training behavior.
3. [LLM Course: Introduction](https://huggingface.co/learn/llm-course/chapter1/1) — Hugging Face · Overview. Orient yourself among NLP tasks, model families, and the training workflow.
4. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.

## 04. NLP and language-model evolution

### 04.1 Language and classical NLP

- [ ] Morphology, syntax, semantics, pragmatics, and discourse
- [ ] Language ambiguity, coreference, and compositionality
- [ ] Unicode, normalization, multilingual scripts, and text processing
- [ ] N-gram language models, smoothing, and backoff
- [ ] Bag of words, TF–IDF, and traditional sparse retrieval
- [ ] Word2Vec, CBOW, skip-gram, GloVe, and fastText

1. [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) — Jurafsky & Martin · Open textbook. Use the language-modeling and classical NLP chapters for n-grams, smoothing, syntax, and task foundations.
2. [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) — Jay Alammar · Visual guide. Understand learned embeddings, similarity, context prediction, and negative sampling.
3. [LLM Course: Introduction](https://huggingface.co/learn/llm-course/chapter1/1) — Hugging Face · Overview. Orient yourself among NLP tasks, model families, and the training workflow.

### 04.2 Sequence modeling before transformers

- [ ] Feed-forward neural language models
- [ ] RNN, LSTM, and GRU sequence models
- [ ] Teacher forcing and exposure bias
- [ ] Encoder–decoder sequence-to-sequence learning
- [ ] Additive and multiplicative attention
- [ ] Beam search in classical seq2seq systems

1. [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) — Andrej Karpathy · Article with code. Build intuition for sequence modeling through character-level generation experiments.
2. [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — Christopher Olah · Visual guide. Follow recurrent state and gates to understand long-range credit assignment.
3. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar · Visual guide. Build intuition for encoder-decoder architecture, attention, positional information, and output probabilities.

### 04.3 Foundation-model history

- [ ] ELMo, ULMFiT, and contextual embeddings
- [ ] Transformer, BERT, GPT, T5, and BART paradigms
- [ ] Masked, causal, prefix, and span-corruption objectives
- [ ] Instruction-tuned and chat-oriented models
- [ ] Scaling of language models and multimodal extension

1. [The Illustrated BERT, ELMo, and co.](https://jalammar.github.io/illustrated-bert/) — Jay Alammar · Visual guide. Trace contextual representations and the transition to pretrained NLP transfer learning.
2. [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — Jay Alammar · Visual guide. Follow tokens through a decoder-only model and understand how next-token predictions are produced.
3. [On the Opportunities and Risks of Foundation Models](https://crfm.stanford.edu/report.html) — Stanford CRFM · Research overview. Understand the foundation-model framing, adaptation opportunities, and systemic limitations.

## 05. Pretraining corpora, sources, and dataset design

### 05.1 Data sources and composition

- [ ] Web crawls and Common Crawl-style corpora
- [ ] Books, encyclopedias, academic papers, and educational text
- [ ] Source code, documentation, repositories, and issue trackers
- [ ] Question–answer, dialog, instructional, and tool-use traces
- [ ] Mathematics, proofs, equations, and structured reasoning corpora
- [ ] Multilingual and low-resource language corpora
- [ ] Multimodal text–image–audio–video paired data

1. [FineWeb: decanting the web for the finest text data at scale](https://huggingfacefw-blogpost-fineweb-v1.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Study controlled experiments on web extraction, filtering, deduplication, and educational quality.
2. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.
3. [Nemotron-CC Data Curation](https://docs.nvidia.com/nemotron/0.2.0/nemotron/data/curation/nemotron-cc.html) — NVIDIA · Engineering recipe. Follow a concrete Common Crawl curation pipeline with synthetic-data stages.

### 05.2 Dataset provenance and governance

- [ ] Licenses, terms, consent, and provenance metadata
- [ ] Personally identifiable information and sensitive data
- [ ] Copyrighted content and opt-out handling
- [ ] Data retention, deletion, and audit logs
- [ ] Contamination risk and benchmark overlap
- [ ] Geographic, linguistic, temporal, and demographic coverage

1. [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards) — Hugging Face · Documentation. Document dataset composition, licensing, intended use, and limitations.
2. [FineWeb: decanting the web for the finest text data at scale](https://huggingfacefw-blogpost-fineweb-v1.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Study controlled experiments on web extraction, filtering, deduplication, and educational quality.
3. [Thinking about High-Quality Human Data](https://lilianweng.github.io/posts/2024-02-05-human-data-quality/) — Lilian Weng · Research explainer. Reason about annotation quality, rater agreement, noisy labels, and data selection.
4. [Deduplicating Training Data Makes Language Models Better](https://research.google/pubs/deduplicating-training-data-makes-language-models-better/) — Google Research · Original research. Understand why repeated text affects memorization and evaluation, then follow the released implementation.

### 05.3 Mixture construction

- [ ] Dataset sampling weights and source balancing
- [ ] Temperature sampling and domain reweighting
- [ ] Data quality versus data quantity
- [ ] Repeated-token exposure and epoch accounting
- [ ] Data curriculum, staged mixtures, and annealing
- [ ] General-domain versus specialist data trade-offs

1. [FineWeb: decanting the web for the finest text data at scale](https://huggingfacefw-blogpost-fineweb-v1.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Study controlled experiments on web extraction, filtering, deduplication, and educational quality.
2. [ATLAS: Practical scaling laws for multilingual models](https://www.research.google/blog/atlas-practical-scaling-laws-for-multilingual-models/) — Google Research · Research explainer. Study how language transfer and model size inform multilingual mixture choices.
3. [Scaling laws of learning from repeated data](https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data) — Anthropic · Research article. Examine how excessive repetition can harm training and alter data-budget decisions.
4. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.

## 06. Data processing, quality filtering, and synthesis

### 06.1 Extraction and normalization

- [ ] HTML parsing, boilerplate removal, and document segmentation
- [ ] PDF extraction, tables, equations, and layout-aware parsing
- [ ] Unicode normalization, whitespace, and text encoding
- [ ] Language identification and script detection
- [ ] Line, paragraph, document, and conversation boundaries
- [ ] Broken-text, encoding-error, and malformed-markup detection

1. [FineWeb: decanting the web for the finest text data at scale](https://huggingfacefw-blogpost-fineweb-v1.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Study controlled experiments on web extraction, filtering, deduplication, and educational quality.
2. [DataTrove: composable data-processing pipelines](https://github.com/huggingface/datatrove) — Hugging Face · Implementation guide. Inspect executable extraction, filtering, deduplication, tokenization, and pipeline examples.
3. [Nemotron-CC Data Curation](https://docs.nvidia.com/nemotron/0.2.0/nemotron/data/curation/nemotron-cc.html) — NVIDIA · Engineering recipe. Follow a concrete Common Crawl curation pipeline with synthetic-data stages.

### 06.2 Deduplication and contamination

- [ ] Exact hashes, near-duplicate detection, and MinHash/LSH
- [ ] Semantic deduplication and embedding-based clustering
- [ ] Repetition and template spam detection
- [ ] Train–validation–test overlap detection
- [ ] Benchmark contamination and decontamination
- [ ] Time-aware splits and leakage diagnostics

1. [Deduplicating Training Data Makes Language Models Better](https://research.google/pubs/deduplicating-training-data-makes-language-models-better/) — Google Research · Original research. Understand why repeated text affects memorization and evaluation, then follow the released implementation.
2. [DataTrove: composable data-processing pipelines](https://github.com/huggingface/datatrove) — Hugging Face · Implementation guide. Inspect executable extraction, filtering, deduplication, tokenization, and pipeline examples.
3. [Scaling laws of learning from repeated data](https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data) — Anthropic · Research article. Examine how excessive repetition can harm training and alter data-budget decisions.
4. [FineWeb: decanting the web for the finest text data at scale](https://huggingfacefw-blogpost-fineweb-v1.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Study controlled experiments on web extraction, filtering, deduplication, and educational quality.

### 06.3 Filtering and quality estimation

- [ ] Heuristic, classifier-based, and LLM-based quality filters
- [ ] Toxicity, unsafe content, profanity, and sensitive-data screening
- [ ] Educational-value and reasoning-quality scoring
- [ ] Code compilability, unit tests, and license filtering
- [ ] Multilingual quality scoring and language balance
- [ ] Quality–diversity trade-offs, coverage, and bias

1. [FineWeb: decanting the web for the finest text data at scale](https://huggingfacefw-blogpost-fineweb-v1.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Study controlled experiments on web extraction, filtering, deduplication, and educational quality.
2. [Thinking about High-Quality Human Data](https://lilianweng.github.io/posts/2024-02-05-human-data-quality/) — Lilian Weng · Research explainer. Reason about annotation quality, rater agreement, noisy labels, and data selection.
3. [Nemotron-CC Data Curation](https://docs.nvidia.com/nemotron/0.2.0/nemotron/data/curation/nemotron-cc.html) — NVIDIA · Engineering recipe. Follow a concrete Common Crawl curation pipeline with synthetic-data stages.

### 06.4 Synthetic data and augmentation

- [ ] Self-instruct and instruction generation
- [ ] Paraphrasing, translation, back-translation, and perturbations
- [ ] Synthetic chain-of-thought and solution traces
- [ ] Verifier-based filtering and answer checking
- [ ] Self-play, simulation, and adversarial data generation
- [ ] Model collapse, synthetic-data feedback loops, and diversity controls

1. [Using Llama 3 and distilabel to build fine-tuning datasets](https://huggingface.co/blog/dvilasuero/synthetic-data-with-llama3-distilabel) — Daniel Vila / Hugging Face · Hands-on article. Construct a reproducible synthetic-data pipeline and refine generation quality.
2. [Generate a Preference Dataset with distilabel](https://huggingface.co/learn/cookbook/generate_preference_dataset_distilabel) — Hugging Face · Code walkthrough. Generate and score preference pairs for downstream alignment experiments.
3. [Nemotron-CC Data Curation](https://docs.nvidia.com/nemotron/0.2.0/nemotron/data/curation/nemotron-cc.html) — NVIDIA · Engineering recipe. Follow a concrete Common Crawl curation pipeline with synthetic-data stages.

## 07. Tokenization and text representation

### 07.1 Tokenizer algorithms

- [ ] Character, word, subword, byte, and byte-level tokenization
- [ ] Byte Pair Encoding (BPE) and byte-level BPE
- [ ] WordPiece and Unigram language-model tokenization
- [ ] SentencePiece and whitespace-agnostic processing
- [ ] tiktoken-style vocabulary design and byte fallback
- [ ] Morphology-aware and multilingual tokenizer design

1. [Byte-Pair Encoding tokenization](https://huggingface.co/learn/llm-course/chapter6/5) — Hugging Face · Worked tutorial. Implement frequency-based merges and trace how text becomes subword tokens.
2. [WordPiece tokenization](https://huggingface.co/learn/llm-course/chapter6/6) — Hugging Face · Worked tutorial. Compare WordPiece vocabulary construction and segmentation with BPE.
3. [Unigram tokenization](https://huggingface.co/learn/llm-course/chapter6/7) — Hugging Face · Worked tutorial. Understand probabilistic segmentation and vocabulary pruning.
4. [minbpe: minimal byte-pair encoding](https://github.com/karpathy/minbpe) — Andrej Karpathy · Annotated implementation. Implement byte-level BPE, regex splitting, and special-token handling.

### 07.2 Vocabulary and token semantics

- [ ] Vocabulary size, token frequency, and fertility
- [ ] Special tokens: BOS, EOS, PAD, UNK, MASK, SEP
- [ ] Chat delimiters, role tokens, tool-call tokens, and turn endings
- [ ] FIM/infill tokens and multimodal sentinel tokens
- [ ] Added tokens, token collisions, and reserved IDs
- [ ] Whitespace, capitalization, numerals, emojis, and Unicode edge cases

1. [Byte-Pair Encoding tokenization](https://huggingface.co/learn/llm-course/chapter6/5) — Hugging Face · Worked tutorial. Implement frequency-based merges and trace how text becomes subword tokens.
2. [Chat templates](https://huggingface.co/docs/transformers/chat_templating) — Hugging Face · Practical guide. Understand role delimiters, special tokens, and generation prompts.
3. [WordPiece tokenization](https://huggingface.co/learn/llm-course/chapter6/6) — Hugging Face · Worked tutorial. Compare WordPiece vocabulary construction and segmentation with BPE.

### 07.3 Tokenization engineering

- [ ] Tokenizer training, normalization, pretokenization, and decoding
- [ ] Offsets, token-to-character alignment, and spans
- [ ] Padding, truncation, packing, and padding side
- [ ] Attention masks, loss masks, and shifted labels
- [ ] Tokenizer migration, embedding resize, and compatibility
- [ ] Token counting, API costs, and tokenizer attack surface

1. [Building a tokenizer, block by block](https://huggingface.co/learn/llm-course/chapter6/8) — Hugging Face · Code walkthrough. Assemble normalization, pre-tokenization, token modeling, post-processing, and decoding.
2. [minbpe: minimal byte-pair encoding](https://github.com/karpathy/minbpe) — Andrej Karpathy · Annotated implementation. Implement byte-level BPE, regex splitting, and special-token handling.
3. [How to train a new language model from scratch](https://huggingface.co/blog/how-to-train) — Julien Chaumond / Hugging Face · Hands-on article. Connect a custom tokenizer to model configuration and masked-language-model training.
4. [Chat templates](https://huggingface.co/docs/transformers/chat_templating) — Hugging Face · Practical guide. Understand role delimiters, special tokens, and generation prompts.

## 08. Embeddings and representation geometry

### 08.1 Input and output representations

- [ ] Token embedding lookup and learned embedding matrices
- [ ] Weight tying between embeddings and LM head
- [ ] Embedding scaling and initialization
- [ ] Hidden states, layerwise representations, and anisotropy
- [ ] Contextual versus static embeddings
- [ ] Output logits, vocabulary projection, and logit lens

1. [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) — Jay Alammar · Visual guide. Understand learned embeddings, similarity, context prediction, and negative sampling.
2. [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — Jay Alammar · Visual guide. Follow tokens through a decoder-only model and understand how next-token predictions are produced.
3. [The Illustrated BERT, ELMo, and co.](https://jalammar.github.io/illustrated-bert/) — Jay Alammar · Visual guide. Trace contextual representations and the transition to pretrained NLP transfer learning.

### 08.2 Sentence and document embeddings

- [ ] Mean, CLS, last-token, and weighted pooling
- [ ] Bi-encoders and dual-encoder training
- [ ] Contrastive losses: InfoNCE, triplet, and multiple negatives
- [ ] Embedding normalization and similarity functions
- [ ] Instruction-aware and query/document asymmetric embeddings
- [ ] Multilingual and multimodal embedding spaces

1. [Quickstart: embeddings and rerankers](https://sbert.net/docs/quickstart.html) — Sentence Transformers · Code walkthrough. Compare bi-encoder embeddings with cross-encoder reranking and run similarity examples.
2. [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Sentence Transformers · Practical guide. Distinguish query-document search from symmetric similarity and build a retrieval pipeline.
3. [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka) — Hugging Face · Technical article. Understand nested embedding dimensions and their retrieval cost-quality tradeoffs.

### 08.3 Representation analysis and retrieval

- [ ] Cosine, dot product, and Euclidean distance
- [ ] Nearest-neighbor search and approximate nearest neighbors
- [ ] Embedding dimensions, truncation, and Matryoshka representations
- [ ] Embedding drift, domain shift, and recalibration
- [ ] Embedding evaluation (retrieval, classification, clustering)
- [ ] Semantic similarity versus relevance versus factual entailment

1. [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Sentence Transformers · Practical guide. Distinguish query-document search from symmetric similarity and build a retrieval pipeline.
2. [Hierarchical Navigable Small Worlds](https://www.pinecone.io/learn/series/faiss/hnsw/) — Pinecone · Illustrated engineering guide. Understand graph construction, approximate neighbors, and recall-speed tradeoffs.
3. [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka) — Hugging Face · Technical article. Understand nested embedding dimensions and their retrieval cost-quality tradeoffs.

## 09. Transformer architecture fundamentals

### 09.1 Transformer computation graph

- [ ] Encoder block versus decoder block
- [ ] Input embeddings, positional information, and residual stream
- [ ] Self-attention, cross-attention, and feed-forward sublayers
- [ ] Pre-norm versus post-norm and normalization order
- [ ] Residual connections and layer stacking
- [ ] Vocabulary projection, logits, and language-model loss

1. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar · Visual guide. Build intuition for encoder-decoder architecture, attention, positional information, and output probabilities.
2. [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP · Annotated implementation. Translate attention equations, masks, residual blocks, and training into runnable PyTorch.
3. [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — Jay Alammar · Visual guide. Follow tokens through a decoder-only model and understand how next-token predictions are produced.

### 09.2 Attention math

- [ ] Queries, keys, values, and learned projections
- [ ] Scaled dot-product attention and 1/sqrt(d_k) scaling
- [ ] Attention scores, masking, and softmax
- [ ] Causal, bidirectional, padding, and cross-attention masks
- [ ] Multi-head splitting, reshaping, concatenation, and output projection
- [ ] Tensor-shape derivations for B × T × d
- [ ] Computational and memory complexity of attention

1. [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention/) — 3Blue1Brown · Visual lesson. Visualize queries, keys, values, and the contextual mixing performed by attention.
2. [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP · Annotated implementation. Translate attention equations, masks, residual blocks, and training into runnable PyTorch.
3. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar · Visual guide. Build intuition for encoder-decoder architecture, attention, positional information, and output probabilities.

### 09.3 Training versus autoregressive inference

- [ ] Parallel teacher-forced training and shifted targets
- [ ] Autoregressive next-token generation
- [ ] Prefill versus decode computation
- [ ] Causal masks with variable sequence lengths
- [ ] Attention KV reuse and incremental decoding
- [ ] Sequence packing and document boundary isolation

1. [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — Jay Alammar · Visual guide. Follow tokens through a decoder-only model and understand how next-token predictions are produced.
2. [How caching works](https://huggingface.co/docs/transformers/cache_explanation) — Hugging Face · Technical guide. Understand why autoregressive decoding reuses keys and values and how masks change.
3. [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP · Annotated implementation. Translate attention equations, masks, residual blocks, and training into runnable PyTorch.

## 10. Attention mechanisms and variants

### 10.1 Head organization

- [ ] Multi-head attention (MHA)
- [ ] Multi-query attention (MQA)
- [ ] Grouped-query attention (GQA)
- [ ] Multi-head latent attention (MLA)
- [ ] Multi-scale, multi-granular, and heterogeneous heads
- [ ] Head dimensions, KV-head counts, and head pruning

1. [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention/) — 3Blue1Brown · Visual lesson. Visualize queries, keys, values, and the contextual mixing performed by attention.
2. [Grouped-Query Attention](https://www.sebastianraschka.com/llms-from-scratch/ch04/04_gqa/) — Sebastian Raschka · From-scratch guide. Implement shared key-value heads and quantify KV-cache memory savings.
3. [Multi-Query Attention is All You Need](https://fireworks.ai/blog/multi-query-attention-is-all-you-need?rp=3) — Fireworks AI · Engineering article. Connect head sharing to memory bandwidth, serving throughput, and implementation details.

### 10.2 Attention pattern variants

- [ ] Local, sliding-window, and dilated attention
- [ ] Block-sparse and global–local attention
- [ ] BigBird, Longformer, and sparse transformer patterns
- [ ] Sink tokens, attention sinks, and global memory tokens
- [ ] Linearized/kernel attention and approximation limits
- [ ] Cross-attention and bidirectional conditioning

1. [Sliding Window Attention](https://sebastianraschka.com/llm-architecture-gallery/swa/) — Sebastian Raschka · Architecture explainer. Distinguish local attention windows from full-prefix attention and head sharing.
2. [The Transformer Family Version 2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — Lilian Weng · Research explainer. Compare positional schemes, sparse patterns, recurrence, and adaptive-depth transformers.
3. [Sparse Attention and Long Context](https://www.theorempath.com/topics/sparse-attention-and-long-context) — TheoremPath · Theory guide. Study sparse patterns, distributed attention, streaming, and context-extension limitations.

### 10.3 Novel and hybrid attention ideas

- [ ] Differential attention and attention-score modifications
- [ ] Talking-heads and gated attention
- [ ] Multi-latent and compressed attention representations
- [ ] Multi-dimensional and grouped-query attention trade-offs
- [ ] Attention-free and recurrent alternatives
- [ ] Combining full attention with local/recurrent layers

1. [Multi-Head Latent Attention](https://sebastianraschka.com/llm-architecture-gallery/mla/) — Sebastian Raschka · Architecture explainer. Understand compressed key-value representations and their cache tradeoffs.
2. [Hybrid Attention](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/) — Sebastian Raschka · Architecture explainer. Examine designs combining different attention mechanisms within one model.
3. [State Space Duality: Mamba-2, Part I](https://tridao.me/blog/2024/mamba2-part1-model/) — Tri Dao · Author explanation. Relate selective state spaces to attention through the SSD formulation.
4. [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — Sebastian Raschka / Ahead of AI · Illustrated article. Compare real models' attention, feed-forward, normalization, and parameter-allocation choices.

## 11. Positional information and context length

### 11.1 Position encoding families

- [ ] Absolute learned positional embeddings
- [ ] Sinusoidal positional encodings
- [ ] Relative positional encodings and relative biases
- [ ] ALiBi and attention-bias methods
- [ ] Rotary positional embeddings (RoPE)
- [ ] Complex-number and rotation-matrix view of RoPE
- [ ] Multi-axis and multimodal positional encoding

1. [You could have designed state of the art positional encoding](https://huggingface.co/blog/designing-positional-encoding) — Christopher Fleetwood / Hugging Face · Visual derivation. Derive positional representations from simple requirements and build toward rotary embeddings.
2. [The Transformer Family Version 2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — Lilian Weng · Research explainer. Compare positional schemes, sparse patterns, recurrence, and adaptive-depth transformers.
3. [How LLMs Scaled from 512 to 2M Context](https://amaarora.github.io/posts/2025-09-21-rope-context-extension.html) — Aman Arora · Math and code. Work through RoPE frequencies, interpolation, NTK scaling, and YaRN implementations.

### 11.2 RoPE and extrapolation details

- [ ] Base frequencies, theta, wavelength, and head dimension
- [ ] Rotation on Q and K and relative-position identity
- [ ] RoPE scaling and position interpolation
- [ ] NTK-aware scaling, YaRN, and LongRoPE approaches
- [ ] Extrapolation versus interpolation and failure modes
- [ ] Position-ID offsets, packed sequences, and KV-cache compatibility

1. [You could have designed state of the art positional encoding](https://huggingface.co/blog/designing-positional-encoding) — Christopher Fleetwood / Hugging Face · Visual derivation. Derive positional representations from simple requirements and build toward rotary embeddings.
2. [How LLMs Scaled from 512 to 2M Context](https://amaarora.github.io/posts/2025-09-21-rope-context-extension.html) — Aman Arora · Math and code. Work through RoPE frequencies, interpolation, NTK scaling, and YaRN implementations.
3. [How caching works](https://huggingface.co/docs/transformers/cache_explanation) — Hugging Face · Technical guide. Understand why autoregressive decoding reuses keys and values and how masks change.

### 11.3 Long-context learning

- [ ] Context extension by continued training
- [ ] Long-sequence data synthesis and packing
- [ ] Lost-in-the-middle and positional bias
- [ ] Needle-in-a-haystack versus multi-hop long-context retrieval
- [ ] Effective context window versus advertised context length
- [ ] Long-context attention alternatives and segment recurrence
- [ ] Long-context evaluation and memory–compute bottlenecks

1. [How LLMs Scaled from 512 to 2M Context](https://amaarora.github.io/posts/2025-09-21-rope-context-extension.html) — Aman Arora · Math and code. Work through RoPE frequencies, interpolation, NTK scaling, and YaRN implementations.
2. [Sparse Attention and Long Context](https://www.theorempath.com/topics/sparse-attention-and-long-context) — TheoremPath · Theory guide. Study sparse patterns, distributed attention, streaming, and context-extension limitations.
3. [The Transformer Family Version 2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — Lilian Weng · Research explainer. Compare positional schemes, sparse patterns, recurrence, and adaptive-depth transformers.

## 12. Transformer blocks, normalization, and activation design

### 12.1 Feed-forward network design

- [ ] Positionwise MLP/FFN expansion and contraction
- [ ] ReLU, GELU, SiLU/Swish, and gated activations
- [ ] GLU, GEGLU, and SwiGLU
- [ ] FFN expansion ratio and parameter budgeting
- [ ] Weight tying, factorization, and depth/width trade-offs

1. [How might LLMs store facts?](https://www.3blue1brown.com/lessons/mlp/) — 3Blue1Brown · Visual lesson. Understand transformer feed-forward computations and one interpretation of how facts may be represented.
2. [SiLU / Swish](https://sebastianraschka.com/llms-from-scratch/ch04/11_silu/) — Sebastian Raschka · Implementation guide. Examine the smooth activation used inside modern gated feed-forward blocks.
3. [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP · Annotated implementation. Translate attention equations, masks, residual blocks, and training into runnable PyTorch.
4. [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — Sebastian Raschka / Ahead of AI · Illustrated article. Compare real models' attention, feed-forward, normalization, and parameter-allocation choices.

### 12.2 Normalization and residual topology

- [ ] LayerNorm versus RMSNorm
- [ ] Pre-LN, Post-LN, and sandwich normalization
- [ ] Residual scaling and deep-network stability
- [ ] QK normalization and attention logit control
- [ ] Bias-free and bias-containing projections
- [ ] Initialization and stabilization of very deep transformers

1. [RMSNorm](https://sebastianraschka.com/llms-from-scratch/ch04/09_rmsnorm/) — Sebastian Raschka · Implementation guide. Compare RMS-based rescaling with LayerNorm and inspect the normalization code.
2. [QK-Norm](https://sebastianraschka.com/llm-architecture-gallery/qk-norm/) — Sebastian Raschka · Architecture explainer. See how normalizing queries and keys controls attention-logit scale.
3. [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP · Annotated implementation. Translate attention equations, masks, residual blocks, and training into runnable PyTorch.

### 12.3 Structural design choices

- [ ] Parallel versus sequential attention/FFN blocks
- [ ] Shared versus separate input/output embeddings
- [ ] Weight sharing across layers and recurrent depth
- [ ] Layer dropping, early exits, and adaptive depth
- [ ] Multi-token prediction heads and auxiliary losses
- [ ] Memory tokens and architectural conditioning

1. [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — Sebastian Raschka / Ahead of AI · Illustrated article. Compare real models' attention, feed-forward, normalization, and parameter-allocation choices.
2. [The Transformer Family Version 2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — Lilian Weng · Research explainer. Compare positional schemes, sparse patterns, recurrence, and adaptive-depth transformers.
3. [Beyond Standard LLMs](https://magazine.sebastianraschka.com/p/beyond-standard-llms) — Sebastian Raschka / Ahead of AI · Research explainer. Explore alternatives to conventional transformers and their architectural tradeoffs.

## 13. Architecture families beyond standard decoder-only LLMs

### 13.1 Transformer family variants

- [ ] Decoder-only causal LMs
- [ ] Encoder-only masked language models
- [ ] Encoder–decoder text-to-text models
- [ ] Prefix language models and infilling architectures
- [ ] Retrieval-augmented language-model architectures
- [ ] Prefix conditioning and multimodal decoder variants

1. [The Illustrated BERT, ELMo, and co.](https://jalammar.github.io/illustrated-bert/) — Jay Alammar · Visual guide. Trace contextual representations and the transition to pretrained NLP transfer learning.
2. [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — Jay Alammar · Visual guide. Follow tokens through a decoder-only model and understand how next-token predictions are produced.
3. [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP · Annotated implementation. Translate attention equations, masks, residual blocks, and training into runnable PyTorch.
4. [The Transformer Family Version 2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — Lilian Weng · Research explainer. Compare positional schemes, sparse patterns, recurrence, and adaptive-depth transformers.

### 13.2 Recurrence and state-space alternatives

- [ ] Recurrent language models and persistent hidden state
- [ ] State-space models and selective state spaces (Mamba family)
- [ ] RWKV and attention-free recurrent variants
- [ ] Retention and RetNet-style mechanisms
- [ ] xLSTM and gated recurrent alternatives
- [ ] Convolutional/long-filter sequence models

1. [The Annotated S4](https://srush.github.io/annotated-s4/) — Sasha Rush & Sidd Karamcheti · Annotated implementation. Connect state-space equations to recurrent and convolutional implementations in JAX.
2. [State Space Duality: Mamba-2, Part I](https://tridao.me/blog/2024/mamba2-part1-model/) — Tri Dao · Author explanation. Relate selective state spaces to attention through the SSD formulation.
3. [Beyond Standard LLMs](https://magazine.sebastianraschka.com/p/beyond-standard-llms) — Sebastian Raschka / Ahead of AI · Research explainer. Explore alternatives to conventional transformers and their architectural tradeoffs.

### 13.3 Hybrid and adaptive computation

- [ ] Transformer–SSM and attention–recurrence hybrids
- [ ] Mixture of depths and adaptive computation time
- [ ] Dynamic layer skipping and early exit
- [ ] Token pruning, token merging, and token routing
- [ ] Recurrent memory and compressed context models
- [ ] Architecture search and train–serve co-design

1. [Hybrid Attention](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/) — Sebastian Raschka · Architecture explainer. Examine designs combining different attention mechanisms within one model.
2. [Beyond Standard LLMs](https://magazine.sebastianraschka.com/p/beyond-standard-llms) — Sebastian Raschka / Ahead of AI · Research explainer. Explore alternatives to conventional transformers and their architectural tradeoffs.
3. [The Transformer Family Version 2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — Lilian Weng · Research explainer. Compare positional schemes, sparse patterns, recurrence, and adaptive-depth transformers.

## 14. Mixture-of-experts (MoE) and sparsity

### 14.1 MoE fundamentals

- [ ] Dense FFN versus sparse expert FFNs
- [ ] Token-choice routing and top-k expert selection
- [ ] Router logits, softmax, and gating gradients
- [ ] Shared experts versus routed experts
- [ ] Active parameters versus total parameters
- [ ] Capacity factors, dropped tokens, and overflow handling

1. [Mixture of Experts Explained](https://huggingface.co/blog/moe) — Hugging Face · Technical explainer. Understand routers, active parameters, load balancing, capacity, and fine-tuning tradeoffs.
2. [makeMoE: a sparse MoE language model from scratch](https://huggingface.co/blog/AviSoori1x/makemoe-from-scratch) — Avinash Sooriyarachchi · Code walkthrough. Build expert modules, noisy top-k routing, and a complete sparse language model.
3. [Applying Mixture of Experts in LLM Architectures](https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/) — NVIDIA · Engineering article. Connect routing decisions and expert activation patterns to practical model behavior.

### 14.2 Training and routing mechanics

- [ ] Load-balancing auxiliary losses
- [ ] Router entropy, z-loss, and stability
- [ ] Expert specialization, redundancy, and collapse
- [ ] Expert-choice routing and alternative assignment schemes
- [ ] Fine-grained expert segmentation and expert grouping
- [ ] Noisy routing, token dispatch, and expert parallelism

1. [makeMoE: a sparse MoE language model from scratch](https://huggingface.co/blog/AviSoori1x/makemoe-from-scratch) — Avinash Sooriyarachchi · Code walkthrough. Build expert modules, noisy top-k routing, and a complete sparse language model.
2. [Mixture of Experts Explained](https://huggingface.co/blog/moe) — Hugging Face · Technical explainer. Understand routers, active parameters, load balancing, capacity, and fine-tuning tradeoffs.
3. [Applying Mixture of Experts in LLM Architectures](https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/) — NVIDIA · Engineering article. Connect routing decisions and expert activation patterns to practical model behavior.
4. [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — Sebastian Raschka / Ahead of AI · Illustrated article. Compare real models' attention, feed-forward, normalization, and parameter-allocation choices.

### 14.3 MoE inference and adaptation

- [ ] All-to-all communication and load imbalance
- [ ] Expert caching, offloading, and hot-expert placement
- [ ] Expert quantization and heterogeneous precision
- [ ] Expert parallel deployment and batch utilization
- [ ] Expert merging, pruning, and distillation
- [ ] Multi-LoRA expert mixtures and task-conditioned routing

1. [Mixture of Experts Explained](https://huggingface.co/blog/moe) — Hugging Face · Technical explainer. Understand routers, active parameters, load balancing, capacity, and fine-tuning tradeoffs.
2. [Mixture of Experts Inference](https://www.deepspeed.ai/tutorials/mixture-of-experts-inference/) — DeepSpeed · Implementation guide. Configure expert-parallel inference and understand deployment requirements.
3. [The Ultra-Scale Playbook](https://nanotron-ultrascale-playbook.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Work through memory, communication, and combinations of distributed-training parallelism.

## 15. Scaling laws, compute, and model design

### 15.1 Empirical scaling behavior

- [ ] Parameter, data, and compute scaling laws
- [ ] Compute-optimal training and Chinchilla-style trade-offs
- [ ] Kaplan-style loss scaling and data regimes
- [ ] Scaling versus downstream task performance
- [ ] Test-time scaling and inference budget allocation
- [ ] Diminishing returns and benchmark saturation

1. [Scaling Laws](https://theorempath.com/topics/scaling-laws) — TheoremPath · Theory guide. Compare Kaplan and Chinchilla fits, data repetition, emergence claims, and extrapolation limits.
2. [An empirical analysis of compute-optimal large language model training](https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/) — Google DeepMind · Research explainer. See why parameter count and training-token budget must be chosen together.
3. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Kaplan et al. · Original research. Inspect the original fitted relationships and assumptions rather than treating scaling laws as universal rules.

### 15.2 Model and compute budgeting

- [ ] Parameters and training FLOP estimators
- [ ] Tokens per parameter and repeated epochs
- [ ] Effective batch size and sequence length trade-offs
- [ ] Dense versus MoE compute/quality trade-offs
- [ ] Training from scratch versus continued pretraining
- [ ] GPU utilization, MFU, throughput, and wall-clock cost

1. [An empirical analysis of compute-optimal large language model training](https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/) — Google DeepMind · Research explainer. See why parameter count and training-token budget must be chosen together.
2. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.
3. [The Ultra-Scale Playbook](https://nanotron-ultrascale-playbook.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Work through memory, communication, and combinations of distributed-training parallelism.
4. [Scaling laws of learning from repeated data](https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data) — Anthropic · Research article. Examine how excessive repetition can harm training and alter data-budget decisions.

### 15.3 Research design questions

- [ ] Model size, depth, width, and head-count selection
- [ ] Context length versus attention cost
- [ ] Data diversity versus extra training tokens
- [ ] Longer training versus post-training investment
- [ ] Smaller specialized models versus larger general models
- [ ] Scaling failures, emergent behavior claims, and causal confounders

1. [Scaling Laws](https://theorempath.com/topics/scaling-laws) — TheoremPath · Theory guide. Compare Kaplan and Chinchilla fits, data repetition, emergence claims, and extrapolation limits.
2. [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — Sebastian Raschka / Ahead of AI · Illustrated article. Compare real models' attention, feed-forward, normalization, and parameter-allocation choices.
3. [An empirical analysis of compute-optimal large language model training](https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/) — Google DeepMind · Research explainer. See why parameter count and training-token budget must be chosen together.

## 16. Pretraining objectives and objectives beyond next-token prediction

### 16.1 Core LM objectives

- [ ] Autoregressive causal language modeling
- [ ] Masked language modeling
- [ ] Span corruption and denoising autoencoding
- [ ] Prefix language modeling
- [ ] Sequence-to-sequence denoising objectives
- [ ] Fill-in-the-middle (FIM) and code infilling

1. [Causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling) — Hugging Face · Code walkthrough. Prepare token blocks and labels, train a next-token model, and evaluate its loss.
2. [Masked language modeling](https://huggingface.co/docs/transformers/tasks/masked_language_modeling) — Hugging Face · Code walkthrough. Build masked-token training data and compare its objective with causal prediction.
3. [Exploring Transfer Learning with T5](https://research.google/blog/exploring-transfer-learning-with-t5-the-text-to-text-transfer-transformer/) — Google Research · Research explainer. Compare text-to-text tasks, denoising objectives, and transfer-learning choices.
4. [Efficient Training of Language Models to Fill in the Middle](https://arxiv.org/abs/2207.14255) — Bavarian et al. · Original research. Understand prefix-suffix-middle transformations and the infilling training objective.

### 16.2 Specialized and auxiliary objectives

- [ ] Multi-token prediction and multiple prediction heads
- [ ] Contrastive and discriminative auxiliary objectives
- [ ] Document coherence and next-segment objectives
- [ ] Retrieval or grounded-generation auxiliary tasks
- [ ] Instruction-aware continued pretraining
- [ ] Multimodal next-token and joint-token prediction

1. [Better & Faster Large Language Models via Multi-token Prediction](https://arxiv.org/abs/2404.19737) — Gloeckle et al. · Original research. Study auxiliary future-token heads and their effects on learning and inference.
2. [Exploring Transfer Learning with T5](https://research.google/blog/exploring-transfer-learning-with-t5-the-text-to-text-transfer-transformer/) — Google Research · Research explainer. Compare text-to-text tasks, denoising objectives, and transfer-learning choices.
3. [The Illustrated BERT, ELMo, and co.](https://jalammar.github.io/illustrated-bert/) — Jay Alammar · Visual guide. Trace contextual representations and the transition to pretrained NLP transfer learning.

### 16.3 Objective mechanics

- [ ] Teacher forcing and exposure bias
- [ ] Shifted labels and ignore-index masks
- [ ] Cross-entropy, label smoothing, and loss weighting
- [ ] Packing-aware per-token versus per-document normalization
- [ ] Vocabulary loss and rare-token learning
- [ ] Perplexity interpretation across tokenizers

1. [Causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling) — Hugging Face · Code walkthrough. Prepare token blocks and labels, train a next-token model, and evaluate its loss.
2. [Perplexity of fixed-length models](https://huggingface.co/docs/transformers/perplexity) — Hugging Face · Technical guide. Compute sliding-window perplexity and understand context-length and tokenizer comparability pitfalls.
3. [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP · Annotated implementation. Translate attention equations, masks, residual blocks, and training into runnable PyTorch.

## 17. Pretraining optimization and experimental practice

### 17.1 Training-loop implementation

- [ ] Forward, loss, backward, optimizer step, and scheduler step
- [ ] Gradient accumulation and microbatching
- [ ] AdamW settings, betas, epsilon, and weight decay
- [ ] Learning-rate warmup, decay, and cooldown
- [ ] Gradient norm monitoring, clipping, and anomaly detection
- [ ] Dropout, regularization, and mixed-precision training

1. [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — Andrej Karpathy · Practical article. Debug data, establish baselines, overfit a tiny batch, and add complexity deliberately.
2. [nanoGPT](https://github.com/karpathy/nanoGPT) — Andrej Karpathy · Compact implementation. Read a complete GPT training loop with accumulation, scheduling, checkpointing, and distributed execution.
3. [An overview of gradient descent optimization algorithms](https://www.ruder.io/optimizing-gradient-descent/) — Sebastian Ruder · Technical article. Compare SGD, momentum, adaptive optimizers, and practical optimization difficulties.

### 17.2 Stability and debugging

- [ ] Loss spikes, gradient explosions, and divergence
- [ ] NaNs, infinities, overflow, and optimizer-state corruption
- [ ] Activation statistics and initialization sensitivity
- [ ] Batch-size changes and optimization rescaling
- [ ] Data-quality anomalies and anomalous batches
- [ ] Seed control, determinism, and reproducibility

1. [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — Andrej Karpathy · Practical article. Debug data, establish baselines, overfit a tiny batch, and add complexity deliberately.
2. [Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html) — PyTorch · Engineering guide. Identify randomness sources and the costs and limits of deterministic execution.
3. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.

### 17.3 Training stages and checkpoints

- [ ] Warmup, steady-state training, and cooldown
- [ ] Stagewise data-mixture changes
- [ ] Continued pretraining and domain-adaptive pretraining
- [ ] Checkpoint frequency, retention, and restart
- [ ] Optimizer-state checkpointing and resumption fidelity
- [ ] Intermediate evaluation and checkpoint selection

1. [Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html) — PyTorch · Practical tutorial. Save model and optimizer state and distinguish inference loading from training resumption.
2. [nanoGPT](https://github.com/karpathy/nanoGPT) — Andrej Karpathy · Compact implementation. Read a complete GPT training loop with accumulation, scheduling, checkpointing, and distributed execution.
3. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.

## 18. Training hardware and distributed systems

### 18.1 Accelerator and memory fundamentals

- [ ] GPUs, TPUs, NPUs, and accelerator memory hierarchies
- [ ] HBM, cache, PCIe, NVLink, InfiniBand, and network topology
- [ ] Compute-bound versus memory-bandwidth-bound kernels
- [ ] GPU occupancy, warp execution, and kernel launch overhead
- [ ] BF16, FP16, FP8, and lower-precision training
- [ ] Activation, parameter, gradient, and optimizer-state memory

1. [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) — Google DeepMind authors · Systems textbook. Relate accelerator hardware, communication, model math, and training or inference costs.
2. [The Ultra-Scale Playbook](https://nanotron-ultrascale-playbook.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Work through memory, communication, and combinations of distributed-training parallelism.
3. [Introducing Fully Sharded Data Parallel](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/) — PyTorch · Engineering article. Understand how sharding parameters, gradients, and optimizer state reduces per-device memory.

### 18.2 Parallelism strategies

- [ ] Data parallelism and distributed data parallel (DDP)
- [ ] Tensor parallelism
- [ ] Pipeline parallelism and pipeline bubbles
- [ ] Sequence parallelism and context parallelism
- [ ] Expert parallelism for MoE
- [ ] ZeRO optimizer stages and FSDP sharding
- [ ] 3D/4D/5D parallelism combinations

1. [The Ultra-Scale Playbook](https://nanotron-ultrascale-playbook.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Work through memory, communication, and combinations of distributed-training parallelism.
2. [Introducing Fully Sharded Data Parallel](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/) — PyTorch · Engineering article. Understand how sharding parameters, gradients, and optimizer state reduces per-device memory.
3. [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) — Google DeepMind authors · Systems textbook. Relate accelerator hardware, communication, model math, and training or inference costs.

### 18.3 Memory and runtime optimization

- [ ] Gradient checkpointing / activation recomputation
- [ ] CPU/NVMe optimizer and parameter offloading
- [ ] FlashAttention and fused training kernels
- [ ] Sequence packing, bucketing, and dynamic batching
- [ ] Fused optimizers, fused normalization, and fused MLPs
- [ ] Distributed checkpointing and sharded state

1. [Current and New Activation Checkpointing Techniques](https://pytorch.org/blog/activation-checkpointing-techniques/) — PyTorch · Engineering article. Visualize the memory-compute tradeoff of recomputation and selective checkpointing.
2. [The Ultra-Scale Playbook](https://nanotron-ultrascale-playbook.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Work through memory, communication, and combinations of distributed-training parallelism.
3. [Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html) — PyTorch · Practical tutorial. Save model and optimizer state and distinguish inference loading from training resumption.

### 18.4 Operational training infrastructure

- [ ] PyTorch distributed, DeepSpeed, Megatron, FSDP, and JAX ecosystems
- [ ] Cluster scheduling, job orchestration, and preemption
- [ ] Fault tolerance, elastic training, and restart strategies
- [ ] Data-loader throughput and streaming data pipelines
- [ ] Performance profiling, traces, and bottleneck diagnosis
- [ ] Energy usage, utilization, cost, and carbon accounting

1. [The Ultra-Scale Playbook](https://nanotron-ultrascale-playbook.static.hf.space/index.html) — Hugging Face · Engineering deep dive. Work through memory, communication, and combinations of distributed-training parallelism.
2. [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/) — Hugging Face · Engineering deep dive. Follow a real model through data decisions, pretraining, post-training, and infrastructure debugging.
3. [Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html) — PyTorch · Engineering guide. Identify randomness sources and the costs and limits of deterministic execution.

## 19. Fine-tuning, adaptation, and transfer learning

### 19.1 Fine-tuning paradigms

- [ ] Full-parameter fine-tuning
- [ ] Continued pretraining versus task fine-tuning
- [ ] Instruction fine-tuning and conversational adaptation
- [ ] Domain-adaptive and task-adaptive fine-tuning
- [ ] Multitask fine-tuning and dataset mixtures
- [ ] Continual learning, catastrophic forgetting, and replay

1. [Transfer Learning](https://cs231n.github.io/transfer-learning/) — Stanford CS231n · Practical tutorial. Distinguish frozen feature extraction from fine-tuning; examples use vision networks.
2. [Practical Tips for Finetuning LLMs Using LoRA](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms) — Sebastian Raschka / Ahead of AI · Experimental article. Evaluate LoRA ranks, target layers, precision choices, and adaptation tradeoffs.
3. [How to train a new language model from scratch](https://huggingface.co/blog/how-to-train) — Julien Chaumond / Hugging Face · Hands-on article. Connect a custom tokenizer to model configuration and masked-language-model training.

### 19.2 Parameter-efficient fine-tuning (PEFT)

- [ ] Low-rank adaptation (LoRA) mathematics
- [ ] LoRA rank, scaling alpha, target modules, and dropout
- [ ] QLoRA and quantized frozen backbones
- [ ] DoRA, AdaLoRA, rsLoRA, and low-rank variants
- [ ] IA3, adapters, prefix tuning, and prompt tuning
- [ ] BitFit, selective fine-tuning, and layer freezing

1. [Practical Tips for Finetuning LLMs Using LoRA](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms) — Sebastian Raschka / Ahead of AI · Experimental article. Evaluate LoRA ranks, target layers, precision choices, and adaptation tradeoffs.
2. [Making LLMs even more accessible with 4-bit quantization and QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes) — Hugging Face & bitsandbytes · Technical tutorial. Understand frozen quantized weights, low-rank adapters, and memory-efficient fine-tuning.
3. [LoRA configuration and methods](https://huggingface.co/docs/peft/developer_guides/lora) — Hugging Face PEFT · Implementation reference. Inspect ranks, target modules, scaling, initialization, and supported adapter variants.

### 19.3 Adapter composition and deployment

- [ ] LoRA merging and unmerging
- [ ] Multi-adapter serving and adapter hot swapping
- [ ] Task arithmetic and model merging
- [ ] TIES, DARE, and merging conflicts
- [ ] Mixtures of adapters, gating, and routing
- [ ] Adapter interpolation, transfer, and interference

1. [PEFT welcomes new merging methods](https://huggingface.co/blog/peft_merging) — Hugging Face · Engineering tutorial. Compare adapter merging strategies including task arithmetic, TIES, and DARE.
2. [Hotswapping adapters](https://huggingface.co/docs/peft/developer_guides/hotswapping) — Hugging Face PEFT · Implementation guide. Swap LoRA adapters in a running model and understand compilation constraints.
3. [LoRA configuration and methods](https://huggingface.co/docs/peft/developer_guides/lora) — Hugging Face PEFT · Implementation reference. Inspect ranks, target modules, scaling, initialization, and supported adapter variants.

### 19.4 Fine-tuning quality controls

- [ ] Chat template and tokenizer consistency
- [ ] Loss masking on user/system versus assistant tokens
- [ ] Response-only versus full-conversation loss
- [ ] Packing, truncation, and EOS correctness
- [ ] Overfitting, forgetting, and generality regression tests
- [ ] Fine-tuning hyperparameter sweeps and reproducibility

Reading-list review pending; see the original index for candidate links.

## 20. Instruction tuning and supervised post-training (SFT)

### 20.1 Instruction datasets

- [ ] Instruction–response pairs and multi-turn conversations
- [ ] System, developer, user, assistant, and tool-message roles
- [ ] Chat templates and message serialization
- [ ] Task diversity, difficulty, and data balancing
- [ ] Human-written versus synthetic demonstrations
- [ ] Refusal, safety, format-following, and tool-call examples

Reading-list review pending; see the original index for candidate links.

### 20.2 SFT objectives and methods

- [ ] Token-level negative log likelihood
- [ ] Assistant-response loss masking
- [ ] Full-sequence versus completion-only SFT
- [ ] Multi-turn context windows and conversational packing
- [ ] Curriculum and quality-weighted SFT
- [ ] Multi-objective SFT and auxiliary losses

Reading-list review pending; see the original index for candidate links.

### 20.3 SFT failure modes and evaluation

- [ ] Style imitation versus genuine capability gain
- [ ] Hallucinations induced by weak demonstrations
- [ ] Over-refusal and under-refusal
- [ ] Instruction hierarchy confusion
- [ ] Catastrophic forgetting of pretrained capabilities
- [ ] Distribution mismatch between training and usage

Reading-list review pending; see the original index for candidate links.

## 21. Preference learning, reward modeling, and RLHF

### 21.1 Human preference data

- [ ] Pairwise chosen–rejected responses
- [ ] Preference annotation rubrics and inter-rater agreement
- [ ] Bradley–Terry and pairwise choice models
- [ ] Helpfulness, harmlessness, honesty, and task-specific rewards
- [ ] Preference noise, position bias, and annotator disagreement
- [ ] Online versus offline preference collection

Reading-list review pending; see the original index for candidate links.

### 21.2 Reward-model training

- [ ] Scalar reward models and pairwise ranking loss
- [ ] Process reward models versus outcome reward models
- [ ] Verifiable rewards versus learned rewards
- [ ] Reward-model calibration and uncertainty
- [ ] Reward hacking, specification gaming, and overoptimization
- [ ] Reward ensemble models and disagreement detection

Reading-list review pending; see the original index for candidate links.

### 21.3 Classical RLHF pipeline

- [ ] SFT initialization, reward model, and policy optimization
- [ ] PPO objective, advantage estimation, and clipping
- [ ] KL penalty to a reference policy
- [ ] Policy–value model roles and critic training
- [ ] Rollouts, generation sampling, and sequence rewards
- [ ] Credit assignment for token-level decisions

Reading-list review pending; see the original index for candidate links.

### 21.4 Offline and direct preference objectives

- [ ] Direct Preference Optimization (DPO)
- [ ] IPO and DPO variants
- [ ] ORPO, SimPO, and reference-free approaches
- [ ] KTO and unpaired preference learning
- [ ] CPO, RLOO, online DPO, and related methods
- [ ] DPO beta, margin, data quality, and instability

Reading-list review pending; see the original index for candidate links.

### 21.5 Alignment feedback sources

- [ ] RLHF versus RLAIF and AI-generated critiques
- [ ] Constitutional AI and rule-guided feedback
- [ ] Human-written versus model-generated reward rubrics
- [ ] Multi-objective reward trade-offs
- [ ] Personalized preference modeling and pluralistic alignment
- [ ] Preference drift and iterative alignment updates

Reading-list review pending; see the original index for candidate links.

## 22. Reinforcement learning for reasoning and verifiable tasks

### 22.1 RL foundations applied to LLMs

- [ ] Markov decision process view of token generation
- [ ] Trajectories, actions, returns, and episodic rewards
- [ ] REINFORCE and policy-gradient estimators
- [ ] Baselines, advantages, and variance reduction
- [ ] Importance ratios and on-policy versus off-policy sampling
- [ ] Exploration, entropy bonuses, and reward sparsity

Reading-list review pending; see the original index for candidate links.

### 22.2 LLM-centric RL objectives

- [ ] GRPO and group-relative advantages
- [ ] RLOO and leave-one-out baselines
- [ ] DAPO and dynamic sampling/optimization choices
- [ ] GSPO and sequence-level policy optimization
- [ ] REINFORCE++ and critic-free variants
- [ ] PPO versus GRPO versus DPO conceptual comparisons

Reading-list review pending; see the original index for candidate links.

### 22.3 Training with verifiers and environments

- [ ] Exact-match and programmatic reward functions
- [ ] Math answer verification and symbolic checks
- [ ] Unit-test and compiler-based code rewards
- [ ] Tool-call outcomes and environment feedback
- [ ] Process-level and step-level rewards
- [ ] Reward shaping and sparse terminal rewards

Reading-list review pending; see the original index for candidate links.

### 22.4 Reasoning-RL pathologies

- [ ] Reward hacking and exploitable verifiers
- [ ] Long-response bias and length normalization
- [ ] Entropy collapse, mode collapse, and exploration failure
- [ ] KL drift, policy lag, and stale rollouts
- [ ] Incorrect answer extraction and false negatives
- [ ] Goodhart's law and benchmark-specific overfitting

Reading-list review pending; see the original index for candidate links.

### 22.5 Online RL engineering

- [ ] Rollout generation versus gradient-update workers
- [ ] Asynchronous rollouts and policy staleness
- [ ] Actor–learner architecture and inference–training coupling
- [ ] Reward service scaling and sandboxed evaluation
- [ ] vLLM/SGLang-backed rollouts and distributed training
- [ ] Reproducible seeds, reward logging, and checkpoint analysis

Reading-list review pending; see the original index for candidate links.

## 23. Reasoning, planning, and test-time computation

### 23.1 Reasoning behaviors

- [ ] Arithmetic, symbolic, causal, spatial, and temporal reasoning
- [ ] Multi-hop and compositional reasoning
- [ ] Deduction, induction, abduction, and analogy
- [ ] Formal proofs versus natural-language explanations
- [ ] Planning and search versus pattern completion
- [ ] Reasoning faithfulness and unfaithful explanations

Reading-list review pending; see the original index for candidate links.

### 23.2 Prompt-level reasoning strategies

- [ ] Zero-shot and few-shot reasoning prompts
- [ ] Chain-of-thought as a prompting paradigm
- [ ] Least-to-most and decomposition prompting
- [ ] Self-consistency and majority voting
- [ ] ReAct-style interleaved reasoning and actions
- [ ] Debate, critique, and self-refinement

Reading-list review pending; see the original index for candidate links.

### 23.3 Search and inference-time algorithms

- [ ] Best-of-N and rejection sampling
- [ ] Tree of Thoughts and branching search
- [ ] Beam search with verifier scoring
- [ ] Monte Carlo tree search for language tasks
- [ ] Process reward guided search
- [ ] Dynamic compute budgets and early stopping

Reading-list review pending; see the original index for candidate links.

### 23.4 Advanced reasoning paradigms

- [ ] Latent-space versus verbalized reasoning
- [ ] Hidden reasoning tokens and intermediate computation
- [ ] Deliberation models and fast/slow modes
- [ ] Parallel versus sequential thinking
- [ ] Verifier–generator systems and proof checking
- [ ] Test-time training and adaptation

Reading-list review pending; see the original index for candidate links.

### 23.5 Math and formal reasoning

- [ ] Symbolic algebra and numerical tool augmentation
- [ ] Formal theorem provers and proof assistants
- [ ] Program synthesis and executable reasoning
- [ ] Constraint solving and SAT/SMT integration
- [ ] Robustness to superficial math perturbations
- [ ] Measuring reasoning depth and out-of-distribution transfer

Reading-list review pending; see the original index for candidate links.

## 24. Autoregressive generation and decoding

### 24.1 Logits to output tokens

- [ ] Temperature scaling and categorical sampling
- [ ] Greedy decoding
- [ ] Top-k sampling and nucleus (top-p) sampling
- [ ] Min-p, typical sampling, and alternative truncation rules
- [ ] Repetition, frequency, and presence penalties
- [ ] Logit bias, bad-token masks, and stop sequences

Reading-list review pending; see the original index for candidate links.

### 24.2 Search and multiple candidates

- [ ] Beam search and length penalties
- [ ] Diverse beam search and constrained beam search
- [ ] Best-of-N sampling and candidate reranking
- [ ] Contrastive search and contrastive decoding
- [ ] Diverse generations and stochastic seed control
- [ ] Confidence-aware stopping and stopping criteria

Reading-list review pending; see the original index for candidate links.

### 24.3 Structured and constrained generation

- [ ] JSON schema-constrained generation
- [ ] Regex, grammars, and finite-state decoders
- [ ] Tool-call argument constrained decoding
- [ ] Format validation and repair loops
- [ ] Handling partial JSON and incremental streaming parsers
- [ ] Decoder-level versus prompt-only format guarantees

Reading-list review pending; see the original index for candidate links.

### 24.4 Decoding pitfalls

- [ ] Degeneration, loops, and repetition
- [ ] Temperature versus entropy and diversity
- [ ] Length bias and EOS behavior
- [ ] Sampling-induced variability and nondeterminism
- [ ] Label smoothing and logit calibration
- [ ] Exposure bias and long-horizon error propagation

Reading-list review pending; see the original index for candidate links.

## 25. Prompt engineering and context engineering

### 25.1 Prompt construction

- [ ] Instruction clarity, task specification, and success criteria
- [ ] System versus developer versus user instructions
- [ ] Prompt templates and reusable prompt components
- [ ] Zero-shot, one-shot, and few-shot examples
- [ ] Positive/negative exemplars and edge cases
- [ ] Delimiters, quoted content, and role separation

Reading-list review pending; see the original index for candidate links.

### 25.2 Advanced prompt techniques

- [ ] Decomposition and stepwise task organization
- [ ] Self-critique, refinement, and verification prompts
- [ ] Role/persona conditioning and its limitations
- [ ] Prompt chaining and prompt programs
- [ ] Structured output and tool-calling prompts
- [ ] Multi-modal prompting with images/audio/video

Reading-list review pending; see the original index for candidate links.

### 25.3 Context assembly

- [ ] Relevant context selection and ordering
- [ ] Lost-in-the-middle and position effects
- [ ] Context compression, summarization, and trimming
- [ ] Source attribution and explicit uncertainty handling
- [ ] Retrieval-aware prompt design
- [ ] Token-budget allocation among instructions, data, and output

Reading-list review pending; see the original index for candidate links.

### 25.4 Prompt reliability and measurement

- [ ] Prompt injection versus legitimate instructions
- [ ] Evaluating prompt variants on held-out cases
- [ ] Prompt overfitting and prompt sensitivity
- [ ] Perturbation testing and consistency checks
- [ ] Template version control and regression testing
- [ ] Prompt optimization using search or automated optimizers

Reading-list review pending; see the original index for candidate links.

## 26. Long-context systems, compression, and persistent context

### 26.1 Long-context use cases

- [ ] Full-document analysis and multi-document synthesis
- [ ] Repository-scale code analysis
- [ ] Multi-hour meeting/conversation analysis
- [ ] Long-horizon agents and ongoing tasks
- [ ] Long-context extraction and structured query answering
- [ ] Long-range dependencies and cross-document references

Reading-list review pending; see the original index for candidate links.

### 26.2 Context-reduction strategies

- [ ] Sliding-window history and message trimming
- [ ] Hierarchical document summaries
- [ ] Query-aware compression and contextual compression
- [ ] Extractive versus abstractive compression
- [ ] Semantic chunk selection and salience scoring
- [ ] Lossy compression, forgetting, and summary drift

Reading-list review pending; see the original index for candidate links.

### 26.3 Memory integration

- [ ] External long-term memory versus model weights
- [ ] Episodic, semantic, and procedural memory
- [ ] Retrieval over user history and project state
- [ ] Memory consolidation, expiration, and contradiction handling
- [ ] Persistent notes, knowledge graphs, and structured memories
- [ ] Privacy-aware memory boundaries and deletion

Reading-list review pending; see the original index for candidate links.

## 27. KV cache and inference memory management

### 27.1 KV cache mathematics and layout

- [ ] Deriving key/value tensor shapes per layer
- [ ] KV cache versus query recomputation
- [ ] KV size as function of B, T, H_kv, d_head, layers, and dtype
- [ ] Effect of MHA, MQA, GQA, and MLA on KV storage
- [ ] Cache indexing, RoPE positions, and attention masks
- [ ] Prefill-created versus decode-appended KV entries

Reading-list review pending; see the original index for candidate links.

### 27.2 Cache memory architectures

- [ ] Contiguous cache allocation versus paged cache
- [ ] PagedAttention block tables and indirection
- [ ] Prefix caching and shared prompt blocks
- [ ] Copy-on-write and forked sequence caches
- [ ] Cache eviction, swapping, and compaction
- [ ] Host/device offload and hierarchical KV storage

Reading-list review pending; see the original index for candidate links.

### 27.3 KV compression and advanced caching

- [ ] KV quantization and per-head quantization
- [ ] Sliding-window and sink-token retention
- [ ] Selective token eviction and importance-based pruning
- [ ] Cache pooling, low-rank compression, and latent cache
- [ ] Cross-request cache reuse and cache correctness
- [ ] Distributed KV transfers and prefill–decode disaggregation

Reading-list review pending; see the original index for candidate links.

### 27.4 Cache performance and validation

- [ ] Cache-aware scheduling and fragmentation
- [ ] KV bandwidth versus attention compute cost
- [ ] Cache pollution, tenant isolation, and leakage
- [ ] Long-context cache stress tests
- [ ] Speculative decoding cache rollback
- [ ] Memory profiler calculations and capacity planning

Reading-list review pending; see the original index for candidate links.

## 28. Efficient attention kernels and GPU optimization

### 28.1 IO-aware attention

- [ ] Standard attention's intermediate attention matrix
- [ ] FlashAttention intuition and tile-based softmax
- [ ] Online softmax and numerical equivalence
- [ ] FlashAttention variants and backward recomputation
- [ ] FlashDecoding and incremental attention
- [ ] Memory traffic analysis and arithmetic intensity

Reading-list review pending; see the original index for candidate links.

### 28.2 GPU kernel engineering

- [ ] Triton and CUDA kernel fundamentals
- [ ] Shared-memory tiling and register pressure
- [ ] Fused RMSNorm, RoPE, MLP, and softmax kernels
- [ ] GEMM layouts, tensor cores, and precision selection
- [ ] CUDA graphs and launch-overhead elimination
- [ ] Kernel autotuning and architecture-specific optimization

Reading-list review pending; see the original index for candidate links.

### 28.3 Attention alternatives and benchmarking

- [ ] FlashInfer and attention backend selection
- [ ] Sparse attention kernel efficiency
- [ ] MLA-specific kernels and cache representations
- [ ] Chunked attention and context parallelism
- [ ] Kernel correctness under different masks and shapes
- [ ] Roofline analysis, throughput, and memory profiling

Reading-list review pending; see the original index for candidate links.

## 29. Quantization, pruning, sparsity, and distillation

### 29.1 Numeric formats and quantization basics

- [ ] FP32, TF32, BF16, FP16, FP8, and FP4
- [ ] Integer formats INT8, INT4, and mixed precision
- [ ] Symmetric versus asymmetric quantization
- [ ] Per-tensor, per-channel, and per-group scales
- [ ] Zero points, clipping, and calibration
- [ ] Quantization error and outlier activation distributions

Reading-list review pending; see the original index for candidate links.

### 29.2 Weight and activation quantization

- [ ] Post-training quantization (PTQ)
- [ ] Quantization-aware training (QAT)
- [ ] GPTQ and Hessian-aware quantization
- [ ] AWQ and activation-aware quantization
- [ ] SmoothQuant and activation smoothing
- [ ] GGUF/GGML ecosystem and portable formats
- [ ] NF4 and double quantization in QLoRA

Reading-list review pending; see the original index for candidate links.

### 29.3 Inference-oriented compression

- [ ] Weight-only versus weight–activation quantization
- [ ] KV cache quantization
- [ ] Dynamic versus static activation quantization
- [ ] Mixed-bit and layer-sensitive quantization
- [ ] Structured/unstructured pruning and N:M sparsity
- [ ] Low-rank factorization and neural compression

Reading-list review pending; see the original index for candidate links.

### 29.4 Distillation and compact modeling

- [ ] Teacher–student distillation and soft labels
- [ ] Logit-level versus feature-level distillation
- [ ] Sequence-level and on-policy distillation
- [ ] Reasoning-trace and tool-use distillation
- [ ] Distillation from ensembles or verifier-filtered samples
- [ ] Compression quality–latency–memory Pareto frontiers

Reading-list review pending; see the original index for candidate links.

## 30. LLM inference execution and throughput optimization

### 30.1 Prefill/decode computational regimes

- [ ] Prefill compute profile and first-token latency
- [ ] Decode memory-bandwidth profile and tokens/sec
- [ ] Time to first token (TTFT) versus inter-token latency (ITL)
- [ ] Throughput, goodput, and tail-latency definitions
- [ ] Arithmetic intensity and roofline model
- [ ] Latency–batch size and concurrency trade-offs

Reading-list review pending; see the original index for candidate links.

### 30.2 Batching and request scheduling

- [ ] Static batching versus continuous batching
- [ ] Dynamic batching, request admission, and waiting queues
- [ ] Chunked prefill and prefill–decode interleaving
- [ ] Prefix sharing and response-length prediction
- [ ] Fairness, priority, deadlines, and preemption
- [ ] Head-of-line blocking and straggler requests

Reading-list review pending; see the original index for candidate links.

### 30.3 Speculative and parallel generation

- [ ] Draft-model speculative decoding and acceptance/rejection
- [ ] Self-speculative decoding and early-exit drafts
- [ ] N-gram and suffix speculation
- [ ] EAGLE-style draft heads and verification
- [ ] Multi-token prediction for inference
- [ ] Parallel decoding and tree verification

Reading-list review pending; see the original index for candidate links.

### 30.4 Distributed inference architecture

- [ ] Tensor parallelism versus pipeline parallelism
- [ ] Expert parallelism for MoE serving
- [ ] Context parallelism and long-sequence inference
- [ ] Disaggregated prefill, decode, and encode
- [ ] Multi-node KV transfer and remote cache access
- [ ] Elastic scaling and heterogeneous accelerator fleets

Reading-list review pending; see the original index for candidate links.

## 31. Model serving engines and deployment stacks

### 31.1 Open and commercial inference runtimes

- [ ] Hugging Face Transformers generation API
- [ ] vLLM engine and OpenAI-compatible APIs
- [ ] SGLang runtime and structured generation
- [ ] TensorRT-LLM and compiler-driven inference
- [ ] llama.cpp, GGUF, and CPU/local inference
- [ ] MLX, ONNX Runtime, TGI, and alternate runtimes

Reading-list review pending; see the original index for candidate links.

### 31.2 Serving design

- [ ] Model loading, warmup, and weight distribution
- [ ] Multi-model placement, routing, and autoscaling
- [ ] Multi-LoRA adapter hosting
- [ ] Streaming responses and SSE/WebSocket transport
- [ ] Multi-tenant isolation, quotas, and rate limits
- [ ] Offline batch processing versus low-latency serving

Reading-list review pending; see the original index for candidate links.

### 31.3 Production performance

- [ ] End-to-end latency decomposition
- [ ] Token throughput and GPU utilization dashboards
- [ ] Prefix caching and cache-hit metrics
- [ ] Model replicas, scaling policies, and queue saturation
- [ ] Tail latency, retries, and overload protection
- [ ] Benchmarking representative workloads and capacity planning

Reading-list review pending; see the original index for candidate links.

## 32. LLM APIs, protocols, and application integration

### 32.1 API fundamentals

- [ ] Chat-completion versus response-oriented APIs
- [ ] Message roles, content parts, and output modalities
- [ ] Tokens, usage accounting, and token budgets
- [ ] Streaming token events and incremental output handling
- [ ] Retries, backoff, idempotency, and timeouts
- [ ] Version pinning, model deprecation, and compatibility

Reading-list review pending; see the original index for candidate links.

### 32.2 Structured interfaces

- [ ] Tool/function-call schemas and validation
- [ ] JSON schema, XML, and grammar-constrained output
- [ ] Parallel tool calls and tool-result correlation
- [ ] Schema evolution and backward compatibility
- [ ] Function-calling failure recovery and argument repair
- [ ] Multimodal message payload representation

Reading-list review pending; see the original index for candidate links.

### 32.3 System integration

- [ ] Queues, background workers, and orchestration
- [ ] REST, gRPC, WebSockets, and event streams
- [ ] Authentication, authorization, and secrets management
- [ ] Provider abstraction, fallbacks, and model routing
- [ ] Cost governance and usage observability
- [ ] API privacy, retention, and regional hosting controls

Reading-list review pending; see the original index for candidate links.

## 33. Retrieval, search, ranking, and embedding systems

### 33.1 Search paradigms

- [ ] Lexical search, BM25, and inverted indexes
- [ ] Dense vector retrieval
- [ ] Hybrid sparse–dense search
- [ ] Cross-encoder reranking
- [ ] Late-interaction retrieval such as ColBERT
- [ ] Learned sparse retrieval and SPLADE-style methods

Reading-list review pending; see the original index for candidate links.

### 33.2 Indexing and vector databases

- [ ] Exact nearest-neighbor search
- [ ] ANN techniques: IVF, HNSW, and product quantization
- [ ] FAISS internals and GPU indexing
- [ ] Vector databases and metadata filtering
- [ ] Index build/update/delete, sharding, and replication
- [ ] Embedding version migration and reindexing

Reading-list review pending; see the original index for candidate links.

### 33.3 Retrieval training and metrics

- [ ] Contrastive learning for query/document matching
- [ ] Hard negatives, in-batch negatives, and false negatives
- [ ] Recall@k, precision@k, MRR, MAP, and nDCG
- [ ] Retrieval query understanding and expansion
- [ ] Domain-specific embeddings and rerankers
- [ ] Calibration, freshness, and retrieval drift

Reading-list review pending; see the original index for candidate links.

## 34. Retrieval-augmented generation (RAG)

### 34.1 Document ingestion and chunking

- [ ] PDF, HTML, DOCX, Markdown, table, and code ingestion
- [ ] Fixed-size, semantic, structure-aware, and recursive chunking
- [ ] Overlap sizing and parent–child chunk linkage
- [ ] Metadata, citations, provenance, and document versioning
- [ ] Table/image extraction and multimodal document parsing
- [ ] ACL-aware indexing and content redaction

Reading-list review pending; see the original index for candidate links.

### 34.2 RAG query pipeline

- [ ] Query rewriting, decomposition, and multi-query search
- [ ] Hybrid retrieval, filtering, and reranking
- [ ] Context assembly and answer grounding
- [ ] Citation spans and source verification
- [ ] Query routing and retrieval-depth selection
- [ ] Handling no-answer and low-retrieval-confidence cases

Reading-list review pending; see the original index for candidate links.

### 34.3 Advanced RAG strategies

- [ ] Agentic RAG and iterative retrieval
- [ ] GraphRAG and entity/relation retrieval
- [ ] Hierarchical and long-document RAG
- [ ] Corrective, adaptive, and self-reflective RAG
- [ ] Multimodal RAG and vision-based page retrieval
- [ ] Knowledge graph plus vector-store hybrids

Reading-list review pending; see the original index for candidate links.

### 34.4 RAG evaluation and optimization

- [ ] Retrieval relevance versus answer faithfulness
- [ ] Context precision, context recall, and citation correctness
- [ ] Groundedness, answer completeness, and abstention
- [ ] RAGAS-style and task-specific eval frameworks
- [ ] Dataset construction and synthetic QA pairs
- [ ] Latency–accuracy–cost trade-offs and caching

Reading-list review pending; see the original index for candidate links.

## 35. Tool use, function calling, and external computation

### 35.1 Tool-use fundamentals

- [ ] Tool descriptions, schemas, and capability boundaries
- [ ] Tool selection and argument generation
- [ ] Parallel versus sequential tool invocation
- [ ] Tool observations and result incorporation
- [ ] Errors, retries, timeouts, and partial failures
- [ ] Human approval before consequential tool actions

Reading-list review pending; see the original index for candidate links.

### 35.2 Tool-use categories

- [ ] Search/browser tools and source retrieval
- [ ] Code execution, calculators, and sandboxes
- [ ] SQL querying and database connectors
- [ ] Filesystem and document operations
- [ ] Scheduling, messaging, and third-party actions
- [ ] Scientific tools, symbolic solvers, and APIs

Reading-list review pending; see the original index for candidate links.

### 35.3 Tool-use reliability and safety

- [ ] Tool-output injection and untrusted content
- [ ] Least-privilege permissions and scoped credentials
- [ ] Side-effect isolation and idempotency
- [ ] Tool-call trace auditing and replay
- [ ] Transaction boundaries and compensation actions
- [ ] Tool-call benchmark design and pass/fail criteria

Reading-list review pending; see the original index for candidate links.

## 36. LLM agents and workflow architectures

### 36.1 Agent fundamentals

- [ ] LLM as planner/controller versus LLM as component
- [ ] Perception, planning, action, observation, and feedback
- [ ] ReAct loops and state machines
- [ ] Workflow orchestration versus autonomous agents
- [ ] Tool-augmented execution and environment interaction
- [ ] Task completion, stopping conditions, and verification

Reading-list review pending; see the original index for candidate links.

### 36.2 Agent patterns

- [ ] Plan-and-execute agents
- [ ] ReAct and iterative observation-action agents
- [ ] Reflection and critique loops
- [ ] Supervisor–worker and hierarchical orchestration
- [ ] Event-driven agents and durable workflows
- [ ] Graph-based state-machine orchestrators

Reading-list review pending; see the original index for candidate links.

### 36.3 Reliability and governance

- [ ] State persistence, checkpoints, and resumability
- [ ] Max-step controls, budgets, and termination criteria
- [ ] Retry handling, idempotency, and compensating actions
- [ ] Human-in-the-loop review and escalation
- [ ] Agent evaluation by trajectory, outcome, and cost
- [ ] Agent sandboxing and permission boundaries

Reading-list review pending; see the original index for candidate links.

## 37. Multi-agent systems, coordination, and protocols

### 37.1 Multi-agent coordination

- [ ] Role-specialized agent teams
- [ ] Manager–worker and planner–executor patterns
- [ ] Debate, voting, and critique ensembles
- [ ] Collaborative blackboard and shared-memory systems
- [ ] Negotiation, delegation, and task decomposition
- [ ] Coordination overhead and emergent failure modes

Reading-list review pending; see the original index for candidate links.

### 37.2 Agent communication and interoperability

- [ ] Agent-to-agent message schemas and contracts
- [ ] Model Context Protocol (MCP) concepts and tool/resources interfaces
- [ ] Agent-to-Agent (A2A) communication concepts
- [ ] Tool discovery and capability registries
- [ ] Stateful handoffs, provenance, and correlation IDs
- [ ] Trust boundaries and authenticated inter-agent messaging

Reading-list review pending; see the original index for candidate links.

### 37.3 Agent evaluation and optimization

- [ ] Single-agent versus multi-agent baselines
- [ ] Task success, communication cost, and latency
- [ ] Credit assignment across agents
- [ ] Redundant work, conflicts, and deadlock avoidance
- [ ] Trace-level analysis and root-cause attribution
- [ ] Failover, human override, and orchestration policies

Reading-list review pending; see the original index for candidate links.

## 38. Agent memory, state, and long-horizon autonomy

### 38.1 Memory taxonomies

- [ ] Working memory, short-term history, and long-term memory
- [ ] Episodic memories of events and interactions
- [ ] Semantic memory and structured facts
- [ ] Procedural memory, learned skills, and reusable workflows
- [ ] Model-internal knowledge versus external storage
- [ ] Shared versus per-agent memories

Reading-list review pending; see the original index for candidate links.

### 38.2 Memory operations

- [ ] Memory write policy and salience selection
- [ ] Retrieval and relevance scoring
- [ ] Consolidation, summarization, and conflict resolution
- [ ] Temporal decay, forgetting, and memory expiration
- [ ] Attribution, provenance, and uncertainty metadata
- [ ] User correction, deletion, and memory access control

Reading-list review pending; see the original index for candidate links.

### 38.3 Long-horizon execution

- [ ] Durable plans and hierarchical task tracking
- [ ] Resuming work after context loss
- [ ] State snapshots, event sourcing, and action replay
- [ ] Subgoal decomposition and progress verification
- [ ] Stuck-agent detection and recovery
- [ ] Memory poisoning defenses and permissioned recall

Reading-list review pending; see the original index for candidate links.

## 39. Multimodal LLM fundamentals

### 39.1 Multimodal representations

- [ ] Text, image, audio, video, and spatial tokens
- [ ] Modality encoders, adapters, projectors, and decoders
- [ ] Early, middle, and late fusion
- [ ] Cross-attention versus token-concatenation fusion
- [ ] Shared embedding spaces and contrastive alignment
- [ ] Modality-specific preprocessing and patching

Reading-list review pending; see the original index for candidate links.

### 39.2 Multimodal training

- [ ] Image–text and audio–text paired data
- [ ] Captioning, contrastive, and generative objectives
- [ ] Instruction tuning with multimodal conversations
- [ ] Interleaved text–image and text–audio sequences
- [ ] Cross-modal grounding and hallucination mitigation
- [ ] Multimodal preference optimization and reward modeling

Reading-list review pending; see the original index for candidate links.

### 39.3 Evaluation and integration

- [ ] Modalities in a shared context window
- [ ] Modality-specific token cost and memory footprints
- [ ] Cross-modal consistency and grounding
- [ ] Accessibility and alternative text generation
- [ ] Robustness to low-quality input and missing modalities
- [ ] Multimodal safety and privacy evaluation

Reading-list review pending; see the original index for candidate links.

## 40. Vision-language models (VLMs) and documents

### 40.1 Vision encoders and alignment

- [ ] CNN versus Vision Transformer (ViT) image encoders
- [ ] CLIP-style contrastive vision–language alignment
- [ ] Image patches, resolution, tiling, and crops
- [ ] Visual projector and Q-Former-style adapters
- [ ] Perceiver resampling and token compression
- [ ] Variable-resolution and dynamic visual tokens

Reading-list review pending; see the original index for candidate links.

### 40.2 VLM capabilities

- [ ] Image captioning and visual question answering
- [ ] OCR, scene text, and handwriting interpretation
- [ ] Charts, tables, diagrams, and document QA
- [ ] Spatial grounding, localization, and referring expressions
- [ ] Multi-image comparison and visual reasoning
- [ ] GUI/screen understanding and screenshot-based agents

Reading-list review pending; see the original index for candidate links.

### 40.3 Vision-specific limitations

- [ ] Object counting and spatial relation failures
- [ ] Fine-detail recognition and resolution bottlenecks
- [ ] Visual hallucinations and grounding errors
- [ ] OCR/layout confusion and page ordering
- [ ] Adversarial image and embedded-text injection
- [ ] Evaluation of vision reasoning and document accuracy

Reading-list review pending; see the original index for candidate links.

## 41. Audio, speech, music, and spoken language models

### 41.1 Audio foundations

- [ ] Waveforms, sample rates, spectrograms, and mel features
- [ ] Audio codecs, discrete acoustic tokens, and neural quantizers
- [ ] Streaming chunks, timestamps, and speaker diarization
- [ ] Speech activity detection and noise robustness
- [ ] Audio embeddings and speech encoders
- [ ] Cross-modal audio–text alignment

Reading-list review pending; see the original index for candidate links.

### 41.2 Speech tasks and models

- [ ] Automatic speech recognition (ASR)
- [ ] Speech translation and multilingual transcription
- [ ] Text-to-speech (TTS) and speech generation
- [ ] Speech-to-speech and simultaneous translation
- [ ] Voice activity and turn-taking prediction
- [ ] Speaker identification, diarization, and separation

Reading-list review pending; see the original index for candidate links.

### 41.3 Real-time voice systems

- [ ] Cascaded ASR→LLM→TTS versus end-to-end audio models
- [ ] Streaming speech input and output generation
- [ ] Barge-in, interruption, and full-duplex conversation
- [ ] End-of-turn detection and latency budgeting
- [ ] Prosody, emotion, and voice consistency
- [ ] Audio safety, spoofing, and voice consent

Reading-list review pending; see the original index for candidate links.

## 42. Video, real-time multimodal systems, and embodied agents

### 42.1 Video representation

- [ ] Frames, clips, timestamps, and temporal sampling
- [ ] Video tokenization and temporal compression
- [ ] Spatiotemporal positional encodings
- [ ] Event recognition and temporal localization
- [ ] Long-video summarization and retrieval
- [ ] Audio–video synchronization

Reading-list review pending; see the original index for candidate links.

### 42.2 Real-time multimodal interaction

- [ ] Streaming visual and audio observations
- [ ] Incremental perception and state updates
- [ ] Live multimodal conversation and event triggers
- [ ] Time-aligned memory and synchronized outputs
- [ ] Latency management under continuous perception
- [ ] Multimodal hallucination and temporal grounding

Reading-list review pending; see the original index for candidate links.

### 42.3 Action and embodied language models

- [ ] Vision-language-action (VLA) models
- [ ] Action tokenization and trajectory prediction
- [ ] Robotics instruction following and manipulation
- [ ] World models and predictive latent states
- [ ] Affordance learning and spatial planning
- [ ] Sim-to-real transfer, safety, and closed-loop evaluation

Reading-list review pending; see the original index for candidate links.

## 43. Code language models and software-engineering agents

### 43.1 Code modeling

- [ ] Programming-language tokenization and syntax patterns
- [ ] Repository pretraining, licensing, and decontamination
- [ ] Fill-in-the-middle code completion
- [ ] Code generation, translation, and refactoring
- [ ] Static analysis, ASTs, and type information
- [ ] Multi-file and repository-level code understanding

Reading-list review pending; see the original index for candidate links.

### 43.2 Code reasoning and verification

- [ ] Program synthesis and algorithmic reasoning
- [ ] Test-case generation and property-based testing
- [ ] Compiler and interpreter feedback
- [ ] Execution traces, stack traces, and debugging
- [ ] Patch generation, code editing, and differential testing
- [ ] Secure coding and vulnerability detection

Reading-list review pending; see the original index for candidate links.

### 43.3 Software-engineering agents

- [ ] Repository search, code navigation, and dependency mapping
- [ ] Issue localization and root-cause analysis
- [ ] Tool-driven edit–test–debug loops
- [ ] CI integration and test execution sandboxes
- [ ] PR generation, review, and merge-conflict resolution
- [ ] SWE-bench-style evaluation and leakage controls

Reading-list review pending; see the original index for candidate links.

## 44. Domain-specific and multilingual LLMs

### 44.1 Domain adaptation

- [ ] Medical, scientific, legal, financial, and educational LLMs
- [ ] Domain vocabulary and specialist tokenization
- [ ] Domain-adaptive continued pretraining
- [ ] Domain-specific SFT and preference optimization
- [ ] Domain-specific retrieval and knowledge bases
- [ ] Validation with domain experts and external standards

Reading-list review pending; see the original index for candidate links.

### 44.2 Multilingual and cross-lingual learning

- [ ] Language-balanced pretraining and sampling
- [ ] Cross-lingual transfer and zero-shot transfer
- [ ] Translation-based augmentation and evaluation
- [ ] Code-switching, transliteration, and mixed scripts
- [ ] Morphologically rich and low-resource languages
- [ ] Regional language safety and cultural context

Reading-list review pending; see the original index for candidate links.

### 44.3 Specialized model families

- [ ] Mathematical reasoning models
- [ ] Scientific and symbolic reasoning models
- [ ] Legal document reasoning models
- [ ] Financial and time-series language models
- [ ] Biology/chemistry/protein-sequence foundation models
- [ ] Tabular, database, and structured-data language models

Reading-list review pending; see the original index for candidate links.

## 45. Evaluation methodology and benchmark engineering

### 45.1 Offline evaluation basics

- [ ] Held-out testing and dataset stratification
- [ ] Perplexity, loss, exact match, F1, and task accuracy
- [ ] Human evaluation and annotation rubrics
- [ ] Pairwise preference and win-rate evaluation
- [ ] Statistical confidence intervals and significance testing
- [ ] Variance across prompts, seeds, and decoding settings

Reading-list review pending; see the original index for candidate links.

### 45.2 Capability benchmark families

- [ ] General knowledge and MMLU-style evaluation
- [ ] Graduate knowledge and GPQA-style evaluation
- [ ] Math benchmarks and verifiable problem solving
- [ ] Code benchmarks: HumanEval, MBPP, LiveCodeBench
- [ ] Software-agent benchmarks: SWE-bench and terminal tasks
- [ ] Long-context benchmarks: LongBench, RULER, needle tests
- [ ] Instruction following and IFEval-style tests

Reading-list review pending; see the original index for candidate links.

### 45.3 Specialized benchmarking

- [ ] Tool calling and function argument correctness
- [ ] RAG factuality, retrieval, and citation benchmarks
- [ ] Embedding and retrieval evaluation (MTEB-style)
- [ ] VLM, audio, video, and multimodal reasoning benchmarks
- [ ] Safety, bias, jailbreak, and refusal testing
- [ ] Multilingual and low-resource benchmarks

Reading-list review pending; see the original index for candidate links.

### 45.4 Evaluation reliability

- [ ] Data contamination, leaderboard overfitting, and test leakage
- [ ] Static versus rolling/private test sets
- [ ] LLM-as-a-judge strengths and position/style bias
- [ ] Judge calibration, reference checks, and rubric design
- [ ] Goodhart's law and benchmark gaming
- [ ] Reproducible harnesses, versions, and environment control

Reading-list review pending; see the original index for candidate links.

### 45.5 Online and product evaluation

- [ ] A/B tests and interleaving experiments
- [ ] User satisfaction, task success, and downstream outcomes
- [ ] Latency, cost, availability, and quality trade-offs
- [ ] Human escalation and error-severity metrics
- [ ] Shadow evaluation and canary model releases
- [ ] Longitudinal drift and regression monitoring

Reading-list review pending; see the original index for candidate links.

## 46. Factuality, uncertainty, calibration, and robustness

### 46.1 Hallucinations and factual errors

- [ ] Intrinsic versus extrinsic hallucination
- [ ] Unsupported claims, fabricated citations, and invented entities
- [ ] Retrieval failure versus generation failure
- [ ] Knowledge cutoff and temporal staleness
- [ ] Multi-hop fact composition and contradiction
- [ ] Grounded generation and evidence attribution

Reading-list review pending; see the original index for candidate links.

### 46.2 Uncertainty and calibration

- [ ] Token probability versus answer correctness
- [ ] Predictive entropy and confidence aggregation
- [ ] Verbal confidence and confidence elicitation
- [ ] Temperature scaling and post-hoc calibration
- [ ] Selective prediction and abstention
- [ ] Conformal prediction and uncertainty sets

Reading-list review pending; see the original index for candidate links.

### 46.3 Robustness and stress testing

- [ ] Paraphrase and formatting sensitivity
- [ ] Long context and distractor robustness
- [ ] Out-of-distribution and distribution-shift tests
- [ ] Contradictory evidence and adversarial examples
- [ ] Tool error robustness and API schema drift
- [ ] Reliability under nondeterminism and sampling changes

Reading-list review pending; see the original index for candidate links.

## 47. Interpretability, mechanistic analysis, and model editing

### 47.1 Black-box interpretability

- [ ] Probing classifiers and representation similarity
- [ ] Layerwise behavior and intermediate activations
- [ ] Attention visualization and its limitations
- [ ] Logit lens and tuned lens
- [ ] Model behavior attribution and counterfactual tests
- [ ] Feature visualization and activation statistics

Reading-list review pending; see the original index for candidate links.

### 47.2 Mechanistic interpretability

- [ ] Residual-stream decomposition and circuit hypotheses
- [ ] Induction heads and in-context copying circuits
- [ ] Activation patching and causal tracing
- [ ] Path patching, ablation, and causal mediation
- [ ] Sparse autoencoders (SAEs) and feature dictionaries
- [ ] Superposition, polysemanticity, and feature geometry

Reading-list review pending; see the original index for candidate links.

### 47.3 Model editing and steering

- [ ] Knowledge editing and targeted factual updates
- [ ] Rank-one and locate-and-edit approaches
- [ ] Representation steering and activation addition
- [ ] Steering vectors and inference-time control
- [ ] Unlearning, concept erasure, and side effects
- [ ] Evaluating edit specificity, locality, and persistence

Reading-list review pending; see the original index for candidate links.

## 48. Alignment, model behavior, and responsible AI

### 48.1 Alignment objectives

- [ ] Helpful, honest, harmless, and user-intent-aligned behavior
- [ ] Instruction hierarchy and authorized directives
- [ ] Corrigibility and appropriate human oversight
- [ ] Moral uncertainty and pluralistic values
- [ ] Reward–objective mismatch and specification gaming
- [ ] Alignment tax and capability–safety trade-offs

Reading-list review pending; see the original index for candidate links.

### 48.2 Safety post-training

- [ ] Safety-specific SFT and preference data
- [ ] Refusal policies and safe-completion strategies
- [ ] Rule-based, classifier-based, and model-based guardrails
- [ ] Safety evaluation before and after fine-tuning
- [ ] Robustness to indirect and multi-turn attacks
- [ ] Escalation, tool action gating, and high-stakes domains

Reading-list review pending; see the original index for candidate links.

### 48.3 Fairness and societal impacts

- [ ] Stereotypes, representational harms, and disparate performance
- [ ] Cultural and multilingual fairness evaluations
- [ ] Toxicity, bias amplification, and content moderation
- [ ] Accessibility and inclusive interaction design
- [ ] Transparency, explainability, and affected-user recourse
- [ ] Environmental and workforce effects of deployment

Reading-list review pending; see the original index for candidate links.

## 49. LLM security, prompt injection, and adversarial ML

### 49.1 Threat modeling

- [ ] Assets, trust boundaries, attackers, and attack surfaces
- [ ] Model, prompt, tool, retrieval, and data supply chains
- [ ] Direct versus indirect prompt injection
- [ ] Jailbreaks versus application-level security failures
- [ ] Attacker-controlled documents, websites, and tool results
- [ ] Agent authority boundaries and privilege escalation

Reading-list review pending; see the original index for candidate links.

### 49.2 Attack classes

- [ ] Prompt injection and instruction override attempts
- [ ] Sensitive-data disclosure and hidden-context exposure
- [ ] Excessive agency and unauthorized tool actions
- [ ] Data poisoning, model poisoning, and backdoors
- [ ] Model extraction, membership inference, and inversion
- [ ] Tool-output misuse and insecure output handling
- [ ] Vector/embedding store poisoning and retrieval hijacking
- [ ] Unbounded consumption and denial-of-wallet attacks

Reading-list review pending; see the original index for candidate links.

### 49.3 Defenses and secure architecture

- [ ] Treating retrieved text and tool output as untrusted data
- [ ] Instruction hierarchy enforcement and role separation
- [ ] Tool allowlists, schema validation, and permission checks
- [ ] Sandboxed execution and network/file-system isolation
- [ ] Secret minimization and least-privilege service accounts
- [ ] Rate limiting, monitoring, audit trails, and kill switches
- [ ] Continuous red teaming and attack regression suites

Reading-list review pending; see the original index for candidate links.

### 49.4 Security standards and research

- [ ] OWASP Top 10 for LLM Applications (2026)
- [ ] OWASP agentic security threat categories
- [ ] MITRE ATLAS and adversarial ML mapping
- [ ] Threat-model-driven evaluations and incident response
- [ ] AI supply-chain integrity, model artifact signing, and provenance
- [ ] Security–utility trade-offs and defense-in-depth limits

Reading-list review pending; see the original index for candidate links.

## 50. Privacy, intellectual property, governance, and compliance

### 50.1 Privacy-preserving learning

- [ ] Differential privacy definitions and epsilon/delta accounting
- [ ] DP-SGD and privacy–utility trade-offs
- [ ] Private fine-tuning and privacy budgets
- [ ] Data minimization and retention windows
- [ ] Federated/distributed privacy-preserving adaptation
- [ ] Memorization, extraction, and training-data leakage

Reading-list review pending; see the original index for candidate links.

### 50.2 Intellectual property and provenance

- [ ] Copyright and licensing of model weights and datasets
- [ ] Open-source license compatibility
- [ ] Dataset and model provenance tracking
- [ ] Memorized passages and verbatim reproduction risk
- [ ] Output ownership and commercial-use constraints
- [ ] Watermarking, content credentials, and provenance metadata

Reading-list review pending; see the original index for candidate links.

### 50.3 Governance and operational controls

- [ ] Model cards, dataset cards, and risk documentation
- [ ] Model release evaluations and risk acceptance
- [ ] Audit trails, incident reporting, and access reviews
- [ ] Regional data residency and cross-border data flows
- [ ] Sector-specific standards and regulatory checks
- [ ] Monitoring policy changes over time

Reading-list review pending; see the original index for candidate links.

## 51. Synthetic training loops, self-improvement, and knowledge distillation

### 51.1 Synthetic instruction and reasoning data

- [ ] Self-instruct pipelines
- [ ] Teacher-generated demonstrations and explanations
- [ ] Multi-sample solution generation with verification
- [ ] Curriculum and difficulty selection
- [ ] Error-driven counterexample generation
- [ ] Diversity and coverage validation

Reading-list review pending; see the original index for candidate links.

### 51.2 Self-improvement strategies

- [ ] Rejection sampling fine-tuning (RFT)
- [ ] Iterative SFT and preference optimization cycles
- [ ] Self-play and competitive training setups
- [ ] Critique–revise–verify pipelines
- [ ] Online feedback and data flywheel design
- [ ] Guarding against reward gaming and distribution collapse

Reading-list review pending; see the original index for candidate links.

### 51.3 Distillation and transfer mechanics

- [ ] Sequence-level distillation from a stronger teacher
- [ ] On-policy versus offline distillation
- [ ] Hidden-state/feature distillation
- [ ] Reasoning compression and short-answer distillation
- [ ] Specialist-to-generalist and generalist-to-specialist transfer
- [ ] Maintaining diversity and avoiding brittle imitation

Reading-list review pending; see the original index for candidate links.

## 52. LLMOps, observability, testing, and production lifecycle

### 52.1 Experiment management

- [ ] Dataset, prompt, tokenizer, and weight versioning
- [ ] Experiment tracking and artifact registries
- [ ] Reproducibility manifests and environment locking
- [ ] Model cards and evaluation reports
- [ ] CI/CD for prompts, agents, and models
- [ ] Offline eval gates and canary releases

Reading-list review pending; see the original index for candidate links.

### 52.2 Inference and agent observability

- [ ] Request/response tracing and span correlation
- [ ] Prompt, retrieval, tool, and model-step traces
- [ ] Token usage, TTFT, ITL, throughput, and error rates
- [ ] Quality regression, hallucination, and safety metrics
- [ ] User feedback and annotation queues
- [ ] PII-safe logging, sampling, and redaction

Reading-list review pending; see the original index for candidate links.

### 52.3 Reliability operations

- [ ] SLIs, SLOs, and service-level agreements
- [ ] Capacity planning, autoscaling, and fallback routing
- [ ] Circuit breakers, timeouts, retries, and graceful degradation
- [ ] Prompt/model drift and scheduled regression tests
- [ ] Postmortems and root-cause analysis
- [ ] Rollback plans and model lifecycle management

Reading-list review pending; see the original index for candidate links.

## 53. Cost, latency, architecture, and product optimization

### 53.1 Token economics

- [ ] Input, output, cached, and reasoning-token billing
- [ ] Batch discounts and prompt caching
- [ ] Cost per task versus cost per million tokens
- [ ] Context window expansion and hidden cost
- [ ] Model routing and small-model-first cascades
- [ ] Cost–quality–latency Pareto optimization

Reading-list review pending; see the original index for candidate links.

### 53.2 System architecture choices

- [ ] API-hosted versus self-hosted models
- [ ] On-device, edge, single-GPU, and distributed deployment
- [ ] RAG versus fine-tuning versus long-context prompting
- [ ] Dense versus MoE model choice
- [ ] Multi-model routing, verifier ensembles, and fallbacks
- [ ] Constrained decoding versus prompt-only formatting

Reading-list review pending; see the original index for candidate links.

### 53.3 Performance engineering

- [ ] Prompt/prefix caching and semantic caching
- [ ] Request coalescing and deduplication
- [ ] GPU memory budget and effective concurrency
- [ ] Tail latency optimization and queuing behavior
- [ ] Speculative decoding and batching ROI
- [ ] Quality validation for quantized/optimized models

Reading-list review pending; see the original index for candidate links.

### 53.4 Product and UX design

- [ ] Streaming interface and partial-output management
- [ ] Cited answers and source provenance UX
- [ ] Human verification for consequential actions
- [ ] Feedback collection and evaluation loop
- [ ] Failure messaging and trustworthy uncertainty
- [ ] Accessibility, multilingual UX, and interaction modalities

Reading-list review pending; see the original index for candidate links.

## 54. Research frontiers and unresolved questions

### 54.1 Capability and scaling frontiers

- [ ] Scaling pretraining data and high-quality data scarcity
- [ ] Test-time compute allocation and adaptive deliberation
- [ ] Long-horizon planning and coherent execution
- [ ] Continual learning without catastrophic forgetting
- [ ] Robust out-of-distribution generalization
- [ ] Knowledge updating without full retraining

Reading-list review pending; see the original index for candidate links.

### 54.2 Architecture frontiers

- [ ] Efficient long-sequence and near-linear attention alternatives
- [ ] Recurrent memory and persistent-state architectures
- [ ] Sparse computation, dynamic routing, and MoE scaling
- [ ] Latent reasoning and nonverbal intermediate representations
- [ ] Native multimodal token/action spaces
- [ ] Hardware-aware architecture co-design

Reading-list review pending; see the original index for candidate links.

### 54.3 Learning and alignment frontiers

- [ ] Better process supervision and verifier reliability
- [ ] RL with real-world, delayed, or noisy rewards
- [ ] Exploration in long-horizon environments
- [ ] Scalable oversight and automated interpretability
- [ ] Reliable uncertainty estimation and calibrated abstention
- [ ] Secure tool-using autonomy and agentic evaluations

Reading-list review pending; see the original index for candidate links.

### 54.4 Research methodology

- [ ] Reading model technical reports and paper appendices
- [ ] Separating empirical claims from theoretical claims
- [ ] Identifying baselines, confounders, and ablation requirements
- [ ] Reproduction with limited compute
- [ ] Benchmark construction with contamination controls
- [ ] Reporting variance, confidence intervals, and negative results

Reading-list review pending; see the original index for candidate links.

## 55. Hands-on implementations and capstone projects

### 55.1 From-scratch components

- [ ] Implement BPE or Unigram tokenizer on a text corpus
- [ ] Implement token embeddings and a causal attention mask
- [ ] Implement MHA, GQA, and RoPE with shape tests
- [ ] Implement LayerNorm/RMSNorm and SwiGLU
- [ ] Build a small decoder-only transformer in PyTorch
- [ ] Train a toy causal LM and monitor perplexity

Reading-list review pending; see the original index for candidate links.

### 55.2 Training and post-training projects

- [ ] Pretrain a tiny model with packing and mixed precision
- [ ] Implement LoRA and compare with full fine-tuning
- [ ] Run QLoRA SFT on a small instruct dataset
- [ ] Train a pairwise reward model
- [ ] Reproduce DPO on a preference dataset
- [ ] Run a tiny verifiable-reward RL/GRPO experiment

Reading-list review pending; see the original index for candidate links.

### 55.3 Inference and serving projects

- [ ] Implement naive autoregressive generation
- [ ] Add per-layer KV caching and compare decode speed
- [ ] Derive KV memory for MHA versus GQA versus MLA
- [ ] Serve a model with vLLM or SGLang
- [ ] Benchmark continuous batching and prefix caching
- [ ] Compare FP16, FP8, and INT4 memory/performance
- [ ] Implement and evaluate speculative decoding

Reading-list review pending; see the original index for candidate links.

### 55.4 RAG and agent projects

- [ ] Build BM25, dense, hybrid, and reranked retrieval baselines
- [ ] Build a citation-grounded document RAG application
- [ ] Evaluate retrieval quality separately from answer quality
- [ ] Build a tool-calling agent with permission checks
- [ ] Implement durable agent state and memory updates
- [ ] Benchmark an agent with deterministic task environments

Reading-list review pending; see the original index for candidate links.

### 55.5 Research replication and security projects

- [ ] Replicate a positional encoding or attention paper
- [ ] Compare dense versus MoE under controlled compute
- [ ] Audit a benchmark for contamination
- [ ] Analyze reasoning trace faithfulness and verifier failures
- [ ] Build a prompt-injection test corpus and defensive regression suite
- [ ] Profile GPU memory, kernel runtime, and service latency

Reading-list review pending; see the original index for candidate links.

## 56. Developer tools, libraries, ecosystems, and workflows

### 56.1 Model development libraries

- [ ] PyTorch and torch.compile
- [ ] Hugging Face Transformers, Tokenizers, and Datasets
- [ ] Accelerate, PEFT, and TRL
- [ ] DeepSpeed, FSDP, and Megatron frameworks
- [ ] JAX/Flax and alternate training frameworks
- [ ] Model hubs, safetensors, and checkpoint formats

Reading-list review pending; see the original index for candidate links.

### 56.2 Model inference and optimization libraries

- [ ] vLLM, SGLang, TensorRT-LLM, and TGI
- [ ] llama.cpp, MLX, ONNX Runtime, and local model tools
- [ ] FlashAttention, FlashInfer, Triton, and kernel tooling
- [ ] GPTQ/AWQ/quantization toolchains
- [ ] Benchmarking and profiling suites
- [ ] Deployment containers and orchestration platforms

Reading-list review pending; see the original index for candidate links.

### 56.3 Retrieval, orchestration, and evaluation tools

- [ ] FAISS and vector-search libraries
- [ ] OpenSearch/Elasticsearch and hybrid search engines
- [ ] Agent orchestration frameworks and state graphs
- [ ] MCP-compatible tool and resource servers
- [ ] lm-evaluation-harness and custom evaluation runners
- [ ] Tracing, experiment tracking, and quality-monitoring tools

Reading-list review pending; see the original index for candidate links.

### 56.4 Scientific reading and implementation workflow

- [ ] Original papers versus secondary blog explanations
- [ ] Inspecting official source implementations
- [ ] Minimal reproducible experiments and unit tests
- [ ] Ablation tables and per-experiment hypotheses
- [ ] Version-pinned code, environments, and datasets
- [ ] Maintaining a personal concept index and revision questions

Reading-list review pending; see the original index for candidate links.

## 57. In-context learning, meta-learning, and capability theory

### 57.1 In-context learning behavior

- [ ] Few-shot learning without weight updates
- [ ] Demonstration selection, order, and label bias
- [ ] Task induction versus pattern matching
- [ ] In-context linear regression and Bayesian interpretations
- [ ] In-context algorithm learning and implicit optimization
- [ ] Context length, example diversity, and generalization

Reading-list review pending; see the original index for candidate links.

### 57.2 Emergence and capability analysis

- [ ] Induction heads and sequence copying
- [ ] Task vectors and latent task representations
- [ ] Compositional generalization and systematicity
- [ ] Grokking, memorization, and circuit formation
- [ ] Phase transitions and metric-dependent emergence claims
- [ ] Model scaling, data composition, and reasoning transfer

Reading-list review pending; see the original index for candidate links.

### 57.3 Inference-time adaptation

- [ ] Retrieval as non-parametric adaptation
- [ ] In-context demonstration optimization
- [ ] Test-time training and gradient-based updates
- [ ] Activation steering and temporary state changes
- [ ] Personalization without fine-tuning
- [ ] When to choose ICL versus RAG versus PEFT

Reading-list review pending; see the original index for candidate links.

## 58. Diffusion and non-autoregressive language models

### 58.1 Alternative generative modeling paradigms

- [ ] Autoregressive versus non-autoregressive text generation
- [ ] Masked token denoising and iterative refinement
- [ ] Discrete diffusion and categorical noising processes
- [ ] Absorbing/mask-state diffusion objectives
- [ ] Continuous-latent diffusion for text and hybrid approaches
- [ ] Diffusion versus causal language-model likelihoods

Reading-list review pending; see the original index for candidate links.

### 58.2 Training and generation

- [ ] Noise schedules, transition kernels, and denoising losses
- [ ] Iterative unmasking and confidence-based token updates
- [ ] Remasking, blockwise refinement, and parallel token decoding
- [ ] Variable iteration budgets and quality–latency trade-offs
- [ ] Conditioning, infilling, and constrained editing
- [ ] Diffusion-model serving and cache challenges

Reading-list review pending; see the original index for candidate links.

### 58.3 Models and research questions

- [ ] D3PM and theoretical foundations of discrete diffusion
- [ ] LLaDA/Dream-style masked diffusion language modeling
- [ ] Block diffusion and hybrid autoregressive–diffusion designs
- [ ] Reasoning and planning with iterative denoising
- [ ] Comparisons on throughput, quality, and controllability
- [ ] Evaluation pitfalls and emerging scaling laws

Reading-list review pending; see the original index for candidate links.

## 59. Midtraining, annealing, and specialization recipes

### 59.1 Training-stage distinctions

- [ ] General pretraining versus midtraining versus post-training
- [ ] Domain upsampling and curated high-quality mixtures
- [ ] Knowledge acquisition versus instruction following
- [ ] Context extension as an intermediate training stage
- [ ] Code/math/reasoning-focused continued pretraining
- [ ] Risk of forgetting general capabilities during specialization

Reading-list review pending; see the original index for candidate links.

### 59.2 Data-mixture and optimization schedules

- [ ] Data annealing and late-stage high-quality data
- [ ] Token-budget allocation by domain and stage
- [ ] Learning-rate restart versus continued schedule
- [ ] Replay of general data during specialist adaptation
- [ ] Dynamic mixture adjustment by validation loss
- [ ] Checkpoint selection across training transitions

Reading-list review pending; see the original index for candidate links.

### 59.3 Evaluation of staged training

- [ ] Pretrained base versus midtrained versus aligned checkpoints
- [ ] General and domain-specific capability trade-offs
- [ ] Knowledge retention and transfer benchmarks
- [ ] Measuring gains from curation versus extra compute
- [ ] Stage-ablation experiments and train–serve outcomes
- [ ] Decontamination and time-aware held-out tests

Reading-list review pending; see the original index for candidate links.

## 60. Computer-use, browser, and GUI agents

### 60.1 Perception and action interfaces

- [ ] Screenshot-based UI grounding
- [ ] DOM/accessibility tree versus visual observations
- [ ] Mouse, keyboard, scroll, and touch action spaces
- [ ] Element localization, coordinate grounding, and scaling
- [ ] Multi-step interaction plans and state tracking
- [ ] Browser sessions, authentication, and isolated execution

Reading-list review pending; see the original index for candidate links.

### 60.2 Reliability and evaluation

- [ ] Visual state-change detection and action verification
- [ ] Waiting for page loads and asynchronous UI changes
- [ ] Handling popups, captchas, errors, and dynamic layouts
- [ ] Benchmarking web and desktop task completion
- [ ] Recovery from misplaced clicks and navigation errors
- [ ] Human approval for irreversible or sensitive actions

Reading-list review pending; see the original index for candidate links.

### 60.3 Security and production architecture

- [ ] Web content as untrusted instructions
- [ ] Session sandboxing and permissions
- [ ] Credential handling and secret isolation
- [ ] Auditable interaction traces and replay
- [ ] Rate limits, policy constraints, and termination controls
- [ ] Cross-application workflow design and failure boundaries

Reading-list review pending; see the original index for candidate links.
