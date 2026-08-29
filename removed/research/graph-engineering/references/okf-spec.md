---
type: Source Reference
title: "Open Knowledge Format SPEC.md v0.2 (GoogleCloudPlatform/knowledge-catalog)"
description: The normative OKF specification, read from a local clone at commit 9a15b13 — the format contract this bundle follows.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags: [level-1, standards, knowledge-representation]
source_author: "Google Cloud (knowledge-catalog maintainers)"
source_date: "2026 (v0.2; read at commit 9a15b13)"
retrieved: "2026-08-24"
availability: local-clone
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:local-clone-read", at: 2026-08-24T22:55:00Z }
status: stable
---

# About

OKF v0.2: "an open, human- and agent-friendly format for representing knowledge," deliberately minimal (markdown + YAML frontmatter, `type` the only required key) with first-class provenance (`sources`), trust (`generated`/`verified`, trust tiers), lifecycle (`status`, `stale_after`), and attested computations. Quoted from disk, so verification is a file read. The spec's own motivation section is itself evidence for this bundle's thesis — it assumes knowledge corpora are now "continuously written and maintained by agents."

# Excerpts in this bundle

- [A corpus continuously maintained by agents](../excerpts/a-corpus-continuously-maintained-by-agents.md)
