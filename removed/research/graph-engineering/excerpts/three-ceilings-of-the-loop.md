---
type: Excerpt
subtype: problem
role: argument
title: "Three ceilings of the loop"
description: Simmons' bill of particulars against the single agent loop — serial execution, transcript-as-state, and no pause button.
tags: [loop-engineering, control-flow, concurrency, memory, risk]
speaker: "Josh C. Simmons"
sources:
  - id: js
    resource: /references/simmons-graph-engineering-phase.md
    title: "We Are Entering the Graph Engineering Phase"
deps:
  - { concept: /excerpts/the-loop-exposed-its-own-ceiling.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "The loop is serial, so a task that splits into ten independent subtasks, which describes most research and most large coding jobs, runs one subtask at a time anyway." [^js]

> "The loop's entire state is a transcript, so \"memory\" means whatever survived compaction and \"audit trail\" means somebody scrolling a wall of text. Failure is all or nothing: die at step 40 of 60 and your choices are start over or perform surgery on a context window." [^js]

> "There is no pause button, so an agent cannot take a human approval on Thursday and pick the work back up Friday without duct tape. And the moment you want a planner with three workers, or a builder with a critic checking its output, the loop has nothing to offer you. It is one process. It was always one process." [^js]

# Note

Simmons' bill of particulars; curl-verified. Each ceiling maps to one of the term's three competing meanings; the durable-execution and checkpointer evidence answer it.

# Relations

- **supports** → [The loop exposed its own ceiling](../excerpts/the-loop-exposed-its-own-ceiling.md)

[^js]: We Are Entering the Graph Engineering Phase
