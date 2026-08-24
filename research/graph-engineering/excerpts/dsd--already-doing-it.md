---
type: Excerpt
subtype: inference
title: "You were already doing it"
description: The frameworks argument — anyone using LangGraph, Microsoft Agent Framework, ADK, or CrewAI was doing "graph engineering" before the name existed.
tags: [term-genealogy, tooling, skepticism, era-agentic]
speaker: "Ayesha Aamir (Data Science Dojo)"
sources:
  - id: dsd
    resource: /references/dsdojo-frameworks-before-name.md
    title: "The frameworks that were doing \"graph engineering\" before it had a name"
deps:
  - { concept: /excerpts/lb--this-weeks-name.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "If you're already using any of the frameworks above, you were already doing what's being called 'graph engineering' this month" [^dsd]

> "LangGraph's own documentation describes exactly the node/edge/state model that 'graph engineering' is now being used to describe" [^dsd]

# Analysis

The practice-precedes-name argument in its most checkable form: the referent of the July 2026 term is the installed base of orchestration frameworks — LangGraph, Microsoft Agent Framework (GA April 2026), Google ADK, CrewAI — whose node/edge/state models predate it by one to three years. This bundle confirms the LangGraph claim directly against [its documentation](lg--stateful-orchestration.md). What the argument establishes and what it doesn't: it establishes that the *capability* existed; it doesn't address [Simmons' point](js--loop-exposed-its-ceiling.md) that a naming event marks when a capability becomes the *binding constraint* — plenty of people had LangGraph installed and still ran everything through one loop. Naming events reorganize attention, not inventories. See [LangChain's own version](lgblog--three-years.md) of this argument, made with an owner's interest.

# Relations

- **supports** → [This week's name](lb--this-weeks-name.md)
- **confirmed against** → [Deterministic and agentic steps in one graph](lg--stateful-orchestration.md)
- **vendor version** → [We've been doing it for three years](lgblog--three-years.md)

[^dsd]: The frameworks that were doing "graph engineering" before it had a name
