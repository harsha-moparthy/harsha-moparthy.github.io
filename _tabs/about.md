---
# the default layout is 'page'
icon: fas fa-info-circle
order: 5
---

Hey, I am Harsha — an ML engineer interested in the systems side of machine learning: how models are
served efficiently, how agents are made reliable enough to trust, and how both fail under adversarial
pressure.

Most of my recent work is in [projects]({{ '/projects/' | relative_url }}) — {{ site.projects | size }}
machine-learning systems built across seven areas:

- **[PageServe]({{ '/projects/pageserve/' | relative_url }})**,
  **[KVStudy]({{ '/projects/kvstudy/' | relative_url }})** and
  **[SpecDec]({{ '/projects/specdec/' | relative_url }})** — LLM serving internals: continuous
  batching, paged KV caches, what cache compression costs in quality, and why an exactly-correct
  speculative decoder can still lose on wall-clock.
- **[Trajeval]({{ '/projects/trajeval/' | relative_url }})** and
  **[Computer-Use Agent Sandbox]({{ '/projects/computer-use-agent-sandbox/' | relative_url }})** —
  agent reliability: telling a real regression from run-to-run noise, and benchmarking a browser agent
  against a fixture proven solvable first.
- **[Durable Agents]({{ '/projects/durable-agents/' | relative_url }})** and
  **[A2A Interop]({{ '/projects/a2a-interop/' | relative_url }})** — multi-agent systems: surviving a
  `kill -9` mid-task, and what an agent-interop protocol under-specifies once you implement it.
- **[InjectGuard]({{ '/projects/injectguard/' | relative_url }})** and
  **[MCPGate]({{ '/projects/mcpgate/' | relative_url }})** — AI systems security: prompt-injection
  containment by construction, and putting authorization in the graph rather than the prompt.
- **[RAGStudy]({{ '/projects/ragstudy/' | relative_url }})** and
  **[Memlayer]({{ '/projects/agent-long-term-memory/' | relative_url }})** — retrieval and memory:
  where an agentic retrieval loop actually pays for itself, and isolating a memory layer's contribution
  from the model's own ability.
- **[CostRouter]({{ '/projects/costrouter/' | relative_url }})** and
  **[GenAI Observability]({{ '/projects/genai-observability-otel/' | relative_url }})** — cost and
  observability: routing against the honest null of random-at-equal-spend, and instrumenting an LLM app
  to the OpenTelemetry GenAI conventions.
- **[Synth Pipeline]({{ '/projects/synth-pipeline/' | relative_url }})** — training data: measuring
  that unfiltered synthetic data made a model *worse* than no synthetic data at all.

A habit that runs through all of them: reporting the baseline I lose to, the metric that disagrees with
my conclusion, and the bugs that produced convincing-looking wrong answers before I caught them.

## Interests

1. LLM inference and serving efficiency
2. Agent reliability, evaluation, and durable execution
3. Deep learning architectures and their applications
4. Information retrieval and recommendation systems
5. The intersection of ML and privacy

## Publication

**Data Efficient Subset Training with Differential Privacy** —
[arXiv:2503.06732](https://arxiv.org/abs/2503.06732)

I am also passionate about open source and contributing to the community. You can find my code on
[GitHub](https://github.com/harsha-moparthy).
