---
type: Excerpt
subtype: inference
title: "Loop engineering is a simple version of graphs"
description: LangChain's formal subsumption — loops are the one-node special case, and production agents need cycles anyway.
tags: [control-flow, loop-engineering, graph-engineering, orchestration, era-agentic]
speaker: "Sydney Runkle and Harrison Chase (LangChain)"
sources:
  - id: lgb
    resource: /references/langchain-3-years-langgraph.md
    title: "3 Years of Graph Engineering with LangGraph"
deps:
  - { concept: /excerpts/lb--graphs-contain-loops.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Loop engineering isn't an alternative to graphs, so much as a simple version of them." [^lgb]

**[claim]** — the node model and the cycles argument:

> "In LangGraph, nodes do work. A node can be deterministic code, a single LLM call, a tool call, or a full agent with its own internal loop." [^lgb]

> "Production agents need cycles: retrying failed tool calls, asking users for missing information, revising answers after validation." [^lgb]

# Analysis

The mathematical resolution of loop-vs-graph, from the party that implemented both: a loop is a graph with one node and one back-edge, so the "shift" is generalization, not succession. The node taxonomy matches [Simmons'](js--nodes-edges-state.md) almost verbatim (deterministic code / LLM call / tool / full agent — Simmons adds the human), and "a full agent with its own internal loop" is [Gao Dalie's nesting](gd--loops-inside-graphs.md) as an API. The cycles line carries the historical irony this bundle keeps meeting: the 2023 orchestration world was DAGs (Airflow, no cycles — and agents promised to [throw the DAG away](12fa--throw-the-dag-away.md)); LangGraph's founding differentiator was *adding cycles back* to graphs; loop engineering then celebrated the cycle alone; graph engineering now re-adds the topology around it. The whole treadmill is one data structure being rediscovered from different ends — cyclic directed graphs with typed nodes — which is either deflating or clarifying depending on your camp.

# Relations

- **refines** → [Graphs contain loops](lb--graphs-contain-loops.md)
- **API version of** → [Loops live inside the nodes](gd--loops-inside-graphs.md)
- **closes the arc from** → [Throw the DAG away](12fa--throw-the-dag-away.md)

[^lgb]: 3 Years of Graph Engineering with LangGraph
