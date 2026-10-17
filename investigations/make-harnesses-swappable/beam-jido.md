# Applying harness portability to BEAM, Elixir, and Jido

This is an optional architectural companion and research spike. Start with
[README.md](README.md) for the investigation's question and current assessment.
The main argument is in [analysis.md](analysis.md); this document asks how an
Elixir application could implement it, where Jido fits, and whether retaining a
coding harness such as Claude Code would still be useful.

**Assessment, checked 2026-10-17:** BEAM and OTP provide useful machinery for
running and supervising independent work. Jido adds agent abstractions and an
optional model loop. Neither automatically supplies the durable application
contract that makes work portable. A Jido application can also delegate a
bounded coding task to an existing harness. There is already a Jido ecosystem
project for that composition, and related work outside Elixir. MCP's published
2026-07-28 revision strengthens the case for explicit application identifiers
and recovery rules by removing implicit protocol sessions.

The evidence here is documentation, specifications, repository documentation,
selected package metadata, and a research-paper abstract. No Elixir application,
Jido integration, failure test, or coding benchmark was run. Proposed designs
and examples below are ours; they are not claims about the Reddit author's
unpublished implementation. Source provenance and open checks are recorded in
[investigation.yaml](investigation.yaml).

## Reading route

Read this document in order: first the runtime foundations, then Jido's role,
then harness composition, related work, and MCP's protocol changes. The final
section proposes experiments. Use [definitions.md](definitions.md) for unfamiliar
terms. This is an optional branch after [analysis.md](analysis.md), not a
replacement for the source-order [claim-analysis.md](claim-analysis.md).

## Start with BEAM and Elixir

### The application contract comes first

