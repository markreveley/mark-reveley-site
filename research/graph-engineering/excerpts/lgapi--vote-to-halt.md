---
type: Excerpt
subtype: observation
role: evidence
title: "Supersteps and the vote to halt"
description: LangGraph's execution semantics are Pregel's, verbatim — supersteps, message passing, and termination by inactive-node vote.
tags: [tooling, orchestration, history, era-agentic, determinism]
speaker: "LangGraph documentation (Graph API)"
sources:
  - id: lgapi
    resource: /references/langgraph-overview.md
    title: "LangGraph overview (LangChain docs)"
deps:
  - { concept: /excerpts/pre--vertex-centric.md, rel: exemplifies }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "A super-step can be considered a single iteration over the graph nodes. Nodes that run in parallel are part of the same super-step, while nodes that run sequentially belong to separate super-steps." [^lgapi]

> "At the end of each super-step, nodes with no incoming messages vote to halt by marking themselves as inactive. The graph execution terminates when all nodes are inactive and no messages are in transit." [^lgapi]

# Note

Curl-verified documentation. Pregel's exact terms of art — superstep, vote to halt — as the 2026 runtime's execution semantics.

# Relations

- **exemplifies** → [Vertex-centric iteration](../excerpts/pre--vertex-centric.md)

[^lgapi]: LangGraph Graph API documentation (docs.langchain.com)
