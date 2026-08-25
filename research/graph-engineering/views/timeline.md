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

| Year | Event | Lineage | Evidence |
|---|---|---|---|
| 1736 | Euler formalizes the Königsberg bridge problem; graph theory founded — delete the territory, keep the connectivity | mathematical | [Euler, 1736](../excerpts/euler-1736-and-the-founding-of-graph-theory.md) |
| 1840s–1860s | Graphs enter engineering practice: Kirchhoff's circuit analysis; dot-and-line molecular diagrams in chemistry | mathematical | [Euler, 1736](../excerpts/euler-1736-and-the-founding-of-graph-theory.md) (chemistry note, unverified) |
| 1956→ | Semantic networks; later ontology engineering (Protégé, METHONTOLOGY) — the pre-2026 discipline closest to owning the phrase "graph engineering" | knowledge | [bundle README §3, open question](../README.md) |
| 1962 | Petri nets: typed bipartite graphs, tokens as state, concurrency as structure; workflow nets later give BPM its formal semantics | systems | [Places, transitions, tokens](../excerpts/places-transitions-tokens.md) |
| ~1970 | IBIS (Kunz & Rittel): typed argumentation graphs — issues/positions/arguments with attachment rules — for wicked problems; gIBIS makes it hypertext in 1988 | knowledge | [Issues, positions, arguments](../excerpts/issues-positions-arguments.md) |
| early 1970s | Blackboard architecture (Hearsay-II, CMU): specialist knowledge sources cooperating via shared state under a control shell | coordination | [Specialists at a blackboard](../excerpts/specialists-at-a-blackboard.md) |
| 1980 | Contract Net Protocol (Smith): managers announce tasks, contractors bid, work is delegated and subcontracted | coordination | [Managers, contractors, and bids](../excerpts/managers-contractors-and-bids.md) |
| 2001–2006 | Semantic Web program; Berners-Lee's linked data: links "so that a person or machine can explore the web of data" | knowledge | [Making links](../excerpts/making-links-so-a-person-or-machine-can-explore.md) |
| 2010 | Google Pregel: coordination of large-scale computation as vertex-centric graph iteration | systems | [Vertex-centric iteration](../excerpts/vertex-centric-iteration.md) |
| 2010–2013 | The BPMN engine wave: Activiti (Dec 2010), BPMN 2.0 released (Jan 2011), jBPM, Camunda — executable process graphs with gateways *and human tasks* (interpretive nodes, at human cost) | systems | [Activities, gateways, events](../excerpts/activities-gateways-events-and-human-tasks.md) |
| 2012-02-21 | Amazon Simple Workflow Service: deciders + workers + durable execution state — the maintainer's hypothesized ancestor, confirmed | systems | [Deciders, workers, durable state](../excerpts/deciders-workers-durable-state-2012.md) |
| 2012-05-16 | Google Knowledge Graph launches: "things, not strings" — 500M entities, 3.5B facts; the industrial knowledge graph | knowledge | [Things, not strings](../excerpts/things-not-strings.md) |
| 2010s | DAG orchestration era (Airflow and kin): explicit graphs of deterministic tasks | systems | context in [Throw the DAG away](../excerpts/throw-the-dag-away-and-what-happened-next.md) |
| 2019 | Temporal founded (from SWF via Uber's Cadence, by SWF's own tech lead): "Durable Execution" named as a paradigm | systems | [The same two engineers, three times](../excerpts/the-same-two-engineers-three-times.md) |

## The agentic run-up

