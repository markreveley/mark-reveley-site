---
type: Excerpt
subtype: solution
role: position
title: "A temporally-aware knowledge graph engine"
description: Zep's Graphiti — agent memory as a temporal knowledge graph synthesizing conversation and business data while keeping historical relationships.
tags: [memory, temporal, academic]
speaker: "Rasmussen et al. (Zep)"
sources:
  - id: zep
    resource: /references/zep-graphiti-paper.md
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
deps:
  - { concept: /excerpts/neo--buffer-and-static-kb.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

**[problem]** — the limitation named:

> "While existing retrieval-augmented generation (RAG) frameworks for large language model (LLM)-based agents are limited to static document retrieval, enterprise applications demand dynamic knowledge integration from diverse sources including ongoing conversations and business data." [^zep]

**[solution]**:

> "Zep addresses this fundamental limitation through its core component Graphiti -- a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships." [^zep]

# Note

Curl-verified against the arXiv abstract; problem half quoted as secondary. Adds time as the second axis of edge semantics after type.

# Relations

- **answers** → [A buffer and a static knowledge base](../excerpts/neo--buffer-and-static-kb.md)

[^zep]: Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv:2501.13956)
