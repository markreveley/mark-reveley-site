---
type: Excerpt
subtype: claim
title: "Things, not strings"
description: Google's 2012 slogan — an intelligent model, "in geek-speak, a graph," of real-world entities and their relationships.
tags: [history, knowledge-representation, era-knowledge-graph, definition]
speaker: "Amit Singhal (Google)"
sources:
  - id: gkg
    resource: /references/google-knowledge-graph-2012.md
    title: "Introducing the Knowledge Graph: things, not strings"
deps:
  - { concept: /excerpts/tbl--making-links.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "[…] an intelligent model—in geek-speak, a 'graph'—that understands real-world entities and their relationships to one another: things, not strings." [^gkg]

# Analysis

The moment "knowledge graph" became an industrial category (May 2012; 500M entities, 3.5B facts at launch). Historically it is the pragmatic fork off the [semantic-web lineage](tbl--making-links.md): where the W3C program sought a decentralized, standards-based web of data, Google built a centralized, proprietary graph and shipped it to a billion users — the vision privatized, and thereby proven. Note that "in geek-speak, a 'graph'" needed a gloss in 2012; by 2026 the term needs anti-hype field guides instead ([twelve words](aio--twelve-words.md)) — a fair measure of the concept's fourteen-year journey from esoterica to discourse. The slogan also states, three years before "embeddings" entered common parlance, the exact axis of the 2024–2026 retrieval debate: strings (and their vectors) versus things (and their edges) — [route by question type](aio--route-by-question-type.md) is the eventual truce.

# Relations

- **refines** → [Making links](tbl--making-links.md) (the vision, centralized and shipped)
- **axis of** → [The skeptic's question](rl--just-fancier-retrieval.md), [Route by question type](aio--route-by-question-type.md)
- **updated by** → [A graph is two things](aio--nodes-and-edges.md) (same model, private domains)

[^gkg]: Introducing the Knowledge Graph: things, not strings
