---
type: Excerpt
subtype: solution
role: position
title: "Three memories, one context graph"
description: Neo4j's proposal — long-term knowledge, short-term conversation, and reasoning memory for decision traces, unified in a graph grounded in the data's entities.
tags: [memory]
speaker: "Jim Webber (Neo4j)"
sources:
  - id: neo
    resource: /references/neo4j-context-graphs.md
    title: "Context graphs: Why AI agents need three types of memory"
deps:
  - { concept: /issues/one-graph-or-two.md, rel: responds-to }
  - { concept: /excerpts/neo--buffer-and-static-kb.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "We propose a context graph (or agentic memory model) with three components: long-term memory for knowledge, short-term memory for conversation, and reasoning memory for decision traces." [^neo]

> "A context graph works by capturing decision traces and linking them directly to the entities in your data, ensuring that your agent's reasoning is grounded in the actual state of the world." [^neo]

# Note

Curl-verified. The unification position: knowledge, conversation, and decision traces in one context graph.

# Relations

- **responds-to** → [One graph or two?](../issues/one-graph-or-two.md)
- **answers** → [A buffer and a static knowledge base](../excerpts/neo--buffer-and-static-kb.md)

[^neo]: Context graphs: Why AI agents need three types of memory
