---
type: Excerpt
subtype: prescription
role: position
title: "Own your control flow"
description: Factor 8 — build your own control structures around the loop; good agents are mostly just software.
tags: [control-flow, practice, loop-engineering]
speaker: "Dex Horthy (12-Factor Agents)"
sources:
  - id: fa
    resource: /references/humanlayer-12-factor-agents.md
    title: "12-Factor Agents"
deps:
  - { concept: /excerpts/throw-the-dag-away-and-what-happened-next.md, rel: answers }
  - { concept: /excerpts/find-the-simplest-solution-possible.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:local-clone-read", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Agents, at least the good ones, don't follow the [\"here's your prompt, here's a bag of tools, loop until you hit the goal\"] pattern. Rather, they are comprised of mostly just software." [^fa]

> "If you own your control flow, you can do lots of fun things. […] Build your own control structures that make sense for your specific use case. Specifically, certain types of tool calls may be reason to break out of the loop and wait for a response from a human or another long-running task like a training pipeline." [^fa]

*(Bracketed phrase in the first quote is a hyperlink in the original README — the link text is quoted verbatim.)*

# Note

Quoted from the cloned repository (commit d20c728). The owned-control-structure position; the graph-era commitments productize its enumerated interventions.

# Relations

- **answers** → [Throw the DAG away (and what happened next)](../excerpts/throw-the-dag-away-and-what-happened-next.md)
- **supports** → [Find the simplest solution possible](../excerpts/find-the-simplest-solution-possible.md)

[^fa]: 12-Factor Agents (README and Factor 8, commit d20c728)
