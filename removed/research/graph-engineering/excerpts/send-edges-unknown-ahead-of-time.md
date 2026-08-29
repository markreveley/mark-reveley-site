---
type: Excerpt
subtype: solution
role: evidence
title: "Send: edges unknown ahead of time"
description: LangGraph's Send API — dynamic map-reduce fan-out where the number of branches is not known when the graph is written.
tags: [tooling, concurrency, orchestration, control-flow]
speaker: "LangGraph documentation (Graph API)"
sources:
  - id: lgapi
    resource: /references/langgraph-overview.md
    title: "LangGraph overview (LangChain docs)"
deps:
  - { concept: /excerpts/the-constraint-moved-to-coordination.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "A common example of this is with map-reduce design patterns. In this design pattern, a first node may generate a list of objects, and you may want to apply some other node to all those objects." [^lgapi]

> "The number of objects may be unknown ahead of time (meaning the number of edges may not be known) and the input State to the downstream Node should be different (one for each generated object)." [^lgapi]

# Note

Curl-verified documentation. Runtime-decided fan-out cardinality; data-driven multiplicity, not structural self-modification (which Pregel had in 2010).

# Relations

- **answers** → [The constraint moved to coordination](../excerpts/the-constraint-moved-to-coordination.md)

[^lgapi]: LangGraph Graph API documentation (docs.langchain.com)
