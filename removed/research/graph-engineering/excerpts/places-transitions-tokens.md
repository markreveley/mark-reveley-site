---
type: Excerpt
subtype: definition
role: evidence
title: "Places, transitions, tokens"
description: The 1962 formalism — Petri nets as directed bipartite graphs whose token flow models concurrency, later specialized into workflow nets.
tags: [workflow-engines, history, control-flow, academic]
speaker: "Wikipedia (Petri net)"
sources:
  - id: pet
    resource: /references/petri-net-wikipedia.md
    title: "Petri net (Wikipedia)"
deps:
  - { concept: /excerpts/activities-gateways-events-and-human-tasks.md, rel: precedes }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "A Petri net is a directed bipartite graph that has two types of elements: places and transitions." [^pet]

> "The German computer scientist Carl Adam Petri, after whom such structures are named, analyzed Petri nets extensively in his 1962 Ph.D. dissertation." [^pet]

> "Workflow nets (WF-nets) are a subclass of Petri nets intending to model the workflow of process activities." [^pet]

# Note

Curl-verified against Wikipedia. The 1962 root of the control-flow lineage; workflow nets carry it into the BPM wave.

# Relations

- **precedes** → [Activities, gateways, events — and human tasks](../excerpts/activities-gateways-events-and-human-tasks.md)

[^pet]: Petri net (Wikipedia)
