---
type: Excerpt
subtype: problem
title: "A buffer and a static knowledge base"
description: Neo4j's diagnosis of agent unreliability — memory that is only a conversation buffer plus a static store, losing the plan across loops.
tags: [memory, risk, era-agentic]
speaker: "Jim Webber (Neo4j)"
sources:
  - id: neo
    resource: /references/neo4j-context-graphs.md
    title: "Context graphs: Why AI agents need three types of memory"
deps:
  - { concept: /excerpts/js--three-ceilings.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Many AI agents today are unreliable because their memory, if it even exists, consists of a simple conversation buffer and static knowledge base." [^neo]

> "They read your goal, plan their actions, look up facts from one store, and run a similarity search in another. After many more loops, they forget the original plan." [^neo]

# Analysis

The memory-strand problem statement with the sharpest phenomenology: "after many more loops, they forget the original plan" locates the failure *inside the loop* — iteration itself erodes intent when state lives only in a window. That makes this the vendor-side twin of [Simmons' transcript ceiling](js--three-ceilings.md) (independent sources, same month vs. same season, same diagnosis: the transcript is not a memory), and the 2026 restatement of what [Zep argued academically](zep--graphiti-temporal.md) in January 2025. Note the tell in "look up facts from one store, and run a similarity search in another": the problem isn't absence of storage but *disconnection* between stores — which primes the graph as connective tissue and, less charitably, primes the reader for the vendor's product. This bundle keeps the diagnosis and holds the prescription to the same scrutiny as any other ([three memories](neo--three-memories.md)).

# Relations

- **supports** → [Three ceilings of the loop](js--three-ceilings.md) (memory ceiling)
- **answered by** → [Three memories, one context graph](neo--three-memories.md), [A temporally-aware knowledge graph engine](zep--graphiti-temporal.md)

[^neo]: Context graphs: Why AI agents need three types of memory
