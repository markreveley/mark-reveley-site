---
type: Excerpt
subtype: observation
role: evidence
title: "A corpus continuously maintained by agents"
description: The OKF spec's motivating observation — knowledge is no longer authored once and read; agents write it continuously, which makes provenance, trust, freshness, lifecycle, and attestation first-class problems.
tags: [standards, knowledge-representation, memory]
speaker: "OKF SPEC.md v0.2 (Google Cloud)"
sources:
  - id: spec
    resource: /references/okf-spec.md
    title: "Open Knowledge Format SPEC.md v0.2"
deps:
  - { concept: /excerpts/okf--formalizes-llm-wiki.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-25T01:10:00Z }
verified: { by: "process:local-clone-read", at: 2026-08-24T22:55:00Z }
status: stable
---

# Quotes

> "Increasingly, a knowledge corpus is not authored once and then read: it is **continuously written and maintained by agents**." [^spec]

**[problem]** — the five questions that follow:

> "When most concepts are machine-generated, a consumer needs answers that a plain markdown-plus-frontmatter convention does not make first-class:
> 1. What was this created from, and how was it verified? (**provenance**)
> 2. How much should I trust it? (**trust**)
> 3. Is it still true? (**freshness**)
> 4. Is it the current version? (**lifecycle**)
> 5. Was this number produced the way we said it must be? (**attestation**)" [^spec]

# Note

Quoted directly from the cloned spec (commit 9a15b13). The world-state the spec assumes, plus its five trust questions — machinery this bundle itself uses.

# Relations

- **refines** → [OKF formalizes the LLM-wiki pattern](../excerpts/okf--formalizes-llm-wiki.md)

[^spec]: Open Knowledge Format SPEC.md v0.2 (knowledge-catalog, commit 9a15b13)
