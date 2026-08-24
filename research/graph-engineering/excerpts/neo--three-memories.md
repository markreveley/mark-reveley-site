---
type: Excerpt
subtype: solution
title: "Three memories, one context graph"
description: Neo4j's proposal — long-term knowledge, short-term conversation, and reasoning memory for decision traces, unified in a graph grounded in the data's entities.
tags: [memory, solution, era-agentic]
speaker: "Jim Webber (Neo4j)"
sources:
  - id: neo
    resource: /references/neo4j-context-graphs.md
    title: "Context graphs: Why AI agents need three types of memory"
deps:
  - { concept: /excerpts/neo--buffer-and-static-kb.md, rel: answers }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "We propose a context graph (or agentic memory model) with three components: long-term memory for knowledge, short-term memory for conversation, and reasoning memory for decision traces." [^neo]

> "A context graph works by capturing decision traces and linking them directly to the entities in your data, ensuring that your agent's reasoning is grounded in the actual state of the world." [^neo]

# Analysis

The taxonomy borrows cognitive psychology's memory systems, but the third component is the novel one: **reasoning memory** — decision traces stored as first-class graph citizens, *linked to the entities they were about*. That link is the mechanism to note: it joins the knowledge graph (what is) to the execution history (what we did and why), which is precisely the join [Flowtivity's dual definition](ft--explicit-graphs-definition.md) assumes and most real stacks lack. It is also the database-native version of [the field guide's decision example](aio--decision-lives-in-structure.md) (decision → superseded thing → triggering incident) and of graph engineering's [checkpointed state](js--nodes-edges-state.md) — a checkpoint *is* a decision trace, indexed by the edge that produced it. Standing caveat from the [source reference](../references/neo4j-context-graphs.md): the prescriber sells the substrate.

# Relations

- **answers** → [A buffer and a static knowledge base](neo--buffer-and-static-kb.md)
- **joins** → [The decision lives in the structure](aio--decision-lives-in-structure.md) with [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md)

[^neo]: Context graphs: Why AI agents need three types of memory
