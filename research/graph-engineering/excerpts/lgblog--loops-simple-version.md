---
type: Excerpt
subtype: inference
role: position
title: "Loop engineering is a simple version of graphs"
description: LangChain's formal subsumption — loops are the one-node special case, and production agents need cycles anyway.
tags: [control-flow, loop-engineering, graph-engineering, orchestration]
speaker: "Sydney Runkle and Harrison Chase (LangChain)"
sources:
  - id: lgb
    resource: /references/langchain-3-years-langgraph.md
    title: "3 Years of Graph Engineering with LangGraph"
deps:
  - { concept: /issues/loops-vs-graphs.md, rel: responds-to }
  - { concept: /excerpts/lb--graphs-contain-loops.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Loop engineering isn't an alternative to graphs, so much as a simple version of them." [^lgb]

**[claim]** — the node model and the cycles argument:

> "In LangGraph, nodes do work. A node can be deterministic code, a single LLM call, a tool call, or a full agent with its own internal loop." [^lgb]

> "Production agents need cycles: retrying failed tool calls, asking users for missing information, revising answers after validation." [^lgb]

# Note

Curl-verified. The formal subsumption position: a loop is the one-node cyclic graph; node taxonomy matches the commitments node nearly verbatim.

# Relations

- **responds-to** → [Loops versus graphs](../issues/loops-vs-graphs.md)
- **refines** → [Graphs contain loops](../excerpts/lb--graphs-contain-loops.md)

[^lgb]: 3 Years of Graph Engineering with LangGraph
