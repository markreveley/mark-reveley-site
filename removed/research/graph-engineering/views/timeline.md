---
type: Synthesis
title: "Timeline: 1736 → 2026"
description: "A view over the quote DAG: dated genealogy of graph engineering — the three lineages, the agentic run-up, and the June–July 2026 naming events — each entry linked to its evidence. No narrative conclusions; synthesis lives in ob6to8/direction."
tags: [term-genealogy, history, synthesis]
sources:
  - id: bundle
    resource: /excerpts/index.md
    title: "Level 2 excerpt corpus (55 units)"
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
status: stable
---

# Timeline: 1736 → 2026

Dates in the deep sections are the conventionally cited ones; where sources disagree (1735 vs 1736; nine vs twelve words) the variance is preserved in the linked excerpt or reference rather than silently resolved.

## The three lineages

- Year: 1736

  Event: Euler formalizes the Königsberg bridge problem; graph theory founded —
  delete the territory, keep the connectivity

  Lineage: mathematical

  Evidence: [Euler,
  1736](../excerpts/euler-1736-and-the-founding-of-graph-theory.md)

- Year: 1840s–1860s

  Event: Graphs enter engineering practice: Kirchhoff's circuit analysis;
  dot-and-line molecular diagrams in chemistry

  Lineage: mathematical

  Evidence: [Euler,
  1736](../excerpts/euler-1736-and-the-founding-of-graph-theory.md) (chemistry
  note, unverified)

- Year: 1956→

  Event: Semantic networks; later ontology engineering (Protégé, METHONTOLOGY) —
  the pre-2026 discipline closest to owning the phrase "graph engineering"

  Lineage: knowledge

  Evidence: [bundle README §3, open question](../README.md)

- Year: 1962

  Event: Petri nets: typed bipartite graphs, tokens as state, concurrency as
  structure; workflow nets later give BPM its formal semantics

  Lineage: systems

  Evidence: [Places, transitions,
  tokens](../excerpts/places-transitions-tokens.md)

- Year: ~1970

  Event: IBIS (Kunz & Rittel): typed argumentation graphs —
  issues/positions/arguments with attachment rules — for wicked problems; gIBIS
  makes it hypertext in 1988

  Lineage: knowledge

  Evidence: [Issues, positions,
  arguments](../excerpts/issues-positions-arguments.md)

- Year: early 1970s

  Event: Blackboard architecture (Hearsay-II, CMU): specialist knowledge sources
  cooperating via shared state under a control shell

  Lineage: coordination

  Evidence: [Specialists at a
  blackboard](../excerpts/specialists-at-a-blackboard.md)

- Year: 1980

  Event: Contract Net Protocol (Smith): managers announce tasks, contractors
  bid, work is delegated and subcontracted

  Lineage: coordination

  Evidence: [Managers, contractors, and
  bids](../excerpts/managers-contractors-and-bids.md)

- Year: 2001–2006

  Event: Semantic Web program; Berners-Lee's linked data: links "so that a
  person or machine can explore the web of data"

  Lineage: knowledge

  Evidence: [Making
  links](../excerpts/making-links-so-a-person-or-machine-can-explore.md)

- Year: 2010

  Event: Google Pregel: coordination of large-scale computation as
  vertex-centric graph iteration

  Lineage: systems

  Evidence: [Vertex-centric iteration](../excerpts/vertex-centric-iteration.md)

- Year: 2010–2013

  Event: The BPMN engine wave: Activiti (Dec 2010), BPMN 2.0 released (Jan
  2011), jBPM, Camunda — executable process graphs with gateways *and human
  tasks* (interpretive nodes, at human cost)

  Lineage: systems

  Evidence: [Activities, gateways,
  events](../excerpts/activities-gateways-events-and-human-tasks.md)

- Year: 2012-02-21

  Event: Amazon Simple Workflow Service: deciders + workers + durable execution
  state — the maintainer's hypothesized ancestor, confirmed

  Lineage: systems

  Evidence: [Deciders, workers, durable
  state](../excerpts/deciders-workers-durable-state-2012.md)

- Year: 2012-05-16

  Event: Google Knowledge Graph launches: "things, not strings" — 500M entities,
  3.5B facts; the industrial knowledge graph

  Lineage: knowledge

  Evidence: [Things, not strings](../excerpts/things-not-strings.md)

- Year: 2010s

  Event: DAG orchestration era (Airflow and kin): explicit graphs of
  deterministic tasks

  Lineage: systems

  Evidence: context in [Throw the DAG
  away](../excerpts/throw-the-dag-away-and-what-happened-next.md)

- Year: 2019

  Event: Temporal founded (from SWF via Uber's Cadence, by SWF's own tech lead):
  "Durable Execution" named as a paradigm

  Lineage: systems

  Evidence: [The same two engineers, three
  times](../excerpts/the-same-two-engineers-three-times.md)

## The agentic run-up

- Date: 2022

  Event: ReAct (Princeton/Google): the reason-act-observe cycle modern agent
  loops trace to

  Evidence: [Act, observe, repeat](../excerpts/act-observe-decide-repeat.md)

