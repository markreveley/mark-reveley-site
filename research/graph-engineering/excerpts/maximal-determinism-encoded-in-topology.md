---
type: Excerpt
subtype: claim
role: position
title: "Maximal determinism, encoded in topology"
description: LangChain's own characterization of LangGraph — domain knowledge encoded in the graph's shape instead of left to the model's judgment.
tags: [tooling, determinism, control-flow]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: da
    resource: /references/langchain-deep-agents.md
    title: "Deep Agents vs LangChain vs LangGraph"
deps:
  - { concept: /excerpts/the-ai-moves-within-a-pre-designed-map.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "LangGraph offers maximal determinism: it lets you encode domain knowledge directly into the graph's topology instead of leaving that judgment to a model." [^da]

> "LangGraph is the escape hatch that lets you build a completely custom graph, encoding your workflow's specific logic directly into its shape." [^da]

# Note

Curl-verified. The vendor's own characterization, three weeks after the naming event: topology as a knowledge medium — and the graph as escape hatch, not default.

# Relations

- **supports** → [The AI moves within a pre-designed map](../excerpts/the-ai-moves-within-a-pre-designed-map.md)

[^da]: Deep Agents vs LangChain vs LangGraph (LangChain blog)
