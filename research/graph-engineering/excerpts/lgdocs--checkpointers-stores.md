---
type: Excerpt
subtype: solution
title: "Checkpointers and stores"
description: LangGraph's persistence — thread-scoped checkpoints for interrupts, time travel, and fault tolerance; cross-thread stores for durable knowledge.
tags: [tooling, durable-execution, memory, era-agentic]
speaker: "LangGraph documentation (Persistence)"
sources:
  - id: lgdocs
    resource: /references/langgraph-overview.md
    title: "LangGraph overview (LangChain docs)"
deps:
  - { concept: /excerpts/js--three-ceilings.md, rel: answers }
  - { concept: /excerpts/tmp--durable-execution.md, rel: exemplifies }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "Checkpointers persist a thread's graph state as checkpoints. Use them for short-term, thread-scoped memory, including conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance." [^lgdocs]

> "Stores persist application-defined data outside the graph state. Use them for long-term, cross-thread memory, including user preferences, facts, and shared knowledge." [^lgdocs]

# Analysis

The capability audit's second pillar: [Simmons' three ceilings](js--three-ceilings.md) — transcript-as-state, no pause button, all-or-nothing failure — are each answered by shipped machinery here: schema'd state checkpointed per superstep, interrupts for human approval with resume, time travel, fault tolerance. This is [durable execution](tmp--durable-execution.md) implemented for agent graphs, and it means the *orchestration* sense of graph engineering is not aspirational: it is documented product. The audit's honest gap sits in the second quote: `Store` is application-defined key-value/vector memory — "facts, shared knowledge" — but not a typed, temporal knowledge graph; nothing in the runtime relates two stored facts by `supersedes` or `caused`. The knowledge half of graph engineering ([typed edges](aio--typed-edges-one-bit.md), [temporal graphs](zep--graphiti-temporal.md)) lives in separate systems, joined to the execution graph by application code — the "one graph or two" gap, visible at the API surface.

# Relations

- **answers** → [Three ceilings of the loop](js--three-ceilings.md)
- **exemplifies** → [Durable Execution](tmp--durable-execution.md)
- **gap remains** → [A temporally-aware knowledge graph engine](zep--graphiti-temporal.md)

[^lgdocs]: LangGraph Persistence documentation (docs.langchain.com)
