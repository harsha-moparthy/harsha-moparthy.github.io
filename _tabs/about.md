---
# the default layout is 'page'
icon: fas fa-info-circle
order: 5
---

Hey, I am Harsha — an ML engineer interested in the systems side of machine learning: how models are
served efficiently, how agents are made reliable enough to trust, and how both fail under adversarial
pressure.

Most of my recent work is in [projects]({{ '/projects/' | relative_url }}) — six systems built around
LLM inference and agent reliability:

- **[PageServe]({{ '/projects/pageserve/' | relative_url }})** and
  **[KVStudy]({{ '/projects/kvstudy/' | relative_url }})** — LLM serving internals: continuous batching,
  paged KV caches, and what cache compression actually costs in quality.
- **[InjectGuard]({{ '/projects/injectguard/' | relative_url }})** and
  **[MCPGate]({{ '/projects/mcpgate/' | relative_url }})** — AI systems security: prompt-injection
  containment by construction, and putting authorization in the graph rather than the prompt.
- **[Trajeval]({{ '/projects/trajeval/' | relative_url }})** and
  **[Durable Agents]({{ '/projects/durable-agents/' | relative_url }})** — agent reliability: telling a
  real regression from run-to-run noise, and surviving a `kill -9` mid-task.

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
