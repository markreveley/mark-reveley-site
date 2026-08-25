---
type: Excerpt
subtype: claim
role: position
title: "Autonomy versus reliability"
description: The spectrum stated plainly — more autonomy, more potential value, less reliability; determinism for sensitive or preset workflows.
tags: [control-flow, determinism, risk, era-agentic]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: da
    resource: /references/langchain-deep-agents.md
    title: "Deep Agents vs LangChain vs LangGraph"
deps:
  - { concept: /issues/how-much-structure.md, rel: responds-to }
  - { concept: /excerpts/anth--simplest-solution.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "More autonomy gives an agent more potential value, at the cost of reliability. Determinism is the better call for sensitive or preset workflows." [^da]

**[prescription]** — the default, and the exception:

> "Start with Deep Agents. […] When you need to model a complex workflow or want complete control of every step, reach for LangChain and LangGraph." [^da]

# Note

Curl-verified. The stated exchange rate on the structure axis, with the harness-first default as its secondary prescription.

# Relations

- **responds-to** → [How much structure?](../issues/how-much-structure.md)
- **refines** → [Find the simplest solution possible](../excerpts/anth--simplest-solution.md)

[^da]: Deep Agents vs LangChain vs LangGraph (LangChain blog)
