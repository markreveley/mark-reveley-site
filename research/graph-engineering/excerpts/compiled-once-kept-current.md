---
type: Excerpt
subtype: claim
role: position
title: "Compiled once, kept current"
description: Karpathy's LLM-wiki principle — knowledge as a persistent, compounding, cross-referenced artifact the model maintains, not something re-derived per query.
tags: [knowledge-representation, memory, practice]
speaker: "Andrej Karpathy"
sources:
  - id: ka
    resource: /references/karpathy-llm-wiki.md
    title: "llm-wiki (gist)"
deps:
  - { concept: /excerpts/a-map-of-how-something-works.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "The knowledge is compiled once and then _kept current_, not re-derived on every query." [^ka]

> "the wiki is a persistent, compounding artifact. The cross-references are already there." [^ka]

# Note

Curl-verified against the gist's raw text. Compile-once-keep-current as a retrieval-architecture position; OKF formalizes it two months later.

# Relations

- **supports** → [A map of how something works](../excerpts/a-map-of-how-something-works.md)

[^ka]: llm-wiki (Karpathy gist)
