---
type: Excerpt
subtype: observation
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
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "In 2002, Max, now CTO of Temporal, joined Amazon amid a pivotal transition from monolithic applications to a service-oriented architecture" […] "Samar, CEO of Temporal, who had worked alongside Max at Amazon, carried these lessons to Microsoft." [^tmp]

> "Max and Samar reunited at Uber, creating Cadence — an orchestration framework designed from the outset as fully open source." [^tmp]

> "Temporal was born as a direct answer to the challenges Max and Samar encountered at Amazon, Microsoft, and Uber." [^tmp]

# Analysis

Genealogy at the resolution of individual careers, which is the strongest form descent claims come in. Maxim Fateev (technical lead on [Amazon SWF](swf--durable-state-2012.md)) and Samar Abbas (whose Microsoft work became the Durable Task Framework behind Azure Durable Functions) built the same system three times — SWF (2012), Cadence (Uber), Temporal (2019) — each iteration fixing what the last deployment taught them. Vendor-authored source, so the heroic framing is discounted; the employment facts are checkable and corroborated elsewhere. Why it matters for the paradigm question: when 2026 agent frameworks advertise durable execution, checkpointing, and resumable long-running work, they are adopting a design lineage whose authors have been shipping it since the year the maintainer's hypothesis names — the continuity is not analogical but literal. And the convergence runs both directions: Temporal now markets durable execution *for AI agents* (Fateev, WorkOS interview, April 2026), the 2012 lineage claiming the 2026 workload.

# Relations

- **refines** → [Deciders, workers, durable state — 2012](swf--durable-state-2012.md)
- **design carried into** → [Durable Execution](tmp--durable-execution.md)

[^tmp]: Building resilient Workflows: from Azure to Cadence to Temporal (Temporal blog)
