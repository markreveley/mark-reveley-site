---
type: Excerpt
subtype: solution
role: evidence
title: "OKF formalizes the LLM-wiki pattern"
description: Google's June 2026 answer to knowledge-for-agents — an open spec turning directories of markdown into portable, interoperable graphs.
tags: [standards, knowledge-representation]
speaker: "Sam McVeety and Amir Hormati (Google Cloud)"
sources:
  - id: okf
    resource: /references/google-okf-announcement.md
    title: "Introducing the Open Knowledge Format"
deps:
  - { concept: /excerpts/compiled-once-kept-current.md, rel: refines }
  - { concept: /excerpts/making-links-so-a-person-or-machine-can-explore.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "That's why today, we're introducing the Open Knowledge Format (OKF), an open specification that formalizes the LLM-wiki pattern into a portable, interoperable format." [^okf]

> "Concepts link to each other with normal markdown links, turning the directory into a graph of relationships that is richer than the parent/child links implied by the file system." [^okf]

**[observation]** — Karpathy, as quoted in the post:

> "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass" [^okf]

# Note

Curl-verified. The standards-track artifact of the agent-maintained-knowledge trend; this bundle's own carrier format.

# Relations

- **refines** → [Compiled once, kept current](../excerpts/compiled-once-kept-current.md)
- **supports** → [Making links, so a person or machine can explore](../excerpts/making-links-so-a-person-or-machine-can-explore.md)

[^okf]: Introducing the Open Knowledge Format (Google Cloud blog)
