---
type: Excerpt
subtype: claim
role: evidence
title: "Deterministic and agentic steps in one graph"
description: LangGraph's self-definition — a low-level orchestration runtime whose core strength is mixing hand-coded and LLM-driven steps in a single stateful graph.
tags: [tooling, orchestration, determinism, control-flow]
speaker: "LangChain (LangGraph documentation)"
sources:
  - id: lg
    resource: /references/langgraph-overview.md
    title: "LangGraph overview"
deps:
  - { concept: /excerpts/workflows-vs-agents.md, rel: exemplifies }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents." [^lg]

> "LangGraph gives you fine-grained control to mix deterministic, hand-coded steps with LLM-driven agentic steps in the same graph." [^lg]

# Note

Curl-verified documentation. The runtime implementing both poles of the 2024 dichotomy in one graph.

# Relations

- **exemplifies** → [Workflows vs agents](../excerpts/workflows-vs-agents.md)

[^lg]: LangGraph overview (LangChain docs)
