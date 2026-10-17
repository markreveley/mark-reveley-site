# Terminology for making harnesses swappable

This glossary supports our investigation of how a workflow can retain its
behavior and progress when we switch coding harnesses. It explains terminology
from the r/LLMDevs thread [Have coding agents made us forget ‘program to an
interface, not an implementation’?][discussion], our
[architectural analysis][analysis], and the
[planned source-report experiment][purpose]. The experiment uses a small reporting
task to compare a Claude Code procedure with a shared application.

**Aligned** means the cited source uses the term consistently with our definition.
**Qualified** identifies a scope distinction. **Local** identifies our design or
recordkeeping convention, rather than terminology imposed by a framework or
protocol. Sources checked 2026-10-17.

The discussion citations refer to the preserved paste, not a newly verified live
thread. Protocol definitions below use MCP revision `2026-07-28`; an implementation
must record the revision its SDK and hosts actually support.

## Architecture

### Harness

The software around a model that manages its working context, instructions, tool
execution, and interaction loop. A **coding harness** applies that machinery to
software work. Our **conversational harness** is the user-facing side of the
proposed split: it manages the conversation and requests application capabilities.

**Aligned, with local scope:** the [post][post] separates this harness from durable
workflow logic. [Anthropic's harness article][harness] likewise describes an agent
harness supplying tools and context management. “Harness” has no single formal
boundary here; it is broader than a chat window and distinct from the model itself.

### Baseline and proposed arrangement

The **[baseline][baseline]** is our chosen Claude Code setup: a skill and helper
scripts, with the conversational model coordinating the reporting procedure. The
**[proposed arrangement][proposal]** moves step validation, saved domain results,
and retry semantics into a shared application called through CLI or MCP adapters.

**Local comparison:** Claude Code can be the conversational harness in both.
“Traditional” describes the selected arrangement, not a claim that Claude Code
cannot host other architectures.

### Source-report task

Our example workload: read the [YAML capture of the Reddit thread][record] and
produce factual counts, participant names, and source metadata. **Local:** the
[task definition][source-report] explains why we chose it and what it produces.
We devised it to test a workflow handoff; the Reddit authors did not specify it.

### Model and agent

A **model**, or **LLM** (large language model), produces responses from supplied
context. An **agent** combines model decisions with software that executes actions
and supplies their results. An **agent loop** repeats this decision/action/result
cycle until a stopping condition. **Agentic system** is a broader label for systems
using model-directed behavior; it does not specify how autonomous they are.

**Qualified:** [Anthropic distinguishes agents from predefined workflows][agents]
by who controls the process. We reserve **inner agent** for a model-directed loop
inside a capability. An **inner model call** can be just one summary request. The
**outer model** participates in the conversational harness. Inner and outer describe
roles, not necessarily different model families or providers. Those role names are
our [local decomposition][summary-comparison].

### Subagent and inner agent

A Claude Code **subagent** performs delegated work in a harness-managed context,
with its own prompt and tool configuration. An **inner agent** in our proposal
would run inside the shared application's runtime. Both can involve model-led
work; the distinction is which system defines and operates that work.

**Qualified:** [Claude Code subagents][claude-subagents] already provide nested
model execution. Our [summary example][summary-comparison] moves ownership of the
prompt, provider call, and saved result. Its single model call is not yet an
inner loop.

### Workflow

A defined arrangement of steps, their inputs and state, and the rules for moving
between them. It can contain deterministic code, model calls, or an agent loop.
**Orchestration** is the code that coordinates those steps and their lifecycle.

**Qualified:** this investigation includes a completely deterministic workflow.
[Anthropic's article][agents] discusses workflows involving LLMs and tools;
[LangGraph's graph model][graph] allows ordinary code in nodes. Fixed control flow
does not imply deterministic model output.

### Interface and contract

An **interface**, **API** (application programming interface), or **surface** is
the set of operations callers can use. The **contract** adds their meaning:
arguments, results, errors, side effects, and retry behavior. **Implementation**
means the code that fulfills that contract. A **stable surface** preserves the
behavior callers rely on across implementation or harness changes.

**Aligned interpretation:** the [post][post] proposes a stable surface; [c08][c08]
emphasizes agreement between CLI help, tool descriptions, and documentation.
Our [operation definitions][contract] supply the concrete contract. Matching function
names alone is insufficient to establish behavioral compatibility.

### Capability and tool

An **application capability** is useful behavior provided by our system, such as
preparing a [source report][source-report]. A **tool** is an operation exposed for
invocation; one tool may implement a small action or invoke a larger workflow.
**Tool surface** means the exposed operations and descriptions; **tool layer** means the code
serving those operations and applying its checks.

**Qualified:** this matches the [post][post] and [MCP tools][tools]. MCP also uses
**capability** for declared protocol features such as support for tools; that is
a different meaning from our source-report capability. [MCP architecture][mcp]

### Seam and adapter

A **seam** is the chosen boundary between components. Here it separates the
conversation from application behavior. An **adapter**, or **wrapper**, translates
a caller's format into the shared core's operations. **Thin** means that this
adapter contains little domain logic. The **shared application core** implements
the behavior both CLI and MCP adapters invoke.

**Aligned interpretation:** [c01][c01] and [c03][c03] describe portable tools and
thin wrappers. The core's exact boundaries are our [design choice][proposal].
**Separation of concerns** means assigning these distinct responsibilities to
different components; it does not require separate machines or processes.

### Portability and harness swapping

**Portable** means the capability can be used through multiple harnesses while
preserving its contract. **Swappable** means changing the conversational harness
without rebuilding that capability. Our experiment additionally asks whether a
second harness can recover the same persisted run.

**Qualified:** the [post][post] proposes portability;
the [reproduction][reproduction] defines our narrower observable test. Neither
term guarantees identical model
choices, universal host compatibility, or automatic background execution.

## Instructions and packaging

### Prompt, instructions, prose

Text supplied to guide a model. “Skill prose” is the instructional portion of a
skill. **Aligned:** [post][post], [c08][c08]. An instruction is distinct from a
check that executing code enforces.

### Rules file

A file containing guidance loaded by a harness. `AGENTS.md`, `CLAUDE.md`,
`GEMINI.md`, and `.cursorrules` are names mentioned in the thread.
**Qualified:** [c03][c03], [c06][c06]; their discovery and interpretation are
host-specific.

### Skill

A reusable bundle of task instructions and potentially scripts, references, or
assets. **Qualified:** the thread emphasizes prose, while the [Agent Skills
format][skills] explicitly permits bundled code and resources. A skill is not
inherently prose-only or inherently tied to one harness.

### Plugin

A package of extensions installed through a host's extension mechanism. **Local
scope from the [post][post]:** it may combine skill instructions and code.
Packaging as a plugin alone says nothing about which parts can be reused
elsewhere.

### Hook

A handler triggered at a lifecycle event, such as before a tool executes.
**Aligned:** [Claude Code hooks][hooks]. A hook can run code or invoke a model;
event triggering alone does not make the handler deterministic. Our core can
define its own lifecycle callbacks.

### Symlink

A filesystem link to another path. In [c06][c06], multiple rules-file names
point to one file. **Qualified:** this shares text; it does not make every
harness interpret or enforce it identically.

### Package, distribution, dependency

A package groups installable code/resources; distribution gets it to users; a
dependency is another package it requires. **Local application:** install the
common core and adapters together, as contemplated by the [post][post] and
[build plan][reproduction].

### SDK and framework

An SDK is a software development kit for an API or protocol. A framework
supplies reusable structures for building applications. **Aligned examples:**
[the MCP SDK][sdk] implements protocol machinery; [LangGraph][graph] supplies
graph structures. Neither term implies an installed or tested dependency here.

### Version pinning

Recording and selecting an exact dependency release, source revision, or
configuration version. **Local:** [working instructions][instructions]. A link
to a mutable repository branch is a reference, not a version pin.

### Provider and model version

The service or local backend executing inference, and the particular model
configuration it runs. **Local:** the [later model step][model-step] records
these separately from prompt and workflow versions.

### Frontier model

An informal label for models considered near the leading edge of capability.
**Source usage:** the [post][post] supplies no measurable threshold; it is not a
requirement for this reproduction.

## Protocol and user interfaces

### MCP

Model Context Protocol, the communication standard between an AI application's
client and servers exposing tools or context. **Aligned:** [MCP
architecture][mcp]. Our workflow semantics and persistence are application
responsibilities.

### MCP host

The AI application managing MCP clients; in our design, the conversational
harness plays this role. **Aligned:** [MCP architecture][mcp]. “Host” here names
a protocol role, not necessarily a network machine.

### MCP client

The host-side component that communicates with a server. **Aligned:** [MCP
architecture][mcp]. The model itself is not the client implementation.

### MCP server

A program offering MCP features to clients, locally or remotely. **Aligned:**
[MCP architecture][mcp]. Our adapter exposes the shared core as tools.

### Protocol and transport

A protocol defines message rules; a transport carries the messages. **Aligned:**
[MCP transport overview][transports]. These are separate from the application
contract.

### stdio, stdin, stdout, stderr

Standard process streams: input, output, and diagnostic output. MCP stdio
communicates with a subprocess over stdin/stdout; diagnostics can use stderr.
**Aligned:** [stdio specification][stdio]. Keep ordinary log text off protocol
stdout.

### Streamable HTTP

MCP's HTTP transport option. **Aligned:** [transport overview][transports]. It
is an alternative transport, deferred in the local reproduction.

### JSON-RPC

The request/response message format used by MCP. **Aligned:** [transport
overview][transports]. Its request ID correlates an exchange; our durable
`request_key` has a separate application purpose.

### Tool discovery and invocation

Finding available tools with `tools/list`, and calling one with `tools/call`.
**Aligned:** [MCP tools][tools]. `start_run` and `advance_run` are our tool
names, not protocol methods.

### Schema and validation

A schema describes data structure and constraints; validation checks data
against them. MCP tool arguments use JSON Schema. **Aligned:** [MCP
tools][tools]. Domain checks, such as whether a source is allowed, require
additional application logic.

### Payload and envelope

A payload is the useful application data; an envelope wraps it with response or
protocol metadata. **Local:** our `{ok, result/error}` shape is defined in the
[contract][contract], not mandated by MCP.

### CLI, TUI, IDE

Command-line interface, text user interface, and integrated development
environment. Here: a command producing JSON, an interactive terminal
application, and an editor/development host. **Context:** the discussion's
[CLI/TUI][c09] and [IDE adapters][c03].

### Shell and exit status

A shell launches commands; an exit status is the process's numeric
success/failure signal. **Local:** the [CLI plan][contract] uses JSON output
plus a nonzero status on failure. Shell access is a separate route to resources
from our MCP tools.

## Execution and stored state

### Runtime

Software executing work and managing its lifecycle. **Aligned:**
[Switchplane][switchplane] runs application-defined tasks. A runtime can sit
inside a harness or behind an interface.

### Graph, node, edge

A graph connects units of work; a node performs computation; an edge determines
subsequent execution. **Aligned:** [LangGraph graph API][graph]. Nodes may
contain ordinary code or model calls.

### Step and transition

A step is one unit of our workflow; a transition changes its recorded progress.
**Local:** “prepare” and “render” are the two steps in the [storage
design][storage]. They do not require LangGraph.

### State

Data describing work at a point in time, such as saved facts and the next step.
**Aligned concept:** [LangGraph][graph]. Our particular fields are defined in
the [run record][storage].

### Run, task, run ID

A run is one workflow instance, identified by `run_id`. **Local:** [storage
design][storage]. Switchplane's durable task and task ID are analogous concepts,
not shared identifier formats. [Switchplane][switchplane]

### Conversation, session, thread

A conversation/session is the outer interaction; a Reddit thread is source
material. A LangGraph thread groups checkpointed graph state. **Qualified:**
[LangGraph persistence][persistence]. These differ from our run ID.

The [recovery comparison][recovery-comparison] distinguishes resuming a harness
conversation from resuming an application run. The proposed design can retain
both kinds of state.

### Persistence and durable state

Keeping data after its producing process exits. **Qualified:** [LangGraph
persistence][persistence] distinguishes persistent backends from in-memory
storage. Here, durable means surviving process restart, not arbitrary storage
failure.

### Checkpoint and checkpointer

A checkpoint is saved execution state usable as a recovery point; a checkpointer
is the component saving/loading it. **Aligned:** [LangGraph
persistence][persistence]. Our SQLite step records serve that purpose without
implementing LangGraph's checkpoint format.

**Different scope:** Claude Code's [file checkpointing][claude-checkpoints]
supports rewinding certain edits. Our checkpoint records completed application
work and its result; the word alone does not imply the same recovery behavior.

### Store and backend

“Store” here generically means a persistence location; “backend” is its
implementation. **Qualified:** LangGraph's named Store is specifically for data
outside thread-scoped graph checkpoints. Our SQLite database is not
automatically a LangGraph Store. [Persistence documentation][persistence]

### In-memory

Held in process memory rather than restart-persistent storage. **Aligned:**
[LangGraph persistence][persistence]; an in-memory checkpointer loses its
checkpoints when its process exits.

### Retry

Attempting an operation again, including after an uncertain response.
**Aligned:** [AWS idempotency guidance][idempotency]. A retry can be a new
attempt, a replay of saved results, or a resumed computation depending on the
contract.

### Resume and recovery

Resume continues from retained progress. Recovery is the broader procedure for
restoring useful operation after interruption; it may resume or restart.
**Qualified:** [Switchplane recovery][switchplane] requires explicit retry and
checkpoint-aware task code. The [author's later setup][c11] does not specify its
exact resume semantics.

### Process, subprocess, worker

A process is a running program instance; a subprocess is launched by another
process, as in [MCP stdio][stdio]. A worker executes assigned work. **Local
scope:** the [model and worker extension plan][model-step] treats separately
supervised workers as a later experiment.

### Daemon and supervisor

A daemon is a background service; a supervisor manages worker lifecycles.
**Context:** [Switchplane][switchplane]. Exposing MCP tools does not
automatically supply either.

### Continued execution and automatic recovery

Continued execution means work keeps running after the client disconnects.
Automatic recovery means interrupted work is restarted/resumed without a new
user request. **Local distinction:** see
[process lifetime and restart][process-lifetime] and [c11][c11]. The planned
prototype is intended to demonstrate explicit resume only.

## Correctness and authority

### Deterministic and nondeterministic

Deterministic logic gives the same relevant result for the same inputs and
relevant state; nondeterministic behavior can vary. **Local scope consistent
with [c09][c09]:** repeatable code transitions do not imply repeatable model
output or concurrent timing.

### Side effect

A change beyond a returned value, such as storing a run, writing a file, or
submitting a remote request. **Aligned:** [AWS retry guidance][idempotency]. Our
contract must say which effects a retry may repeat.

### Idempotency

Repeating the same logical request causes no additional intended effect.
**Aligned:** [AWS guidance][idempotency]. It does not mean code executes only
once, or require every response byte to be identical. Our contract separately
promises stored receipts for completed steps.

### Duplicate request and idempotency key

A repeated attempt at the same intended operation, and the caller-provided
identifier used to recognize it. **Aligned:** [AWS guidance][idempotency]. Equal
parameters alone need not mean the caller intended only one operation.

### Transaction, commit, rollback

A transaction groups database operations; commit accepts its changes; rollback
abandons them. **Aligned:** [SQLite transaction documentation][transactions]. A
filesystem write or external API call does not join that transaction
automatically.

### Atomicity

The transaction's changes appear as a complete unit or not at all. **Aligned:**
[SQLite atomic commit][atomicity]. Our proposed unit contains the result, step
receipt, progress update, and event.

### Concurrency and serialization

Concurrency means operations overlap; serialization orders conflicting work so
shared state is handled consistently. **Aligned:** SQLite permits only one
simultaneous write transaction. Our read/check/update sequence must be protected
as a unit. [SQLite transactions][transactions]

### Transactional outbox

Store an intended outgoing message alongside the state update in one
transaction, then deliver it separately. **Aligned:** [AWS outbox
pattern][outbox]. Delivery can repeat, so the recipient still needs duplicate
handling. Deferred in this prototype.

### Work ownership

A rule determining which worker may perform a step, and when another may take
over. **Local requirement:** [model-step plan][model-step]. The implementation
and recovery mechanism have not been selected.

### Policy, permission, enforcement

A policy is a rule; a permission grants an action; enforcement checks and
allows/refuses it in executing code. **Qualified:** [c05][c05], [c08][c08]. A
tool's refusal governs that route, not every other route the harness possesses.

### Allowlist and authority boundary

An allowlist enumerates permitted resources/actions. The authority boundary is
the scope within which the component controls access. **Local:** our [source-ID
allowlist][contract] constrains these operations; it does not remove the
harness's separate shell access.

### Authentication, authorization, credentials

Authentication establishes identity; authorization determines access;
credentials provide evidence used in those checks. **Qualified:** MCP's
[authorization specification][authorization] addresses HTTP access; stdio
credentials and application resource checks are separate concerns. “Auth” in
[c02][c02] is underspecified.

### Sandbox

An enforced environment restricting what executing code can access.
**Qualified:** [Switchplane explicitly says its task processes are not security
sandboxes][switchplane]. A subprocess, prompt rule, or local server is not by
itself such a boundary.

### Protected branch and main

`main` is a conventional Git branch name. Protection means actual restrictions
on operations involving a branch. **Source usage:** [c05][c05] gives “never push
to main” as an instruction; that text alone establishes no enforced protection.

## Observation and verification

### Observability

Understanding system behavior through emitted evidence such as logs, metrics,
and traces. **Aligned:** [Langfuse][langfuse]. It helps explain execution but
does not itself save recoverable workflow state.

### Trace and tracing

A trace relates operations within a request or workflow, often with timing,
inputs, and outputs; tracing records those relationships. **Aligned:**
[Langfuse][langfuse]. A trace is different from a checkpoint.

### Event, log, audit event

An event records an occurrence; a log collects records; an audit event records a
relevant action or refusal. **Local:** [the prototype][storage] persists ordered
events. This is not a claim of a tamper-proof audit system or complete tracing
coverage.

### Fixture

Fixed input used to exercise the implementation. **Local:** the
[source-report plan][source-report] uses a temporary copy of the
[Reddit thread's YAML capture][record].

### Contract test and acceptance check

A contract test exercises promised operation behavior across adapters; an
acceptance check establishes a required observable outcome. **Local:**
[acceptance checks][acceptance]. Expected outcomes become results only after
execution.

### Reproduction

A small implementation that tests the proposed architectural mechanism.
**Local:** [build plan][reproduction]. It is not a claim to recreate the
author's unpublished system or reproduce every product feature.

### Artifact

A retained output, such as a report, saved receipt, draft, or experiment result.
**Local:** [investigation record][manifest]. A diagnostic artifact is not
necessarily executable state.

## Prototype identifiers and data

All names in this section are **local conventions** defined by the
[reproduction contract][contract] and [storage design][storage]. They are not
MCP or LangGraph field requirements.

### `source_id`

The allowlisted identity of an input source. It selects a source without
accepting arbitrary file paths.

### `source_snapshot`

The immutable source bytes captured when the run is created. Later source edits
do not change this run's input.

### `source_sha256`, source hash

A SHA-256 digest identifying the captured bytes for comparison. This establishes
byte identity for the test, not truth or authorship of the content.

### `request_key`

The idempotency key for [start_run][start-run]. Reuse with the same source returns
its existing run and snapshot; reuse with another source is a conflict.

### `run_id`

The identity used to retrieve or advance one persisted workflow instance,
independent of a conversation or process.

### `expected_step` and `next_step`

The step the caller requests and the next step the stored run expects. Their
comparison in [advance_run][advance-run] prevents a repeated request from
accidentally advancing additional work.

### Step receipt

The saved result of a completed step, retrieved by `(run_id, step_number)` on a
repeated request. It is our application record, not a protocol acknowledgment.

### `workflow_version`

The recorded version of the workflow's meaning and behavior. Storing it does not
itself implement migration between versions.

### Error code

A machine-readable category such as `unknown_source`, `unknown_run`,
`request_conflict`, or `step_mismatch`; the accompanying message explains the
particular failure. See the [response conventions][responses].

## Source records

These are **local editorial conventions** from the [investigations guide][guide]
and [discussion record][record].

### YAML and JSON

Structured text data formats. YAML holds our source and investigation records;
JSON carries the proposed CLI responses and protocol data. A data format is
separate from a schema defining permitted fields.

### Raw capture

The [original supplied paste][raw], retained unchanged, including interface noise.

### Structured record and canonical source

The [normalized YAML record][record] used to regenerate the
[readable transcript][discussion].
“Canonical” identifies our maintained copy; it does not certify the source's
claims.

### Metadata and provenance

Metadata describes content, such as author and captured age. Provenance records
where it came from and what transformations or checks were applied.

### Local ID and source locator

[post][post] and [c01][c01]–[c11][c11] identify entries in this capture. They are not
platform-issued Reddit comment IDs.

### Claim, evidence, hypothesis

A claim asserts something; evidence bears on that assertion; a hypothesis is a
tentative explanation to test. A comment is evidence of an author's account, not
proof that the described implementation works.

### Verification and consistency

Verification records a particular check. Terminological consistency means our
meaning agrees with the cited usage in the stated scope; it does not validate
the prototype or every claim in the source.

## Named systems in the discussion

### Cursor, Claude Code, Codex, pi, opencode

Examples the [post][post] gives of coding harnesses. Their inclusion does not
establish tested compatibility with our proposed tools.

### LangGraph

A library for stateful workflows built from graphs, nodes, and edges. [Graph
API][graph]

### Switchplane

The author's local workflow runtime; see [runtime and recovery
terminology](#execution-and-stored-state). The author distinguishes it from the
later conversational split. [c09][c09], [c11][c11]

### Langfuse

The observability product named in the post, relevant here for application
tracing. [Product documentation][langfuse]

### Kin and Festival

Projects mentioned by commenters in [c08][c08] and [c07][c07]. Treat their
described capabilities as commenter accounts; this investigation has not
inspected their implementations.

[post]: reddit-post-program-interface.md#post
[c01]: reddit-post-program-interface.md#c01
[c02]: reddit-post-program-interface.md#c02
[c03]: reddit-post-program-interface.md#c03
[c05]: reddit-post-program-interface.md#c05
[c06]: reddit-post-program-interface.md#c06
[c07]: reddit-post-program-interface.md#c07
[c08]: reddit-post-program-interface.md#c08
[c09]: reddit-post-program-interface.md#c09
[c11]: reddit-post-program-interface.md#c11
[analysis]: analysis.md
[discussion]: reddit-post-program-interface.md
[raw]: sources/raw/reddit-post-program-interface.txt
[purpose]: reproduction.md#purpose-of-the-experiment
[source-report]: reproduction.md#source-report-task
[baseline]: analysis.md#the-baseline-in-claude-code
[proposal]: analysis.md#the-proposed-arrangement
[summary-comparison]: analysis.md#follow-the-same-model-assisted-task-through-both-arrangements
[recovery-comparison]: analysis.md#conversation-recovery-and-application-recovery
[process-lifetime]: analysis.md#process-lifetime-and-restart
[reproduction]: reproduction.md
[contract]: reproduction.md#define-the-contract-before-the-adapters
[start-run]: reproduction.md#start_run
[advance-run]: reproduction.md#advance_run
[responses]: reproduction.md#response-conventions
[storage]: reproduction.md#store-enough-state-to-recover
[model-step]: reproduction.md#add-a-model-inside-the-capability
[acceptance]: reproduction.md#acceptance-checks
[instructions]: instructions.md
[manifest]: investigation.yaml
[guide]: ../README.md
[record]: sources/reddit-program-interface.yaml
[harness]: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
[claude-subagents]: https://code.claude.com/docs/en/sub-agents
[claude-checkpoints]: https://code.claude.com/docs/en/checkpointing
[agents]: https://www.anthropic.com/engineering/building-effective-agents
[mcp]: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
[tools]: https://modelcontextprotocol.io/specification/2026-07-28/server/tools
[transports]: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports
[stdio]: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio
[authorization]: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
[sdk]: https://github.com/modelcontextprotocol/python-sdk
[skills]: https://agentskills.io/home
[hooks]: https://code.claude.com/docs/en/hooks
[graph]: https://docs.langchain.com/oss/python/langgraph/graph-api
[persistence]: https://docs.langchain.com/oss/python/langgraph/persistence
[switchplane]: https://github.com/salesforce-misc/switchplane#runtime-model
[transactions]: https://www.sqlite.org/lang_transaction.html
[atomicity]: https://www.sqlite.org/atomiccommit.html
[idempotency]: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
[outbox]: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
[langfuse]: https://langfuse.com/docs/observability/overview
