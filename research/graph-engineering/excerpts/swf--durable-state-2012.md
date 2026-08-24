---
type: Excerpt
subtype: definition
title: "Deciders, workers, durable state — 2012"
description: Amazon SWF (announced February 2012) — coordinate distributed tasks, track state durably, and let a decider program choose each next step.
tags: [workflow-engines, durable-execution, history, era-classical, control-flow]
speaker: "AWS documentation (Amazon SWF developer guide)"
sources:
  - id: swf
    resource: /references/aws-swf-docs.md
    title: "Amazon Simple Workflow Service developer guide"
deps:
  - { concept: /excerpts/tmp--durable-execution.md, rel: precedes }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "With Amazon Simple Workflow Service (Amazon SWF) you can build, run, and scale background jobs that have parallel or sequential steps. You can coordinate work across distributed components and track the state of tasks." [^swf]

> "To coordinate tasks, you write a program that gets the latest task state from Amazon SWF and uses that state to initiate subsequent tasks. Amazon SWF maintains an application's execution state durably, so your application is resilient to individual component failures." [^swf]

# Analysis

The specific 2012 engine (announced February 21, 2012), and its architecture rewards close reading: SWF splits orchestration into *workers* (execute tasks) and a *decider* — "a program that gets the latest task state… and uses that state to initiate subsequent tasks." Substitute a model for that program and the sentence describes a 2026 agent harness without edits: the decider is the LLM choosing the next tool call; durable task state is [checkpointed graph state](lgdocs--checkpointers-stores.md); resilience to component failure is [the pause button Simmons found missing from loops](js--three-ceilings.md). The decider was even *deliberately* a black box to SWF — the service never saw the control logic, only its decisions — which is precisely the relationship between an agent runtime and the model today. What SWF lacked: a decider that could read a novel situation (its deciders were compiled code), and any economics of running ten thousand of them. Its personnel line runs unbroken to the present ([the same two engineers, three times](tmp--shipped-it-three-times.md)).

# Relations

- **precedes** → [Durable Execution](tmp--durable-execution.md)
- **decider ≈ model** → [Anatomy of the agent loop](ora--anatomy-of-the-loop.md)
- **answered then what loops lack now** → [Three ceilings of the loop](js--three-ceilings.md)

[^swf]: Amazon SWF developer guide (docs.aws.amazon.com)
