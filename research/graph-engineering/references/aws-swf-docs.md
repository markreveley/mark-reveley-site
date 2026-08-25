---
type: Source Reference
title: "Amazon Simple Workflow Service developer guide (AWS)"
description: The 2012 cloud workflow engine — durable execution state, deciders and workers, coordination of distributed tasks — quoted from the current developer guide.
resource: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-welcome.html
tags: [level-1, era-classical, workflow-engines, durable-execution, history]
source_author: "Amazon Web Services (documentation)"
source_date: "living document (service announced 2012-02-21)"
retrieved: "2026-08-24"
availability: fetched
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# About

Added in research push #2 — the specific 2012 workflow engine, in its own words. Announced February 21, 2012 ([AWS what's-new](https://aws.amazon.com/about-aws/whats-new/2012/02/21/aws-announces-swf/)), SWF split orchestration into *deciders* (a program that reads the latest state and chooses next tasks) and *workers* (task executors), with durable execution state as the service's core promise — the exact architecture of a 2026 agent harness with the decider's judgment implemented in code instead of a model. Its tech lead, Maxim Fateev, later carried the design through Uber's Cadence to Temporal (see [the lineage post](temporal-lineage-blog.md)).

# Excerpts in this bundle

- [Deciders, workers, durable state — 2012](../excerpts/swf--durable-state-2012.md)
