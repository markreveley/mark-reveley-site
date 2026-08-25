---
type: Excerpt
subtype: problem
role: argument
title: "Organized nonsense at industrial scale"
description: The graph era's characteristic failure mode — agent nodes interpret rather than execute, so a graph of agents checking agents can compound error with perfect structure.
tags: [risk, multi-agent, control-flow, skepticism]
speaker: "Louis-François Bouchard"
sources:
  - id: lb
    resource: /references/bouchard-what-actually-changed.md
    title: "Graph Engineering vs Loop Engineering: What Actually Changed"
deps:
  - { concept: /excerpts/gd--three-tier-reliability.md, rel: objects-to }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

**[inference]** — what actually changed:

> "Because of what lives inside the nodes. A step in a normal pipeline follows fixed rules. An agent interprets its task" [^lb]

**[problem]**:

> "a graph of agents checking agents can produce extremely organized nonsense" [^lb]

# Note

Curl-verified; two quotes, same source. Objects to the group-reliability claim by exhibiting correlated failure; the per-hop node is its edge-level analogue.

# Relations

- **objects-to** → [Three tiers of reliability](../excerpts/gd--three-tier-reliability.md)

[^lb]: Graph Engineering vs Loop Engineering: What Actually Changed
