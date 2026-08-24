---
type: Excerpt
subtype: inference
title: "Graphs force you to acknowledge the unmodeled"
description: Luis Catacora's double-edged observation — loops are fault-tolerant precisely because they are vague; graphs surface how much of the workflow was never really modeled.
tags: [control-flow, determinism, skepticism, era-agentic]
speaker: "Luis Catacora (as reported by 36Kr)"
sources:
  - id: kr
    resource: /references/36kr-father-of-lobster.md
    title: "Father of Lobster's Viral Tweet: Has the Loop Era Officially Ended?"
deps:
  - { concept: /excerpts/js--loop-exposed-its-ceiling.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Loops have a lot of fault tolerance. Graphs force you to acknowledge how much of the workflow isn't really modeled." [^kr]

# Analysis

The subtlest sentence in the July discourse, because both halves are compliments *and* warnings. Loops are fault-tolerant the way natural language is: the model improvises across the gaps in your specification, which is resilience when it works and silent scope creep when it doesn't. Making the workflow an explicit graph converts unknown unknowns into visible missing nodes — a cost (you must now model what you were free-riding on the model's judgment for) that is also the whole benefit (you finally *see* the free-riding). This reframes the loop→graph transition as a legibility trade rather than a capability upgrade, refining [Simmons' ceiling argument](js--loop-exposed-its-ceiling.md): the ceiling was partly invisible *because* the loop absorbed specification debt. It also gives the pro-loop camp its best steelman — sometimes deferring modeling to a capable model is correct ([Anthropic's open-ended criterion](anth--simplest-solution.md)) — and names the exact tax [Gao Dalie's pre-designed map](gd--pre-designed-map.md) glosses over.

# Relations

- **refines** → [The loop exposed its own ceiling](js--loop-exposed-its-ceiling.md)
- **taxes** → [The AI moves within a pre-designed map](gd--pre-designed-map.md)
- **steelmans** → [Find the simplest solution possible](anth--simplest-solution.md)

[^kr]: Father of Lobster's Viral Tweet: Has the Loop Era Officially Ended?
