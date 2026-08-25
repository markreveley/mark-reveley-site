---
type: Source Reference
title: "Pregel: a system for large-scale graph processing (Google, SIGMOD 2010)"
description: Google's vertex-centric graph-processing system — the acknowledged ancestor of LangGraph's runtime.
resource: https://dl.acm.org/doi/10.1145/1807167.1807184
tags: [level-1, orchestration, history, academic]
source_author: "Grzegorz Malewicz, Matthew H. Austern, Aart J.C. Bik, James C. Dehnert, Ilan Horn, Naty Leiser, Grzegorz Czajkowski"
source_date: "2010 (SIGMOD, pp. 135–146)"
retrieved: "2026-08-24"
availability: fetched
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified: { by: "process:local-file-extract", at: 2026-08-24T22:55:00Z }
status: stable
---

# About

The systems-lineage anchor: iterative, message-passing computation over graphs ("supersteps"), designed so distribution details hide behind an abstract API. Sixteen years later, [LangGraph's documentation](langgraph-overview.md) names Pregel as the inspiration for its agent-orchestration runtime — the cleanest single wire from classical graph *processing* to agentic graph *engineering*. Abstract text was extracted from a mirrored PDF (`kowshik.github.io/JPregel/pregel_paper.pdf`) by decompressing the PDF's text streams; ligatures reconstructed (ffi/fl/fi).

# Excerpts in this bundle

- [Vertex-centric iteration](../excerpts/pre--vertex-centric.md)
