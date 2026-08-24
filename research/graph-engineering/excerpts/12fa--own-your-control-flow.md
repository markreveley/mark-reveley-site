---
type: Excerpt
subtype: prescription
title: "Own your control flow"
description: Factor 8 — build your own control structures around the loop; good agents are mostly just software.
tags: [control-flow, prescription, practice, loop-engineering, era-agentic]
speaker: "Dex Horthy (12-Factor Agents)"
sources:
  - id: fa
    resource: /references/humanlayer-12-factor-agents.md
    title: "12-Factor Agents"
deps:
  - { concept: /excerpts/12fa--throw-the-dag-away.md, rel: answers }
  - { concept: /excerpts/anth--simplest-solution.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:local-clone-read", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Agents, at least the good ones, don't follow the [\"here's your prompt, here's a bag of tools, loop until you hit the goal\"] pattern. Rather, they are comprised of mostly just software." [^fa]

> "If you own your control flow, you can do lots of fun things. […] Build your own control structures that make sense for your specific use case. Specifically, certain types of tool calls may be reason to break out of the loop and wait for a response from a human or another long-running task like a training pipeline." [^fa]

*(Bracketed phrase in the first quote is a hyperlink in the original README — the link text is quoted verbatim.)*

# Analysis

The missing middle term between Anthropic 2024 and the 2026 disciplines, and the reason the loop→graph succession felt inevitable to production engineers. "Mostly just software" rejects the pure-loop identity of agents *from the loop era itself*: the loop is one component inside owned, designed control structure. Read the enumerated interventions — break on human approval, pause for long-running tasks, summarize, judge structured output — against [Simmons' ceilings](js--three-ceilings.md): pause buttons, approval gates, resumability. Factor 8 is those graph-era features specified as custom code a year earlier; graph engineering, on this reading, is Factor 8 *productized* — the control structures you were told to hand-roll, given a common shape (nodes, typed edges, checkpointed state) and a runtime. The kinship with [simplicity](anth--simplest-solution.md) is real but distinct: Anthropic says add structure late; 12-factor says whatever structure exists must be *yours*. Graph frameworks satisfy the second and threaten the first.

# Relations

- **answers** → [Throw the DAG away](12fa--throw-the-dag-away.md)
- **supports** → [Find the simplest solution possible](anth--simplest-solution.md)
- **productized by** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md)

[^fa]: 12-Factor Agents (README and Factor 8, commit d20c728)
