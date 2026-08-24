---
type: Excerpt
subtype: solution
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
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities." [^grag]

# Analysis

The solution's important property is *who builds the graph*: an LLM. Two decades of knowledge-graph practice foundered on construction cost — ontologists, curation, entity resolution by hand (the failure mode of the semantic-web era). GraphRAG's bet is that the same models that need the structure can now afford to build it, which is also [Karpathy's LLM-wiki premise](ka--compiled-once.md) ("compiled once and then kept current" — by the model) and [OKF's motivating assumption](spec--maintained-by-agents.md) (corpora "continuously written and maintained by agents"). That inversion — graphs became cheap because the consumer became the producer — is this bundle's best candidate for the *material* cause of the whole 2024–2026 graph revival, beneath the discourse. The community-summary stage is [route-by-question-type](aio--route-by-question-type.md) built in: local questions hit entities, global questions hit community summaries.

# Relations

- **answers** → [RAG fails on global questions](grag--rag-fails-global.md)
- **shares the construction bet with** → [Compiled once, kept current](ka--compiled-once.md), [A corpus continuously maintained by agents](spec--maintained-by-agents.md)

[^grag]: From Local to Global: A Graph RAG Approach to Query-Focused Summarization (arXiv:2404.16130)
