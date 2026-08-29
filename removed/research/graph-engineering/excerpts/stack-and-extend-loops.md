---
type: Excerpt
subtype: definition
role: position
title: "Stack and extend loops"
description: Loop engineering defined as loop composition — agent, verification, event-driven, and hill-climbing loops stacked into systems.
tags: [loop-engineering, verification]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: lc
    resource: /references/langchain-art-of-loop-engineering.md
    title: "The Art of Loop Engineering"
deps:
  - { concept: /excerpts/a-model-calling-tools-in-a-loop-until-done.md, rel: refines }
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

- **refines** → [A model calling tools in a loop until done](../excerpts/a-model-calling-tools-in-a-loop-until-done.md)

[^lc]: The Art of Loop Engineering
