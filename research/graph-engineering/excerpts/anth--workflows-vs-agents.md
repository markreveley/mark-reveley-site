---
type: Excerpt
subtype: definition
role: position
title: "Workflows vs agents"
description: The December 2024 distinction both 2026 camps descend from — predefined code paths versus LLMs directing their own process, in a loop.
tags: [control-flow, history, loop-engineering, era-agentic]
speaker: "Anthropic (Building Effective Agents)"
sources:
  - id: anth
    resource: /references/anthropic-building-effective-agents.md
    title: "Building Effective Agents"
deps:
  - { concept: /issues/loops-vs-graphs.md, rel: responds-to }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks." [^anth]

> "[Agents] are typically just LLMs using tools based on environmental feedback in a loop." [^anth]

# Note

Curl-verified. The common-ancestor framing both 2026 camps descend from; the BPMN evidence precedes it, and the commitments position relocates it per-edge.

# Relations

- **responds-to** → [Loops versus graphs](../issues/loops-vs-graphs.md)

[^anth]: Building Effective Agents
