---
type: Excerpt
subtype: claim
title: "This week's name for an orchestrated system of loops"
description: Bouchard's deflationary definition — graph engineering as the newest label on a rename treadmill, for a practice that already existed.
tags: [definition, term-genealogy, skepticism, graph-engineering, era-agentic]
speaker: "Louis-François Bouchard"
sources:
  - id: lb
    resource: /references/bouchard-what-actually-changed.md
    title: "Graph Engineering vs Loop Engineering: What Actually Changed"
deps:
  - { concept: /excerpts/aio--treadmill-of-terms.md, rel: supports }
  - { concept: /excerpts/anth--workflows-vs-agents.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Graph engineering is this week's name for connecting several agent loops into one orchestrated system" [^lb]

**[observation]** — the treadmill, in his rendering:

> "Steinberger was poking at how fast we rename things. Prompt engineering became context engineering, then harness engineering, and then loop engineering. Which all mostly means the same." [^lb]

**[claim]** — the priority claim:

> "the concept itself is not new. Anthropic's Building Effective Agents post from 2024 already drew every one of these patterns" [^lb]

# Analysis

The most quotable deflationary position, and usefully *not* pure deflation: "connecting several agent loops into one orchestrated system" is a real definition (the orchestration sense, loops-as-nodes), and Bouchard elsewhere concedes the joke "points at something real." Two things to check against other sources. His treadmill inserts "harness engineering" between context and loop — a term [Ghelbur's dated list](aio--treadmill-of-terms.md) omits — and waves the whole sequence off as "mostly means the same," where Ghelbur insists each term marked a real shift; that disagreement is the live historiographic question, not a factual error. His priority claim is checkable and this bundle checked it: [Anthropic's 2024 post](anth--workflows-vs-agents.md) did define workflow patterns (routing, parallelization, orchestrator-workers) that are graph topologies in all but name — though it drew them as *predefined code paths* versus agents, without the 2026 move of typing the choice per-edge ([Simmons](js--nodes-edges-state.md)). Reporting variance recorded: "Nine words from Peter Steinberger… 2.6 million views" vs. [twelve words](aio--twelve-words.md) — both cannot be right about the count.

# Relations

- **supports** → [The treadmill of terms](aio--treadmill-of-terms.md) (while disputing its "real shift" reading), [Workflows vs agents](anth--workflows-vs-agents.md)
- **kindred** → [You were already doing it](dsd--already-doing-it.md), [We've been doing it for three years](lgblog--three-years.md)

[^lb]: Graph Engineering vs Loop Engineering: What Actually Changed
