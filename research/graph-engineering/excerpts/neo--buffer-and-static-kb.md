---
type: Excerpt
subtype: problem
role: position
title: "A buffer and a static knowledge base"
description: Neo4j's diagnosis of agent unreliability — memory that is only a conversation buffer plus a static store, losing the plan across loops.
tags: [memory, risk, era-agentic]
speaker: "Jim Webber (Neo4j)"
sources:
  - id: neo
    resource: /references/neo4j-context-graphs.md
    title: "Context graphs: Why AI agents need three types of memory"
deps:
  - { concept: /excerpts/js--three-ceilings.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Many AI agents today are unreliable because their memory, if it even exists, consists of a simple conversation buffer and static knowledge base." [^neo]

> "They read your goal, plan their actions, look up facts from one store, and run a similarity search in another. After many more loops, they forget the original plan." [^neo]

# Note

Curl-verified. Vendor diagnosis of agent-memory failure; note the interest — Neo4j sells the prescribed substrate.

# Relations

- **supports** → [Three ceilings of the loop](../excerpts/js--three-ceilings.md)

[^neo]: Context graphs: Why AI agents need three types of memory
