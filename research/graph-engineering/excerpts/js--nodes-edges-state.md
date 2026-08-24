---
type: Excerpt
subtype: definition
title: "Boring nodes, typed edges, checkpointed state"
description: Simmons' three commitments — the definitional core of graph engineering in its orchestration sense.
tags: [graph-engineering, control-flow, typed-edges, determinism, era-agentic]
speaker: "Josh C. Simmons"
sources:
  - id: js
    resource: /references/simmons-graph-engineering-phase.md
    title: "We Are Entering the Graph Engineering Phase"
deps:
  - { concept: /excerpts/anth--workflows-vs-agents.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Graph engineering is designing agentic systems as explicit graphs instead of implicit loops. Three commitments, none of them exotic. Nodes are units of capability. A node can be a model running the familiar think-act-observe cycle, a plain deterministic function, a retrieval step, or a human being. A good node is boring. It does one thing, you can test it alone, and you can swap it out without touching anything else." [^js]

> "Edges are decisions. An edge is a typed transition that carries state from one node to the next. Some edges are deterministic: tests pass, deploy. Some are model-decided: does this ticket go to billing or to abuse. The job is knowing which is which, and defaulting to deterministic everywhere you can afford to." [^js]

> "State is an object with a schema, checkpointed every time you cross an edge." [^js]

# Analysis

The definition with the most engineering content in the July corpus. Three details repay attention. First, a node "can be… a human being" — humans are typed into the graph as capability nodes, which quietly generalizes the framework beyond automation into org design. Second, "the job is knowing which is which, and defaulting to deterministic everywhere you can afford to" — this is [Anthropic's workflows-vs-agents](anth--workflows-vs-agents.md) distinction relocated from the *system* level to the *edge* level: the 2024 question "is this a workflow or an agent?" becomes a per-transition dial. [LangGraph's design goal](lg--stateful-orchestration.md) (mix deterministic and agentic steps in one graph) is the same idea shipped as software. Third, "state is an object with a schema" — versus the loop's transcript — is what makes [pause/resume and audit](js--three-ceilings.md) possible at all. Note the typed-edge commitment shows up independently in the *knowledge* strand the same month ([one bit vs. meaning](aio--typed-edges-one-bit.md)): the two senses of graph engineering converge on typing as the substance.

# Relations

- **refines** → [Workflows vs agents](anth--workflows-vs-agents.md) (per-edge, not per-system)
- **supported by** → [Explicit graphs an agent can traverse](ft--explicit-graphs-definition.md), [Deterministic and agentic steps in one graph](lg--stateful-orchestration.md)
- **converges with** → [An untyped edge is one bit](aio--typed-edges-one-bit.md)

[^js]: We Are Entering the Graph Engineering Phase
