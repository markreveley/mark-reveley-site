---
type: Excerpt
subtype: definition
role: evidence
title: "Anatomy of the agent loop"
description: The harness-level definition — assemble context, reason, act, repeat until stop — and why loops exist at all.
tags: [loop-engineering]
speaker: "Richmond Alake (Oracle Developers blog)"
sources:
  - id: ora
    resource: /references/oracle-agent-loop-decoded.md
    title: "The Agent Loop Decoded"
deps:
  - { concept: /excerpts/lc--model-calling-tools-in-loop.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
status: stable
---

# Quotes

> "The agent loop is the repeating cycle a harness runs within a single agent turn: assemble context, invoke the model to reason, act on its decision, and go again until a stop condition ends the run." [^ora]

**[inference]** — why loops exist:

> "The agent loop exists because long-horizon tasks cannot be completed in a single forward pass." [^ora]

# Note

UNVERIFIED: the Oracle page could not be re-fetched raw (firewall); quotes are as first extracted and carry no verified field. Locates the loop in the harness and context assembly inside each iteration.

# Relations

- **refines** → [A model calling tools in a loop until done](../excerpts/lc--model-calling-tools-in-loop.md)

[^ora]: The Agent Loop Decoded
