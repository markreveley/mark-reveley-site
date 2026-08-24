---
type: Excerpt
subtype: observation
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
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "A super-step can be considered a single iteration over the graph nodes. Nodes that run in parallel are part of the same super-step, while nodes that run sequentially belong to separate super-steps." [^lgapi]

> "At the end of each super-step, nodes with no incoming messages vote to halt by marking themselves as inactive. The graph execution terminates when all nodes are inactive and no messages are in transit." [^lgapi]

# Analysis

The genealogy's smoking gun, at the level of mechanism rather than acknowledgement. "Superstep" and "vote to halt" are not generic distributed-systems vocabulary — they are Pregel's specific terms of art (Malewicz et al., SIGMOD 2010) for its bulk-synchronous execution and termination protocol, and here they are, verbatim, as the execution semantics of 2026's dominant agent-orchestration runtime. This upgrades the [acknowledged inspiration](lg--pregel-lineage.md) from a courtesy citation to inherited machinery: when a 2026 multi-agent graph runs, its parallelism barrier and its stopping rule are 2010 large-scale-graph-processing constructs, executing prompts instead of PageRank. For the [termination problem](ms--termination.md) specifically, note what this does: the *runtime's* halting rule is crisp and inherited (no messages in transit); what remains stochastic is whether a model-decided edge keeps *sending* messages — the old protocol wrapped around the new uncertainty.

# Relations

- **exemplifies** → [Vertex-centric iteration](pre--vertex-centric.md) (machinery, not homage)
- **sharpens** → [Without a termination condition](ms--termination.md)

[^lgapi]: LangGraph Graph API documentation (docs.langchain.com)
