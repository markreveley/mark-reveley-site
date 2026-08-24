---
type: Excerpt
subtype: claim
title: "Graphs contain loops"
description: Bouchard's containment claim — the graph is not a replacement for the loop but an extra layer of delegated trust above it.
tags: [control-flow, loop-engineering, graph-engineering, era-agentic]
speaker: "Louis-François Bouchard"
sources:
  - id: lb
    resource: /references/bouchard-what-actually-changed.md
    title: "Graph Engineering vs Loop Engineering: What Actually Changed"
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Graphs contain loops. A graph is just the extra layer where we trust agents even more" [^lb]

# Analysis

Four words settle the succession question the discourse kept framing as a versus: the relationship between loop and graph engineering is containment, not replacement. (Formally true too — a cyclic directed graph *is* the general object; a single loop is its one-node special case, which is [LangGraph's version](lgblog--loops-simple-version.md) of the same point, and [Gao Dalie's](gd--loops-inside-graphs.md) from the design side.) The second sentence adds the governance reading: each layer of the [treadmill](aio--treadmill-of-terms.md) marks an increment of *delegated trust* — from trusting a model with a completion (prompt), to a window (context), to a cycle of actions (loop), to a topology of cooperating cycles (graph). That reading converts the rename treadmill from fashion into a trust ratchet, and it names the stake that makes [organized nonsense](lb--organized-nonsense.md) the matching risk: more delegated trust, more correlated failure.

# Relations

- **agrees with** → [Loop engineering is a simple version of graphs](lgblog--loops-simple-version.md), [Loops live inside the nodes](gd--loops-inside-graphs.md)
- **risk counterpart** → [Organized nonsense at industrial scale](lb--organized-nonsense.md)

[^lb]: Graph Engineering vs Loop Engineering: What Actually Changed
