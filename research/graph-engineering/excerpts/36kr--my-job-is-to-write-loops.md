---
type: Excerpt
subtype: observation
title: "My job is to write loops"
description: Boris Cherny's first-person report of the practice shift — running loops that prompt Claude and decide what to do next.
tags: [loop-engineering, practice, era-agentic]
speaker: "Boris Cherny (as reported by 36Kr)"
sources:
  - id: kr
    resource: /references/36kr-father-of-lobster.md
    title: "Father of Lobster's Viral Tweet: Has the Loop Era Officially Ended?"
deps:
  - { concept: /excerpts/36kr--design-loops-not-prompts.md, rel: exemplifies }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "I don't prompt Claude anymore. I run loops that prompt Claude and decide what to do next. My job is to write loops." [^kr]

# Analysis

The practice shift stated as a job description, by the creator of Claude Code — i.e., the person who built the era's canonical agent harness describing what using it at the frontier actually looks like. As evidence it is a different kind than the definitional excerpts: not "loop engineering is X" but "here is what my day is now," which is how discipline formation actually shows up before it has a curriculum. The phrase "and decide what to do next" quietly contains the graph turn: a loop that decides *which loop runs next* is already an edge function — [Bouchard's containment](lb--graphs-contain-loops.md) and [LangGraph's loops-as-simple-graphs](lgblog--loops-simple-version.md) just make the topology explicit. Same as-reported caveat as its [sibling excerpt](36kr--design-loops-not-prompts.md): verified against the 36Kr page, not the unfetchable original post.

# Relations

- **exemplifies** → [Design loops that prompt agents](36kr--design-loops-not-prompts.md)
- **contains the seed of** → [Graphs contain loops](lb--graphs-contain-loops.md)

[^kr]: Father of Lobster's Viral Tweet: Has the Loop Era Officially Ended?
