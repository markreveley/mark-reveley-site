---
type: Excerpt
subtype: observation
title: "Throw the DAG away (and what happened next)"
description: "The 2023-era promise recorded by 12-factor-agents — give the agent a goal and skip the graph — followed immediately by the verdict: it doesn't quite work."
tags: [control-flow, history, loop-engineering, era-agentic]
speaker: "Dex Horthy (12-Factor Agents)"
sources:
  - id: fa
    resource: /references/humanlayer-12-factor-agents.md
    title: "12-Factor Agents"
deps:
  - { concept: /excerpts/anth--workflows-vs-agents.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:local-clone-read", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "my biggest takeaway when I started learning about agents, was that you get to throw the DAG away. Instead of software engineers coding each step and edge case, you can give the agent a goal and a set of transitions […] And let the LLM make decisions in real time to figure out the path" [^fa]

> "As we'll see later, it turns out this doesn't quite work." [^fa]

# Analysis

The pivot of the whole historical arc, preserved in one document with its own refutation attached. The founding promise of agents (2023) was explicitly *anti-graph*: the DAG — the artifact of a decade of data engineering — was the thing you got to delete, replaced by a goal and a model's judgment. 12-factor (2025) is the production world's field report that the deletion overshot ("doesn't quite work"), and its remedy ([own your control flow](12fa--own-your-control-flow.md)) is designed control structure readmitted around the loop. Graph engineering (2026) completes the arc: [the graph returns](js--loop-exposed-its-ceiling.md) — but cyclic, checkpointed, with agentic nodes, i.e. *not* the old DAG. Thesis, antithesis, synthesis, with each stage written down by practitioners in real time. Anyone claiming 2026's graphs are "just Airflow again" ([the deflationary camp](dsd--already-doing-it.md)) has to account for the middle step this excerpt documents: the loop era permanently changed what a node is ([Bouchard](lb--organized-nonsense.md)).

# Relations

- **refines** → [Workflows vs agents](anth--workflows-vs-agents.md) (the promise Anthropic's taxonomy tamed)
- **resolved by** → [Own your control flow](12fa--own-your-control-flow.md), then [The loop exposed its own ceiling](js--loop-exposed-its-ceiling.md)

[^fa]: 12-Factor Agents (README, commit d20c728)
