---
type: Excerpt
subtype: observation
role: evidence
title: "The same two engineers, three times"
description: The personnel continuity of the workflow lineage — Amazon (SWF) → Microsoft (Durable Task) → Uber (Cadence) → Temporal.
tags: [workflow-engines, durable-execution, history, era-agentic]
speaker: "Tim Imkin (Temporal blog)"
sources:
  - id: tmp
    resource: /references/temporal-lineage-blog.md
    title: "Building resilient Workflows: from Azure to Cadence to Temporal"
deps:
  - { concept: /excerpts/swf--durable-state-2012.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "In 2002, Max, now CTO of Temporal, joined Amazon amid a pivotal transition from monolithic applications to a service-oriented architecture" […] "Samar, CEO of Temporal, who had worked alongside Max at Amazon, carried these lessons to Microsoft." [^tmp]

> "Max and Samar reunited at Uber, creating Cadence — an orchestration framework designed from the outset as fully open source." [^tmp]

> "Temporal was born as a direct answer to the challenges Max and Samar encountered at Amazon, Microsoft, and Uber." [^tmp]

# Note

Curl-verified; vendor-authored, employment facts checkable. Personnel continuity: SWF → Cadence → Temporal, same two engineers.

# Relations

- **refines** → [Deciders, workers, durable state — 2012](../excerpts/swf--durable-state-2012.md)

[^tmp]: Building resilient Workflows: from Azure to Cadence to Temporal (Temporal blog)
