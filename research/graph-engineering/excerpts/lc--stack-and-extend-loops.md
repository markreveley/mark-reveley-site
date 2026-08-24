---
type: Excerpt
subtype: definition
title: "Stack and extend loops"
description: Loop engineering defined as loop composition — agent, verification, event-driven, and hill-climbing loops stacked into systems.
tags: [loop-engineering, verification, era-agentic]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: lc
    resource: /references/langchain-art-of-loop-engineering.md
    title: "The Art of Loop Engineering"
deps:
  - { concept: /excerpts/lc--model-calling-tools-in-loop.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "[…] the idea that you can stack and extend loops to build more effective agents" [^lc]

**[prescription]** — the second loop:

> "[…] it's often useful to wrap it in a verification loop that checks the output and sends feedback back to the model when it falls short." [^lc]

# Analysis

Loop engineering at its most developed, one month before the graph turn — and, read carefully, already pregnant with it. The piece's four levels (agent loop; verification loop; event-driven loop; hill-climbing loop over traces) are loops *around* loops: a composition hierarchy. But composition of loops has a shape, and the shape is a graph — a verifier wrapping a worker is two nodes and a feedback edge; an event trigger fanning into agents is a topology. [Simmons](js--loop-exposed-its-ceiling.md) would say this piece documents the practice hitting the ceiling from below: once value concentrates in loops 3–4 ("where value compounds by embedding agents into your ecosystem"), the design object is already the connective structure, and the same authors' [July piece](lgblog--loops-simple-version.md) says so outright. The verification loop is also the corpus's main defense against [organized nonsense](lb--organized-nonsense.md) — with the caveat that a verifier is only as decorrelated as its design.

# Relations

- **refines** → [A model calling tools in a loop until done](lc--model-calling-tools-in-loop.md)
- **matures into** → [Loop engineering is a simple version of graphs](lgblog--loops-simple-version.md)
- **defends against** → [Organized nonsense at industrial scale](lb--organized-nonsense.md)

[^lc]: The Art of Loop Engineering
