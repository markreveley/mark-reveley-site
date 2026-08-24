---
type: Excerpt
subtype: problem
title: "The decision lives in the structure"
description: The field guide's case against similarity search — the ten most similar chunks cannot explain a decision whose meaning is carried by relationships.
tags: [retrieval, knowledge-representation, era-agentic, skepticism]
speaker: "Eugeniu Ghelbur (The AI Operator)"
sources:
  - id: aio
    resource: /references/aioperator-field-guide.md
    title: "What Is Graph Engineering? A Field Guide for Builders"
deps:
  - { concept: /excerpts/rl--just-fancier-retrieval.md, rel: answers }
  - { concept: /excerpts/rl--decision-trees-vs-csv.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Vector search embeds the question and pulls the ten chunks most similar to it. […] None of them explains the decision, because the decision lives in the structure: a decision record, the thing it replaced, and the incident that triggered it." [^aio]

*(Ellipsis: intervening sentences in the original walk through the specific failing example; both quoted spans verified verbatim.)*

# Analysis

The crispest direct answer to [the skeptic's "just fancier retrieval?"](rl--just-fancier-retrieval.md): no — because similarity is a property of *text*, while the answer to "why" is a property of *relationships between records*. A decision's meaning is constituted by supersedes/caused/triggered edges; no chunk contains it, so no top-k over chunks retrieves it. This is [the seed thread's "storage shapes retrieval"](rl--yes-and-no.md) with the mechanism named, and the everyday-scale version of [GraphRAG's corpus-global failure case](grag--rag-fails-global.md). It also sets up the guide's own discipline: the argument only holds if edges are typed ([one bit vs. meaning](aio--typed-edges-one-bit.md)) — an untyped link graph would leave "why" just as unrecoverable as the chunk store does.

# Relations

- **answers** → [The skeptic's question](rl--just-fancier-retrieval.md)
- **supports** → [Decision trees don't fit CSV rows](rl--decision-trees-vs-csv.md)
- **formal version** → [RAG fails on global questions](grag--rag-fails-global.md)

[^aio]: What Is Graph Engineering? A Field Guide for Builders
