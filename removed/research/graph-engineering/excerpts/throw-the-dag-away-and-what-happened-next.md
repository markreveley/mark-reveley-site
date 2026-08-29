---
type: Excerpt
subtype: observation
role: evidence
title: "Throw the DAG away (and what happened next)"
description: "The 2023-era promise recorded by 12-factor-agents — give the agent a goal and skip the graph — followed immediately by the verdict: it doesn't quite work."
tags: [control-flow, history, loop-engineering]
speaker: "Dex Horthy (12-Factor Agents)"
sources:
  - id: fa
    resource: /references/humanlayer-12-factor-agents.md
    title: "12-Factor Agents"
deps:
  - { concept: /excerpts/workflows-vs-agents.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:local-clone-read", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "my biggest takeaway when I started learning about agents, was that you get to throw the DAG away. Instead of software engineers coding each step and edge case, you can give the agent a goal and a set of transitions […] And let the LLM make decisions in real time to figure out the path" [^fa]

> "As we'll see later, it turns out this doesn't quite work." [^fa]

# Note

Quoted directly from the cloned repository (commit d20c728); bracketed phrase is a hyperlink in the original. Documents the 2023 anti-graph promise and its in-source refutation.

# Relations

- **refines** → [Workflows vs agents](../excerpts/workflows-vs-agents.md)

[^fa]: 12-Factor Agents (README, commit d20c728)
