---
type: Excerpt
subtype: claim
title: "The AI moves within a pre-designed map"
description: Gao Dalie's determinist definition — humans design the objectives, criteria, and the entire path; the AI does not wander.
tags: [determinism, control-flow, graph-engineering, definition, era-agentic]
speaker: "Gao Dalie (高達烈)"
sources:
  - id: gd
    resource: /references/gaodalie-forget-loop-engineering.md
    title: "FORGET Loop Engineering. Graph Engineering is about THIS"
deps:
  - { concept: /excerpts/rl--map-metaphor.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "In graph engineering, humans design not only the objectives and passing criteria, but also the entire path through which the work will proceed." [^gd]

> "In other words, in a graph, the AI doesn't wander around freely, but rather moves within a pre-designed map." [^gd]

# Analysis

The maximal-control pole of the definitional spectrum, and the mirror image of the [seed thread's map metaphor](rl--map-metaphor.md): there, the graph is a map the system makes of the world and reads back; here, it is a map humans make of the *work* and the system is confined to. Same figure, opposite direction of authority. Read against [Anthropic's 2024 taxonomy](anth--workflows-vs-agents.md), this position defines graph engineering as… workflows — "predefined code paths" — which Anthropic explicitly distinguished *from* agents. That makes this excerpt the cleanest evidence that part of the 2026 graph turn is a partial retreat from agent autonomy back toward designed control flow, with the loop's autonomy preserved only *inside* nodes ([loops live inside the nodes](gd--loops-inside-graphs.md)). [Simmons' per-edge dial](js--nodes-edges-state.md) ("defaulting to deterministic everywhere you can afford to") is the moderate version; [12-factor's "own your control flow"](12fa--own-your-control-flow.md) said it in 2025 without the map imagery.

# Relations

- **refines (authority reversed)** → [A map of how something works](rl--map-metaphor.md)
- **retreats toward** → [Workflows vs agents](anth--workflows-vs-agents.md) (the workflow pole)
- **moderated by** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md)

[^gd]: FORGET Loop Engineering. Graph Engineering is about THIS
