# Reading the harness portability argument claim by claim

This investigation asks how reusable coding workflows can retain their behavior
and progress when we change coding assistants. Its starting point is the
r/LLMDevs thread [Have coding agents made us forget ‘program to an interface,
not an implementation’?][discussion], preserved as a post and 11 captured comment
entries. This document explains that argument passage by passage, checks its
technical premises, and identifies what still needs evidence.

The [architectural analysis][analysis] compares a Claude Code skill and helper
scripts with a shared application called through CLI and MCP adapters. The
[reproduction plan][purpose] proposes a source-report workload: generate factual
counts and metadata from our [YAML capture][record], interrupt the work, and try
to finish it in another harness. We devised that workload; it is not a task the
Reddit authors specified. No prototype or harness comparison has been run.

## How to follow the source

`T01` covers the title. `P01`–`P12` follow the post's 12 paragraphs, counted by
blank-line breaks in the [canonical post body][record]. Letter suffixes split
dense paragraphs into separate claims. `C01`–`C11` follow the captured comment
IDs; unknown reply nesting is not inferred. Every unit links back to its source.
Short source excerpts below are exact; explicitly labeled paraphrases cover
longer passages. The complete wording remains in the [reading view][discussion].

The capture has no known capture date, and its live contents have not been
verified. Follow-up documentation was checked on 2026-10-17 and is indexed in the
[investigation record][manifest]. Current documentation qualifies present-day
claims; it does not establish the historical setup behind the author's account.
The [glossary](definitions.md) defines terminology used across the investigation.

## T01: Program to an interface, not an implementation

**Source:** [title][discussion]: “program to an interface, not an implementation”.

**Meaning.** In software engineering, client code should depend on an agreed set
of behaviors rather than the internal details of one component that supplies
them. The principle is associated with the Gang of Four's *Design Patterns*.
Coauthor Erich Gamma explains it in terms of managing dependencies: a component
can change its implementation while callers continue to use its published API.
An interface here is a software boundary, not necessarily a graphical interface
or a particular language's `interface` keyword. [Gamma interview][gamma]

For an illustration of our own, a report writer might ask a storage component to
`save(report)` and `load(id)`. It need not know whether that component uses files
or a database. Calling database-specific methods throughout the report writer
would couple it to that implementation. Interchangeability also needs agreement
about behavior, such as what a missing ID means; matching method names alone
does not supply that agreement.

