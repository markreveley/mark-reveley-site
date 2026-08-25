---
type: Excerpt
subtype: definition
role: evidence
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
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "With Amazon Simple Workflow Service (Amazon SWF) you can build, run, and scale background jobs that have parallel or sequential steps. You can coordinate work across distributed components and track the state of tasks." [^swf]

> "To coordinate tasks, you write a program that gets the latest task state from Amazon SWF and uses that state to initiate subsequent tasks. Amazon SWF maintains an application's execution state durably, so your application is resilient to individual component failures." [^swf]

# Note

Curl-verified against the current AWS developer guide; service announced 2012-02-21. The decider/worker split with durable state — the operator's hypothesized ancestor, in its own words.

# Relations

- **precedes** → [Durable Execution](../excerpts/tmp--durable-execution.md)

[^swf]: Amazon SWF developer guide (docs.aws.amazon.com)
