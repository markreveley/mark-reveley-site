---
type: Excerpt
subtype: claim
title: "Three tiers of reliability"
description: The cleanest layering claim in the corpus — prompt engineering makes a call reliable, loop engineering an agent, graph engineering a group of agents.
tags: [term-genealogy, orchestration, multi-agent, definition, era-agentic]
speaker: "Gao Dalie (高達烈)"
sources:
  - id: gd
    resource: /references/gaodalie-forget-loop-engineering.md
    title: "FORGET Loop Engineering. Graph Engineering is about THIS"
deps:
  - { concept: /excerpts/aio--treadmill-of-terms.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Prompt Engineering makes a single model call more reliable. Loop engineering makes an agent's behavior more reliable. Graph Engineering makes the collaboration of a group of agents more reliable." [^gd]

# Analysis

The treadmill of terms, recast as an architecture: each discipline is the reliability layer for one unit of composition — call, agent, organization — and each layer takes the previous layer's product as its component. This is the strongest *pro* reading of the rename sequence: not fashion ([Bouchard's shrug](lb--this-weeks-name.md)) but a stack, with the term churn tracking which layer currently binds. Two caveats the excerpt's cleanness hides. It silently drops context engineering (mid-2025), which doesn't fit the units-of-composition scheme — context is a resource inside every layer, not a layer. And "makes … more reliable" is aspiration, not mechanism: [organized nonsense](lb--organized-nonsense.md) is the standing counterexample where the group layer *amplifies* correlated error. Still, as a one-breath answer to "why do the names keep changing?", nothing else in the corpus is this legible.

# Relations

- **refines** → [The treadmill of terms](aio--treadmill-of-terms.md)
- **contradicted (tempered) by** → [Organized nonsense at industrial scale](lb--organized-nonsense.md)

[^gd]: FORGET Loop Engineering. Graph Engineering is about THIS
