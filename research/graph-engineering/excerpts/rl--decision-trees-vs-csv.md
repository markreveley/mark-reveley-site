---
type: Excerpt
subtype: problem
title: "Decision trees don't fit CSV rows"
description: The concrete failure case — decision structures for 10,000 behaviors can be flattened into linked rows, but reading and retrieval degrade because the encoding fights the shape of the data.
tags: [knowledge-representation, retrieval, era-agentic, legibility]
speaker: "responding commenter, r/LLMDevs"
sources:
  - id: rl
    resource: /references/reddit-llmdevs-graph-trend.md
    title: "r/LLMDevs: What's up with new trend with graphs?"
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
status: stable
---

# Quote

> "So, we're trying to build decision making trees for 10,000 different things our system does, that's not something that is described well in a traditional CSV data format. I suppose you could break each decision node down and encode in into rows that are linked together. But, then the data wouldn't be easy to read and you would have to hop and skip around because of the links. Then retrieving it would be slower than it needs to be, because it's encoded across multiple rows, instead of just 1." [^rl]

# Analysis

The thread's one worked example, and note what it is: not documents, not facts — *decision structures*, i.e. control flow. The commenter is describing agent behavior space ("10,000 different things our system does") a year into the loop-engineering era, which quietly aligns the seed thread with the orchestration sense of graph engineering ([humans design the path](gd--pre-designed-map.md), [boring nodes, typed edges](js--nodes-edges-state.md)) as much as with the knowledge sense. The argument form is classic impedance mismatch: any structure *can* be flattened to rows (or chunks, or a transcript), but every consumer then pays a reassembly tax — in legibility ("hop and skip around") and latency. Simmons' [transcript-as-state ceiling](js--three-ceilings.md) is the same tax paid by loops instead of tables.

Quote provenance: user-attested transcript; see [source reference](../references/reddit-llmdevs-graph-trend.md).

# Relations

- **answered by** → [The graph as abstraction layer](rl--abstraction-layer.md)
- **paralleled by** → [Three ceilings of the loop](js--three-ceilings.md) (flattening tax, transcript edition)

[^rl]: r/LLMDevs: What's up with new trend with graphs?
