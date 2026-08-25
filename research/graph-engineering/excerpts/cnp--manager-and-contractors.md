---
type: Excerpt
subtype: definition
role: evidence
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
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "The Contract Net Protocol (CNP) is a task-sharing protocol in multi-agent systems, introduced in 1980 by Reid G. Smith. It is used to allocate tasks among autonomous agents." [^cnp]

> "[…] a manager proposes a task to several agents. The latter make a proposal among which the manager chooses to allocate the task. […] This task can then be divided and subcontracted." [^cnp]

> "This protocol can be used to implement hierarchical organizations, where a manager assigns tasks to contractors." [^cnp]

# Note

Curl-verified against Wikipedia; protocol is Smith, IEEE Trans. Computers 29(12), 1980. Orchestrator-worker delegation as a protocol, 45 years early.

# Relations

- **precedes** → [The constraint moved to coordination](../excerpts/js--coordinate-a-thousand-steps.md)

[^cnp]: Contract Net Protocol (Wikipedia)
