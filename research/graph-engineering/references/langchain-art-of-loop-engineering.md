---
type: Source Reference
title: "The Art of Loop Engineering (LangChain)"
description: "LangChain's June 2026 loop-engineering piece — four stacked loop levels: agent, verification, event-driven, hill-climbing."
resource: https://www.langchain.com/blog/the-art-of-loop-engineering
tags: [level-1, loop-engineering, verification]
source_author: "Sydney Runkle"
source_date: "2026-06-16"
retrieved: "2026-08-24"
availability: fetched
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# About

Written at loop engineering's peak month, one month before the graph turn. Defines loop engineering as stacking and extending loops: (1) the agent loop (model + tools until done), (2) a verification loop wrapping it, (3) event-driven loops that trigger agents, (4) hill-climbing loops that improve the system from traces. Levels 3–4 are where the piece says value compounds — an argument that the unit of engineering was already growing beyond the single loop.

# Excerpts in this bundle

- [A model calling tools in a loop until done](../excerpts/a-model-calling-tools-in-a-loop-until-done.md)
- [Stack and extend loops](../excerpts/stack-and-extend-loops.md)