**Assessment and implication.** The title applies a familiar dependency principle
to agent tooling. The question is which boundary should remain stable when a
harness changes. [P04](#p04-what-is-the-implementation-in-this-analogy) examines
an ambiguity in the analogy; our [contract definition][interface] makes the
required behavioral agreement explicit.

## P01: From Cursor customization to repeated migration and drift

**Source:** [post, paragraph 1][post], beginning “My introduction to customizing
agentic coding harnesses was building out cursor rules.”

**Source account, paraphrased.** The author invested time in Cursor rules,
invested more in moving to Claude Code, then maintained both while additional
harnesses appeared. They describe the resulting maintenance as chaotic and also
assert that Claude Code took market share.

**Meaning.** The investment can include learning what instructions a tool loads,
writing repository conventions, explaining commands, and refining prompts after
failures. A “lift and shift” means carrying an existing setup into another
environment while trying to preserve its purpose. Here that may involve changing
instruction locations, command wiring, and assumptions about available tools.
The passage does not identify the author's actual files or migration steps.

An illustration: suppose a Cursor rule says how to run a repository's checks and
interpret failures. Someone translates it into Claude Code instructions, then
later fixes only the Claude version. Cursor still follows the older procedure.
Adding a third copy creates another place to update. This is configuration drift:
copies intended to express one procedure gradually express different procedures.
Even identical text may be loaded in different circumstances by different hosts.

**Follow-up and assessment.** Cursor documents scoped rules and their inclusion
in model context. Claude Code documents `CLAUDE.md` instruction loading. These
are concrete examples of host integration details that a migration must inspect.
They support the plausibility of translation work, not the author's time estimate
or the market-share claim. No adoption data accompanies the capture.
[Cursor rules][cursor-rules], [Claude Code memory][claude-memory]

**Investigation consequence.** In the [baseline comparison][baseline], record the
files actually changed during a handoff. Separate shared content, host wiring,
and observed behavior instead of assuming every migration requires a rewrite.

## P02: Differentiation has moved toward the harness

**Source:** [post, paragraph 2][post]: “As the models have improved,
differentiation has increasingly moved into the harness around them.” The
paragraph also describes competing benchmarks and pressure to keep adapting.

**Meaning.** A coding assistant's behavior depends on more than its model. The
surrounding software supplies context, executes tools, and decides how a session
is managed. Two products using similar models can therefore provide different
experiences. Claude Code's documented context/tool/result loop is one concrete
example of that surrounding machinery. [How Claude Code works][claude-loop]

**Assessment.** That mechanism is credible. The stronger claim that competition
has *increasingly* shifted there is a trend claim requiring comparisons over
time. The paragraph supplies no benchmark names, configurations, or measurements.
It also does not show whether a score difference comes from a model, harness,
prompt, tool environment, or task selection.

**Follow-up.** If benchmark superiority becomes part of a future post, identify
the evaluation and controlled variables first. Our [handoff checks][acceptance]
answer a narrower question about reusable workflow behavior; they will not rank
coding assistants or establish a market trend.

## P03: Product promotion encourages dependence on an ecosystem

**Source:** [post, paragraph 3][post]: “Demos and press releases tend to emphasize
features that pull you deeper into a particular ecosystem.”

**Meaning.** The author sees a tension between a convenient integrated feature
and the cost of moving work elsewhere. If a workflow depends on host-specific
configuration or session behavior, changing hosts may require adaptation.

**Assessment.** This is an interpretation of product incentives, not a measured
finding about particular vendors. No demo or press release is identified.
Dependence also needs to be described concretely: a proprietary configuration
file can be easy to translate, while a superficially standard integration can
still depend on unusual credentials or lifecycle assumptions.

**Follow-up.** Use the [migration comparison][baseline] to identify an actual
dependency and its replacement cost. A demonstrated cost gives this argument
more substance than speculation about vendors' motives.

## P04: What is the implementation in this analogy?

**Source:** [post, paragraph 4][post]: “thinking about frontier coding harnesses
as the implementation” and building agentic systems against an interface.

**Meaning.** The intention appears to be that choosing a different conversational
assistant should not require rebuilding valuable capabilities. But the later MCP
example does not define one abstract harness API implemented by every product.
Instead, several harnesses become callers of a separately implemented capability.
That is our reading of the proposed dependency direction.

```text
Claude Code + its adapter -> application operation -> shared implementation
Another host + its adapter -> same operation       -> shared implementation
```

**Assessment.** These are related applications of interface-based design, but the
distinction matters. A common tool interface does not make the entire harness
interchangeable: its conversation, permissions, context handling, and tool choices
can still differ. The proposal reduces a particular dependency.

**Investigation consequence.** Name both sides of each boundary. Our
[proposed arrangement][proposal] keeps the conversation in the harness and moves
workflow rules and saved results into application code.

## P05: Put the capability in a CLI or local MCP server

**Source:** [post, paragraph 5][post], contrasting a Claude Code plugin containing
skill prose and ad-hoc code with a local MCP server or CLI usable as a tool.
This is a paraphrase of the paragraph's example.

**Meaning.** A CLI exposes commands a harness can execute through a shell. An MCP
server exposes operations through a protocol client in the host. In either case,
the reusable implementation can be packaged separately from the host integration.
MCP defines a client/server connection, not the application's workflow semantics.
[MCP architecture][mcp]

**Follow-up and qualification.** Claude Code skills can already bundle executable
scripts and be shared through project files or plugins. A plugin is therefore
not inherently prose-only, undistributable, or incapable of calling reusable
code. The author's example describes a possible poorly separated package, not
a limitation of all plugins. [Claude Code skills][claude-skills]

**Investigation consequence.** Compare ownership of behavior rather than file
extensions. If a skill calls a shared program that already validates requests
and saves progress, it overlaps with the proposed design. “Any harness” also
requires suitable tool access and compatible configuration; it is not established
merely by writing the server. See the [two-adapter plan][contract].

## P06: Keep capabilities under a stable surface

**Source:** [post, paragraph 6][post]: “Make the harness swappable, keep the
capabilities you build under a stable surface.”

**Meaning.** Callers should keep relying on the same operation while the host
changes. Stability includes inputs, results, errors, and the effects of retries.
For example, our proposed [start_run operation][start-run] promises that repeating
a request key retrieves the same run. A replacement adapter that creates a new
run on every retry would violate that promise despite exposing the same name.

**Assessment.** This is a design objective, not an observed result. A stable
contract takes maintenance and versioning. It also cannot require two outer
models to choose the same tool at the same moment.

**Follow-up.** The [acceptance checks][acceptance] compare application outcomes
through both adapters and then through two actual hosts. Keep protocol
compatibility, operation compatibility, and model behavior distinct.

## P07: Convergence and possible prior discussion

**Source:** [post, paragraph 7][post], paraphrased: the author senses convergence,
has not seen the question framed this way, and invites pointers to related work.

**Meaning and assessment.** This is a qualified impression and a request for
references. It is not a priority claim. The [title analysis][title-analysis]
establishes the older engineering principle; [MCP's architecture][mcp] provides
a concrete protocol example. Neither source establishes how common this exact
workflow split is among practitioners.

**Follow-up.** Treat examples found in the comments as leads. Inspect what each
actually moves out of the harness before calling it the same architecture.

## P08a: Separate conversation from durable workflow and tool logic

**Source:** [post, paragraph 8][post]: “Splitting the conversational harness from
the durable workflow and tool logic”. The author reports a positive experience.

**Meaning.** The conversational assistant can interpret the user's request while
another application owns a reusable procedure. In the [chosen baseline][baseline],
the conversational model coordinates helpers. In the [proposal][proposal], the
application validates transitions and retains results that another conversation
can query. These are our concrete versions of the source's broad description.

**Assessment.** An MCP boundary does not itself make a workflow durable.
LangGraph distinguishes graph checkpoints from other stored application data;
an in-memory checkpointer loses its contents when the process exits. Recovery
requires retained state and code that uses it. [LangGraph persistence][persistence]

**Follow-up.** Specify the unit of saved work, storage location, and resume
operation, as in our [storage plan][storage]. The author's experience is evidence
of their report; the capture does not expose enough implementation detail to
verify its durability guarantees.

## P08b: Langfuse makes the interaction observable

**Source:** [post, paragraph 8][post]: “I’ve been using LangFuse for my
observability layer”.

**Meaning.** Application tracing can relate requests, model calls, tool calls,
timing, and results. It helps a developer see what happened across a workflow.
This is consistent with [Langfuse's description of tracing][langfuse].

**Assessment and implication.** Seeing a sequence in a trace is different from
having the state needed to resume it. A log saying that a report was prepared
does not necessarily retain the prepared data or settle whether a later write
committed. Our [event records][storage] should make the experiment inspectable;
the checkpoints and receipts must independently support recovery. No trace from
the author's system is supplied, so its actual behavior remains unverified.

## P09a: Put hooks in application code

**Source:** [post, paragraph 9, first sentence][post]: “You want hooks? Add them
to your own code.”

**Meaning.** A workflow can call its own handlers before or after an application
step. For example, our proposed core could validate a source before creating a
run and record an event afterward. Both adapters would use those same checks.

**Follow-up and qualification.** Claude Code already has lifecycle hooks,
including handlers before tool execution. Moving a handler into application code
changes which lifecycle it observes. A core handler sees requests to that core;
it does not automatically see every unrelated shell command or file edit made
by the host. [Claude Code hooks][claude-hooks]

**Investigation consequence.** Specify the event and component before claiming
equivalence. [Application enforcement][enforcement] and host permission checks
can complement each other, and may need different implementations.

## P09b: A little stdio boilerplate can host the same prose

**Source:** [post, paragraph 9, remaining sentences][post], paraphrased: a small
local MCP server over stdio can contain an agent using the same prose and deliver
portable capabilities through the language's package ecosystem.

**Meaning.** Stdio connects the client's and server's standard input/output
streams. The MCP specification describes the client launching a subprocess and
exchanging protocol messages with it. That makes a local integration possible
without first operating a network service. [MCP stdio][stdio]

**Assessment.** The transport wrapper may be small; the behavior behind it still
needs implementation. A prompt file does nothing until code loads it, prepares
input, invokes a model, and handles the response. An agent loop additionally needs
tool execution, feedback, and stopping rules. This matches the distinction between
predefined workflows and model-directed agents in
[Anthropic's architectural explanation][agents].

Moving the exact prose also changes its surrounding context and possibly its
model, so equivalent wording does not guarantee equivalent output. Packaging the
server does not automatically package credentials, installed executables, or
access to the same saved state.

**Follow-up.** Compare the [same summary task in both arrangements][summary].
Record the prompt, model configuration, input, provider access, and saved result.
Test the installation and handoff before describing portability as complete.

## P10: The proposal does not prescribe one framework or boundary

**Source:** [post, paragraph 10][post], paraphrased: the argument concerns
separation of concerns, not a mandatory framework, language, or exact architecture.

**Meaning and assessment.** The durable idea is assigning responsibilities so
that changing the conversation layer does not unnecessarily disturb reusable
work. MCP, a CLI, LangGraph, and a particular process layout are possible choices.
The source explicitly leaves their selection open.

**Investigation consequence.** Our [Python and SQLite plan][implementation] is a
locally devised experiment, not a reconstruction of an endorsed stack. Start
with enough machinery to expose the boundary and its failure behavior; record
additional requirements before adopting a workflow framework.

## P11: Keep useful host features, with thin integrations

**Source:** [post, paragraph 11][post]: “the harness-specific aspects should
become lean and not onerous to translate from harness to harness.”

**Meaning.** The author allows host-specific conveniences while asking that the
valuable capability remain reusable. A thin adapter translates request and
response formats or tells the host how to invoke a tool; it should not contain
another independent implementation of the workflow.

**Assessment.** “Thin” needs a practical test. A small file can still carry a
critical rule whose omission changes behavior. Conversely, a longer integration
may contain only configuration. Count responsibilities and duplicated decisions,
not just lines of code.

**Follow-up.** In the [two-host exercise][handoff], list everything changed for
the second host. Check whether refusals, retry behavior, and saved results remain
in the core, and identify any behavior that still relies on host instructions.

## P12: Explain the architectural case to other people

**Source:** [post, paragraph 12][post], paraphrased: the author asks whether others
have adopted this approach and successfully communicated that the harness may
own too much of the architecture.

**Meaning and assessment.** This is an invitation to discuss adoption and
organizational persuasion. It does not supply an adoption result. The proposed
benefit is reduced repeated work when tools change; the cost is maintaining the
shared application's contract, dependencies, state, and failures.

**Follow-up.** Build the case from the [comparison's results][acceptance]: what
was reused, what still changed, and how interruptions were handled. Report setup
and maintenance costs alongside migration savings. A result where simple shared
scripts suffice is useful evidence too.

## C01: Rewriting tool logic motivates thin wrappers

**Source:** [c01][c01], paraphrased: the commenter reports repeatedly rewriting
tool logic and favors portable capabilities with a thin wrapper for each harness.

**Meaning and assessment.** This reinforces the opening migration account, but
does not identify which code actually had to change. Rewriting a tool's algorithm
is different from changing its argument format, executable path, or registration.
A shared library can address the first problem; an adapter can address the latter.

**Follow-up.** Classify every change in the [handoff experiment][handoff]. This
will show whether the proposed separation reduces duplicated behavior or merely
repackages configuration work.

## C02: Authentication and state can be solved once in a library

**Source:** [c02][c02], paraphrased: upstream MCP authentication and durable state
add complications, but reusable library code can solve them once.

**Meaning.** Common code can centralize credential handling and persistence
mechanisms. “Upstream” likely means a service called by the capability, but the
comment does not identify that service or credential flow.

**Follow-up and qualification.** MCP's authorization specification covers HTTP
transport access and treats stdio credentials separately. Reusing an integration
does not make every host share an identity, permission set, or state location.
[MCP authorization][authorization]

The reusable part is the mechanism; deployments still supply configuration and
authority. Our [initial implementation][implementation] requires both adapters
to use the same explicit source mapping and database path. Remote authentication
is deferred, so this reproduction will not validate that part of the claim.

## C03: Rules files should become thin adapters

**Source:** [c03][c03]: “Keep the tool contracts in one place, keep the harness
prompts thin, and treat each IDE's rules as thin adapters.”

**Meaning.** Instructions can explain when to use a capability and how to read
its result while application code owns the behavior. This removes the need to
copy a full workflow procedure into every rules file.

**Assessment.** Prose still affects discovery and tool selection. If one host is
told to retry and another to start a new run, the shared tool can receive different
requests. The contract should make invalid or repeated operations explicit, and
the integration instructions should describe those semantics consistently.

**Follow-up.** Read each host's instructions against the
[operation contract][contract]. Test both direct tool requests and requests
chosen by the host's model; those checks answer different questions.

## C04: No captured body

**Source:** [c04][c04] preserves commenter metadata but has no body in the capture.

**Assessment and consequence.** There is no claim to analyze. The missing body
does not establish deletion, agreement, disagreement, or a reply relationship.
Keep the omission visible rather than completing the conversation by inference.

## C05: A permission rule in the tool layer is a wall

**Source:** [c05][c05], contrasting “never push to main” in an instruction file
with enforcement and a refusal trace in the tool layer.

**Meaning.** Instruction text asks the model to avoid an action. An executing
check can reject a request even when the model asks for it. Claude Code's own
documentation distinguishes instruction guidance from settings-based enforcement;
enforcement is already available within a conventional harness.
[Claude Code memory and settings][claude-memory]

**Assessment.** The “wall” applies only where requests must pass through the
check. A guarded push tool does not block a separate shell command using the
same credentials. A refusal trace also requires logging code and somewhere to
retain its output. Neither property follows just from naming a layer “tools.”

**Follow-up.** State the [authority boundary][enforcement]. Our proposed source
allowlist constrains this application's operations; it does not establish a
system-wide prohibition on reading files through other tools.

## C06: Share one instructions file through symlinks

**Source:** [c06][c06], proposing one `AGENTS.md` file with `CLAUDE.md` and
`GEMINI.md` symlinks as a cheap alternative to repeated migration.

**Meaning.** A symbolic link points another filesystem name at the same content.
Editing the shared file can therefore remove one source of copied-text drift.
This is a smaller intervention than implementing an application service.

**Assessment.** Shared bytes do not establish shared loading scope, instruction
priority, available tools, or model behavior. Cursor's current documentation even
lists `AGENTS.md` as a supported instruction format, showing that the need for
filename translation itself depends on the host and version. We have not tested
the suggested three-file setup. [Cursor rules][cursor-rules]

**Follow-up.** Include shared instructions and helpers in a fair
[baseline][baseline]. Establish whether the problem is duplicated prose,
duplicated executable behavior, or missing recoverable state before choosing
the larger design.

## C07: Festival uses Git and the filesystem

**Source:** [c07][c07], linking Festival and saying it is based around Git and
the filesystem.

**Follow-up research.** Festival's current README describes an environment that
keeps context and progress in files and Git. It describes agents requesting a
next step through `fest next`, carrying out work, and recording results. That
supports the comment's broad characterization at the documentation level.
[Festival README][festival]

**Assessment.** This is a relevant alternative boundary: portable files and CLI
operations can coordinate work without requiring our particular MCP and SQLite
design. A Git record of work is not automatically a checkpoint of a running
computation, and a documented demonstration is not our own reproduction. We
read the README; we did not install Festival or inspect its implementation.

**Follow-up.** Compare what a fresh host can reconstruct from those saved files
with the [application run state][storage] our plan requires. Pin a revision before
any execution-based comparison.

## C08a: Kin centralizes behavior in one MCP server and CLI

**Source:** [c08, paragraph 1][c08], paraphrased: Kin puts behavior in a server
and CLI, with thin host integrations; the commenter calls prose the least stable
layer.

**Meaning.** The architecture described resembles our
[shared-core proposal][proposal]: several callers use one behavior implementation.
The claim about prose may mean its interpretation varies between models or that
copies drift during maintenance.
Those are different failure modes and need different checks.

**Assessment.** The capture supplies no Kin repository URL or version. We have
not independently identified or inspected that implementation. “Least stable”
also lacks a stated metric; code and tool descriptions can drift too.

**Follow-up.** Obtain an unambiguous project reference before making product
claims. Meanwhile, test the described pattern with the [same-source acceptance
checks][acceptance], without attributing our implementation choices to Kin.

## C08b: Instructions do not enforce prohibitions

**Source:** [c08, paragraph 2][c08], paraphrased: if an action remains available,
a model may eventually take it despite an instruction prohibiting it.

**Meaning.** A prohibition that matters to the application should be checked
where the application accepts or executes requests. Prose can explain the rule
and help select valid actions, but is not itself an execution barrier.

**Assessment.** The engineering distinction is sound; the prediction that some
model will violate every available prohibition is stronger than the evidence
supplied. Host permissions and application checks can both enforce restrictions.
The important question is which routes each check covers, as explained in
[C05](#c05-a-permission-rule-in-the-tool-layer-is-a-wall).

**Follow-up.** Send a forbidden request directly through both adapters. Observe
the refusal and recorded event rather than relying on a cooperative model never
asking for it. This is part of our [unknown-source check][acceptance].

## C08c: Help, tool descriptions, and documentation must agree

**Source:** [c08, paragraph 3][c08], describing different harness behavior when
CLI help, MCP tool descriptions, and plugin documentation disagree. This is a
paraphrase of the commenter's reported lesson.

**Meaning.** The model's understanding of an operation comes partly from its
description. If help says a command creates work while the MCP description says
it resumes work, callers may form different requests even when the underlying
code is shared.

**Assessment.** This is a plausible mechanism and a useful maintenance concern,
but no discrepant descriptions or measured outcomes are supplied. Agreement in
prose is necessary for clear communication, not sufficient for behavioral
equivalence; implementations must also satisfy their promises.

**Follow-up.** Check all descriptions against the [shared contract][contract],
then exercise the same success, rejection, and retry cases through CLI and MCP.
Treat tests of model tool selection as a separate comparison.

## C09a: Add deterministic properties after model mistakes

**Source:** [c09, opening sentences][c09], describing efforts to add deterministic
properties after a model failed to follow an instruction.

**Meaning.** Some decisions can be expressed as explicit checks: reject an
unknown source, validate a step number, or retrieve a saved receipt for a repeated
request. Their result need not depend on the model interpreting a reminder.

**Assessment.** This can make those particular properties repeatable. It does
not make the whole system deterministic when it also contains model outputs,
concurrent requests, or external services. Even deterministic code needs correct
inputs and synchronization. See [determinism][determinism] for the local scope.

**Follow-up.** Name each property and its counterexample. Our
[retry checks][acceptance] are meant to expose accidental duplicate execution or
unintended step advances; they are not a test of identical model-generated prose.

## C09b: Switchplane preceded the later conversational split

**Source:** [c09, remaining sentences][c09], describing Switchplane as a local
durable LangGraph runtime with a TUI/CLI, followed by a move to a split system
under an MCP boundary. This is a paraphrase of the author's account.

**Follow-up research.** Switchplane's README describes explicit task retry,
optional LangGraph checkpoints, and application-provided resume logic. Its MCP
section describes tasks consuming tools from MCP servers. That is a different
direction from exposing the whole workflow as a tool to another harness.
[Switchplane README][switchplane]

**Assessment.** The README supports investigating a durable runtime; it does not
prove every detail of the later arrangement. The
[author's clarification][c11-analysis] explicitly distinguishes the two. We have
inspected documentation, not executed either system.

**Follow-up.** Keep the [open implementation question][manifest] unresolved until
the later server, contract, and recovery path can be inspected. Do not use the
Switchplane name as a substitute for that missing evidence.

## C10: Who resumes work after the conversational side restarts?

**Source:** [c10][c10], expressing a preference for local durability and asking
whether the graph resumes automatically or the harness must request it.

**Meaning.** The commenter identifies a coordination problem. The workflow may
have committed a result just before the conversation lost the response. The new
conversation may believe the step never happened and request it again. Durable
state can establish what committed; retry semantics determine what happens next.

**Assessment.** Local-only operation is a preference here, not a demonstrated
universal default. The recovery question correctly separates saved progress from
the component that decides to continue execution. It is a question, not evidence
that automatic recovery exists.

**Follow-up.** The [lost-response and restart checks][acceptance] exercise this
uncertainty. Compare [conversation recovery with application recovery][recovery]
and identify whose state is authoritative for the operation.

## C11a: Restarting work is user-triggered

**Source:** [c11][c11]: “switchplane was pre-conversational harness split,
self-contained runtime.” The next paragraph says the user must request another
start if the harness dies.

**Meaning and assessment.** The author clarifies that Switchplane and the later
split system should not be conflated. For the later system, another user request
triggers work after the harness fails. “start up the operation again” leaves
unspecified whether that retrieves a saved run, resumes a checkpoint, or repeats
the work from the beginning.

Switchplane's own documented behavior is more specific: retry can recover an
opt-in checkpoint when the task implements the resume path; otherwise it can
rerun from the beginning. That documentation cannot fill in the unspecified
semantics of the later system. [Switchplane recovery][switchplane]

**Follow-up.** Our [handoff plan][handoff] explicitly requires finding the same
run ID and snapshot. This is our testable requirement, not a guarantee extracted
from the author's wording.

## C11b: A server could continue tasks automatically on startup

**Source:** [c11, final sentence][c11]: “Nothing preventing the server from
auto-continuing the tasks on startup if one should choose to do so though.”

**Meaning.** The author suggests adding a startup policy that finds unfinished
work and resumes it without another user request. This is a possible extension,
not a claim that their current setup already does it.

**Assessment.** Startup recovery still requires something to start the server,
a rule for selecting unfinished runs, ownership of work, and safe handling of
uncertain side effects. Continuing while the host is closed additionally requires
a process whose lifetime is independent of that host. A saved checkpoint alone
does not supply either mechanism.

**Follow-up.** Keep [process lifetime and restart][process-lifetime] separate.
The first reproduction tests explicit resume. A supervised worker and automatic
restart policy would need their own experiment and failure observations.

[discussion]: reddit-post-program-interface.md
[title-analysis]: #t01-program-to-an-interface-not-an-implementation
[c11-analysis]: #c11a-restarting-work-is-user-triggered
[post]: reddit-post-program-interface.md#post
[c01]: reddit-post-program-interface.md#c01
[c02]: reddit-post-program-interface.md#c02
[c03]: reddit-post-program-interface.md#c03
[c04]: reddit-post-program-interface.md#c04
[c05]: reddit-post-program-interface.md#c05
[c06]: reddit-post-program-interface.md#c06
[c07]: reddit-post-program-interface.md#c07
[c08]: reddit-post-program-interface.md#c08
[c09]: reddit-post-program-interface.md#c09
[c10]: reddit-post-program-interface.md#c10
[c11]: reddit-post-program-interface.md#c11
[record]: sources/reddit-program-interface.yaml
[manifest]: investigation.yaml
[analysis]: analysis.md
[baseline]: analysis.md#the-baseline-in-claude-code
[proposal]: analysis.md#the-proposed-arrangement
[summary]: analysis.md#follow-the-same-model-assisted-task-through-both-arrangements
[enforcement]: analysis.md#instructions-and-enforced-restrictions
[recovery]: analysis.md#conversation-recovery-and-application-recovery
[process-lifetime]: analysis.md#process-lifetime-and-restart
[purpose]: reproduction.md#purpose-of-the-experiment
[implementation]: reproduction.md#keep-the-first-implementation-small
[contract]: reproduction.md#define-the-contract-before-the-adapters
[start-run]: reproduction.md#start_run
[storage]: reproduction.md#store-enough-state-to-recover
[handoff]: reproduction.md#build-and-exercise-it-in-this-order
[acceptance]: reproduction.md#acceptance-checks
[interface]: definitions.md#interface-and-contract
[determinism]: definitions.md#deterministic-and-nondeterministic
[gamma]: https://www.artima.com/articles/design-principles-from-design-patterns
[cursor-rules]: https://cursor.com/docs/rules
[claude-memory]: https://code.claude.com/docs/en/memory
[claude-loop]: https://code.claude.com/docs/en/how-claude-code-works
[claude-skills]: https://code.claude.com/docs/en/skills
[claude-hooks]: https://code.claude.com/docs/en/hooks
[mcp]: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
[stdio]: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio
[authorization]: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
[agents]: https://www.anthropic.com/engineering/building-effective-agents
[persistence]: https://docs.langchain.com/oss/python/langgraph/persistence
[langfuse]: https://langfuse.com/docs/observability/overview
[festival]: https://raw.githubusercontent.com/Obedience-Corp/festival/main/README.md
[switchplane]: https://raw.githubusercontent.com/salesforce-misc/switchplane/main/README.md
