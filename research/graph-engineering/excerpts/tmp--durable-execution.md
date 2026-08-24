---
type: Excerpt
subtype: definition
title: "Durable Execution"
description: The abstraction the workflow lineage converged on — automatically preserving a workflow's full state so execution survives failure.
tags: [durable-execution, workflow-engines, control-flow, era-agentic]
speaker: "Tim Imkin (Temporal blog)"
sources:
  - id: tmp
    resource: /references/temporal-lineage-blog.md
    title: "Building resilient Workflows: from Azure to Cadence to Temporal"
deps:
  - { concept: /excerpts/js--three-ceilings.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "At its core lies the concept of 'Durable Execution,' a groundbreaking abstraction that automatically preserves the full state of a Workflow" [^tmp]

> "You practically end up writing pure business logic without thinking about other things — no event handlers, callbacks, or explicit database interactions." [^tmp]

# Analysis

The workflow lineage's terminal abstraction, and the load-bearing overlap with graph engineering's third commitment: [Simmons' "state is an object with a schema, checkpointed every time you cross an edge"](js--nodes-edges-state.md) is durable execution restated, and [LangGraph's checkpointer machinery](lgdocs--checkpointers-stores.md) is its implementation for agent graphs. That overlap cuts both ways for the paradigm question. Deflationary reading: the "new" discipline's most operationally valuable property — pause, resume, survive failure, audit ([the three ceilings](js--three-ceilings.md), answered) — is a 2012-lineage primitive with a 2019 brand name, not a 2026 invention. Substantive reading: durable execution was built for *deterministic* replay (re-run the code, get the same decisions), and stochastic nodes break that contract — replaying an LLM decider does not reproduce the run, so agent-era durability must checkpoint *outcomes* rather than assume re-derivability. Same word, subtly harder problem. That delta is one of the genuinely new engineering constraints this bundle's [verdict](../synthesis/paradigm-or-hype.md) weighs.

# Relations

- **answers** → [Three ceilings of the loop](js--three-ceilings.md)
- **implemented for agent graphs by** → [Checkpointers and stores](lgdocs--checkpointers-stores.md)
- **strained by** → stochastic nodes (see [Organized nonsense](lb--organized-nonsense.md))

[^tmp]: Building resilient Workflows: from Azure to Cadence to Temporal (Temporal blog)
