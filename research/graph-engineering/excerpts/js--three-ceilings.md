---
type: Excerpt
subtype: problem
title: "Three ceilings of the loop"
description: Simmons' bill of particulars against the single agent loop — serial execution, transcript-as-state, and no pause button.
tags: [loop-engineering, control-flow, concurrency, memory, risk, era-agentic]
speaker: "Josh C. Simmons"
sources:
  - id: js
    resource: /references/simmons-graph-engineering-phase.md
    title: "We Are Entering the Graph Engineering Phase"
deps:
  - { concept: /excerpts/js--loop-exposed-its-ceiling.md, rel: supports }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "The loop is serial, so a task that splits into ten independent subtasks, which describes most research and most large coding jobs, runs one subtask at a time anyway." [^js]

> "The loop's entire state is a transcript, so \"memory\" means whatever survived compaction and \"audit trail\" means somebody scrolling a wall of text. Failure is all or nothing: die at step 40 of 60 and your choices are start over or perform surgery on a context window." [^js]

> "There is no pause button, so an agent cannot take a human approval on Thursday and pick the work back up Friday without duct tape. And the moment you want a planner with three workers, or a builder with a critic checking its output, the loop has nothing to offer you. It is one process. It was always one process." [^js]

# Analysis

The most concrete problem statement in the corpus, and each ceiling maps onto one of the [three competing meanings](aio--twelve-words.md) the term acquired days later: serial execution → orchestration graphs; transcript-as-state → knowledge/memory graphs (the same complaint as [Neo4j's buffer-and-static-KB](neo--buffer-and-static-kb.md), from the opposite vendor position); no pause/resume and no roles → multi-agent topology graphs. That mapping is evidence the "three competing definitions" are less competing than co-symptomatic — three ceilings of one artifact. Notice also that every ceiling is a *harness* property, not a model property: nothing here is fixed by a smarter LLM. That is the strongest version of the case that a new engineering layer (not a new model) was due — and it is the same flattening tax the seed thread found in [CSV rows](rl--decision-trees-vs-csv.md), paid in transcripts instead of tables.

# Relations

- **supports** → [The loop exposed its own ceiling](js--loop-exposed-its-ceiling.md)
- **paralleled by** → [Decision trees don't fit CSV rows](rl--decision-trees-vs-csv.md), [A buffer and a static knowledge base](neo--buffer-and-static-kb.md)

[^js]: We Are Entering the Graph Engineering Phase
