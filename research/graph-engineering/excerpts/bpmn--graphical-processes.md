---
type: Excerpt
subtype: definition
title: "Activities, gateways, events — and human tasks"
description: BPMN — the workflow-engine era's standardized process graphs, version 2.0 released January 2011.
tags: [workflow-engines, control-flow, history, era-classical]
speaker: "Wikipedia (BPMN)"
sources:
  - id: bpmn
    resource: /references/bpmn-wikipedia.md
    title: "Business Process Model and Notation (Wikipedia)"
deps:
  - { concept: /excerpts/anth--workflows-vs-agents.md, rel: precedes }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "Business Process Model and Notation (BPMN) is a standard for business process modeling that provides a graphical notation for specifying business processes in a Business Process Diagram (BPD), based on a flowcharting technique very similar to activity diagrams from Unified Modeling Language (UML)." [^bpmn]

> "Version 2.0 of BPMN was released in January 2011." [^bpmn]

> "An activity is represented with a rounded-corner rectangle and describes the kind of work which must be done." / "A gateway is represented with a diamond shape and determines forking and merging of paths." [^bpmn]

# Analysis

The maintainer's "workflow engines in 2012" hypothesis, at its documentary core. BPMN 2.0 (January 2011) made process graphs *executable standard artifacts*: activities as nodes, gateways as routing (deterministic edges, in 2026 language), events as triggers — run by the 2010–2013 engine wave (Activiti, December 2010, built by ex-jBPM architects; jBPM; Camunda). Two features make BPMN the closest single ancestor of agent graph engineering. First, its notation includes **user tasks and manual tasks** — nodes whose work is performed by a judging human. The 2012 process graph already contained interpretive nodes; they simply cost salaries and hours. On this reading, [what changed in 2026](lb--organized-nonsense.md) is not the introduction of judgment into the graph but its unit price and speed. Second, BPMN's gateway/activity split is exactly [Simmons' deterministic-vs-model-decided edge dial](js--nodes-edges-state.md), standardized fifteen years earlier — with the difference that BPMN gateways evaluate *rules* where 2026 edges may evaluate *judgment*. What BPMN's world never had: nodes cheap enough to spawn twelve before lunch, or any notion that the process artifact might write itself.

# Relations

- **precedes** → [Workflows vs agents](anth--workflows-vs-agents.md) ("predefined code paths," standardized)
- **already contained** → interpretive nodes (human tasks); see [Organized nonsense](lb--organized-nonsense.md) for what changed
- **formal roots** → [Places, transitions, tokens](pet--places-transitions.md)

[^bpmn]: Business Process Model and Notation (Wikipedia)
