---
type: Excerpt
subtype: definition
role: evidence
title: "Goldens: a pending test case"
description: Evals' own term of art for the input/expected-output pair a dataset is built from — a golden, defined by what it lacks (the outputs an LLM hasn't produced yet) rather than what a standards body legislates.
tags: [definitions, evaluation]
speaker: "DeepEval docs (Confident AI)"
sources:
  - id: deepeval
    resource: /references/deepeval-evaluation-datasets.md
    title: "Datasets — DeepEval: The LLM Evaluation Framework"
generated: { by: research_agent/claude-code, at: 2026-08-25T13:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-25T13:00:00Z }
status: stable
---

# Quotes

> "Goldens represent a more flexible alternative to test cases in `deepeval`, and is the preferred way to initialize a dataset." [^de]

> "Unlike test cases, goldens: Only require `input`/`scenario` to initialize, Store expected results like `expected_output`/`expected_outcome`, Serve as templates before becoming fully-formed test cases." [^de]

> "Think of goldens as 'pending test cases' - they contain all the input data and expected results, but are missing the dynamic elements (`actual_output`, `retrieval_context`, `tools_called`) that will be generated when your LLM processes them." [^de]

# Note

Evals' definitions don't come from a standards body — `deepeval` is one framework among several — but the shape of the term is consistent across the field: a golden is an input plus a human- or spec-defined expected output, recorded *before* any model has run on it, so the same golden can be replayed against every model or prompt version under test. An eval harness then loops over a dataset of goldens, runs each one, and turns it into a scored test case — the golden is the fixed half of that comparison, the run is the variable half.

[^de]: DeepEval docs, "Datasets" (Confident AI)
