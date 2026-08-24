---
type: Excerpt
subtype: claim
title: "Deterministic and agentic steps in one graph"
description: LangGraph's self-definition — a low-level orchestration runtime whose core strength is mixing hand-coded and LLM-driven steps in a single stateful graph.
tags: [tooling, orchestration, determinism, control-flow, era-agentic]
speaker: "LangChain (LangGraph documentation)"
sources:
  - id: lg
    resource: /references/langgraph-overview.md
    title: "LangGraph overview"
deps:
  - { concept: /excerpts/anth--workflows-vs-agents.md, rel: exemplifies }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents." [^lg]

> "LangGraph gives you fine-grained control to mix deterministic, hand-coded steps with LLM-driven agentic steps in the same graph." [^lg]

# Analysis

The reference implementation of the whole debate's resolution, described in its own documentation. "Mix deterministic … with LLM-driven … in the same graph" is [Anthropic's workflow/agent dichotomy](anth--workflows-vs-agents.md) implemented as a type system rather than decided as an architecture choice — each node (and edge) takes a side, the graph holds both. This is what [Data Science Dojo points at](dsd--already-doing-it.md) when it says the term's referent already shipped, and the software substrate beneath [Simmons' per-edge dial](js--nodes-edges-state.md). "Long-running, stateful" names the other half: durable state outside the context window, which is the loop's [transcript ceiling](js--three-ceilings.md) answered in infrastructure. Worth registering what "low-level" concedes — the framework declines to choose your topology, which is precisely the design work the 2026 discipline claims for humans.

# Relations

- **exemplifies** → [Workflows vs agents](anth--workflows-vs-agents.md) (both poles, one runtime)
- **substrate for** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md)
- **cited by** → [You were already doing it](dsd--already-doing-it.md)

[^lg]: LangGraph overview (LangChain docs)
