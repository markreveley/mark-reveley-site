# Draft outline for what makes a coding harness swappable

This is provisional publication planning. The current assessment and reader
entry point are in [README.md](../README.md); this outline is not part of the
main reading sequence.

This outline is for a post examining whether work can continue when we switch
coding assistants. It investigates the interface proposal in the r/LLMDevs
thread Have coding agents made us forget ‘program to an interface, not an
implementation’?
([reddit-post-program-interface.md](../reddit-post-program-interface.md)). Our
planned example is the source-report task
([reproduction.md — Source-report task](../reproduction.md#source-report-task)),
which generates factual counts and metadata from our capture of that thread. We
devised it to make the workflow's ownership and saved progress observable. Use
the source walkthrough ([claim-analysis.md](../claim-analysis.md)) for the
principle's background, the migration scenario, and the qualifications attached
to each source claim.

Status: outline only; the planned reproduction
([reproduction.md — Purpose of the experiment](../reproduction.md#purpose-of-the-experiment))
has not been implemented and results are pending.

Proposed opening: moving the same rules between coding assistants exposes a
deeper question—what behavior belongs to the assistant, and what belongs to the
capability it calls?

1. **The existing workflow.** Follow the source-report task
   ([reproduction.md — Source-report task](../reproduction.md#source-report-task))
   through the Claude Code baseline
   ([analysis.md — The baseline in Claude Code](../analysis.md#the-baseline-in-claude-code)).
   Establish where control and progress live.
2. **The proposed change.** Follow the same task through the shared application
   ([analysis.md — The proposed arrangement](../analysis.md#the-proposed-arrangement)).
   Identify the responsibilities moved behind CLI and MCP operations.
3. **Locate the rules and state.** Show the operation contract
   ([reproduction.md — Define the contract before the adapters](../reproduction.md#define-the-contract-before-the-adapters)),
   one refusal, and the persisted run record
   ([reproduction.md — Store enough state to recover](../reproduction.md#store-enough-state-to-recover))
   from the experiment.
4. **Switch the harness.** Present commands, versions, and observed results from
   the handoff experiment
   ([reproduction.md — Build and exercise it in this order](../reproduction.md#build-and-exercise-it-in-this-order)).
5. **Break the handoff.** Show the failure and retry checks
   ([reproduction.md — Acceptance checks](../reproduction.md#acceptance-checks)).
   Separate recovery from continued execution.
6. **Compare model execution.** Use the summary comparison
   ([analysis.md — Follow the same model-assisted task through both arrangements](../analysis.md#follow-the-same-model-assisted-task-through-both-arrangements))
   to contrast a main-conversation or subagent summary with an application-owned
   model call. Explain why nested model work alone does not establish the
   difference.
7. **State the useful boundary.** Identify what stayed stable, what required
   host adaptation, and which claims the small reproduction cannot establish.

Before drafting the results sections, create the planned
`experiments/source-report/results.md` with observed behavior, following the
experiment file specification
([reproduction.md — Keep the first implementation small](../reproduction.md#keep-the-first-implementation-small)).
The discussion
([reddit-post-program-interface.md](../reddit-post-program-interface.md))
motivates the experiment; it does not substitute for its outcome.
