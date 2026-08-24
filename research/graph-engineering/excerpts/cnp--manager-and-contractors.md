---
type: Excerpt
subtype: definition
title: "Managers, contractors, and bids"
description: Smith's 1980 Contract Net Protocol — task announcement, bidding, delegation, and recursive subcontracting among autonomous agents.
tags: [multi-agent, orchestration, history, era-classical]
speaker: "Wikipedia (Contract Net Protocol)"
sources:
  - id: cnp
    resource: /references/contract-net-wikipedia.md
    title: "Contract Net Protocol (Wikipedia)"
deps:
  - { concept: /excerpts/js--coordinate-a-thousand-steps.md, rel: precedes }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "The Contract Net Protocol (CNP) is a task-sharing protocol in multi-agent systems, introduced in 1980 by Reid G. Smith. It is used to allocate tasks among autonomous agents." [^cnp]

> "[…] a manager proposes a task to several agents. The latter make a proposal among which the manager chooses to allocate the task. […] This task can then be divided and subcontracted." [^cnp]

> "This protocol can be used to implement hierarchical organizations, where a manager assigns tasks to contractors." [^cnp]

# Analysis

The delegation half of 2026 multi-agent orchestration, specified as a protocol in 1980: task announcement, capability-based selection, hierarchical assignment, recursive decomposition. An orchestrator-worker agent system — a planner fanning subtasks to specialists ([twelve of them before lunch](js--coordinate-a-thousand-steps.md)) — is a contract net where bidding has degenerated into the manager's own judgment. That degeneration is the interesting delta: CNP assumed contractors whose capabilities were opaque and heterogeneous enough to require *negotiation*; 2026 systems mostly skip the market because the workers are interchangeable instances of the same model. If genuinely heterogeneous agent economies emerge (different vendors, priced capabilities), the bidding half of the 1980 protocol is sitting there waiting — and the first wave of multi-agent standards that formalized CNP (FIPA, 1990s–2000s) already wrote the message ontology once.

# Relations

- **precedes** → [The constraint moved to coordination](js--coordinate-a-thousand-steps.md)
- **the delegation half of** → [Specialists at a blackboard](bb--specialists-at-a-blackboard.md) (the shared-state half)

[^cnp]: Contract Net Protocol (Wikipedia)
