---
type: Excerpt
subtype: definition
title: "Places, transitions, tokens"
description: The 1962 formalism — Petri nets as directed bipartite graphs whose token flow models concurrency, later specialized into workflow nets.
tags: [workflow-engines, history, era-classical, control-flow, academic]
speaker: "Wikipedia (Petri net)"
sources:
  - id: pet
    resource: /references/petri-net-wikipedia.md
    title: "Petri net (Wikipedia)"
deps:
  - { concept: /excerpts/bpmn--graphical-processes.md, rel: precedes }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "A Petri net is a directed bipartite graph that has two types of elements: places and transitions." [^pet]

> "The German computer scientist Carl Adam Petri, after whom such structures are named, analyzed Petri nets extensively in his 1962 Ph.D. dissertation." [^pet]

> "Workflow nets (WF-nets) are a subclass of Petri nets intending to model the workflow of process activities." [^pet]

# Analysis

The oldest ancestor in the *control-flow* lineage, and worth precision about what it already contained in 1962: typed nodes (places vs. transitions — a bipartite discipline stricter than anything in the 2026 discourse), state as first-class tokens (not a transcript), concurrency and synchronization as structural properties, and formal analyzability (reachability, liveness, deadlock). The workflow-nets subclass is the bridge: van der Aalst's WF-nets gave the 1990s–2000s workflow-management wave its formal semantics, which [BPMN](bpmn--graphical-processes.md) then standardized as notation and engines executed. When the [paradigm question](../synthesis/paradigm-or-hype.md) asks "or further back?" — this is how far back the skeleton goes: every structural property claimed for agent graphs in 2026 (explicit topology, checkpointable state, parallel branches, join semantics) has a 1962 formalization. What Petri nets could not represent is a transition that *decides for itself* what firing means — the one thing the 2026 node does.

# Relations

- **precedes** → [Activities, gateways, events](bpmn--graphical-processes.md)
- **deep root of** → [Vertex-centric iteration](pre--vertex-centric.md), [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md)

[^pet]: Petri net (Wikipedia)
