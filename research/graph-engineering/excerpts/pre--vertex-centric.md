---
type: Excerpt
subtype: observation
role: evidence
title: "Vertex-centric iteration"
description: Pregel's computational model (2010) — programs as iterations in which vertices receive messages, send messages, and mutate state — the systems ancestor of agent-graph runtimes.
tags: [history, orchestration, academic]
speaker: "Malewicz et al. (Google)"
sources:
  - id: pre
    resource: /references/pregel-paper.md
    title: "Pregel: a system for large-scale graph processing"
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:local-file-extract", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quote

> "Programs are expressed as a sequence of iterations, in each of which a vertex can receive messages sent in the previous iteration, send messages to other vertices, and modify its own state and that of its outgoing edges or mutate graph topology. This vertex-centric approach is flexible enough to express a broad set of algorithms." [^pre]

*(Extracted from a mirrored PDF of the SIGMOD 2010 paper by decompressing its text streams; ligatures reconstructed — see the reference concept for method.)*

# Note

Extracted from a mirrored PDF of the SIGMOD 2010 paper by decompressing its text streams (ligatures reconstructed). The systems-lineage root the runtime evidence exemplifies.

[^pre]: Pregel: a system for large-scale graph processing (SIGMOD 2010)
