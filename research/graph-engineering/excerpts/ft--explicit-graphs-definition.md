---
type: Excerpt
subtype: definition
role: position
title: "Explicit graphs an agent can traverse"
description: Flowtivity's definition uniting both senses — entities, decisions, and concepts as nodes; typed edges; traversal by the agent — plus the concurrency argument against loops.
tags: [graph-engineering, typed-edges, concurrency]
speaker: "Flowtivity (unattributed)"
sources:
  - id: ft
    resource: /references/flowtivity-loops-to-graphs.md
    title: "From Loops to Graphs: The Next Paradigm in AI Agent Engineering"
deps:
  - { concept: /issues/what-is-graph-engineering.md, rel: responds-to }
  - { concept: /excerpts/js--nodes-edges-state.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Graph engineering is designing AI systems around explicit graphs — networks of nodes (entities, decisions, concepts) connected by typed edges (relationships) that an agent can traverse." [^ft]

**[claim]** — the concurrency argument:

> "A loop processes plan, code, review, fix, review again, fix again — sequentially. A graph dispatches 3 reviewers simultaneously." [^ft]

# Note

Curl-verified. The both-senses definition — knowledge-flavored nodes, orchestration-flavored traversal; see the one-graph-or-two issue for what that equivocation opens.

# Relations

- **responds-to** → [What is “graph engineering”?](../issues/what-is-graph-engineering.md)
- **supports** → [Boring nodes, typed edges, checkpointed state](../excerpts/js--nodes-edges-state.md)

[^ft]: From Loops to Graphs: The Next Paradigm in AI Agent Engineering
