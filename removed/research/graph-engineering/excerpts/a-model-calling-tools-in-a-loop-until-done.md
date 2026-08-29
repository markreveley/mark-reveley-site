---
type: Excerpt
subtype: definition
role: evidence
title: "A model calling tools in a loop until done"
description: The loop era's minimal definition of an agent, from LangChain's June 2026 loop-engineering piece.
tags: [loop-engineering]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: lc
    resource: /references/langchain-art-of-loop-engineering.md
    title: "The Art of Loop Engineering"
deps:
  - { concept: /excerpts/workflows-vs-agents.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "At its core, an agent is just a model calling tools in a loop until a task is complete." [^lc]

# Note

Curl-verified. The loop era's consensus axiom, compressing the 2024 definition; the loop-stacking position builds on it.

# Relations

- **refines** → [Workflows vs agents](../excerpts/workflows-vs-agents.md)

[^lc]: The Art of Loop Engineering
