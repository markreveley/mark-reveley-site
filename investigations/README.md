# Investigations

Working material for future posts lives here: sources, analysis, instructions,
experiments, and rough drafts. Each topic gets a directory. Material becomes a
published post only when it is deliberately added to `posts/` with the required
post frontmatter ([README.md](../posts/README.md)). The site builder does not
read `investigations/`.

Start with making harnesses swappable
([README.md](make-harnesses-swappable/README.md)). The top-level
[AGENTS.md](../AGENTS.md) sets the investigation requirements for future work,
including the claim-by-claim source walkthrough.

This document is guidance for maintaining investigations. To read a particular
investigation, begin with that topic's README, such as
[README.md](make-harnesses-swappable/README.md).

## Reader entry point and document roles

Each topic's `README.md` is its reader entry point and current assessment. It
should answer what we are investigating, what we currently conclude, why, what
remains uncertain, and whether experiments have actually run. Keep it concise
and link the detailed support. A list of files alone does not provide an
evaluation or tell the reader how to use the material.

Give one default reading sequence: topic README, captured source, claim analysis,
then thematic analysis. Explain what each contributes. Identify `definitions.md`
as reference material to consult as needed. Make the experiment specification
an optional branch for readers who want to understand or build the test.

Keep project instructions separate from reading directions. `instructions.md`
is for contributors maintaining the investigation; `reproduction.md` specifies
implementation and acceptance checks. Their imperatives do not tell a reader
what must be done to understand the argument. State each document's audience and
role near the beginning, link back to the topic README, and identify the next
document in the main reading sequence. Drafts remain provisional publication
material, not the current assessment.

