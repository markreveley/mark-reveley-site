---
type: Excerpt
subtype: problem
title: "Organized nonsense at industrial scale"
description: The graph era's characteristic failure mode — agent nodes interpret rather than execute, so a graph of agents checking agents can compound error with perfect structure.
tags: [risk, multi-agent, control-flow, skepticism, era-agentic]
speaker: "Louis-François Bouchard"
sources:
  - id: lb
    resource: /references/bouchard-what-actually-changed.md
    title: "Graph Engineering vs Loop Engineering: What Actually Changed"
deps:
  - { concept: /excerpts/gd--three-tier-reliability.md, rel: contradicts }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

**[inference]** — what actually changed:

> "Because of what lives inside the nodes. A step in a normal pipeline follows fixed rules. An agent interprets its task" [^lb]

**[problem]**:

> "a graph of agents checking agents can produce extremely organized nonsense" [^lb]

# Analysis

Bouchard's genuinely original contribution, in two moves. First, the answer to his own title question: graph *structures* are as old as [Pregel](pre--vertex-centric.md) and Airflow; what changed in 2026 is the node semantics — nodes now *interpret* tasks instead of executing rules, so the graph's formal guarantees no longer bound its behavioral guarantees. Second, the consequence: structure can launder error. A review graph whose checkers share the generator's blind spots produces outputs that are *procedurally* impeccable and *substantively* wrong — and the impeccable procedure makes the wrongness more credible, not less. This directly tempers [the three-tier reliability claim](gd--three-tier-reliability.md) (graphs make group collaboration reliable — only if failures are decorrelated) and is the agent-level analogue of [per-hop decay](aio--per-hop-decay.md): both are compounding-error arguments against naive scale. The classical fix — diversity of verifiers, ground-truth anchors ("a real verifier" in Bouchard's prescription) — is conspicuously *not* a graph property.

# Relations

- **contradicts (tempers)** → [Three tiers of reliability](gd--three-tier-reliability.md)
- **edge-level analogue** → [Per-hop accuracy compounds against you](aio--per-hop-decay.md)
- **risk counterpart of** → [Graphs contain loops](lb--graphs-contain-loops.md)

[^lb]: Graph Engineering vs Loop Engineering: What Actually Changed
