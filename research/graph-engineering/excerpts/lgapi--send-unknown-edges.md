---
type: Excerpt
subtype: solution
title: "Send: edges unknown ahead of time"
description: LangGraph's Send API — dynamic map-reduce fan-out where the number of branches is not known when the graph is written.
tags: [tooling, concurrency, orchestration, control-flow, era-agentic]
speaker: "LangGraph documentation (Graph API)"
sources:
  - id: lgapi
    resource: /references/langgraph-overview.md
    title: "LangGraph overview (LangChain docs)"
deps:
  - { concept: /excerpts/js--coordinate-a-thousand-steps.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "A common example of this is with map-reduce design patterns. In this design pattern, a first node may generate a list of objects, and you may want to apply some other node to all those objects." [^lgapi]

> "The number of objects may be unknown ahead of time (meaning the number of edges may not be known) and the input State to the downstream Node should be different (one for each generated object)." [^lgapi]

# Analysis

The key capability fact for "is the new paradigm possible with LangGraph?" — because it addresses the strongest objection. Critics say LangGraph's topology is compile-time-rigid; Send is the documented escape: a node's *output* determines, at runtime, how many parallel branches exist and what state each receives. That gives Simmons his missing verbs ([fan-out and fan-in](js--coordinate-a-thousand-steps.md)) with model-decided cardinality — the planner decides how many workers, at run time. The honest limit: Send is *data-driven multiplicity over predeclared node types*, not structural self-modification — the agent chooses how many of which node run, not what kinds of node exist; a system that authors genuinely new topology (new node types, new edge logic) still does so at the meta level, by generating and compiling a new graph. Pregel, piquantly, allowed runtime topology *mutation* in 2010 ([vertex-centric iteration](pre--vertex-centric.md)); its agent-era descendant is more conservative than its ancestor on exactly this axis.

# Relations

- **answers** → [The constraint moved to coordination](js--coordinate-a-thousand-steps.md)
- **bounds** → the rigidity critique in [Overhead exceeding the problem](dl--overhead-exceeded.md)
- **more conservative than** → [Vertex-centric iteration](pre--vertex-centric.md) (topology mutation)

[^lgapi]: LangGraph Graph API documentation (docs.langchain.com)
