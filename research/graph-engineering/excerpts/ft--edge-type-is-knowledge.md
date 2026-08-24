---
type: Excerpt
subtype: claim
title: "The edge type IS the knowledge"
description: The maximal typed-edge thesis — relatedness is trivial to detect; the typed edge is what answers "why did this change?"
tags: [typed-edges, knowledge-representation, era-agentic]
speaker: "Flowtivity (unattributed)"
sources:
  - id: ft
    resource: /references/flowtivity-loops-to-graphs.md
    title: "From Loops to Graphs: The Next Paradigm in AI Agent Engineering"
deps:
  - { concept: /excerpts/aio--typed-edges-one-bit.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "the edge type IS the knowledge. Not the nodes — any system can find two related documents. The typed edge is what lets an agent answer \"Why did this change?\" […]" [^ft]

# Analysis

The strongest form of the typed-edge position: nodes are commodities (any embedding store can produce "related documents"), so the entire value-add of the graph is concentrated in edge semantics. As an emphasis it is corrective; taken literally it overshoots — nodes carry identity, and identity is where [per-hop decay](aio--per-hop-decay.md) actually enters (a mis-resolved entity corrupts every typed edge attached to it, however precise the types). The productive reading: relatedness is *recall*, typing is *meaning*, identity is *soundness*, and a useful graph needs all three, with typing the scarcest in practice. Independent recurrence of the same thesis in [Ghelbur](aio--typed-edges-one-bit.md) and [Simmons](js--nodes-edges-state.md) the same month — across the knowledge and orchestration camps — makes typed edges the best candidate for "the actual content" of graph engineering, the part that survives if the name does not. It is also the specific dimension on which [OKF's untyped links](okf--formalizes-llm-wiki.md) are thinnest.

# Relations

- **supports** → [An untyped edge is one bit](aio--typed-edges-one-bit.md)
- **refines** → [Explicit graphs an agent can traverse](ft--explicit-graphs-definition.md)
- **tempered by** → [Per-hop accuracy compounds against you](aio--per-hop-decay.md)

[^ft]: From Loops to Graphs: The Next Paradigm in AI Agent Engineering
