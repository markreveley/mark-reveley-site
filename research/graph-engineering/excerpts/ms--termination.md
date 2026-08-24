---
type: Excerpt
subtype: problem
title: "Without a termination condition"
description: The loop's definitional hazard — agents that run forever or stop arbitrarily.
tags: [loop-engineering, risk, era-agentic]
speaker: "Luis Chavez-Mattos (MindStudio)"
sources:
  - id: ms
    resource: /references/mindstudio-what-is-loop-engineering.md
    title: "What Is Loop Engineering? The New Meta for AI Coding Agents"
deps:
  - { concept: /excerpts/ms--act-observe-repeat.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "The loop needs to know what 'done' looks like. Without a termination condition, agents either run forever or stop arbitrarily." [^ms]

# Analysis

The halting problem, arrived at empirically by the trade press. Its significance for the graph turn: "done" is a *predicate over state*, and the loop's state is a transcript ([Simmons' second ceiling](js--three-ceilings.md)) — so a rigorous termination condition wants exactly what graph engineering's third commitment supplies, [state as a schema'd object](js--nodes-edges-state.md) you can evaluate a predicate against. In the loop world, termination is a prompt convention ("repeat until a goal is *actually* met" — the "actually" is load-bearing and unenforceable); in the graph world it is an edge condition ("tests pass, deploy"). That migration — from aspiration in text to predicate on state — is one of the cleanest concrete payoffs the graph camp can claim, and a fair answer to ["what actually changed?"](lb--this-weeks-name.md).

# Relations

- **refines** → [Act, observe, decide, repeat](ms--act-observe-repeat.md)
- **resolved by** → [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md) (state predicates)

[^ms]: What Is Loop Engineering? The New Meta for AI Coding Agents
