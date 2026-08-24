---
type: Excerpt
subtype: problem
title: "Overhead exceeding the problem"
description: A practitioner's exit report — the graph framework taxed a linear pipeline; "structured" mistaken for "complex."
tags: [tooling, skepticism, simplicity, era-agentic, practice]
speaker: "DeadLocker (DEV Community)"
sources:
  - id: dl
    resource: /references/deadlocker-why-i-stopped-langgraph.md
    title: "Why I Stopped Using LangGraph"
deps:
  - { concept: /excerpts/anth--simplest-solution.md, rel: supports }
  - { concept: /excerpts/36kr--graphs-force-acknowledgment.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "I had wrapped a linear pipeline with one branch in a state machine framework that required me to maintain type definitions, node signatures, and graph topology every time I wanted to tweak a prompt or adjust a threshold." [^dl]

> "The overhead of the framework was exceeding the complexity of the actual problem." [^dl]

> "I'd been confusing \"structured\" with \"complex.\" These applications weren't complex—they were sequential operations dressed up in graph because the framework made them feel more rigorous." [^dl]

# Analysis

The field report the paradigm debate needs and mostly lacks: not "graphs don't work" but "graphs *cost*, and the cost is fixed while the benefit scales with real branching." Three precise observations. The maintenance coupling — schema, signatures, topology all move when one prompt changes — is [Catacora's acknowledgment tax](36kr--graphs-force-acknowledgment.md) experienced as toil rather than insight. "Confusing 'structured' with 'complex'" names the psychological mechanism of graph over-adoption: explicit structure *feels* like rigor, so linear problems get dressed in topology (the diagram-theater failure [Gao Dalie warned about](gd--loops-inside-graphs.md) from inside the pro-graph camp). And the implied decision rule — pay for the graph only when the problem's real shape has branches, joins, or long-lived state — is [Anthropic's simplicity prescription](anth--simplest-solution.md) derived from a receipt instead of a principle. For the LangGraph question specifically: this is evidence about *fit*, not capability — the same machinery the [capability audit](lgdocs--checkpointers-stores.md) credits is here misapplied to a problem below its floor.

# Relations

- **supports** → [Find the simplest solution possible](anth--simplest-solution.md)
- **refines** → [Graphs force you to acknowledge the unmodeled](36kr--graphs-force-acknowledgment.md) (the tax, itemized)
- **warned from inside by** → [Loops live inside the nodes](gd--loops-inside-graphs.md)

[^dl]: Why I Stopped Using LangGraph (DEV Community)
