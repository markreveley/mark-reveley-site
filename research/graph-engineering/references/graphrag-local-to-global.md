---
type: Source Reference
title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization (Microsoft Research)"
description: The 2024 paper that put knowledge graphs back at the center of LLM retrieval — GraphRAG.
resource: https://arxiv.org/abs/2404.16130
tags: [level-1, retrieval, academic, knowledge-representation]
source_author: "Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, Jonathan Larson"
source_date: "2024-04-24 (v1); 2025-02-19 (v2)"
retrieved: "2026-08-24"
availability: fetched
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# About

The academic anchor of the retrieval strand: vanilla RAG fails on corpus-global questions; GraphRAG builds an LLM-derived entity knowledge graph plus community summaries and answers global questions by map-reduce over communities. Quotes verified against the arXiv abstract page.

# Excerpts in this bundle

- [RAG fails on global questions](../excerpts/grag--rag-fails-global.md)
- [An LLM-built graph index](../excerpts/grag--graph-index.md)
