---
type: Excerpt
subtype: claim
title: "Autonomy versus reliability"
description: The spectrum stated plainly — more autonomy, more potential value, less reliability; determinism for sensitive or preset workflows.
tags: [control-flow, determinism, risk, era-agentic]
speaker: "Sydney Runkle (LangChain)"
sources:
  - id: da
    resource: /references/langchain-deep-agents.md
    title: "Deep Agents vs LangChain vs LangGraph"
deps:
  - { concept: /excerpts/anth--simplest-solution.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "More autonomy gives an agent more potential value, at the cost of reliability. Determinism is the better call for sensitive or preset workflows." [^da]

**[prescription]** — the default, and the exception:

> "Start with Deep Agents. […] When you need to model a complex workflow or want complete control of every step, reach for LangChain and LangGraph." [^da]

# Analysis

The 2024 workflow-vs-agent dichotomy, matured into a stated exchange rate: autonomy buys option value and sells reliability, and the graph is where you shop when reliability is the binding constraint. As a refinement of [Anthropic's simplicity rule](anth--simplest-solution.md), this converts "start simple" from aesthetics into risk policy — the deterministic graph is not the humble choice but the *conservative* one, chosen for sensitive workflows the way one chooses a checklist over discretion. The prescription half then sets the market's current default: harness first, graph on demand — which triangulates neatly against the July discourse. The graph maximalists ([humans design the entire path](gd--pre-designed-map.md)) and the loop loyalists ([the escape-hatch framing](da--maximal-determinism.md)) are not disagreeing about capability; they are pricing the same tradeoff under different exposure to failure. On the paradigm question this is the strongest evidence for "regime, not revolution": what changed is not what can be built but what the field now has a *dial* for.

# Relations

- **refines** → [Find the simplest solution possible](anth--simplest-solution.md)
- **prices the dispute between** → [The AI moves within a pre-designed map](gd--pre-designed-map.md) and [Workflows vs agents](anth--workflows-vs-agents.md)
- **supports** → [Organized nonsense at industrial scale](lb--organized-nonsense.md) (reliability as the scarce good)

[^da]: Deep Agents vs LangChain vs LangGraph (LangChain blog)
