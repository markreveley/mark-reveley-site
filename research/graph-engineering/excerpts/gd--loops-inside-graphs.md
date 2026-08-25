---
type: Excerpt
subtype: claim
role: position
title: "Loops live inside the nodes"
description: "The nesting claim — important nodes still contain loops; the graph organizes, constrains, and connects them. Plus the restraint prescription: graph only the necessary relationships."
tags: [control-flow, orchestration, loop-engineering, simplicity, era-agentic]
speaker: "Gao Dalie (高達烈)"
sources:
  - id: gd
    resource: /references/gaodalie-forget-loop-engineering.md
    title: "FORGET Loop Engineering. Graph Engineering is about THIS"
deps:
  - { concept: /issues/loops-vs-graphs.md, rel: responds-to }
  - { concept: /excerpts/lb--graphs-contain-loops.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Each important node may still contain a loop; the graph determines how these loops are organized, constrained, and connected." [^gd]

**[prescription]** — the restraint clause:

> "Graph engineering isn't about creating complex diagrams. Design involves clearly indicating only the necessary relationships and discarding unnecessary automation." [^gd]

# Note

Curl-verified; the restraint clause is a secondary prescription from the same source.

# Relations

- **responds-to** → [Loops versus graphs](../issues/loops-vs-graphs.md)
- **supports** → [Graphs contain loops](../excerpts/lb--graphs-contain-loops.md)

[^gd]: FORGET Loop Engineering. Graph Engineering is about THIS
