---
type: Excerpt
subtype: problem
role: argument
title: "Decision trees don't fit CSV rows"
description: The concrete failure case — decision structures for 10,000 behaviors can be flattened into linked rows, but reading and retrieval degrade because the encoding fights the shape of the data.
tags: [knowledge-representation, retrieval, era-agentic, legibility]
speaker: "responding commenter, r/LLMDevs"
sources:
  - id: rl
    resource: /references/reddit-llmdevs-graph-trend.md
    title: "r/LLMDevs: What's up with new trend with graphs?"
deps:
  - { concept: /excerpts/rl--abstraction-layer.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
status: stable
---

# Quote

> "So, we're trying to build decision making trees for 10,000 different things our system does, that's not something that is described well in a traditional CSV data format. I suppose you could break each decision node down and encode in into rows that are linked together. But, then the data wouldn't be easy to read and you would have to hop and skip around because of the links. Then retrieving it would be slower than it needs to be, because it's encoded across multiple rows, instead of just 1." [^rl]

# Note

The commenter's worked example, from the operator-attested transcript. Argues for the abstraction-layer position by exhibiting the flattening tax.

# Relations

- **supports** → [The graph as abstraction layer](../excerpts/rl--abstraction-layer.md)

[^rl]: r/LLMDevs: What's up with new trend with graphs?