- Date: 2023

  Event: "Prompt engineering" era begins (the treadmill's first step); agents
  promise you can *throw the DAG away*

  Evidence: [Treadmill](../excerpts/the-treadmill-of-terms.md), [Throw the DAG
  away](../excerpts/throw-the-dag-away-and-what-happened-next.md)

- Date: 2024-04

  Event: GraphRAG (Microsoft): RAG fails corpus-global questions; LLM-built
  entity graph + community summaries

  Evidence: [RAG fails global](../excerpts/rag-fails-on-global-questions.md),
  [Graph index](../excerpts/an-llm-built-graph-index.md)

- Date: 2024

  Event: LangGraph matures: cyclic, stateful agent orchestration,
  Pregel-inspired

  Evidence: [Pregel lineage](../excerpts/inspired-by-pregel.md), [Stateful
  orchestration](../excerpts/deterministic-and-agentic-steps-in-one-graph.md)

- Date: 2024-12-19

  Event: Anthropic, *Building Effective Agents*: workflows vs agents; "tools in
  a loop"; start simple

  Evidence: [Workflows vs agents](../excerpts/workflows-vs-agents.md), [Simplest
  solution](../excerpts/find-the-simplest-solution-possible.md)

- Date: 2025-01-20

  Event: Zep/Graphiti paper: temporal knowledge graphs as agent memory

  Evidence: [Graphiti](../excerpts/a-temporally-aware-knowledge-graph-engine.md)

- Date: 2025

  Event: 12-Factor Agents: "own your control flow"; good agents are "mostly just
  software"

  Evidence: [Own your control flow](../excerpts/own-your-control-flow.md)

- Date: mid-2025

  Event: "Context engineering" era (treadmill step two)

  Evidence: [Treadmill](../excerpts/the-treadmill-of-terms.md)

- Date: 2025-06-22

  Event: *Graphs Meet AI Agents* survey: graphs-for-agents ratified as an
  academic program

  Evidence: [Structurization](../excerpts/structurization-for-agents.md)

## 2026: the year of the two namings

- Date: 2026-04

  Event: Karpathy's *llm-wiki* gist: the LLM-maintained, cross-referenced
  markdown wiki — "compiled once and then kept current"

  Evidence: [Compiled once](../excerpts/compiled-once-kept-current.md)

- Date: 2026-06-01

  Event: Neo4j: context graphs; three types of agent memory

  Evidence: [Three memories](../excerpts/three-memories-one-context-graph.md)

- Date: 2026-06-09/11/16

  Event: The loop-engineering wave: MindStudio (Jun 9), Oracle (Jun 11),
  LangChain's *Art of Loop Engineering* (Jun 16); "June 2026: loop engineering"
  enters the treadmill

  Evidence: [Act, observe, repeat](../excerpts/act-observe-decide-repeat.md),
  [Anatomy of the loop](../excerpts/anatomy-of-the-agent-loop.md), [Stack and
  extend](../excerpts/stack-and-extend-loops.md)

- Date: 2026-06-12

  Event: Google Cloud announces the **Open Knowledge Format** — the LLM-wiki
  pattern formalized; markdown directories as portable knowledge graphs (this
  bundle's own format)

  Evidence: [OKF](../excerpts/okf-formalizes-the-llm-wiki-pattern.md),
  [Maintained by
  agents](../excerpts/a-corpus-continuously-maintained-by-agents.md)

- Date: loop era

  Event: Steinberger's standing reminder ("design loops that prompt agents");
  Cherny: "My job is to write loops"

  Evidence: [Design loops](../excerpts/design-loops-that-prompt-agents.md),
  [Write loops](../excerpts/my-job-is-to-write-loops.md)

- Date: **2026-07-04**

  Event: **Josh Simmons, "We Are Entering the Graph Engineering Phase"** —
  earliest documented use in the current sense; the loop's three ceilings;
  "boring nodes, typed edges, checkpointed state"

  Evidence: [Loop exposed its
  ceiling](../excerpts/the-loop-exposed-its-own-ceiling.md), [Three
  ceilings](../excerpts/three-ceilings-of-the-loop.md), [Nodes, edges,
  state](../excerpts/boring-nodes-typed-edges-checkpointed-state.md)

- Date: **2026-07-18**

  Event: **Steinberger's twelve-word joke tweet** — "Are we still talking loops
  or did we shift to graphs yet?" — goes viral (2.6M–2.9M views reported)

  Evidence: [Twelve
  words](../excerpts/twelve-words-48-hours-one-fabricated-study.md)

- Date: 2026-07-18→20

  Event: Within 48 hours: three competing definitions; copycat wave; fabricated
  "$3.1M Stanford and Anthropic study" circulates (verified nonexistent);
  courses by the weekend

  Evidence: [Twelve
  words](../excerpts/twelve-words-48-hours-one-fabricated-study.md)

- Date: 2026-07-21/22

  Event: The explainer wave: AI Operator field guide, Data Science Dojo, 36Kr
  (Jul 21); Bouchard, and LangChain's retro-claim "3 Years of Graph Engineering"
  (Jul 22)

  Evidence: [Treadmill](../excerpts/the-treadmill-of-terms.md), [Already doing
  it](../excerpts/you-were-already-doing-it.md), [This week's
  name](../excerpts/this-weeks-name-for-an-orchestrated-system-of-loops.md),
  [Three years](../excerpts/weve-been-doing-it-for-three-years.md)

- Date: 2026-07-25/26

  Event: Second-wave syntheses: Flowtivity (Jul 25), Gao Dalie's three-tier
  framing (Jul 26)

  Evidence: [Explicit
  graphs](../excerpts/explicit-graphs-an-agent-can-traverse.md), [Three
  tiers](../excerpts/three-tiers-of-reliability.md)

- Date: 2026-08-06

  Event: LangChain positions its stack as an autonomy–determinism spectrum:
  "start with Deep Agents"; LangGraph as the "escape hatch" of maximal
  determinism

  Evidence: [Maximal
  determinism](../excerpts/maximal-determinism-encoded-in-topology.md)

- Date: 2026 (thread ids 1vwixw5 / 1vwazom)

  Event: The seed exchange: "What's up with new trend with graphs?" / "Is it
  just fancier way to do retrieval?" — and the FLARE graph-first-IDE thread it
  cites

  Evidence: [The skeptic's
  question](../excerpts/the-skeptics-question-just-fancier-retrieval.md)
