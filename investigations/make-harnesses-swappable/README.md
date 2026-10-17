# Making coding harnesses swappable

This investigation asks how work can continue when we change coding assistants.
We want to understand which instructions, executable behavior, and saved progress
must move with the assistant, and which can remain in a shared application. The
working hypothesis is that a shared core, exposed through CLI and MCP tools, can
preserve workflow behavior and progress while the conversational harness changes.

The starting point is the r/LLMDevs thread
[Have coding agents made us forget ‘program to an interface, not an
implementation’?][discussion], preserved here as a post and its captured comments.
The comparison uses a [Claude Code workflow][baseline] coordinated through a
skill and helper scripts as its baseline. The [proposal][proposal] moves step
rules, domain results, and retry handling into a shared application. Claude Code
can remain the conversational assistant while the application owns the workflow.

The example workload is the [source-report task][task]: produce factual counts
and source metadata from that thread's [YAML capture][source], with a later
summary extension. We designed it for this investigation because the fixed input
and two short steps make interruptions and retries observable. The test is
whether another harness can finish the same saved work, and how much adaptation
each arrangement requires. See the [experiment's purpose][purpose] before its
build instructions.

## Reading order

1. [Discussion](reddit-post-program-interface.md): the original post and 11
   captured comment entries, including one with no captured body.
2. [Definitions](definitions.md): terminology as used here, cross-referenced with
   source usage and marked where it is a local convention.
3. [Analysis](analysis.md): the Claude Code baseline, the proposed boundary,
   and the same task traced through both arrangements.
4. [Reproduction plan](reproduction.md): a small source-report workflow, its
   interface, persistence model, and acceptance checks.
5. [Working instructions](instructions.md): scope for subsequent investigation.
6. [Draft outline](drafts/outline.md): a possible post structure, pending results.

[The investigation record](investigation.yaml) indexes sources and open questions.
[The source YAML][source] is the canonical structured transcript;
[the raw paste][raw] is preserved.

Current state: source intake and an initial design are complete. The reproduction
is specified, but has not been implemented or tested in coding harnesses.

[discussion]: reddit-post-program-interface.md
[baseline]: analysis.md#the-baseline-in-claude-code
[proposal]: analysis.md#the-proposed-arrangement
[task]: reproduction.md#source-report-task
[purpose]: reproduction.md#purpose-of-the-experiment
[source]: sources/reddit-program-interface.yaml
[raw]: sources/raw/reddit-post-program-interface.txt
