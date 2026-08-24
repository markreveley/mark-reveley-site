---
type: Excerpt
subtype: claim
title: "Compiled once, kept current"
description: Karpathy's LLM-wiki principle — knowledge as a persistent, compounding, cross-referenced artifact the model maintains, not something re-derived per query.
tags: [knowledge-representation, memory, era-agentic, practice]
speaker: "Andrej Karpathy"
sources:
  - id: ka
    resource: /references/karpathy-llm-wiki.md
    title: "llm-wiki (gist)"
deps:
  - { concept: /excerpts/rl--map-metaphor.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "The knowledge is compiled once and then _kept current_, not re-derived on every query." [^ka]

> "the wiki is a persistent, compounding artifact. The cross-references are already there." [^ka]

# Analysis

The compiler metaphor is the strand's founding move: RAG interprets (re-derives understanding at query time, paying the cost every time and caching nothing); the wiki compiles (pays the cost at ingest, and every query thereafter reads the compiled form). "The cross-references are already there" is where the graph enters — the compilation's output is not a summary but a *linked structure*, i.e. the [map the seed thread described](rl--map-metaphor.md), built by the model, read back by the model. What makes April 2026 the right moment for a 2004-vintage idea (personal wikis) is stated in the division of labor: the bookkeeping that makes humans abandon wikis — summarizing, cross-referencing, filing — is exactly what LLMs don't tire of ([quoted in Google's OKF post](okf--formalizes-llm-wiki.md): "LLMs don't get bored"). Two months later that gist pattern had a [vendor-neutral spec](okf--formalizes-llm-wiki.md); this bundle is written in it.

# Relations

- **supports** → [A map of how something works](rl--map-metaphor.md)
- **formalized by** → [OKF formalizes the LLM-wiki pattern](okf--formalizes-llm-wiki.md)
- **same bet as** → [An LLM-built graph index](grag--graph-index.md) (the consumer becomes the producer)

[^ka]: llm-wiki (Karpathy gist)
