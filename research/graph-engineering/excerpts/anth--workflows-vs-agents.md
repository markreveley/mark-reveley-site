---
type: Excerpt
subtype: claim
title: "Workflows vs agents"
description: The December 2024 distinction both 2026 camps descend from — predefined code paths versus LLMs directing their own process, in a loop.
tags: [control-flow, definition, history, loop-engineering, era-agentic]
speaker: "Anthropic (Building Effective Agents)"
sources:
  - id: anth
    resource: /references/anthropic-building-effective-agents.md
    title: "Building Effective Agents"
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks." [^anth]

> "[Agents] are typically just LLMs using tools based on environmental feedback in a loop." [^anth]

# Analysis

The common ancestor. Eighteen months before the naming events, this fixes both poles of the 2026 debate in two sentences: workflows are what graph engineering's determinist wing re-embraces ([the pre-designed map](gd--pre-designed-map.md) is "predefined code paths" verbatim in spirit), and the loop definition is what loop engineering canonized ([a model calling tools in a loop](lc--model-calling-tools-in-loop.md) compresses it). [Bouchard's priority claim](lb--this-weeks-name.md) — that this post "already drew every one of these patterns" — checks out for the topologies (its workflow catalog includes routing, parallelization, orchestrator-workers, evaluator-optimizer: graphs in all but name). What 2024 posed as a *system-level choice* (build a workflow OR an agent), 2026 re-poses as a *composition* ([graphs contain loops](lb--graphs-contain-loops.md)) and even a per-edge dial ([Simmons](js--nodes-edges-state.md)). The dichotomy didn't dissolve; it moved inside the architecture.

# Relations

- **refined by** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md), [A model calling tools in a loop until done](lc--model-calling-tools-in-loop.md)
- **claimed as precedent by** → [This week's name](lb--this-weeks-name.md)

[^anth]: Building Effective Agents
