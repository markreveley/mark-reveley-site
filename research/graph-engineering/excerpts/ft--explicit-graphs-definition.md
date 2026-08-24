---
type: Excerpt
subtype: claim
title: "Explicit graphs an agent can traverse"
description: Flowtivity's definition uniting both senses — entities, decisions, and concepts as nodes; typed edges; traversal by the agent — plus the concurrency argument against loops.
tags: [definition, graph-engineering, typed-edges, concurrency, era-agentic]
speaker: "Flowtivity (unattributed)"
sources:
  - id: ft
    resource: /references/flowtivity-loops-to-graphs.md
    title: "From Loops to Graphs: The Next Paradigm in AI Agent Engineering"
deps:
  - { concept: /excerpts/js--nodes-edges-state.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Graph engineering is designing AI systems around explicit graphs — networks of nodes (entities, decisions, concepts) connected by typed edges (relationships) that an agent can traverse." [^ft]

**[claim]** — the concurrency argument:

> "A loop processes plan, code, review, fix, review again, fix again — sequentially. A graph dispatches 3 reviewers simultaneously." [^ft]

# Analysis

Notable for refusing the fork the other definitions take: its node inventory ("entities, decisions, concepts") is knowledge-flavored, but the verb ("traverse") and the concurrency argument are orchestration-flavored — the graph is simultaneously the map of what is known and the plan of what runs. That double reading is either the synthesis the field needs or an equivocation, and which one depends on whether the knowledge graph and the execution graph in a real system are actually the same object (in most 2026 stacks they are not — Graphiti holds knowledge, LangGraph holds control flow, and nothing joins them). The concurrency argument restates [Simmons' serial ceiling](js--three-ceilings.md) as a positive capability; the source's own cost caveat ("Graphs win on cost when the pass rate per cycle is above ~50%") prices it honestly.

# Relations

- **supports** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md), [Three ceilings of the loop](js--three-ceilings.md)
- **refined by** → [The edge type IS the knowledge](ft--edge-type-is-knowledge.md)

[^ft]: From Loops to Graphs: The Next Paradigm in AI Agent Engineering
