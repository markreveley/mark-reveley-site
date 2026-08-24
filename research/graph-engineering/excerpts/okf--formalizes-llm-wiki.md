---
type: Excerpt
subtype: solution
title: "OKF formalizes the LLM-wiki pattern"
description: Google's June 2026 answer to knowledge-for-agents — an open spec turning directories of markdown into portable, interoperable graphs.
tags: [standards, knowledge-representation, solution, era-agentic]
speaker: "Sam McVeety and Amir Hormati (Google Cloud)"
sources:
  - id: okf
    resource: /references/google-okf-announcement.md
    title: "Introducing the Open Knowledge Format"
deps:
  - { concept: /excerpts/ka--compiled-once.md, rel: refines }
  - { concept: /excerpts/tbl--making-links.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "That's why today, we're introducing the Open Knowledge Format (OKF), an open specification that formalizes the LLM-wiki pattern into a portable, interoperable format." [^okf]

> "Concepts link to each other with normal markdown links, turning the directory into a graph of relationships that is richer than the parent/child links implied by the file system." [^okf]

**[observation]** — Karpathy, as quoted in the post:

> "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass" [^okf]

# Analysis

The standards moment of the knowledge strand — and its graph claim is the one to weigh. "Turning the directory into a graph" is literally true (files = nodes, links = edges) and deliberately minimal: per SPEC §6.1 the edges are *untyped*, their meaning "conveyed by the surrounding prose." Against [the typed-edge consensus](aio--typed-edges-one-bit.md) that emerged five weeks later, OKF's graph carries one bit per edge plus prose — a gap this bundle patches with its `deps` extension, and a likely pressure point for future spec versions. The deeper significance is the succession of substrates for the same idea: [triples on the web](tbl--making-links.md) (2001–2012, machine-first, adoption-starved) → [proprietary graph at planet scale](gkg--things-not-strings.md) (2012) → *markdown in a git repo* (2026, exactly as human-legible as agent-legible, adoption-cheap). The format got dumber as the readers got smarter — the intelligence moved from the schema into the consumer, which is the whole era in one design decision.

# Relations

- **refines** → [Compiled once, kept current](ka--compiled-once.md) (pattern → standard)
- **supports** → [Making links](tbl--making-links.md) (the vision, third substrate)
- **thin on** → [An untyped edge is one bit](aio--typed-edges-one-bit.md)
- **motivated by** → [A corpus continuously maintained by agents](spec--maintained-by-agents.md)

[^okf]: Introducing the Open Knowledge Format (Google Cloud blog)
