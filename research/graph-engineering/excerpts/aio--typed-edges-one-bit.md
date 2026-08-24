---
type: Excerpt
subtype: claim
title: "An untyped edge is one bit"
description: The typed-edge distinction — "related" carries one bit of information; supersedes / depends_on / decided_by / caused carry the meaning.
tags: [typed-edges, knowledge-representation, definition, era-agentic]
speaker: "Eugeniu Ghelbur (The AI Operator)"
sources:
  - id: aio
    resource: /references/aioperator-field-guide.md
    title: "What Is Graph Engineering? A Field Guide for Builders"
deps:
  - { concept: /excerpts/aio--nodes-and-edges.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "An untyped edge says \"these two notes are related.\" One bit of information. A typed edge says how: supersedes, depends_on, decided_by, caused." [^aio]

# Analysis

The information-theoretic version of the claim the whole graph camp needs: linking alone is cheap; *typing* the link is where knowledge enters. It disciplines the seed thread's [anything-goes abstraction layer](rl--abstraction-layer.md) (a graph you can interpret however you like is a graph whose edges mean nothing to anyone else), and it names the exact gap in [OKF's](okf--formalizes-llm-wiki.md) current design — SPEC §6.1 makes all links untyped edges with kind "conveyed by the surrounding prose," i.e. one bit plus prose a machine must re-parse. (This bundle's `deps` extension exists because of this excerpt.) The same commitment appears independently in the orchestration strand the same month ([edges are decisions… typed transitions](js--nodes-edges-state.md)) and is escalated by [Flowtivity to "the edge type IS the knowledge"](ft--edge-type-is-knowledge.md). Historical footnote: typed edges are not new — RDF predicates and [linked-data](tbl--making-links.md) properties are exactly this — so the 2026 move is a rediscovery under new pressure, not an invention.

# Relations

- **refines** → [A graph is two things](aio--nodes-and-edges.md)
- **disciplines** → [The graph as abstraction layer](rl--abstraction-layer.md)
- **escalated by** → [The edge type IS the knowledge](ft--edge-type-is-knowledge.md)
- **converges with** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md)

[^aio]: What Is Graph Engineering? A Field Guide for Builders
