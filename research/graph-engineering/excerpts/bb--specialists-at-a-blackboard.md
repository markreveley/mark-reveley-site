---
type: Excerpt
subtype: definition
title: "Specialists at a blackboard"
description: The 1970s coordination architecture — independent knowledge sources cooperating through shared state under a control shell, with a moderator to keep them from trampling each other.
tags: [multi-agent, orchestration, memory, history, era-classical]
speaker: "Wikipedia (Blackboard system)"
sources:
  - id: bb
    resource: /references/blackboard-system-wikipedia.md
    title: "Blackboard system (Wikipedia)"
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "A blackboard system is an artificial intelligence approach based on the blackboard architectural model, where a common knowledge base, the \"blackboard\", is iteratively updated by a diverse group of specialist knowledge sources, starting with a problem specification and ending with a solution." [^bb]

> "A group of specialists are seated in a room with a large blackboard. They work as a team to brainstorm a solution to a problem, using the blackboard as the workplace for cooperatively developing the solution." [^bb]

**[observation]** — the control problem, already understood:

> "Just as the eager human specialists need a moderator to prevent them from trampling each other in a mad dash to grab the chalk, KSs need a mechanism to organize their use in the most effective and coherent fashion." [^bb]

# Analysis

The closest classical ancestor of shared-state multi-agent orchestration, from the Hearsay-II speech-understanding lineage (CMU, early 1970s; Erman, Hayes-Roth, Lesser & Reddy 1980). Map the three components onto a 2026 stack and nothing is left over: the blackboard is [LangGraph's shared `State`](lg--stateful-orchestration.md); knowledge sources are agent nodes; the control shell is the edge logic. Even the failure mode was pre-theorized — the "moderator" quote is the [organized-nonsense](lb--organized-nonsense.md) and coordination problem stated fifty years early, with chalk. Two honest differences: blackboard specialists were hand-built and narrow where 2026 nodes are general and rented; and blackboard control was the *hard research problem* (opportunistic scheduling) where 2026 mostly hardcodes the topology instead — arguably a retreat the field will revisit. The [2025 revival paper](bbllm--blackboard-revival.md) shows the ancestry is acknowledged, not imposed.

# Relations

- **precedes** → [The blackboard, revived](bbllm--blackboard-revival.md)
- **classical form of** → [Deterministic and agentic steps in one graph](lg--stateful-orchestration.md)
- **pre-theorizes** → [Organized nonsense at industrial scale](lb--organized-nonsense.md)

[^bb]: Blackboard system (Wikipedia)