The source discussion proposes moving reusable behavior behind a stable
interface. In Elixir, that can begin with ordinary modules and functions. The
reporting example in
[reproduction.md — Source-report task](reproduction.md#source-report-task)
could expose `start_run`, `advance_run`, `get_run`, `list_runs`, and
`get_events`. CLI, HTTP, and MCP adapters would call that same application API.

The API's meaning matters more than its transport: starting a run snapshots the
input; advancing it checks the expected step; retrying a committed step returns
its recorded result. Those are application rules. An MCP schema can describe
the arguments without implementing those rules. See
[definitions.md — Interface and contract](definitions.md#interface-and-contract).

Elixir behaviours can describe callbacks for replaceable internal components:
for example, a coding-worker adapter or storage implementation. They help make
the expected interface explicit. They do not establish that two implementations
have equivalent cancellation, persistence, or output semantics; those need
contract checks. The language's
[behaviour documentation](https://elixir.hexdocs.pm/typespecs.html#behaviours)
describes the callback mechanism.

This separation is available without Jido. It is also available without a
long-running process. Introduce processes where the application needs concurrent
work, lifecycle management, or owned live state. Elixir's
[GenServer guidance](https://elixir.hexdocs.pm/GenServer.html)
explicitly distinguishes these needs from organizing code into modules.

### What OTP contributes

BEAM is the runtime used by Erlang and Elixir. Its lightweight processes
exchange messages and isolate failures. OTP, the Open Telecom Platform,
supplies standard patterns for building applications from those processes. In
the proposed design, their roles could be:

- A `GenServer` coordinates an active run and serializes messages it handles.
- A `DynamicSupervisor` starts and supervises workers as runs become active.
- A registry maps a stable application identity to the current local process.
- Tasks perform bounded concurrent operations.
- `:gen_statem` is an option when explicit states, events, and timeouts make the
  workflow clearer than a general server callback.

These are design choices, not requirements to put every function in a process.
The relevant mechanisms are documented in
[GenServer](https://elixir.hexdocs.pm/GenServer.html),
[DynamicSupervisor](https://elixir.hexdocs.pm/DynamicSupervisor.html), and
[gen_statem](https://www.erlang.org/doc/apps/stdlib/gen_statem.html).

A process per active run is a plausible implementation. A process per historical
run is usually unnecessary: a completed report can be read from storage without
reviving its worker. A domain run ID must also remain meaningful after the
worker's process identifier, or PID, changes. These are our application design
recommendations, rather than guarantees attached to an OTP process.

### Supervision and durable recovery are separate mechanisms

An OTP supervisor can start a replacement child according to its restart policy.
The child starts through its initialization path. That does not, by itself,
restore the dead process's memory or determine whether its last external action
completed. See the
[Supervisor documentation](https://elixir.hexdocs.pm/Supervisor.html).

For our reporting task, the database would be authoritative. The replacement
worker loads the saved run, checks the committed step receipts, and continues
from the next permitted transition. A receipt records that a particular step's
result was committed. The first reproduction specifies an atomic transaction
for the result, receipt, progress update, and event in
[reproduction.md — Store enough state to recover](reproduction.md#store-enough-state-to-recover).

There are several distinct failure boundaries:

- Losing the chat should not lose an accepted application run.
- Losing a worker should allow a replacement to reconstruct committed state.
- Losing the BEAM VM loses its in-memory processes and Erlang Term Storage
  (ETS) tables; persistent storage and a way to restart the service are separate
  requirements.
- Losing the machine requires recovery appropriate to the database and
  deployment. An OTP restart policy alone does not provide it.

An independent application service can keep working after a chat closes. A BEAM
VM launched as that chat's stdio child has a different lifetime. Keeping a local
adapter small and connecting it to a separately managed service is one possible
design when continued execution is required. The protocol's subprocess model is
described in the
[MCP stdio specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio).

For external effects, a database transaction is only part of the solution. If a
model provider finishes a paid request and the worker dies before saving its
response, retrying may pay again. If a worker pushes a commit and loses the
acknowledgement, replaying the operation may encounter an already changed
remote. Use provider idempotency where available, record operation identities,
and reconcile uncertain outcomes. Combining a supervisor with a database gives
no general exactly-once guarantee. The rationale is developed in
[AWS's idempotent API guidance](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).

### Concurrency still needs application rules

One process can serialize the commands it receives. That does not protect a
shared repository from a second worker, another node, or a human editor. Our
design would use isolated workspaces and database constraints on accepted
transitions. If multiple nodes can take over the same job, it also needs an
ownership mechanism that prevents an old worker from committing after a new
worker has taken over.

Oban is an optional complement when persisted job scheduling, delayed work, and
retries are needed. Its documentation describes database-backed jobs and
transactional insertion; its uniqueness feature governs job insertion rather
than proving that an external effect executes once.
[Oban](https://oban.hexdocs.pm/Oban.html),
[Unique Jobs](https://oban.hexdocs.pm/unique_jobs.html)

Use one explicit owner for each retry decision. Adding Oban, Jido, and a harness
that all independently retry the same coding task would make duplicate work
harder to explain. A reasonable split is a persisted job owning an attempt,
Jido coordinating its lifecycle, and the coding harness controlling edits
within that attempt. Whether all three are useful is an experiment question.

## Narrowing to Jido 2

### Jido's agent abstraction is broader than an LLM loop

Jido core represents an agent as an immutable structure with state. An action
performs work; a signal is an incoming message; a directive describes an effect
for the runtime to carry out, such as spawning a worker. `cmd/2` returns the
updated agent and directives. `AgentServer` holds live state, routes signals,
and executes directives. This can organize ordinary application behavior
without involving a language model.
[Jido core loop](https://jido.hexdocs.pm/core-loop.html),
[Jido runtime](https://jido.hexdocs.pm/runtime.html)

This is a terminology qualification. In the main investigation, an agent means
a model-directed loop. A Jido agent can be a deterministic stateful component.
The distinction is recorded in
[definitions.md — Model and agent](definitions.md#model-and-agent).

The explicit state transition style also does not mean every action is free of
side effects. Actions can perform I/O. An action that changes a file or calls a
provider still needs the corresponding retry and recovery design.
[Jido Action](https://github.com/agentjido/jido_action)

Jido.AI adds model integration and reasoning/tool-use strategies, including
ReAct, which alternates model reasoning and tool actions. That gives an Elixir
application a way to own its prompts, tool selection, context, and stopping
conditions. It is an optional layer over the core agent abstraction.
[Jido.AI](https://github.com/agentjido/jido_ai)

For the deterministic source-report task, Jido.AI is unnecessary. For the later
summary step, a single model call might suffice. A full inner agent is justified
only if the capability needs repeated model decisions, as discussed in
[analysis.md — Follow the same model-assisted task through both arrangements](analysis.md#follow-the-same-model-assisted-task-through-both-arrangements).

### Jido offers persistence mechanisms with specific boundaries

Jido documents checkpoint and thread-journal storage through `Jido.Persist`.
Its storage guide distinguishes the default ephemeral ETS backend from other
backends, and describes hibernation and restoration. Selecting a persistent
backend is consequential; using an agent process alone does not establish
restart durability.
[Jido storage](https://jido.hexdocs.pm/storage.html),
[Jido.Persist](https://jido.hexdocs.pm/Jido.Persist.html)

`Jido.Agent.InstanceManager` manages instances by a stable key, can restore a
stored instance, and can hibernate idle instances. Its documentation describes
error handling when restoration fails rather than silently treating every
failure as a new instance.
[InstanceManager](https://jido.hexdocs.pm/Jido.Agent.InstanceManager.html)

Our application still has to decide what an acknowledgement means. A checkpoint
on idle hibernation is different from committing every accepted business
transition before responding. A documented journal write followed by a
checkpoint write is not evidence that our report result, step receipt, and
domain event share one atomic transaction. We would verify the chosen backend
and write path against the contract in
[reproduction.md — Store enough state to recover](reproduction.md#store-enough-state-to-recover).

Jido's logical agent relationships also should not be mistaken for a complete
storage or OTP recovery policy. The runtime guide distinguishes logical parent
relationships from supervision and identifies the machinery needed for managed
persistence. Our evidence is that these mechanisms are documented; we have not
tested their behavior under crashes.
[Jido runtime](https://jido.hexdocs.pm/runtime.html)

### Is Jido a modular harness?

**In the broad sense, Jido and Jido.AI can be the components of one.** They
provide ways to represent agent state, run actions, and execute a model/tool
loop. Jido also serves a broader application role: it can coordinate
deterministic workers, external services, and agents supplied by other runtimes.

There is no identified BEAM limitation that prevents implementing repository
search, file editing, context selection, compaction, delegation, or a coding
loop. That is different from having an equivalent implementation already built,
tested, and maintained. A general toolkit leaves choices about prompts, tool
behavior, error recovery, permissions, and evaluation to the application.

The useful answer to “what can't Jido implement?” has three parts:

- **Mechanisms we could build:** most harness machinery is application software.
  Jido can host it, subject to engineering effort and integration limits.
- **Assets it does not supply:** a framework does not reproduce a model's
  trained behavior, private provider internals, or an unavailable product API.
  Calling the same model does not establish identical agent behavior.
- **Properties it does not guarantee:** coding quality, safe external retries,
  durable business transactions, and compatibility with every harness feature
  require implementation choices and evidence.

Thus “we can build a harness with Jido” is credible. “Jido already replaces
every valuable part of Claude Code” is not established by the materials
inspected.

## Why retain Claude Code inside a Jido application?

### Preserve an integrated coding implementation

Claude Code packages a coding loop with tools and context management. Retaining
it can preserve that working implementation while an Elixir application owns
the larger job. Which configuration, skills, hooks, and session features remain
available depends on the integration mode.
[How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)

Anthropic's Agent SDK explicitly exposes the Claude Code agent loop for
applications. The official SDKs are for Python and TypeScript; the CLI provides
a subprocess integration route for other languages. The programmatic interface
documents structured and streaming output and session continuation.
[Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview),
[Run Claude Code programmatically](https://code.claude.com/docs/en/headless)

The potential advantage is reuse: the application can concentrate on task
intake, durable records, acceptance checks, and coordination while adopting an
existing coding implementation. The tradeoff is dependency on the harness's
runtime, configuration, provider access, and exposed controls. We have not
measured whether this is better than a Jido.AI implementation for any workload.

There is research support for treating the tool interface as substantive.
Yang and colleagues' *SWE-agent* paper investigates how the agent-computer
interface affects coding behavior and performance. That motivates testing the
harness as part of the system; it does not establish a ranking between Claude
Code and Jido. This spike inspected the abstract, not the paper's experimental
artifacts.
[SWE-agent paper](https://arxiv.org/abs/2405.15793)

### There are two directions across the interface

The original investigation emphasizes a harness calling a shared application:

```text
Claude Code -> MCP adapter -> Elixir/Jido capability -> saved domain results
```

The application can also invoke a coding harness:

```text
Elixir/Jido job -> coding-worker adapter -> Claude Code -> workspace changes
```

The first makes the application usable from different conversational hosts. The
second makes a coding implementation replaceable within an application. These
are different contracts, even if one system supports both. The original source's
interface analogy leaves room for this distinction; see
[claim-analysis.md](claim-analysis.md).

An internal Elixir function call does not need MCP. MCP is appropriate when
exposing capabilities to MCP clients or consuming external MCP tools. An
application controlling a coding agent may instead use that agent's CLI, SDK,
or the Agent Client Protocol, ACP. ACP standardizes communication between coding
clients and agents, including agent sessions and interaction events. It is a
different protocol from MCP, even where representations are reused.
[ACP introduction](https://agentclientprotocol.com/get-started/introduction)

These directions may coexist: a human-facing harness requests a job from Jido,
and Jido delegates a bounded subtask to a worker harness. Our design would keep
the delegation explicit. An inner worker should not recursively ask the same
outer application to start an indistinguishable copy of its own job.

### Jido.Harness is a direct implementation lead

The research found `agentjido/jido_harness`, which supplies a common Elixir
interface to external coding agents. Its current main-branch documentation
describes supervised runs and event handling. It explicitly distinguishes
surviving the calling process from surviving a BEAM VM or host restart; the
latter durability is outside its runtime's guarantee.
[Jido.Harness README](https://raw.githubusercontent.com/agentjido/jido_harness/main/README.md)

Version names need care. The inspected `mix.exs` identifies Jido.Harness as
`3.0.0-rc.1`, with an ExMCP dependency and no direct `jido` dependency. This is
a separately versioned library; Jido core remains on its own version line.
Jido core pages inspected during this spike displayed different 2.3.x and
2.4.0 versions. No single compatible dependency set was installed or resolved.
[Jido.Harness package metadata](https://raw.githubusercontent.com/agentjido/jido_harness/main/mix.exs)

The current provider guide uses ACP through ExMCP, including a Claude ACP
adapter. Here ExMCP supplies the ACP integration for controlling the agent.
This requires the corresponding provider runtime, authentication, and adapter.
Profiles expose different capabilities; the current guide lists no steering
(new guidance during an active turn) and no structured-output support for its
built-in ACP profiles. An underlying CLI may offer a feature that this adapter
does not expose.
[Jido.Harness providers](https://raw.githubusercontent.com/agentjido/jido_harness/main/guides/providers.md)

Its architecture guide assigns workspaces, durable job records, provider
selection, and retry policy to the host application. That is close to the split
we are considering. The older `jido_claude` repository points users toward
Jido.Harness and marks itself deprecated.
[Jido.Harness architecture](https://raw.githubusercontent.com/agentjido/jido_harness/main/guides/reference/architecture.md),
[Jido Claude](https://github.com/agentjido/jido_claude)

For the opposite direction, `jido_mcp` documents both consuming MCP servers and
publishing Jido actions as tools. Its examples mention older protocol revisions;
they do not establish support for the 2026-07-28 changes discussed below.
[Jido MCP](https://github.com/agentjido/jido_mcp)

These are implementation leads, not verified integrations. Main-branch links
can change. A spike that runs code must pin the library, provider adapter, CLI,
and negotiated protocol revisions together.

## A concrete application design

### Compare the same coding task in three arrangements

**Illustration:** a task asks for a fix to one failing test in a repository at a
specified base revision. Success means the expected behavior passes
independently run checks and the resulting patch is available for review.

In a **standalone Claude Code arrangement**, the user supplies the task and
workspace. Claude Code investigates, edits, runs checks, and reports its result.
Existing scripts, hooks, and saved sessions may support repeatability and
recovery. The baseline must record those capabilities before comparison; see
[analysis.md — The baseline in Claude Code](analysis.md#the-baseline-in-claude-code).

In a **Jido-native arrangement**, the application accepts a job, creates a
workspace, and uses Jido.AI plus chosen tools to perform the coding loop. The
application authors own that loop's context policy and tool behavior. They also
own the job history, acceptance checks, and recovery rules.

In a **Jido plus Claude Code arrangement**, the application owns the same outer
job but delegates the bounded investigation/edit/test loop to Claude Code. A
worker adapter translates the application's task and events into the selected
harness interface. Jido receives artifacts and independently evaluates the
acceptance conditions.

What changes in the hybrid is ownership of the outer job. Claude Code can retain
its coding strategy; the application decides when an attempt starts, what inputs
it receives, whether its output satisfies the task, and what happens next. The
same base revision, requested fix, and acceptance checks should be used in all
three arrangements. Prompt, model, tool, or configuration differences must be
recorded rather than attributed to the architecture.

### Proposed components and responsibilities

The proposed application divides responsibilities as follows:

1. **Domain API:** accepts a task and caller request key, validates scope, and
   returns a durable job ID. Exposes status, artifacts, and cancellation.
2. **Persistent records:** store task inputs, base revision, policy and workflow
   versions, attempts, accepted transitions, approvals, and results.
3. **Coordinator:** an OTP/Jido component advances the job through explicit
   states and decides whether an attempt may start or be retried.
4. **Workspace manager:** prepares isolated workspaces and prevents concurrent
   writers from unintentionally sharing one checkout.
5. **Coding-worker behaviour:** provides the common task/result interface, with
   explicit capabilities for continuation, cancellation, approvals, and output.
6. **Worker implementations:** initially one Jido.AI implementation or one
   Jido.Harness/Claude Code implementation. A second tests substitutability.
7. **Acceptance stage:** runs the prescribed checks and saves the patch, logs,
   test evidence, and decision. A worker's statement that it succeeded is input
   to that decision, not the decision itself.
8. **Caller adapters:** CLI, HTTP, or MCP surfaces that request domain
   operations and return the application's saved state.

Avoid a provider interface that promises features some implementations cannot
perform. The common contract can require a bounded task and artifact result,
while advertising optional capabilities. If continuation is unavailable, the
application can start a fresh attempt from saved artifacts and label it as such.

### Keep the different identities separate

The proposed records distinguish:

- **Domain job ID:** the user's task across retries and harness replacements.
- **Attempt ID:** one authorized execution of that job with a particular worker.
- **Library run ID:** Jido.Harness's identity for a live or retained run.
- **Harness session ID:** a provider-specific conversation that may be resumable
  by that provider.
- **PID:** the current process, replaceable when it exits.
- **JSON-RPC ID:** correlation for one protocol exchange.
- **MCP task ID:** an optional handle for the protocol's asynchronous task view.

These identifiers may be mapped, but they have different lifetimes and
guarantees. A new RPC ID on a retry should not create a new domain job when the
caller supplies the original idempotency key. A new worker PID should not erase
the job. A new provider may be unable to read the previous provider's session.

The portable record should therefore include the task, inputs, accepted patch,
checks, decisions, and remaining work. Preserving those artifacts does not
preserve another harness's hidden context or reproduce its next decision. Our
claim of portability should say whether it covers starting a fresh attempt,
continuing a provider session, or resuming a committed workflow step.

### Make authority and cancellation explicit

The application should enforce job scope where it has actual control: supplied
credentials, filesystem access, workspace ownership, permitted operations, and
transition validation. A prompt instructing a shell-capable worker to stay in
scope does not itself create a sandbox. Existing harness permissions can remain
part of the implementation; see
[analysis.md — Instructions and enforced restrictions](analysis.md#instructions-and-enforced-restrictions).

The coordinator can own retry budgets and publication approval while the inner
worker chooses the next file to inspect. This avoids two components both
believing they control the same decision. Approval records should identify the
specific proposed action and inputs so they are not silently reused after the
task changes.

Cancellation needs intermediate state. For example, record `cancel_requested`,
ask the worker to stop, then record the observed outcome. A process that ignores
the request, a tool that already changed a file, and a completed provider call
are different cases. Neither terminating a process nor closing a connection
undoes prior effects. The application must reconcile an uncertain attempt before
starting a potentially conflicting replacement.

## Research spike: is this an active frontier?

### Scope and evidence standard

This was a targeted primary-source review, checked 2026-10-17. We looked for
three things: Elixir libraries composing external coding agents, separation of
coding engines from application orchestration, and protocols or runtimes making
that boundary explicit. It is not a comprehensive ecosystem survey or an
adoption study. Documentation demonstrates stated interfaces and intended
responsibilities; it does not establish reliability in our deployment.

### Direct evidence and adjacent work

**Jido.Harness is the closest match.** The sources examined in
[beam-jido.md — Jido.Harness is a direct implementation lead](#jidoharness-is-a-direct-implementation-lead)
describe an Elixir application supervising external coding agents while
retaining ownership of durable jobs and workspaces. The project offers a
concrete integration to test.

**Anthropic exposes its coding engine for embedding.** The
[Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
supports the proposition that preserving a harness inside another application
is a supported integration direction. It does not prove that all interactive
product behavior is available through every wrapper.

**OpenHands separates execution from automation.** Its SDK repository assigns
agents, conversations, tools, workspaces, and an Agent Server to the execution
layer. It assigns scheduling, webhooks, run history, and dispatch to a separate
automation project. That is a close architectural analogue to an application
owning jobs and delegating coding conversations.
[OpenHands SDK README](https://raw.githubusercontent.com/OpenHands/software-agent-sdk/main/README.md)

An OpenHands update published 2026-10-07 describes September releases connecting
issue triage, development conversations, and PR review, including acceptance
criteria and isolated conversation runtimes. These are the project's reports
of its work; we did not run those workflows.
[OpenHands September 2026 update](https://hub.openhands.dev/blog/new-in-agent-canvas-september-2026)

**ACP is standardizing a related boundary.** Its introduction targets
communication between coding agents and clients such as editors. The inspected
site presents v1 as current and v2 as a draft; remote transport support is still
described as work in progress. It is relevant to substituting agent
integrations, but it does not supply the application's business state or
acceptance policy.
[ACP introduction](https://agentclientprotocol.com/get-started/introduction)

**Durable execution projects address the outer lifecycle.** Temporal's AI
documentation describes durable agent execution, human approval, and workflows
around model and tool calls. Its cookbook includes MCP and agent examples. This
is adjacent evidence for durable orchestration around fallible inference and
tools, not evidence of a tested Jido or Claude Code integration.
[Temporal AI documentation](https://docs.temporal.io/ai),
[Temporal AI cookbook](https://docs.temporal.io/ai/cookbook)

**Research also examines the value within the coding loop.** The
[SWE-agent paper](https://arxiv.org/abs/2405.15793)
studies agent-computer interfaces. It supports investigating tool and context
design as part of agent performance, rather than treating a harness as a
transparent wrapper around a model. It does not answer our durability question.

### Assessment of the frontier

**Yes: the sampled evidence shows active engineering and standardization around
this architecture.** The underlying ideas of stable interfaces, actors,
supervision, and durable workflows are established. The current work concerns
how to compose them with rapidly changing coding agents and interaction
protocols.

Our inference is that the difficult frontier is preserving useful semantics
across boundaries: task acceptance, approvals, artifacts, cancellation,
continuation, retry costs, and context handoff. A common function signature or
JSON message format leaves those questions open.

The evidence does not show that BEAM is uniquely suited, that Jido is the
leading implementation, or that a hybrid outperforms a standalone harness. It
does show that the proposed composition is already being pursued and is
specific enough to test. A useful contribution here would be a careful failure
and handoff experiment, with an honest baseline.

## MCP's move toward statelessness

### What changed, and when?

This is already a published protocol change as of our check date. The transport
working group's December 19, 2025 exploration discussed removing connection
initialization and implicit sessions to simplify routing and scaling. That was
a design discussion, not the final specification.
[Exploring the Future of MCP Transports](https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/)

The July 28, 2026 release announcement identifies the new revision as published.
Its changelog removes `Mcp-Session-Id` sessions and the `initialize` /
`notifications/initialized` handshake, replaces connection assumptions with
request metadata and discovery, and moves asynchronous tasks into an official
extension.
[2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28/),
[2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

Earlier MCP was not uniformly dependent on a server-issued session ID. The
2025-11-25 HTTP transport allowed a server to assign one; that was optional.
Earlier stateless implementations and transport modes therefore do not
contradict the newer change. The newer revision removes the protocol-level
session model and initialization requirement themselves.
[2025-11-25 transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)

### Stateless protocol requests can operate on stateful applications

In the new base protocol, each request carries its protocol version and client
capabilities. Server discovery is explicit. Processing should not depend on
which connection or server process previously handled the client. Cross-call
application state is represented by explicit identifiers. Even a stdio process
should not be equated with one conversation's lifetime.
[MCP base protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic)

For our application, this means a request can say “advance run R, expected step
1” or “get job J.” The server finds the corresponding application record. It
does not infer the user's current job from a connection-local session. A second
connection can identify the same work, subject to authorization.

This fits a stateful BEAM application. A request handler can look up a Jido
instance, route to a live owner, or load a persisted record. The design
condition is that the identifier resolves correctly after reconnection or
failover. Keeping one ephemeral process per MCP connection and treating its
memory as the only job record would undermine that goal.

Stateless routing does not eliminate ownership. If several API instances share
a database, they still need to agree which worker may advance a job. A local
registry is not sufficient evidence of cluster-wide exclusivity. An application
can use shared records and explicit ownership routing while keeping the
protocol requests independent.

The client's declared identity and capabilities also do not authorize access to
arbitrary run IDs. Authentication and domain access checks remain necessary;
self-reported client metadata is not an authentication mechanism.
[MCP base protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic)

### Interaction continues without an implicit session

Multi round-trip requests, MRTR, allow a server to return `input_required` with
requests for input. The client supplies responses by issuing the original
operation again. Optional opaque `requestState` is echoed back, and the retry
uses a new JSON-RPC ID. The specification requires integrity checks when that
state influences authorization or business behavior and notes that preventing
single-use replay still requires server-side enforcement.
[MCP multi round-trip requests](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)

For a Jido application, an approval could therefore be represented explicitly,
without keeping an HTTP request open for the entire human decision. Our design
would associate the approval with the durable job and proposed action. An opaque
continuation value alone would not replace that job's audit and recovery record.

The release also deprecates sampling, roots, and logging; deprecation is not
removal. This is relevant if an inner capability intends to borrow model
execution from its outer MCP host. Owning a direct model integration is another
design, with its own credentials and accounting. We should specify that choice
rather than silently depend on a host feature.
[2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

### Long-running work has an explicit task extension

The dated Tasks extension permits an opted-in `tools/call` to return a task
handle. Clients use `tasks/get` for status and results, `tasks/update` for
requested input, and `tasks/cancel` to request cancellation. The server must
create a resolvable task before returning its ID; clients should persist IDs for
recovery. Cancellation is cooperative, and completion can race with it.
[MCP Tasks, 2026-07-28](https://tasks.extensions.modelcontextprotocol.io/specification/2026-07-28/tasks)

The extension specifies a task-ID routing header for its HTTP operations.
Explicit routing to an owner can therefore coexist with independent protocol
requests. This accommodates a stateful worker behind the protocol interface.
[MCP Tasks, 2026-07-28](https://tasks.extensions.modelcontextprotocol.io/specification/2026-07-28/tasks)

This supplies a common protocol representation for deferred work. Our proposed
adapter could map that representation to a domain job without making the two
identities interchangeable. Storage choice, retry semantics, artifact retention,
and VM recovery remain implementation work.

A domain API with `start_run` and `get_run` remains useful when a host lacks the
extension. Likewise, our domain `list_runs` operation is application-specific;
it should not be confused with an assumed generic `tasks/list` method. The
protocol task surface and application job surface need separate compatibility
checks.

### Stateless does not mean no streams or no cancellation

Streamable HTTP still supports streaming responses, and subscriptions can have
long-lived response streams. The 2026-07-28 transport removes the former SSE
replay mechanism. It also specifies that disconnecting a request's SSE response
stream cancels that request, with the server expected to stop processing as
practical.
[MCP Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)

Consequently, “start a long tool call, close the connection, and assume it keeps
running” is not a valid default design. Separate the short operation accepting
a durable job from the job's later execution, or use supported asynchronous
task semantics. Define the commitment point and the response to a lost
acknowledgement. Cancellation cannot undo an effect already completed.

On a transport retry, keep the application request key stable even when the
JSON-RPC ID changes. The result should reveal the same accepted job or committed
step. Statelessness makes this distinction more visible; it does not create
idempotency automatically.

### How much does this change our proposal?

It reinforces the existing application boundary. The first reproduction already
uses durable run IDs and explicit steps, so its basic contract is compatible
with this direction. Its local stdio transport does not exercise HTTP routing,
stream cancellation, or Tasks. Those are additional experiments, not results
already covered by the reporting fixture.

For Jido, the protocol change strengthens the case for separating a connection
handler from a stateful application instance. It does not require abandoning
stateful agents, using Jido, or embedding Claude Code. ACP-controlled coding
sessions and MCP tool requests also remain separate concerns.

Finally, publication of a specification does not establish deployment across
our intended hosts and adapters. The inspected Jido MCP examples do not prove
2026-07-28 support. Before choosing the wire contract, pin versions and test
actual discovery, metadata, continuation, and task capabilities. A legacy
integration may need to retain its older handshake while using the same domain
API underneath.

## Proposed experiments and unresolved checks

These are future experiments. The existing
[reproduction.md](reproduction.md) remains the first implementation specification;
this companion does not report a BEAM port as underway or completed.

### First: retain the deterministic comparison

Implement the same two-step source-report task with an Elixir core, optionally
adding Jido around its lifecycle. Preserve the fixture, outputs, step contract,
and failure scenarios. Compare it with the baseline helpers and the proposed
Python implementation on the same criteria.

The useful observation is whether another harness can recover the same committed
run and finish it without recomputing accepted work. Additional processes or an
agent abstraction are not themselves success criteria. If plain modules and
database transactions satisfy the task more simply, record that result.

### Then: test a bounded coding worker

Use the illustrative bug fix from
[beam-jido.md — Compare the same coding task in three arrangements](#compare-the-same-coding-task-in-three-arrangements).
Compare standalone Claude Code, a Jido-native loop if implemented, and a Jido
job delegating to Claude Code. Pin the repository revision, acceptance checks,
dependency versions, model configuration, and integration mode. Record prompt
or feature differences that cannot be held constant.

Measure accepted fixes, independently verified checks, elapsed time, provider
usage where available, repeated work after failures, and integration effort.
Include the cost of maintaining the adapter and application. A single successful
task demonstrates connectivity, not a general quality or cost advantage.

### Exercise failure boundaries separately

- Lose the acknowledgement after job acceptance; retry with a new RPC ID and
  the same application key. Expect one domain job.
- Kill a worker before and after a committed step. Record which work is repeated
  and whether its effects can safely repeat.
- Stop the entire BEAM VM. Check what the chosen Jido storage and domain store
  actually restore, separately from process supervision.
- Lose a model response before saving it. Record uncertain provider completion
  and possible duplicated cost rather than claiming exactly-once inference.
- Submit concurrent advances and try a stale worker after takeover. Check that
  only the authorized transition is committed.
- Request cancellation during tool execution. Observe actual termination and
  reconcile workspace effects before allowing a replacement attempt.
- Change harnesses. Distinguish recovering domain artifacts from resuming a
  provider-specific conversation.

### Verify protocol and wrapper compatibility

Use two MCP server instances, alternating independent requests to the same run.
Require shared application state or explicit routing to the current owner;
document that design rather than assuming local process registration is enough.
Test supported protocol revisions separately, including legacy initialization,
new per-request metadata, MRTR, Tasks where available, and HTTP disconnects.

For Jido.Harness, verify the selected Claude adapter's actual tool, permission,
session, cancellation, and output capabilities. Check how unsupported features
are reported. The earlier finding that a caller can exit without stopping a run
must be tested separately from VM restart and durable result recovery.

## Current conclusion and next reading

BEAM can host the persistent application; OTP can supervise its live workers;
Jido can organize agent state and actions; a coding harness can remain a
valuable worker implementation. The stable boundary is the application's task
and recovery contract. Each library and protocol helps implement part of that
boundary.

The research spike found direct and adjacent implementations, so feasibility is
more concrete than a language analogy. What remains unknown is the operational
benefit and cost for our workload. MCP's stateless revision makes explicit job
identity and request semantics especially relevant, while leaving application
durability to the implementation.

Return to [README.md — Current assessment](README.md#current-assessment) for the
overall finding. The next document for evaluating the hypothesis is
[reproduction.md](reproduction.md), the unimplemented experiment specification.
Contributor guidance remains in [instructions.md](instructions.md).
