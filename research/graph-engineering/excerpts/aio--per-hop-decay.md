---
type: Excerpt
subtype: problem
title: "Per-hop accuracy compounds against you"
description: The arithmetic that kills graph projects — at 95% per-hop accuracy a 5-hop chain is 77% trustworthy; at 85%, 44%.
tags: [evaluation, risk, retrieval, era-agentic]
speaker: "Eugeniu Ghelbur (The AI Operator)"
sources:
  - id: aio
    resource: /references/aioperator-field-guide.md
    title: "What Is Graph Engineering? A Field Guide for Builders"
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "At 95% per-hop accuracy, a 5-hop chain is 77% trustworthy. At 85%, it is 44%." [^aio]

# Analysis

The graph camp's own memento mori, stated from inside the camp. Multi-hop traversal is the headline capability graphs add over similarity search ([the decision lives in the structure](aio--decision-lives-in-structure.md)) — and it is also the capability that multiplies error geometrically: 0.95⁵ ≈ 0.77, 0.85⁵ ≈ 0.44. The same arithmetic appears in [Flowtivity](../references/flowtivity-loops-to-graphs.md) ("at 85% per-hop accuracy, a 5-hop traversal is only 44% trustworthy"), suggesting it circulated as a shared caution. Two implications: entity-resolution and edge quality are not hygiene, they are the product (each bad merge poisons every path through it); and hop count is a budget to spend, not a feature to maximize — which is what makes [route by question type](aio--route-by-question-type.md) the rational response rather than graph maximalism. The same compounding logic, applied to agents instead of edges, yields [organized nonsense](lb--organized-nonsense.md).

# Relations

- **tempers** → [The decision lives in the structure](aio--decision-lives-in-structure.md)
- **answered by** → [Route by question type](aio--route-by-question-type.md)
- **agent-level analogue** → [Organized nonsense at industrial scale](lb--organized-nonsense.md)

[^aio]: What Is Graph Engineering? A Field Guide for Builders