| Date | Event | Evidence |
|---|---|---|
| 2022 | ReAct (Princeton/Google): the reason-act-observe cycle modern agent loops trace to | [Act, observe, repeat](../excerpts/act-observe-decide-repeat.md) |
| 2023 | "Prompt engineering" era begins (the treadmill's first step); agents promise you can *throw the DAG away* | [Treadmill](../excerpts/the-treadmill-of-terms.md), [Throw the DAG away](../excerpts/throw-the-dag-away-and-what-happened-next.md) |
| 2024-04 | GraphRAG (Microsoft): RAG fails corpus-global questions; LLM-built entity graph + community summaries | [RAG fails global](../excerpts/rag-fails-on-global-questions.md), [Graph index](../excerpts/an-llm-built-graph-index.md) |
| 2024 | LangGraph matures: cyclic, stateful agent orchestration, Pregel-inspired | [Pregel lineage](../excerpts/inspired-by-pregel.md), [Stateful orchestration](../excerpts/deterministic-and-agentic-steps-in-one-graph.md) |
| 2024-12-19 | Anthropic, *Building Effective Agents*: workflows vs agents; "tools in a loop"; start simple | [Workflows vs agents](../excerpts/workflows-vs-agents.md), [Simplest solution](../excerpts/find-the-simplest-solution-possible.md) |
| 2025-01-20 | Zep/Graphiti paper: temporal knowledge graphs as agent memory | [Graphiti](../excerpts/a-temporally-aware-knowledge-graph-engine.md) |
| 2025 | 12-Factor Agents: "own your control flow"; good agents are "mostly just software" | [Own your control flow](../excerpts/own-your-control-flow.md) |
| mid-2025 | "Context engineering" era (treadmill step two) | [Treadmill](../excerpts/the-treadmill-of-terms.md) |
| 2025-06-22 | *Graphs Meet AI Agents* survey: graphs-for-agents ratified as an academic program | [Structurization](../excerpts/structurization-for-agents.md) |

## 2026: the year of the two namings

| Date | Event | Evidence |
|---|---|---|
| 2026-04 | Karpathy's *llm-wiki* gist: the LLM-maintained, cross-referenced markdown wiki — "compiled once and then kept current" | [Compiled once](../excerpts/compiled-once-kept-current.md) |
| 2026-06-01 | Neo4j: context graphs; three types of agent memory | [Three memories](../excerpts/three-memories-one-context-graph.md) |
| 2026-06-09/11/16 | The loop-engineering wave: MindStudio (Jun 9), Oracle (Jun 11), LangChain's *Art of Loop Engineering* (Jun 16); "June 2026: loop engineering" enters the treadmill | [Act, observe, repeat](../excerpts/act-observe-decide-repeat.md), [Anatomy of the loop](../excerpts/anatomy-of-the-agent-loop.md), [Stack and extend](../excerpts/stack-and-extend-loops.md) |
| 2026-06-12 | Google Cloud announces the **Open Knowledge Format** — the LLM-wiki pattern formalized; markdown directories as portable knowledge graphs (this bundle's own format) | [OKF](../excerpts/okf-formalizes-the-llm-wiki-pattern.md), [Maintained by agents](../excerpts/a-corpus-continuously-maintained-by-agents.md) |
| loop era | Steinberger's standing reminder ("design loops that prompt agents"); Cherny: "My job is to write loops" | [Design loops](../excerpts/design-loops-that-prompt-agents.md), [Write loops](../excerpts/my-job-is-to-write-loops.md) |
| **2026-07-04** | **Josh Simmons, "We Are Entering the Graph Engineering Phase"** — earliest documented use in the current sense; the loop's three ceilings; "boring nodes, typed edges, checkpointed state" | [Loop exposed its ceiling](../excerpts/the-loop-exposed-its-own-ceiling.md), [Three ceilings](../excerpts/three-ceilings-of-the-loop.md), [Nodes, edges, state](../excerpts/boring-nodes-typed-edges-checkpointed-state.md) |
| **2026-07-18** | **Steinberger's twelve-word joke tweet** — "Are we still talking loops or did we shift to graphs yet?" — goes viral (2.6M–2.9M views reported) | [Twelve words](../excerpts/twelve-words-48-hours-one-fabricated-study.md) |
| 2026-07-18→20 | Within 48 hours: three competing definitions; copycat wave; fabricated "$3.1M Stanford and Anthropic study" circulates (verified nonexistent); courses by the weekend | [Twelve words](../excerpts/twelve-words-48-hours-one-fabricated-study.md) |
| 2026-07-21/22 | The explainer wave: AI Operator field guide, Data Science Dojo, 36Kr (Jul 21); Bouchard, and LangChain's retro-claim "3 Years of Graph Engineering" (Jul 22) | [Treadmill](../excerpts/the-treadmill-of-terms.md), [Already doing it](../excerpts/you-were-already-doing-it.md), [This week's name](../excerpts/this-weeks-name-for-an-orchestrated-system-of-loops.md), [Three years](../excerpts/weve-been-doing-it-for-three-years.md) |
| 2026-07-25/26 | Second-wave syntheses: Flowtivity (Jul 25), Gao Dalie's three-tier framing (Jul 26) | [Explicit graphs](../excerpts/explicit-graphs-an-agent-can-traverse.md), [Three tiers](../excerpts/three-tiers-of-reliability.md) |
| 2026-08-06 | LangChain positions its stack as an autonomy–determinism spectrum: "start with Deep Agents"; LangGraph as the "escape hatch" of maximal determinism | [Maximal determinism](../excerpts/maximal-determinism-encoded-in-topology.md) |
| 2026 (thread ids 1vwixw5 / 1vwazom) | The seed exchange: "What's up with new trend with graphs?" / "Is it just fancier way to do retrieval?" — and the FLARE graph-first-IDE thread it cites | [The skeptic's question](../excerpts/the-skeptics-question-just-fancier-retrieval.md) |
