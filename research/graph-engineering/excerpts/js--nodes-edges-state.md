---
type: Excerpt
subtype: definition
role: position
title: "Boring nodes, typed edges, checkpointed state"
description: Simmons' three commitments — the definitional core of graph engineering in its orchestration sense.
tags: [graph-engineering, control-flow, typed-edges, determinism]
speaker: "Josh C. Simmons"
sources:
  - id: js
    resource: /references/simmons-graph-engineering-phase.md
    title: "We Are Entering the Graph Engineering Phase"
deps:
  - { concept: /issues/what-is-graph-engineering.md, rel: responds-to }
  - { concept: /excerpts/anth--workflows-vs-agents.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Graph engineering is designing agentic systems as explicit graphs instead of implicit loops. Three commitments, none of them exotic. Nodes are units of capability. A node can be a model running the familiar think-act-observe cycle, a plain deterministic function, a retrieval step, or a human being. A good node is boring. It does one thing, you can test it alone, and you can swap it out without touching anything else." [^js]

> "Edges are decisions. An edge is a typed transition that carries state from one node to the next. Some edges are deterministic: tests pass, deploy. Some are model-decided: does this ticket go to billing or to abuse. The job is knowing which is which, and defaulting to deterministic everywhere you can afford to." [^js]

> "State is an object with a schema, checkpointed every time you cross an edge." [^js]

# Note

Simmons' three commitments; curl-verified. Relocates the 2024 workflow/agent dichotomy to the per-edge level.

# Relations

- **responds-to** → [What is “graph engineering”?](../issues/what-is-graph-engineering.md)
- **refines** → [Workflows vs agents](../excerpts/anth--workflows-vs-agents.md)

[^js]: We Are Entering the Graph Engineering Phase
