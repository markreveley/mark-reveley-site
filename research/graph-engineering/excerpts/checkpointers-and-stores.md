---
type: Excerpt
subtype: solution
role: evidence
title: "Checkpointers and stores"
description: LangGraph's persistence — thread-scoped checkpoints for interrupts, time travel, and fault tolerance; cross-thread stores for durable knowledge.
tags: [tooling, durable-execution, memory]
speaker: "LangGraph documentation (Persistence)"
sources:
  - id: lgdocs
    resource: /references/langgraph-overview.md
    title: "LangGraph overview (LangChain docs)"
deps:
  - { concept: /excerpts/three-ceilings-of-the-loop.md, rel: answers }
  - { concept: /excerpts/durable-execution.md, rel: exemplifies }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "Checkpointers persist a thread's graph state as checkpoints. Use them for short-term, thread-scoped memory, including conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance." [^lgdocs]

> "Stores persist application-defined data outside the graph state. Use them for long-term, cross-thread memory, including user preferences, facts, and shared knowledge." [^lgdocs]

# Note

Curl-verified documentation. Durable execution shipped for agent graphs; the Store's key-value/vector shape marks the knowledge-graph gap at the API surface.

# Relations

- **answers** → [Three ceilings of the loop](../excerpts/three-ceilings-of-the-loop.md)
- **exemplifies** → [Durable Execution](../excerpts/durable-execution.md)

[^lgdocs]: LangGraph Persistence documentation (docs.langchain.com)
