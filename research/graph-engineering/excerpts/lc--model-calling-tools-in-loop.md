---
type: Excerpt
subtype: definition
title: "A model calling tools in a loop until done"
description: The loop era's minimal definition of an agent, from LangChain's June 2026 loop-engineering piece.
tags: [loop-engineering, era-agentic]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: lc
    resource: /references/langchain-art-of-loop-engineering.md
    title: "The Art of Loop Engineering"
deps:
  - { concept: /excerpts/anth--workflows-vs-agents.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "At its core, an agent is just a model calling tools in a loop until a task is complete." [^lc]

# Analysis

By June 2026 this formula had become the field's shared axiom — a compressed restatement of [Anthropic's December 2024 definition](anth--workflows-vs-agents.md) ("LLMs using tools based on environmental feedback in a loop"), itself downstream of ReAct ([the lineage claim](ms--act-observe-repeat.md)). Its role in this bundle is as the *base unit*: every position in the 2026 debate treats this object as given and argues about what wraps it — verification loops ([stacking](lc--stack-and-extend-loops.md)), harness anatomies ([Oracle's three levels](ora--anatomy-of-the-loop.md)), or topologies ([graphs of them](lb--graphs-contain-loops.md)). The word "just" is doing rhetorical work worth noticing: the same clause appears in 12-factor's *rebuttal* — good agents are ["mostly just software"](12fa--own-your-control-flow.md), not just a loop — so even the axiom's "just" was contested by the production camp before the graph camp arrived.

# Relations

- **refines** → [Workflows vs agents](anth--workflows-vs-agents.md)
- **wrapped by** → [Stack and extend loops](lc--stack-and-extend-loops.md)
- **contested by** → [Own your control flow](12fa--own-your-control-flow.md)

[^lc]: The Art of Loop Engineering
