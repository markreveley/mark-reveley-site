---
type: Excerpt
subtype: problem
role: argument
title: "Overhead exceeding the problem"
description: A practitioner's exit report — the graph framework taxed a linear pipeline; "structured" mistaken for "complex."
tags: [tooling, skepticism, simplicity, practice]
speaker: "DeadLocker (DEV Community)"
sources:
  - id: dl
    resource: /references/deadlocker-why-i-stopped-langgraph.md
    title: "Why I Stopped Using LangGraph"
deps:
  - { concept: /excerpts/find-the-simplest-solution-possible.md, rel: supports }
  - { concept: /excerpts/graphs-force-you-to-acknowledge-the-unmodeled.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "I had wrapped a linear pipeline with one branch in a state machine framework that required me to maintain type definitions, node signatures, and graph topology every time I wanted to tweak a prompt or adjust a threshold." [^dl]

> "The overhead of the framework was exceeding the complexity of the actual problem." [^dl]

> "I'd been confusing \"structured\" with \"complex.\" These applications weren't complex—they were sequential operations dressed up in graph because the framework made them feel more rigorous." [^dl]

# Note

Curl-verified; pseudonymous practitioner report. Itemizes the acknowledgment tax as toil; evidence of misfit below the graph's floor, not of missing capability.

# Relations

- **supports** → [Find the simplest solution possible](../excerpts/find-the-simplest-solution-possible.md)
- **refines** → [Graphs force you to acknowledge the unmodeled](../excerpts/graphs-force-you-to-acknowledge-the-unmodeled.md)

[^dl]: Why I Stopped Using LangGraph (DEV Community)