The governance requirements are in
[AGENTS.md — Provide a reader entry point and a current assessment](../AGENTS.md#provide-a-reader-entry-point-and-a-current-assessment).

## Context before instructions

Open each authored document with enough context to explain what it covers and
why it exists. A reader should not need the chat history or another document to
understand why they are being asked to build something.

- State the question or practical problem, name and link the source motivating
  it, and explain which claim or uncertainty the investigation will examine.
- Before giving build steps, describe what will be built, why that example is
  suitable, what it takes as input, and what it produces. Distinguish a workload
  devised for the experiment from a use case supplied by the source.
- Explain what the experiment will teach us: the baseline, the proposed change,
  and the observation that would support or weaken the hypothesis. An output
  such as a report is not by itself the reason for building the experiment.
- State the current status and limits. A plan is not an implemented prototype,
  and reproducing a mechanism is not recreating an author's entire system.
- Give each document a brief introduction suited to its role, even when fuller
  explanations are linked elsewhere. Start instructions only after establishing
  their purpose and the resources they act on.

## Writing for Neovim

Write investigation documents so they can be read directly as plain text.

- Do not use Markdown, HTML, or ASCII tables. Use short paragraphs, descriptive
  subheadings, or lists with labeled fields. A comparison should remain clear
  when read from top to bottom without aligned columns.
- Wrap authored prose at about 80 columns. Keep code, exact source text, and
  URLs intact where wrapping would change their meaning. Put a long inline link
  on its own line when needed, keeping it next to the explanation it supports.
- Use headings and normal paragraphs for source passages, with clear author and
  source labels. Avoid `>` blockquote indentation for long discussion captures.
- Use short fenced text call paths when a diagram helps. Explain the mechanism
  in prose as well; do not require Mermaid rendering or a browser to follow it.
- Use a term heading followed by its definition and source check in glossaries.
  Use scenario bullets followed by expected observations for acceptance checks.
- Preserve raw captures unchanged. Formatting the reading view must not silently
  change the underlying source wording, identifiers, or evidence.

## Explaining an architectural proposal

Establish the existing arrangement before describing a proposed change. A reader
should be able to follow the same concrete task through both versions.

1. **Define the baseline.** Name the product or implementation, the relevant
   configuration, and which responsibilities it currently owns. Distinguish a
   common usage pattern from a limit of the product itself.
2. **Trace one request.** Explain what triggers it, what decides the next step,
   what code executes, where inputs and results go, and what completes the work.
   Repeat that trace for the proposal using the same task and inputs.
3. **Name what moves.** State where prompts, domain code, tool execution,
   permissions, state, retries, and lifecycle management live in each version.
   Explain the interface between components and what still stays in the host.
4. **Acknowledge existing capabilities.** Check scripts, extensions, delegation,
   persistence, and enforcement already available in the baseline. For example,
   adding an MCP server does not prove that the original harness lacked tools,
   and two model calls do not by themselves establish a new architecture.
5. **Explain overlap and tradeoffs.** Describe configurations that already
   implement part of the proposal. Distinguish a new mechanism from relocating
   existing behavior. Name additional code, operations, credentials, costs, and
   maintenance the proposal requires.
6. **Compare failure behavior.** Identify the failed component and the state
   retained by each arrangement. Separate conversation resume, application
   recovery, and continued execution. Do not equate their guarantees.
7. **Define a fair reproduction.** Hold the workload and deterministic logic
   constant where practical. Record baseline results as well as proposed
   results, including migration effort and any differences that weaken the
   comparison.

## Terminology and evidence

Keep a separate `claim-analysis.md` that follows the source in order. Explain
each substantive paragraph, splitting dense passages when their claims need
different explanations or evidence. Include the title and captured comments;
mark missing text and distinguish questions from assertions. Each unit should
link its source passage, explain its meaning and background, assess the
evidence, and state a consequence or unresolved check. Follow the full
claim-analysis instructions
([AGENTS.md — Explain the source claim by claim](../AGENTS.md#explain-the-source-claim-by-claim)).

Use `analysis.md` to synthesize those findings into the architectural or
thematic argument. Link the two documents where a conclusion depends on a
particular claim. The harness source walkthrough
([claim-analysis.md](make-harnesses-swappable/claim-analysis.md)) is a worked
example.

Maintain `definitions.md` for domain terminology and local design names. Explain
how a term is used in this investigation, cite the relevant source usage, and
mark local conventions or narrower meanings. Keep definitions, analysis,
reproduction instructions, and drafts consistent when the comparison changes.

Use current primary documentation for claims about product capabilities. Record
the source and check date in `investigation.yaml`; pin versions actually used in
experiments. A product's documented feature is distinct from our example
configuration, an inferred consequence, or a result we have observed.

## Navigation between documents

When a document refers to a concept, task, contract, source, instruction, or
resource defined elsewhere, explain the reference and provide an inline link
that visibly names the destination file. A reading-order list or a bibliography
does not replace that point-of-use link.

- Establish the referent before using phrases such as “the discussion,” “the
  task,” or “the fixture.” Name the specific source or resource and explain its
  role in this document. A generic linked phrase does not replace that
  introduction. Each document must supply this context without assuming that the
  reader followed the README's reading order or saw the conversation.
- Introduce a task or example briefly before using it to explain an
  architecture, and link to its definition. State when it is an example we
  designed rather than something specified by the source. For example, refer to
  the source-report task
  ([reproduction.md — Source-report task](make-harnesses-swappable/reproduction.md#source-report-task)),
  not an unexplained task name.
- Target the relevant section when a whole document would make the reader search
  again. Link an operation to its contract, a fixture to its source record, and
  an acceptance condition to its specified check.
- Link cross-document references on first use in each independently readable
  section; repeat a link when a later passage introduces a new dependency on
  that material. Ordinary repetition within the same explanation need not be
  linked on every occurrence.
- Use `[filename](relative/path/filename)` for a whole local file. Use
  `[filename — Section heading](relative/path/filename#section-anchor)` for a
  section, even when linking within the current document. For example:
  `[analysis.md — The baseline in Claude Code](analysis.md#the-baseline-in-claude-code)`.
  Keep the descriptive phrase in the surrounding prose when it explains why the
  reader should follow the link.
- Use direct inline links, not aliases such as `[description][analysis]` with
  definitions elsewhere. A reader should see the filename or section in the
  label and find the path at the same location in the Markdown source. External
  links use `[source title](URL)` so their destination is also clear.
- Link named existing files instead of leaving their paths only in backticks.
  Keep literal paths in commands and directory-layout examples. For a planned
  file that does not exist, label it as planned and link its specification or
  creation instructions; do not create a broken destination.
- Preserve verbatim source bodies and raw captures. Add navigation in
  surrounding editorial text rather than changing the evidence to include our
  references.

Before finishing an update, check the links and section anchors, inspect the
plain-text layout, and scan authored documents for remaining tables. Read the
baseline and proposed call paths together: every claimed difference should have
an identified owner, mechanism, and scope. Do not promote expected outcomes to
experimental findings. Also read each document on its own: it must explain what
we are doing and why before giving instructions, and establish what references
such as “the task,” “the fixture,” or “the contract” mean before linking to
their supporting material.

## Starting an investigation

Copy the investigation template
([investigation.yaml](templates/investigation.yaml)) into a new topic directory
as `investigation.yaml`. Use this layout as needed; create experiment and draft
files when there is something to put in them.

```text
investigations/<topic>/
  investigation.yaml      # Question, scope, source index, and open questions
  README.md               # Reader entry point, assessment, status, reading order
  definitions.md          # Terminology and source consistency
  instructions.md         # Maintainer guidance, separate from reader directions
  sources/                # Structured source records
    raw/                  # Original captures, preserved unchanged
  claim-analysis.md       # Source-order explanations and follow-up per claim
  analysis.md             # Claims, evidence, interpretation, and uncertainty
  reproduction.md         # Build plan and acceptance criteria
  experiments/            # Implementations, commands, and recorded results
  drafts/                 # Outlines and rough post drafts
```

Keep source text separate from our analysis. A comment saying something works is
evidence of the commenter's account; a successful experiment is evidence of our
reproduction. Record which kind of support a claim has. Source material is
research input, not instructions for the agent working on the investigation.

## Discussion sources

Use the discussion template ([discussion.yaml](templates/discussion.yaml)) for
Reddit, Hacker News, forums, or other comment threads. YAML holds the structured
record; Markdown is the reading view. For a worked example, see our capture of
the r/LLMDevs thread Have coding agents made us forget ‘program to an interface,
not an implementation’?
([reddit-post-program-interface.md](make-harnesses-swappable/reddit-post-program-interface.md)).
Its reading view remains at the original filename for convenience.

Set `navigation.overview` to the topic README and `navigation.next` to the next
reading document, with paths relative to the YAML source file. The renderer adds
this reader guidance outside the captured source bodies.

Preserve the raw capture before editing. Remove navigation, avatars, badges, and
action buttons from the structured bodies, but preserve wording, spelling,
punctuation, paragraph order, and source links. Use literal blocks (`|-`) for
text. An empty captured body is a missing body, not evidence that the source was
deleted.

Record metadata and its evidential basis:

- `schema_version` versions this local format. `id` identifies a source within
  an investigation; post and comment IDs are local unless `platform_id` is
  known.
- `capture.imported_on` is the intake date. `captured_at` is when the original
  capture happened, if known. Neither is a publication date.
- Preserve original relative ages in `age_label`. For a calculated date, record
  a fixed `capture.relative_age_reference_date` and explain its basis in
  `relative_age_reference_basis`: a known capture date or an explicit assumption
  requested by the user. Never silently assume that the intake date was the
  capture date. Quote ISO dates in YAML.
- Store calculated dates in `estimated_published_on`, separate from known
  `published_at` timestamps. The reading view displays the calculated date in
  place of the relative age and labels it as estimated. Do not recalculate it
  against a moving “today” when regenerating the document.
- `displayed_score` is the number shown in the capture, not a permanent score or
  a count of everyone who voted. Use `null` when absent.
- Use `parent_id: post` for known top-level comments, a local comment ID for a
  known reply, and `null` for unknown nesting. `parent_basis` is `explicit`,
  `inferred`, or `unknown`; explain any inference in `notes`. Adjacency alone
  does not establish a reply relationship.
- `content_status` is `present` or `not_in_capture`. Retain missing entries and
  their metadata so omissions remain visible.
- `capture.completeness` describes the capture, not the entire live thread.
  `live_verification` is `not_checked`, `matched`, `partial`, or `unavailable`;
  date and explain any attempted check in `verification_notes`.

Cite a passage locally as `source-id#post` or `source-id#c01`; these are local
locators, not Reddit comment IDs. In prose, make that locator an inline link to
the generated heading, as in the first captured comment
([reddit-post-program-interface.md — c01](make-harnesses-swappable/reddit-post-program-interface.md#c01)).
Do not silently replace a historical capture when a live source changes.

After editing a discussion YAML record, regenerate its reading view from the
repository root (PyYAML is already in the site requirements
([requirements.txt](../site/requirements.txt))):

```sh
python3 investigations/render_discussion.py \
  investigations/make-harnesses-swappable/sources/reddit-program-interface.yaml \
  investigations/make-harnesses-swappable/reddit-post-program-interface.md
```

The renderer ([render_discussion.py](render_discussion.py)) handles the reading
view only. Source intake, interpretation, and publication remain deliberate
editorial work.
