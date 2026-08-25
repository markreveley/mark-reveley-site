---
type: Excerpt
subtype: definition
role: position
title: "Stack and extend loops"
description: Loop engineering defined as loop composition — agent, verification, event-driven, and hill-climbing loops stacked into systems.
tags: [loop-engineering, verification, era-agentic]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: lc
    resource: /references/langchain-art-of-loop-engineering.md
    title: "The Art of Loop Engineering"
deps:
  - { concept: /issues/loops-vs-graphs.md, rel: responds-to }
  - { concept: /excerpts/lc--model-calling-tools-in-loop.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "[…] the idea that you can stack and extend loops to build more effective agents" [^lc]

**[prescription]** — the second loop:

> "[…] it's often useful to wrap it in a verification loop that checks the output and sends feedback back to the model when it falls short." [^lc]

# Note

Curl-verified. Loop composition as the discipline, one month before the graph turn; its levels 3–4 already describe connective structure.

# Relations

- **responds-to** → [Loops versus graphs](../issues/loops-vs-graphs.md)
- **refines** → [A model calling tools in a loop until done](../excerpts/lc--model-calling-tools-in-loop.md)

[^lc]: The Art of Loop Engineering
