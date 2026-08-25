---
type: Excerpt
subtype: problem
role: argument
title: "The decision lives in the structure"
description: The field guide's case against similarity search — the ten most similar chunks cannot explain a decision whose meaning is carried by relationships.
tags: [retrieval, knowledge-representation, skepticism]
speaker: "Eugeniu Ghelbur (The AI Operator)"
sources:
  - id: aio
    resource: /references/aioperator-field-guide.md
    title: "What Is Graph Engineering? A Field Guide for Builders"
deps:
  - { concept: /excerpts/rl--yes-and-no.md, rel: supports }
  - { concept: /excerpts/rl--decision-trees-vs-csv.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Vector search embeds the question and pulls the ten chunks most similar to it. […] None of them explains the decision, because the decision lives in the structure: a decision record, the thing it replaced, and the incident that triggered it." [^aio]

*(Ellipsis: intervening sentences in the original walk through the specific failing example; both quoted spans verified verbatim.)*

# Note

Curl-verified; ellipsis spans verified fragments. Argues the “no” half of yes-and-no: relationships, not chunks, carry “why”.

# Relations

- **supports** → [Yes and no: storage shapes retrieval](../excerpts/rl--yes-and-no.md)
- **supports** → [Decision trees don't fit CSV rows](../excerpts/rl--decision-trees-vs-csv.md)

[^aio]: What Is Graph Engineering? A Field Guide for Builders
