---
type: Excerpt
subtype: observation
title: "A corpus continuously maintained by agents"
description: The OKF spec's motivating observation — knowledge is no longer authored once and read; agents write it continuously, which makes provenance, trust, freshness, lifecycle, and attestation first-class problems.
tags: [standards, knowledge-representation, memory, era-agentic]
speaker: "OKF SPEC.md v0.2 (Google Cloud)"
sources:
  - id: spec
    resource: /references/okf-spec.md
    title: "Open Knowledge Format SPEC.md v0.2"
deps:
  - { concept: /excerpts/okf--formalizes-llm-wiki.md, rel: refines }
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
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

# Analysis

The spec's motivation section is itself primary evidence for this bundle's subject: a Google-published standard now *assumes* the [seed thread's world](rl--just-fancier-retrieval.md) — knowledge graphs built and read by agents — and moves on to the second-order problem, which is epistemic. Once the producer is a machine, "who wrote this and why should I believe it" stops being answerable by social context and must be carried *in the data*. The five questions are a governance layer for [Karpathy's compounding wiki](ka--compiled-once.md): compilation without provenance compounds errors as efficiently as knowledge ([organized nonsense](lb--organized-nonsense.md), in document form). Self-referential note: this bundle uses exactly these machineries — its `verified` fields distinguish curl-checked quotes from unverifiable ones — so the spec's answer to its own questions is being field-tested by the document you are reading.

# Relations

- **refines** → [OKF formalizes the LLM-wiki pattern](okf--formalizes-llm-wiki.md)
- **governs** → [Compiled once, kept current](ka--compiled-once.md)
- **document-world analogue of** → [Organized nonsense at industrial scale](lb--organized-nonsense.md)

[^spec]: Open Knowledge Format SPEC.md v0.2 (knowledge-catalog, commit 9a15b13)
