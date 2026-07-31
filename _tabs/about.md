---
# the default layout is 'page'
icon: fas fa-info-circle
order: 5
---

Hey, I am Harsha — an engineer who builds systems and measures them: how models are served
efficiently, how agents are made reliable enough to trust, how both behave under adversarial
pressure, and what the infrastructure underneath — gateways, ledgers, matching engines — actually
costs when you benchmark it honestly.

{% assign ml = site.projects | where: 'track', 'ml' %}
{% assign fde = site.projects | where: 'track', 'fde' %}
{% assign sde = site.projects | where: 'track', 'sde' %}
{% assign hft = site.projects | where: 'track', 'hft' %}
{% assign backend = site.projects | where: 'track', 'backend' %}

Most of my recent work is in [projects]({{ '/projects/' | relative_url }}) —
{{ site.projects | size }} shipped systems across five engineering tracks, every one a working
implementation with committed benchmark reports:

- **[Machine learning & AI systems]({{ '/projects/#ml' | relative_url }})** ({{ ml.size }}) —
  LLM serving internals, agent reliability, multi-agent protocols, AI security, retrieval and
  memory, cost, and post-training. Highlights:
  **[PageServe]({{ '/projects/pageserve/' | relative_url }})** (continuous batching and a paged
  KV cache, token-for-token exact),
  **[Durable Agents]({{ '/projects/durable-agents/' | relative_url }})** (`kill -9` mid-task,
  resumes exactly-once), and
  **[InjectGuard]({{ '/projects/injectguard/' | relative_url }})** (prompt-injection containment
  by construction, 100% → 0% attack success).
- **[Forward-deployed engineering]({{ '/projects/#fde' | relative_url }})** ({{ fde.size }}) —
  making agents function inside real organizations:
  **[Enterprise Agent Deployment]({{ '/projects/enterprise-agent-deployment/' | relative_url }})**
  (approval gates defined over effects, not tool names),
  **[Legacy MCP]({{ '/projects/legacy-mcp/' | relative_url }})** (0/6 → 6/6 task success through a
  governed wrapper over an authentically awful SOAP backend), and
  **[DocPipe]({{ '/projects/docpipe/' | relative_url }})** (a document pipeline that verifies its
  own extractions).
- **[Software engineering]({{ '/projects/#sde' | relative_url }})** ({{ sde.size }}) — developer
  infrastructure for the agent era:
  **[Sandboxd]({{ '/projects/sandboxd/' | relative_url }})** (the same hostile suite run on gVisor
  and Firecracker, so isolation and latency are compared rather than asserted),
  **[RepoCtx]({{ '/projects/repoctx/' | relative_url }})** (repo-scale context that lifts an 8B
  agent's file recall 3.4x), and
  **[MiniTemporal]({{ '/projects/minitemporal/' | relative_url }})** (a durable-execution engine
  in ~2k lines of stdlib Go, chaos-verified).
- **[HFT & low latency]({{ '/projects/#hft' | relative_url }})** ({{ hft.size }}) — latency
  engineering and market microstructure:
  **[Tick2Trade]({{ '/projects/tick2trade/' | relative_url }})** (583 ns p99 internal with a
  published per-hop budget),
  **[Matchbook]({{ '/projects/matchbook/' | relative_url }})** (a zero-unsafe Rust matching engine
  within 1.01-1.09x of pointer-based C++, verified by 2.49B fuzz executions), and
  **[Deadman]({{ '/projects/deadman/' | relative_url }})** (a kill switch model-checked in TLA+,
  with the Go core replaying all 23,240 model sequences).
- **[Backend engineering]({{ '/projects/#backend' | relative_url }})** ({{ backend.size }}) — the
  service layer AI products stand on:
  **[LLM Gateway]({{ '/projects/llmgw/' | relative_url }})** (1.84 ms p99 added latency, cost
  ledger exact to the picodollar),
  **[Meterd]({{ '/projects/meterd/' | relative_url }})** (292,792 chaos deliveries reconciling
  exactly), and
  **[Flowd]({{ '/projects/flowd/' | relative_url }})** (durable execution surviving 165 worker
  SIGKILLs with zero lost or duplicated effects).

A habit that runs through all of them: build the measurement harness before drawing the
conclusion, report the number the harness produced — and keep the honest negatives.

## Interests

1. LLM inference and serving efficiency
2. Agent reliability, evaluation, and durable execution
3. Low-latency systems and market microstructure
4. Backend infrastructure for AI products — gateways, metering, multi-tenant isolation
5. Information retrieval and recommendation systems
6. The intersection of ML and privacy

## Publication

**Data Efficient Subset Training with Differential Privacy** —
[arXiv:2503.06732](https://arxiv.org/abs/2503.06732)

I am also passionate about open source and contributing to the community. You can find my code on
[GitHub](https://github.com/harsha-moparthy).
