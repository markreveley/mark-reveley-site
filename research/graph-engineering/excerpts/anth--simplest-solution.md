---
type: Excerpt
subtype: prescription
title: "Find the simplest solution possible"
description: The standing counterweight to graph maximalism — add complexity only when needed; use agents only where paths can't be hardcoded.
tags: [simplicity, prescription, control-flow, era-agentic]
speaker: "Anthropic (Building Effective Agents)"
sources:
  - id: anth
    resource: /references/anthropic-building-effective-agents.md
    title: "Building Effective Agents"
deps:
  - { concept: /excerpts/lb--organized-nonsense.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "We recommend finding the simplest solution possible, and only increasing complexity when needed." [^anth]

**[prescription]** — the agent criterion:

> "Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path." [^anth]

# Analysis

The oldest prescription in the bundle and the one every later camp must answer. Against 2026 graph maximalism it cuts hard: a topology of agents is the *most* complex solution, so on this rule it comes last, after a prompt, a workflow, and a single loop have failed — which is [Gao Dalie's own restraint clause](gd--loops-inside-graphs.md) and Bouchard's "start simple," meaning even the graph camp's practitioners rediscover it. The agent criterion contains the deeper tension: agents are *for* unpredictable paths — but [graph engineering pre-draws the paths](gd--pre-designed-map.md). Taken together the two quotes imply a decision rule the 2026 discourse never states this cleanly: model the path you can predict (workflow/graph), delegate the path you can't (agent/loop), and [Catacora's observation](36kr--graphs-force-acknowledgment.md) tells you the boundary is exactly where explicit modeling stops paying for itself.

# Relations

- **supports** → [Organized nonsense at industrial scale](lb--organized-nonsense.md) (both counsel restraint)
- **rediscovered by** → [Loops live inside the nodes](gd--loops-inside-graphs.md) (restraint clause)
- **boundary set by** → [Graphs force you to acknowledge the unmodeled](36kr--graphs-force-acknowledgment.md)

[^anth]: Building Effective Agents
