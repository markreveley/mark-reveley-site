---
type: Excerpt
subtype: definition
title: "Issues, positions, arguments"
description: Kunz & Rittel's IBIS — typed argumentation graphs for wicked problems (1960s–1970), made graphical hypertext by Conklin's gIBIS in the late 1980s.
tags: [knowledge-representation, argumentation, history, era-classical, typed-edges]
speaker: "Wikipedia (Issue-based information system)"
sources:
  - id: ibis
    resource: /references/ibis-wikipedia.md
    title: "Issue-based information system (Wikipedia)"
deps:
  - { concept: /excerpts/tbl--making-links.md, rel: precedes }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:55:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-24T23:50:00Z }
status: stable
---

# Quotes

> "The issue-based information system (IBIS) is an argumentation-based approach to clarifying wicked problems—complex, ill-defined problems that involve multiple stakeholders." [^ibis]

> "IBIS was invented by Werner Kunz and Horst Rittel in the 1960s." [^ibis]

> "Issues (questions) can be associated with any node. Positions (answers) can be associated only with issues. Arguments can be associated with positions but not with questions." [^ibis]

**[observation]** — the graphical turn:

> "Jeff Conklin and co-workers adapted the IBIS structure for use in software engineering, creating the gIBIS (graphical IBIS) hypertext system in the late 1980s." [^ibis]

# Analysis

The argumentation-graph ancestor, with typed *nodes* and typed *attachment rules* — a grammar, not just a graph: positions may only answer issues; arguments may only attack or support positions. That is stronger typing discipline than most 2026 knowledge graphs enforce, achieved in the 1970s on paper. gIBIS (Conklin & Begeman, 1988) made it collaborative hypertext for capturing design rationale — "why did we decide this," which is precisely the question the [typed-edge camp](ft--edge-type-is-knowledge.md) says vector search cannot answer and the [decision-trace camp](neo--three-memories.md) now builds memory for. Reflexive note, flagged for the maintainer's format discussion: this bundle's own excerpt schema — `question`/`claim`/`problem`/`solution` subtypes joined by `supports`/`contradicts`/`answers` relations — is an extended IBIS, rediscovered independently. The wheel is round; the question is whether to adopt the original's spokes.

# Relations

- **precedes** → [Making links](tbl--making-links.md) (typed discourse graphs before linked data)
- **1988 answer to** → [The decision lives in the structure](aio--decision-lives-in-structure.md)
- **schema ancestor of** → this bundle's excerpt format (see [README](../README.md))

[^ibis]: Issue-based information system (Wikipedia)
