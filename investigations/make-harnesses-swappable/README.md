# Making coding harnesses swappable

Start here. This README gives the investigation's question, current assessment,
and reading order. Reading the investigation does not require building the
prototype; implementation and maintenance instructions have separate roles below.

We are examining the r/LLMDevs thread *Have coding agents made us forget
‘program to an interface, not an implementation’?*, captured in
[reddit-post-program-interface.md](reddit-post-program-interface.md).
The question is whether reusable workflows can retain their behavior and saved
progress when we change coding assistants, and what must move outside the
assistant to make that possible.

## Current assessment

**Preliminary conclusion:** the proposal describes a useful separation of
responsibilities. A shared application can own workflow rules, results, and
recovery semantics while different coding harnesses request its operations.
The significant change is who owns that behavior; using MCP alone does not
establish the separation. The reasoning is developed in
[analysis.md — The proposed arrangement](analysis.md#the-proposed-arrangement).

**The baseline matters.** Claude Code already supports executable helpers, MCP,
hooks, and saved conversations. Shared scripts may already provide some of the
proposed portability. Our comparison therefore asks which responsibilities move
and whether the resulting handoff is easier, rather than assuming the baseline
cannot support reusable work. See
[analysis.md — The baseline in Claude Code](analysis.md#the-baseline-in-claude-code).

**What the evidence supports:** the source and follow-up documentation establish
the argument and describe mechanisms that could implement it. They do not
establish the author's later system's exact recovery guarantees or show that
this design is generally better than a harness-led workflow. The source-order
explanations and qualifications are in [claim-analysis.md](claim-analysis.md).

**BEAM and Jido extension:** an Elixir application could own the shared workflow
and use Jido to coordinate it, including delegating coding work to an existing
harness. The research spike found Jido.Harness as a direct integration lead and
related work in other ecosystems. MCP's published 2026-07-28 revision also makes
application state explicit across independent requests. These are documented
mechanisms and research findings, not tested recovery or performance results.
See [beam-jido.md](beam-jido.md) for the architecture, sources, and qualifications.

**What remains untested:** the prototype has not been built. We have no measured
handoff, retry, migration-effort, or maintenance results. The proposed test uses
a small source-report task we devised: read the thread's YAML capture, prepare
factual counts and metadata, then render a report. Interrupting those two steps
lets us test whether another harness can finish the same saved work. Its purpose
and limits are in
[reproduction.md — Purpose of the experiment](reproduction.md#purpose-of-the-experiment).

Current status: source intake, claim analysis, architectural analysis, and the
BEAM/Jido research companion are written; the experiment is specified. The next
empirical question is whether the shared application preserves the same run
across a harness change, and what each arrangement requires to do so.

## How to read this investigation

For a first reading, use this order:

1. **This README:** understand the question and preliminary assessment.
2. **The source:** read the original post and captured comments in
   [reddit-post-program-interface.md](reddit-post-program-interface.md).
   These are the participants' statements, not our conclusions.
3. **The explanation:** read [claim-analysis.md](claim-analysis.md) to unpack
   the title, migration scenario, and each subsequent claim. It follows the
   source order and separates interpretation from supporting evidence.
4. **The synthesis:** read [analysis.md](analysis.md) for the architecture as a
   whole: the Claude Code baseline, proposed change, tradeoffs, and unresolved
   questions. This supplies the detailed reasoning behind the assessment above.

Use [definitions.md](definitions.md) as a lookup while reading; it is not a
required chapter to read from beginning to end. If you only want the current
conclusion, this README is sufficient; follow its analysis links for the reasoning.

## When to use the other documents

- **Optional branch after the synthesis:** read [beam-jido.md](beam-jido.md) for
  BEAM and Elixir foundations, Jido 2, retaining a coding harness as a worker,
  related projects, and MCP's move toward stateless requests. Its experiments
  are proposals; the original reproduction remains the first specification.
- **To understand or build the proposed test:** use
  [reproduction.md](reproduction.md). Its purpose and task sections explain the
  example; its later sections are implementation instructions and acceptance
  checks. Building it is a separate activity from reading the analysis.
- **To continue maintaining this investigation:** use
  [instructions.md](instructions.md). Its imperatives tell a researcher or agent
  how to update evidence, conduct future experiments, and prepare a draft. It is
  not a reading guide or the current evaluation.
- **To prepare a future article:** use [outline.md](drafts/outline.md). This is a
  provisional publication outline, pending experimental results.
- **To inspect provenance and open questions:** use
  [investigation.yaml](investigation.yaml). The structured source is
  [reddit-program-interface.yaml](sources/reddit-program-interface.yaml), and
  the original paste is
  [reddit-post-program-interface.txt](sources/raw/reddit-post-program-interface.txt).

The reader's next document is
[reddit-post-program-interface.md](reddit-post-program-interface.md).
