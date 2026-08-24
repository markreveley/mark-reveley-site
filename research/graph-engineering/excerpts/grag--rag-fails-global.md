---
type: Excerpt
subtype: problem
title: "RAG fails on global questions"
description: The GraphRAG paper's problem statement — retrieval cannot answer questions about a corpus as a whole, because they are summarization tasks, not retrieval tasks.
tags: [retrieval, academic, era-agentic, knowledge-representation]
speaker: "Edge et al. (Microsoft Research)"
sources:
  - id: grag
    resource: /references/graphrag-local-to-global.md
    title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
deps:
  - { concept: /excerpts/rl--just-fancier-retrieval.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "However, RAG fails on global questions directed at an entire text corpus, such as \"What are the main themes in the dataset?\", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task." [^grag]

# Analysis

The peer-reviewed version of the seed thread's dispute, and it *refines* rather than merely answers [the OP's "just fancier retrieval?"](rl--just-fancier-retrieval.md): the paper's point is that some questions are **not retrieval tasks at all** — no set of retrieved chunks answers "what are the main themes," because the answer is a property of the corpus's structure, not of any passage in it. So the graph is not fancier retrieval; it is the move that makes a *different task class* (global sensemaking) tractable. This is [the field guide's "the decision lives in the structure"](aio--decision-lives-in-structure.md) with a benchmark attached, and the strongest single citation against the reduction. Dated to April 2024, it also shows the substance preceding the 2026 name by two years.

# Relations

- **refines** → [The skeptic's question](rl--just-fancier-retrieval.md) (some questions aren't retrieval)
- **answered by** → [An LLM-built graph index](grag--graph-index.md)
- **everyday version** → [The decision lives in the structure](aio--decision-lives-in-structure.md)

[^grag]: From Local to Global: A Graph RAG Approach to Query-Focused Summarization (arXiv:2404.16130)
