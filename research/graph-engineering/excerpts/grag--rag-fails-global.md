---
type: Excerpt
subtype: problem
role: position
title: "RAG fails on global questions"
description: The GraphRAG paper's problem statement — retrieval cannot answer questions about a corpus as a whole, because they are summarization tasks, not retrieval tasks.
tags: [retrieval, academic, knowledge-representation]
speaker: "Edge et al. (Microsoft Research)"
sources:
  - id: grag
    resource: /references/graphrag-local-to-global.md
    title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
deps:
  - { concept: /issues/is-it-just-retrieval.md, rel: responds-to }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "However, RAG fails on global questions directed at an entire text corpus, such as \"What are the main themes in the dataset?\", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task." [^grag]

# Note

Curl-verified against the arXiv abstract. The peer-reviewed position that some questions are not retrieval tasks at all; its mechanism node answers it.

# Relations

- **responds-to** → [Is it just fancier retrieval?](../issues/is-it-just-retrieval.md)

[^grag]: From Local to Global: A Graph RAG Approach to Query-Focused Summarization (arXiv:2404.16130)
