---
type: Source Reference
title: "Blackboard system (Wikipedia)"
description: The 1970s multi-specialist coordination architecture (Hearsay-II lineage) — independent knowledge sources cooperating through shared state under a control shell.
resource: https://en.wikipedia.org/wiki/Blackboard_system
tags: [level-1, multi-agent, orchestration, memory, history]
source_author: "Wikipedia contributors"
source_date: "living document"
retrieved: "2026-08-24"
availability: fetched
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# About

Added in research push #2. The blackboard architecture (CMU, early 1970s; canonical system Hearsay-II, Erman/Hayes-Roth/Lesser/Reddy 1980) is the closest classical ancestor of shared-state multi-agent orchestration: specialists contribute partial solutions to a common workspace; a control shell decides who acts next. LangGraph's shared `State` read and written by every node is this pattern with statistical specialists.

# Excerpts in this bundle

- [Specialists at a blackboard](../excerpts/specialists-at-a-blackboard.md)
