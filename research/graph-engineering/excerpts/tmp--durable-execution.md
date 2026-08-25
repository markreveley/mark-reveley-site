---
type: Excerpt
subtype: definition
role: evidence
title: "Durable Execution"
description: The abstraction the workflow lineage converged on — automatically preserving a workflow's full state so execution survives failure.
tags: [durable-execution, workflow-engines, control-flow]
speaker: "Tim Imkin (Temporal blog)"
sources:
  - id: tmp
    resource: /references/temporal-lineage-blog.md
    title: "Building resilient Workflows: from Azure to Cadence to Temporal"
deps:
  - { concept: /excerpts/js--three-ceilings.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "At its core lies the concept of 'Durable Execution,' a groundbreaking abstraction that automatically preserves the full state of a Workflow" [^tmp]

> "You practically end up writing pure business logic without thinking about other things — no event handlers, callbacks, or explicit database interactions." [^tmp]

# Note

Curl-verified. The lineage's terminal abstraction; built for deterministic replay, which stochastic nodes strain — see the organized-nonsense argument.

# Relations

- **answers** → [Three ceilings of the loop](../excerpts/js--three-ceilings.md)

[^tmp]: Building resilient Workflows: from Azure to Cadence to Temporal (Temporal blog)
