---
type: Excerpt
subtype: solution
role: position
title: "An LLM-built graph index"
description: GraphRAG's mechanism — derive an entity knowledge graph from documents, pre-generate community summaries, answer global questions by map-reduce over communities.
tags: [retrieval, solution, academic, knowledge-representation, era-agentic]
speaker: "Edge et al. (Microsoft Research)"
sources:
  - id: grag
    resource: /references/graphrag-local-to-global.md
    title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
deps:
  - { concept: /excerpts/grag--rag-fails-global.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities." [^grag]

# Note

Curl-verified against the arXiv abstract. The construction bet — the consumer becomes the producer — shared with the LLM-wiki and OKF evidence.

# Relations

- **answers** → [RAG fails on global questions](../excerpts/grag--rag-fails-global.md)

[^grag]: From Local to Global: A Graph RAG Approach to Query-Focused Summarization (arXiv:2404.16130)
