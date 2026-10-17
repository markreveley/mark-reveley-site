# Moving a workflow out of the conversational harness

This analysis examines what must be shared for work to continue when we change
coding assistants. The proposed change concerns where a reusable workflow's
decisions, rules, and progress live. In the baseline considered here, Claude Code
coordinates the workflow from instructions and tool results. In the proposed
arrangement, a separate application implements that workflow and exposes
operations Claude Code or another harness can call. Claude Code can remain the
user-facing assistant in both arrangements.

The source argument comes from the r/LLMDevs thread
[Have coding agents made us forget ‘program to an interface, not an
implementation’?][discussion]. Our [source-report task][source-report] is a small
workload devised to test that argument: produce factual counts and metadata from
the captured thread. Its fixed input and two steps let us interrupt work, switch
harnesses, and check which results survive. The [experiment's purpose][purpose]
is to compare that handoff and the work required to support it in each arrangement.

“Traditional” here means this particular harness-led arrangement, not every
possible Claude Code installation. The comparison concerns ownership of the
workflow, rather than a product's inability to run code or connect to tools.
See [definitions](definitions.md) for terminology and source qualifications.

## The baseline in Claude Code

Claude Code supplies a model-driven loop that gathers context, invokes tools,
and evaluates their results. The model chooses subsequent actions within that
loop. File access, command execution, and context management are already part of
that harness. [How Claude Code works][claude-loop]

For the [source-report task][source-report] designed for this investigation,
a baseline implementation could place the procedure in a skill: read the
[source record][fixture], obtain counts, and save a factual report. The
[later summary step][summary-step] adds model-written prose. The skill can include
a deterministic counting script; executable helpers do not require the proposed
architecture.
[Claude Code skills][claude-skills]

In this example, the helper owns the counting algorithm. The harness and its
instructions still coordinate the overall reporting procedure: which helper to
call, when to summarize, and how to proceed after a failure. This is our chosen
baseline, not a claim that all skills must work this way.

```text
User requests a source report
  -> Claude Code loads the reporting instructions
  -> its model chooses a read or helper-script call
  -> the harness executes the call and returns its result
  -> its model chooses the next action or writes the summary
  -> the report and conversation record the outcome
```

## The proposed arrangement

Move the reusable reporting procedure into an application package. Its core
defines source validation, step transitions, saved results, and retry behavior.
CLI and MCP adapters translate requests into calls to that core. The outer
harness decides when to request work and how to explain the result to the user.

```text
User requests a source report
  -> Claude Code or another harness chooses a report operation
  -> CLI or MCP adapter calls the shared application core
  -> the core checks inputs and persisted progress
  -> it executes an allowed step and commits the result
  -> the adapter returns a result and run ID
  -> the conversational model explains them or requests another operation
```

Claude Code already connects to MCP servers. MCP is therefore an integration
mechanism available to both arrangements. The architectural change is placing
the workflow behind a reusable [application contract][contract]. A server exposing
only low-level reads and calculations could still leave the whole workflow under
the conversational model's direction. [Claude Code MCP integration][claude-mcp]

The [initial reproduction][build-sequence] makes that boundary deliberately
small: the harness requests each next step, while the core enforces its order
and saves its result. It does not yet run the entire workflow autonomously.
A later operation could execute several steps internally without changing
who owns their meaning, but that would require additional execution rules.

## Follow the same model-assisted task through both arrangements

The [model-assisted extension][summary-step] adds a prose summary to the factual
report. It is a later stage of our example workload.

**In the baseline**, the reporting skill supplies summary instructions to the
conversational model. That model reads the source or helper output and composes
the summary. The instructions, context preparation, and orchestration belong
to the Claude Code setup selected for this comparison.

The baseline could also delegate summarization to a Claude Code subagent.
Subagents have their own context and can have specialized prompts and tool
access. Nested model work therefore already exists within the harness; simply
drawing an outer model and an inner model does not distinguish the proposal.
[Claude Code subagents][claude-subagents]

**In the proposed arrangement**, the outer model requests a reporting operation.
The application core loads the summary prompt, selects the model provider,
constructs its input, calls it, checks the response, and stores the result with
the run. Another harness can request that same operation without receiving or
reimplementing the internal summarization procedure.

That is the ownership change: prompt, provider configuration, execution rules,
and saved domain result move into the capability's application. A thin host skill
can still explain when to use it. The application must arrange its own model
access in this design; exposing an MCP tool does not automatically supply an
inner model invocation.

One internal summary request is a model-assisted workflow step. An inner agent
loop would additionally make repeated model-directed decisions, execute its
chosen tools, feed back their results, and stop under application-defined rules.
Those are separate implementation stages. See [model and agent][model-agent].

## Compare the responsibilities that matter

### Workflow control and reusable code

In the baseline, a model following the reporting instructions coordinates the
steps. Its deterministic helper can already be shared between harnesses. In the
proposal, more of the procedure becomes shared code: allowed transitions, result
validation, and the meaning of a retry. Both adapters invoke that implementation.

This is a continuum. If a baseline script already accepts a run ID, owns the
whole procedure, and persists its progress, it already has much of the proposed
separation. Adding MCP may then change discoverability and invocation rather
than workflow architecture. Conversely, packaging orchestration prose as a
server description would leave the control decisions in the outer model.

### Instructions and enforced restrictions

Claude Code treats instruction and memory files as context. It also has actual
tool permission rules and lifecycle hooks; the baseline is not limited to asking
the model to behave. [Memory and instructions][claude-memory],
[permissions][claude-permissions], [hooks][claude-hooks]

The proposal adds application checks that follow the capability through either
adapter. For example, [start_run][start-run] rejects a source outside its allowlist
regardless of which harness requested it. That check differs from a host deciding
whether the tool call is permitted at all. Host permissions remain useful.

A core check governs calls through that core. Separate shell access, direct
database writes, or other credentials can provide another route. The portability
claim is about the shared operation's enforcement, not a new system-wide sandbox.

### Conversation recovery and application recovery

Claude Code saves conversations and supports session resume. It also checkpoints
supported file edits for rewind, with documented limits such as changes made
through Bash. The baseline already has continuity mechanisms.
[Claude Code sessions][claude-loop], [checkpointing][claude-checkpoints]

The [proposed database][storage] records a different unit: the report run, its
source snapshot, completed steps, and receipts. A new conversation in another
harness can query that state without importing the original Claude Code transcript.
An application transaction can settle whether a step committed even if its
response never reached the conversational model.

The difference is therefore the kind of state recovered and the contract for
using it. Session resume alone does not specify our report operation's duplicate
handling. A baseline helper could implement the same database contract; doing
so would move it toward the proposed arrangement.

### Process lifetime and restart

Saving a run does not keep its process alive. A local stdio server is commonly
launched as a client-managed subprocess. The protocol describes shutdown and
restart behavior; a restarted server still needs application-specific state
to decide what work was completed. [MCP stdio][stdio]

Our [first reproduction][build-sequence] resumes only when a caller requests
the next step. Continuing work after the host exits would require a worker with
an independent lifecycle. Neither an MCP adapter nor a second model call provides
that worker.
The comparison should test conversation loss, server loss, and worker loss as
different events rather than claim that one architecture simply “survives.”

### Cost and maintenance

The baseline can be economical for a procedure that changes often or benefits
from interactive judgment. Its instructions and small helpers may be sufficient.
The proposal adds code, schemas, storage, versioning, error handling, and tests.
An internal model call also needs provider configuration and has its own cost.

The expected benefit is that these application decisions are maintained once
and exercised through multiple hosts. That benefit must be demonstrated against
the actual migration work. Shared scripts and portable skills can already reduce
that work; the experiment should identify what remains coupled to the harness.

## What the discussion supports

- The [post][post] proposes CLI or MCP access to portable capabilities. It also
  allows useful harness-specific features to remain in thin integrations.
- [c06][c06] proposes shared instruction files as a cheap starting point. This
  shares prose; by itself it says nothing about who executes or persists a run.
- [c05][c05] and [c08][c08] favor code-level refusals and consistent descriptions.
  This motivates shared checks without establishing that existing harnesses
  lack enforcement mechanisms.
- [c09][c09] and [c11][c11] distinguish Switchplane from the author's later
  conversational split. Its public README is not an implementation of every
  detail described in that later system.
- [c10][c10] and [c11][c11] say the user must request another start after a harness
  dies. The capture does not establish exactly which work is resumed or repeated.

Switchplane documents explicit retry with optional graph checkpoints. LangGraph
distinguishes saved graph state from other stored data and requires a persistent
backend to retain checkpoints across process restarts. These clarify possible
mechanisms; they are not results from our experiment.
[Switchplane recovery][switchplane], [LangGraph persistence][persistence]

## What the reproduction should establish

Run the same [reporting task][source-report] first with a harness-coordinated
procedure, then through the shared core. Record where instructions, helper code,
restrictions, and progress live in each version. Keep the source and deterministic
calculations the same so the comparison isolates the boundary change.

For the proposed version, start a run in one harness, close its session and
server, then find and resume the run in another. Check duplicate requests and
refusals through both adapters. Record any instructions or configuration that
still need to change. The [acceptance checks][acceptance] define the observations;
no implementation or cross-harness result has been demonstrated yet.

[claude-loop]: https://code.claude.com/docs/en/how-claude-code-works
[claude-skills]: https://code.claude.com/docs/en/skills
[claude-mcp]: https://code.claude.com/docs/en/mcp
[claude-subagents]: https://code.claude.com/docs/en/sub-agents
[claude-memory]: https://code.claude.com/docs/en/memory
[claude-permissions]: https://code.claude.com/docs/en/permissions
[claude-hooks]: https://code.claude.com/docs/en/hooks
[claude-checkpoints]: https://code.claude.com/docs/en/checkpointing
[stdio]: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio
[model-agent]: definitions.md#model-and-agent
[post]: reddit-post-program-interface.md#post
[c05]: reddit-post-program-interface.md#c05
[c06]: reddit-post-program-interface.md#c06
[c08]: reddit-post-program-interface.md#c08
[c09]: reddit-post-program-interface.md#c09
[c10]: reddit-post-program-interface.md#c10
[c11]: reddit-post-program-interface.md#c11
[switchplane]: https://github.com/salesforce-misc/switchplane#checkpoint-and-retry
[persistence]: https://docs.langchain.com/oss/python/langgraph/persistence
[source-report]: reproduction.md#source-report-task
[purpose]: reproduction.md#purpose-of-the-experiment
[fixture]: sources/reddit-program-interface.yaml
[discussion]: reddit-post-program-interface.md
[summary-step]: reproduction.md#add-a-model-inside-the-capability
[contract]: reproduction.md#define-the-contract-before-the-adapters
[start-run]: reproduction.md#start_run
[storage]: reproduction.md#store-enough-state-to-recover
[build-sequence]: reproduction.md#build-and-exercise-it-in-this-order
[acceptance]: reproduction.md#acceptance-checks
