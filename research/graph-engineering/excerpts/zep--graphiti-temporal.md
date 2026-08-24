---
type: Excerpt
subtype: solution
title: "A temporally-aware knowledge graph engine"
description: Zep's Graphiti — agent memory as a temporal knowledge graph synthesizing conversation and business data while keeping historical relationships.
tags: [memory, temporal, academic, solution, era-agentic]
speaker: "Rasmussen et al. (Zep)"
sources:
  - id: zep
    resource: /references/zep-graphiti-paper.md
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
deps:
  - { concept: /excerpts/neo--buffer-and-static-kb.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

**[problem]** — the limitation named:

> "While existing retrieval-augmented generation (RAG) frameworks for large language model (LLM)-based agents are limited to static document retrieval, enterprise applications demand dynamic knowledge integration from diverse sources including ongoing conversations and business data." [^zep]

**[solution]**:

> "Zep addresses this fundamental limitation through its core component Graphiti -- a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships." [^zep]

# Analysis

The memory strand's flagship (January 2025), adding the dimension the other graph arguments omit: **time**. A static graph answers "what is related to X"; an agent that persists across sessions needs "what was true when," "what superseded what" — validity intervals on edges, not just types. That makes temporality the second axis of edge semantics after [typing](aio--typed-edges-one-bit.md) (note `supersedes` — the type both [Ghelbur](aio--typed-edges-one-bit.md) and the practitioner canon lead with — is inherently temporal). The problem half of the abstract is [Neo4j's buffer-and-static-KB complaint](neo--buffer-and-static-kb.md) said academically, a year earlier; the solution half is [Simmons' transcript ceiling](js--three-ceilings.md) answered on the knowledge side: memory stops being "whatever survived compaction" and becomes a queryable, versioned structure.

# Relations

- **answers** → [A buffer and a static knowledge base](neo--buffer-and-static-kb.md), [Three ceilings of the loop](js--three-ceilings.md) (memory ceiling)
- **extends** → [An untyped edge is one bit](aio--typed-edges-one-bit.md) (typing → typing + time)

[^zep]: Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv:2501.13956)
