# Reproducing a workflow across coding harnesses

## Purpose of the experiment

This investigation asks what must live outside a coding assistant for another
assistant to continue the same work. The r/LLMDevs thread
[Have coding agents made us forget ‘program to an interface, not an
implementation’?][discussion] proposes putting reusable behavior behind interfaces
that different coding harnesses can call. We want to understand the mechanics
of that separation and test which parts of a workflow it actually preserves.

The experiment compares two ways to perform one small reporting task. In the
[Claude Code baseline][baseline], a skill describes the procedure, helper scripts
perform calculations, and the conversational model coordinates the work. In the
[proposed arrangement][proposal], a shared application owns the allowed steps,
saved results, and retry rules. Command-line and MCP adapters let different
harnesses call that application. The first version still relies on a harness to
request each step.

The practical test is to stop partway through the task, switch harnesses, and
finish using the saved work. We will compare what must be carried over or
reconfigured in each arrangement. This can show whether the proposed boundary
preserves the procedure and progress, and what it costs to maintain. If the
baseline's helpers already provide the same behavior, that overlap is a result
to record.

This document is a build specification; no prototype or harness comparison has
been run yet. It tests a mechanism described in the thread, rather than claiming
to recreate the author's unpublished implementation. The
[acceptance checks](#acceptance-checks) define the observations needed before
claiming success.

## Source-report task

The test input is the [structured YAML capture][fixture] of the Reddit thread
named above. Its [readable transcript][discussion] contains the post and 11
captured comment entries; the YAML holds the same material as data for the
prototype.

The source-report task produces a small factual report from that YAML: the source
title, source hash, comment count, missing-body count, and participant names. We
designed this workload for the investigation; the Reddit authors did not propose
it. The capture is a convenient fixed input with facts we can check by hand.
Splitting preparation and rendering into two steps gives us a clear place to
interrupt work and test whether another harness can continue it. The report is
the test workload; the behavior under a harness change is what we are studying.

The planned capability therefore reads a saved copy of the YAML, prepares the
facts, and stores the rendered report. CLI and MCP adapters call the same core,
which persists progress so another harness can inspect and finish the run. The
first stage uses deterministic code to make transport and retry behavior easy
to observe. A [later summary step](#add-a-model-inside-the-capability) adds a
model call so we can also compare who owns the prompt, model invocation, and
saved response. The [definitions](definitions.md) explain the terminology and
application conventions.

## Compare the same task in both arrangements

Start with a concrete [Claude Code baseline][baseline] before building the shared
runtime. Give a reporting skill the procedure for reading the [fixture][fixture],
obtaining factual counts, and preparing a report. Let it invoke a helper for the
counts. Record which steps are directed by the conversational model, which are
implemented by the helper, and where progress is recorded. This is the
[baseline described in the analysis](analysis.md#the-baseline-in-claude-code).

Then implement the same task through the core specified below. Reuse the same
fixture and calculation logic. The changed variable is ownership of step order,
validation, progress, and retry handling. The harness still requests each step
in this first version; the core decides whether that transition is valid and
records its outcome.

For each arrangement, record what a fresh second harness needs to continue:
instructions, executable helpers, configuration, saved files, or a transcript.
Do not assume that the baseline loses all state or must rewrite its scripts.
If its helper already implements the complete durable operation, identify that
overlap: much of the proposed architecture is already present.

The initial comparison is deterministic. Add summarization afterward so model
variation does not obscure whether the shared workflow contract works.

## Keep the first implementation small

Use Python, the existing YAML dependency, and SQLite for runs, checkpoints, and
events. Add the [official MCP Python SDK][mcp-sdk]
for the MCP adapter; choose and pin a released version when implementing.
[LangGraph][langgraph], [Switchplane][switchplane], a [daemon][daemon], and an
external [tracing service][tracing] are optional later additions.

Suggested files under `experiments/source-report/`:

```text
core.py              # Contracts, validation, transitions, and persistence
cli.py               # Argument parsing and JSON responses
mcp_server.py        # Tool registration and delegation to core
test_contract.py    # The same behavioral cases against each adapter
requirements.txt    # Versions actually used
results.md          # Commands, versions, observations, and remaining limits
```

Configure an explicit absolute database path and an allowlisted source ID mapped
to the [YAML fixture][fixture]. Both adapters must receive the same configuration.
Different host working directories must not create different databases. Run only
against a temporary fixture copy; the [original capture][raw] remains evidence.

## Define the contract before the adapters

Names below are proposed application operations, not built-in MCP methods.
Expose each operation as an MCP tool and a corresponding CLI command.

### start_run

Inputs: `source_id`, `request_key`.

Validate the allowlist, capture immutable source bytes and their hash, and create
a run. A repeated key with the same source ID returns the existing run and
snapshot; another source ID with that key returns `request_conflict`. Use a new
key to capture updated source content.

### advance_run

Inputs: `run_id`, `expected_step`.

Execute exactly the named next step and commit its result. Repeating an already
committed step returns its stored receipt. A future step returns `step_mismatch`.

### get_run

Input: `run_id`.

Return status, next step, source hash, workflow version, and any report.

### list_runs

Input: optional `source_id`.

Find existing runs when the new conversation has lost the run ID.

### get_events

Input: `run_id`.

Return ordered durable events for that run.

### Response conventions

Use a consistent envelope: `{ok: true, result: ...}` or
`{ok: false, error: {code: ..., message: ...}}`. Keep error codes stable, including
`unknown_source`, `unknown_run`, `request_conflict`, and `step_mismatch`. Refusals
without a run ID need an event keyed by a request/event ID. Do not expose arbitrary
file paths or shell commands as parameters for this capability.

The MCP adapter handles protocol encoding; the CLI writes the application response
as JSON and uses a nonzero exit status for failure. Compare the application payloads
after removing transport wrappers. Keep protocol messages alone on MCP stdout;
send diagnostic logs to stderr.

## Store enough state to recover

Use a run record with the [prototype identifiers and data][identifiers]:
`run_id`, unique `request_key`, `source_id`, immutable
`source_snapshot`, `source_sha256`, `workflow_version`, `status`, `next_step`, and
timestamps. Store step receipts under a unique `(run_id, step_number)` key and
ordered events with an event ID, operation, outcome, and run/request ID.

The proposed workflow has two short steps:

1. **Prepare, step 0.** Parse the saved snapshot, validate its structure, and store
   the title, participant list, comment count, and missing-body count. Set
   `next_step = 1`.
2. **Render, step 1.** Generate a report from those saved facts, store the report
   text in the database, and mark the run complete with `next_step = 2`.

Keep a step's result, receipt, next-step update, and completion event in one SQLite
transaction. Serialize these short deterministic transitions before reading the
current step. Two clients racing on the same expected step should receive one
committed outcome. A crash before commit leaves the previous checkpoint; a crash
after commit but before the response makes the next call return the saved receipt.

The report stays in the database for this first test. Writing a file or calling a
remote API introduces a separate side effect that cannot be made atomic merely
by committing a checkpoint. Test [idempotency][idempotency] or an
[outbox-style delivery mechanism][outbox] before adding such effects. Likewise,
do not hold a database write transaction open across a slow model call; that later
stage needs explicit work ownership and recovery rules.

## Build and exercise it in this order

1. Run and document the baseline procedure, including helper scripts and saved
   artifacts. Record how it continues in a new conversation and another harness.
2. Implement and test the core directly. Verify the fixture produces 11 comment
   entries, 10 present comment bodies, one missing body, and seven distinct comment
   authors. Do not count the post as a comment.
3. Wrap the core in the CLI. Each invocation is a new process using the same
   database. This already checks that progress does not depend on process memory.
4. Register the same operations in an SDK-based stdio server. Exercise it with an
   MCP client and compare results to the CLI. Record the SDK/protocol versions.
5. Configure two available MCP-capable coding harnesses with the same server
   executable, source mapping, and database. Keep their instructions limited to
   finding, invoking, and interpreting the capability. Record both host versions
   and configuration differences.
6. In harness A, start a run and call `advance_run` for step 0. Save its run ID,
   source hash, receipt, and events. Close the conversation and its server process.
7. In harness B, find the run with `list_runs`, inspect it, and call `advance_run`
   for step 1. Verify the same snapshot and prepared result were used. This is
   explicit resume; no worker is expected to execute while both hosts are closed.

If only a CLI and a test MCP client have been exercised, record that limited result.
The two-harness portability claim requires the two actual host sessions.

## Acceptance checks

- **Compare arrangements.** The same fixture produces the same factual report.
  Record where the procedure and state live, and the actual adaptation required
  to move each arrangement to another harness.
- **Same source through CLI and MCP.** Equivalent requests produce the same
  report facts and error codes.
- **Start called twice with one key.** There is one run ID and one captured
  snapshot.
- **Source changes after start.** The existing run uses its saved snapshot;
  a new key captures the changed source.
- **Repeat step 0 after commit.** Return the same receipt without executing it
  again or accidentally advancing to step 1.
- **Two clients advance the same step.** There is one committed step result.
- **Kill the process before commit.** The previous checkpoint remains;
  retry produces one committed result.
- **Drop the response after commit.** Retry recovers the committed receipt
  without redoing the step.
- **Switch harnesses between steps.** Preserve the run ID, source hash,
  checkpoint, and final report.
- **Unknown source ID through either adapter.** Return the same `unknown_source`
  refusal, record the rejection, and open no source file.
- **Restart with a completed run.** `get_run` returns the stored report
  without regeneration.

Record the observed result for each case. Keep expected outcomes separate from
observations; a written expectation is not a successful experiment.

## Add a model inside the capability

In the [baseline summary arrangement][summary-comparison], let the conversational
model summarize the prepared facts using the skill's prompt. An optional
comparison can delegate that same task to a [Claude Code subagent][subagents].
Record its prompt and input so the comparison has a concrete reference;
delegation is already a harness capability.

In the proposed version, package that summary prompt with the workflow. The core
selects the provider, constructs the input, calls the model, validates the
response, and saves the result. The outer harness requests the operation and
interprets its response. Record the provider access the application requires;
do not assume it inherits the conversational harness's account or model session.

The comparison is who owns and executes the summarization procedure. The
baseline keeps it in the harness setup; the proposed version lets either host
call the same implementation and retrieve the same stored result. Use the same
prompt, source snapshot, and model configuration where available, and record
any differences. A single summary call is not an inner agent loop; that would
require repeated model-directed actions.

Record model and prompt versions alongside the checkpoint. A retry may otherwise
make a second paid model request if the process dies after the provider responds
but before local persistence. Decide whether that is acceptable, or whether the
provider offers a usable idempotency mechanism, before claiming duplicate calls
are prevented. Compare preservation of the stored result across harnesses;
identical regenerated prose is not a requirement.

Afterward, evaluate whether a workflow framework simplifies the demonstrated
requirements. A separately supervised worker would be another experiment: start
work, disconnect the harness, and observe whether execution continues. It answers
a different question from [recovering a checkpoint after a restart][recovery].

[discussion]: reddit-post-program-interface.md
[baseline]: analysis.md#the-baseline-in-claude-code
[proposal]: analysis.md#the-proposed-arrangement
[fixture]: sources/reddit-program-interface.yaml
[raw]: sources/raw/reddit-post-program-interface.txt
[langgraph]: definitions.md#langgraph
[switchplane]: definitions.md#switchplane
[daemon]: definitions.md#daemon-and-supervisor
[tracing]: definitions.md#trace-and-tracing
[identifiers]: definitions.md#prototype-identifiers-and-data
[idempotency]: definitions.md#idempotency
[outbox]: definitions.md#transactional-outbox
[subagents]: definitions.md#subagent-and-inner-agent
[summary-comparison]: analysis.md#follow-the-same-model-assisted-task-through-both-arrangements
[recovery]: analysis.md#process-lifetime-and-restart
[mcp-sdk]: https://github.com/modelcontextprotocol/python-sdk
