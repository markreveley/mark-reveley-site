---
type: Excerpt
subtype: observation
role: evidence
title: "The blackboard, revived"
description: A 2025 LLM multi-agent paper explicitly inspired by the classical blackboard architecture — the ancestry acknowledged from inside current research.
tags: [multi-agent, orchestration, academic, history]
speaker: "Salemi et al. (arXiv 2510.01285)"
sources:
  - id: bbllm
    resource: /references/blackboard-llm-paper.md
    title: "LLM-Based Multi-Agent Blackboard System (arXiv)"
deps:
  - { concept: /excerpts/bb--specialists-at-a-blackboard.md, rel: exemplifies }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "We propose a novel multi-agent paradigm inspired by the blackboard architecture for traditional AI models." [^bbllm]

> "In our framework, a central agent posts requests to a shared blackboard, and autonomous subordinate agents - either responsible for a partition of the data lake or retrieval from the web - volunteer to respond based on their capabilities." [^bbllm]

# Note

Curl-verified against the arXiv abstract. The blackboard ancestry claimed from inside current LLM-agents research.

# Relations

- **exemplifies** → [Specialists at a blackboard](../excerpts/bb--specialists-at-a-blackboard.md)

[^bbllm]: LLM-Based Multi-Agent Blackboard System (arXiv:2510.01285)
