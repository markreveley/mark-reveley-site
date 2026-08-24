---
type: Excerpt
subtype: claim
title: "Making links, so a person or machine can explore"
description: Berners-Lee's 2006 statement of the linked-data vision — the Semantic Web is about links that let people and machines explore a web of data.
tags: [history, knowledge-representation, legibility, era-classical]
speaker: "Tim Berners-Lee"
sources:
  - id: tbl
    resource: /references/berners-lee-linked-data.md
    title: "Linked Data — Design Issues"
deps:
  - { concept: /excerpts/rl--humans-and-machines.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "The Semantic Web isn't just about putting data on the web. It is about making links, so that a person or machine can explore the web of data. With linked data, when you have some of it, you can find other, related, data." [^tbl]

**[inference]** — why it matters:

> "It is the unexpected re-use of information which is the value added by the web." [^tbl]

# Analysis

Twenty years before the agentic turn, this fixes the two ideas the 2026 discourse treats as discoveries: dual legibility ("a person or machine" — the [seed thread's opening claim](rl--humans-and-machines.md), nearly word for word) and traversal as the retrieval mechanism ("when you have some of it, you can find other, related, data" — which is [graph traversal vs. lookup](aio--route-by-question-type.md) avant la lettre). The document's four rules (URIs as names; HTTP lookup; useful data at the name; links onward) map almost one-to-one onto [OKF's conventions](okf--formalizes-llm-wiki.md) — concept IDs as paths, resolvable files, frontmatter at the name, markdown links onward — shrunk from web scale to repo scale. The honest historical note: the machine reader Berners-Lee designed for (logic-based agents over RDF) barely materialized; the machine reader that finally showed up (LLMs over markdown) reads prose, which is *why* the 2026 revival could trade RDF's rigor for markdown's convenience. The vision aged better than its stack.

# Relations

- **supports** → [Legible to humans and machines](rl--humans-and-machines.md)
- **refined by** → [Things, not strings](gkg--things-not-strings.md) (centralized), [OKF formalizes the LLM-wiki pattern](okf--formalizes-llm-wiki.md) (repo-scale)

[^tbl]: Linked Data — Design Issues (w3.org)
