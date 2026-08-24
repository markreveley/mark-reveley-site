---
type: Excerpt
subtype: claim
title: "A graph is two things: nodes and edges"
description: The field guide's buzzword-free minimal definition, cast in knowledge terms — the things you know about, and the connections between them.
tags: [definition, knowledge-representation, graph-engineering, era-agentic]
speaker: "Eugeniu Ghelbur (The AI Operator)"
sources:
  - id: aio
    resource: /references/aioperator-field-guide.md
    title: "What Is Graph Engineering? A Field Guide for Builders"
deps:
  - { concept: /excerpts/gkg--things-not-strings.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Strip every buzzword away and a graph is two things. Nodes: the things you know about. A person, a project, a decision, an incident. Edges: the connections between them." [^aio]

# Analysis

Deliberately deflationary in form, but note the framing baked into "the things you *know* about": where [Simmons defines nodes as units of capability](js--nodes-edges-state.md) (work), Ghelbur defines them as units of knowledge (world). The July 2026 term covers both, and each camp's "minimal" definition smuggles in its preferred sense. The knowledge casting is continuous with [Google's 2012 "things, not strings"](gkg--things-not-strings.md) — entities and relationships as the model of the world — with the example inventory updated from celebrities and monuments to the working artifacts of a software team (decisions, incidents). That drift in examples *is* the historical shift this bundle tracks: knowledge graphs moved from describing the public world to describing your own system's operation.

# Relations

- **supports** → [Things, not strings](gkg--things-not-strings.md) (same model, new domain)
- **contrast** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md) (capability casting)
- **refined by** → [An untyped edge is one bit](aio--typed-edges-one-bit.md)

[^aio]: What Is Graph Engineering? A Field Guide for Builders
