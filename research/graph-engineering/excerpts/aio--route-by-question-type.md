---
type: Excerpt
subtype: prescription
title: "Route by question type"
description: The practitioner consensus — vector for lookups, graph for chains; hybrid, not conversion.
tags: [retrieval, prescription-hybrid, era-agentic, practice]
speaker: "Eugeniu Ghelbur (The AI Operator)"
sources:
  - id: aio
    resource: /references/aioperator-field-guide.md
    title: "What Is Graph Engineering? A Field Guide for Builders"
deps:
  - { concept: /excerpts/aio--per-hop-decay.md, rel: answers }
  - { concept: /excerpts/rl--yes-and-no.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "The practitioner consensus: route by question type. Vector for lookups, graph for chains." [^aio]

# Analysis

Eight words that settle the seed thread's argument better than either of its participants did. The OP's ["just fancier retrieval?"](rl--just-fancier-retrieval.md) presumes one retrieval mechanism with variable fanciness; the consensus answer is that there are (at least) two mechanisms with disjoint strengths — similarity answers "what is X," traversal answers "why/how/what-changed" — and the engineering is in the router, not in picking a winner. It operationalizes the commenter's ["well yes and no"](rl--yes-and-no.md) and prices in [per-hop decay](aio--per-hop-decay.md) (spend hops only where the question demands structure). Consonant with the guide's benchmark summary (graphs win multi-hop, temporal, corpus-synthesis; lose simple lookup and cost) and with [GraphRAG's](grag--graph-index.md) architecture, which keeps both indexes. The unresolved question the prescription hides: who classifies the question — a heuristic, a model, or another graph?

# Relations

- **answers** → [Per-hop accuracy compounds against you](aio--per-hop-decay.md)
- **supports** → [Yes and no: storage shapes retrieval](rl--yes-and-no.md)
- **instantiated by** → [An LLM-built graph index](grag--graph-index.md)

[^aio]: What Is Graph Engineering? A Field Guide for Builders
