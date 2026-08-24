---
type: Excerpt
subtype: definition
title: "Anatomy of the agent loop"
description: The harness-level definition — assemble context, reason, act, repeat until stop — and why loops exist at all.
tags: [loop-engineering, era-agentic]
speaker: "Richmond Alake (Oracle Developers blog)"
sources:
  - id: ora
    resource: /references/oracle-agent-loop-decoded.md
    title: "The Agent Loop Decoded"
deps:
  - { concept: /excerpts/lc--model-calling-tools-in-loop.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
status: stable
---

# Quotes

> "The agent loop is the repeating cycle a harness runs within a single agent turn: assemble context, invoke the model to reason, act on its decision, and go again until a stop condition ends the run." [^ora]

**[inference]** — why loops exist:

> "The agent loop exists because long-horizon tasks cannot be completed in a single forward pass." [^ora]

# Analysis

**Trust note: unverified.** The Oracle page could not be re-fetched raw (firewall), so these quotes are as extracted on first read and carry no `verified` field — the only loop-definition excerpt in this bundle at the unverified tier; treat wording with corresponding care. Content-wise it adds one precision the other definitions blur: the loop belongs to the *harness*, not the model — "assemble context" is step one of every iteration, which locates context engineering *inside* the loop rather than beside it on the [treadmill](aio--treadmill-of-terms.md). The one-sentence rationale is the corpus's most compact answer to "why loops at all": the forward pass is bounded, tasks are not; the loop is how bounded computation covers unbounded horizons — and the graph, by the [same argument one level up](js--coordinate-a-thousand-steps.md), is how bounded loops cover unbounded coordination.

# Relations

- **supports** → [A model calling tools in a loop until done](lc--model-calling-tools-in-loop.md)
- **extended one level by** → [The constraint moved to coordination](js--coordinate-a-thousand-steps.md)

[^ora]: The Agent Loop Decoded
