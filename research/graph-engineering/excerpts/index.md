# Level 2 — Excerpts

Verbatim quotes, one OKF concept each, decomposed from the Level-1 sources. Each carries a `subtype` (its epistemic role, on the eight-value v2 enum: question / claim / definition / problem / solution / observation / inference / prescription), `tags` (topic/discourse/era clusters), a `speaker`, provenance into `../references/`, and typed `deps` to other excerpts. Grouped here by subtype; regroup by any tag by scanning frontmatter.

# Questions (1)

* [The skeptic's question: just fancier retrieval?](rl--just-fancier-retrieval.md) - The trend's illegibility named, and the reduction hypothesis posed. *(seed thread)*

# Claims (13)

* [The loop exposed its own ceiling](js--loop-exposed-its-ceiling.md) - Loop engineering worked; the bottleneck moved, and it is graph-shaped. *(Simmons)*
* [An untyped edge is one bit](aio--typed-edges-one-bit.md) - Typing is where knowledge enters the edge. *(AI Operator)*
* [Graphs contain loops](lb--graphs-contain-loops.md) - Containment, not replacement; a further layer of delegated trust. *(Bouchard)*
* [Three tiers of reliability](gd--three-tier-reliability.md) - Prompt/loop/graph as reliability layers for call/agent/group. *(Gao Dalie)*
* [Loops live inside the nodes](gd--loops-inside-graphs.md) - The graph organizes, constrains, connects the loops. *(Gao Dalie)*
* [The edge type IS the knowledge](ft--edge-type-is-knowledge.md) - The maximal typed-edge thesis. *(Flowtivity)*
* [We've been doing it for three years](lgblog--three-years.md) - The vendor retro-claim. *(LangChain)*
* [Deterministic and agentic steps in one graph](lg--stateful-orchestration.md) - The reference implementation's self-definition. *(LangGraph docs)*
* [Structurization for agents](gmaa--structurization.md) - The academic survey's thesis. *(Bei et al.)*
* [Compiled once, kept current](ka--compiled-once.md) - The LLM-wiki premise. *(Karpathy)*
* [Making links, so a person or machine can explore](tbl--making-links.md) - The 2006 linked-data vision. *(Berners-Lee)*
* [Maximal determinism, encoded in topology](da--maximal-determinism.md) - LangGraph as the "escape hatch"; topology as a knowledge medium. *(LangChain, Aug 2026)*
* [Autonomy versus reliability](da--autonomy-reliability-tradeoff.md) - The stated exchange rate, and the harness-first default. *(LangChain, Aug 2026)*

# Definitions (19)

* [Legible to humans and machines](rl--humans-and-machines.md) - Graphs express complex information for both audiences. *(seed thread)*
* [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md) - The three commitments of orchestration-sense graph engineering. *(Simmons)*
* [A graph is two things: nodes and edges](aio--nodes-and-edges.md) - The knowledge-sense minimal definition. *(AI Operator)*
* [This week's name for an orchestrated system of loops](lb--this-weeks-name.md) - The deflationary definition, plus the treadmill and priority claims. *(Bouchard)*
* [The AI moves within a pre-designed map](gd--pre-designed-map.md) - The maximal-control definition. *(Gao Dalie)*
* [Explicit graphs an agent can traverse](ft--explicit-graphs-definition.md) - The both-senses definition, plus the concurrency argument. *(Flowtivity)*
* [A model calling tools in a loop until done](lc--model-calling-tools-in-loop.md) - The loop era's axiom. *(LangChain)*
* [Stack and extend loops](lc--stack-and-extend-loops.md) - Loop engineering as loop composition. *(LangChain)*
* [Act, observe, decide, repeat](ms--act-observe-repeat.md) - The loop definition plus the ReAct lineage. *(MindStudio)*
* [Anatomy of the agent loop](ora--anatomy-of-the-loop.md) - The harness-level definition. *(Oracle — unverified)*
* [Workflows vs agents](anth--workflows-vs-agents.md) - The 2024 common ancestor of both camps. *(Anthropic)*
* [Things, not strings](gkg--things-not-strings.md) - The 2012 industrial knowledge graph. *(Google)*
* [Places, transitions, tokens](pet--places-transitions.md) - Petri nets, 1962; the control-flow lineage's deepest formalism. *(Wikipedia)*
* [Specialists at a blackboard](bb--specialists-at-a-blackboard.md) - The 1970s shared-state coordination architecture. *(Wikipedia)*
* [Managers, contractors, and bids](cnp--manager-and-contractors.md) - The Contract Net Protocol, 1980. *(Wikipedia)*
* [Issues, positions, arguments](ibis--wicked-problems.md) - IBIS/gIBIS typed argumentation graphs. *(Wikipedia)*
* [Activities, gateways, events — and human tasks](bpmn--graphical-processes.md) - BPMN 2.0, January 2011. *(Wikipedia)*
* [Deciders, workers, durable state — 2012](swf--durable-state-2012.md) - Amazon SWF in its own words. *(AWS docs)*
* [Durable Execution](tmp--durable-execution.md) - The workflow lineage's terminal abstraction. *(Temporal)*

# Problems (9)

* [Decision trees don't fit CSV rows](rl--decision-trees-vs-csv.md) - The flattening tax on structured knowledge. *(seed thread)*
* [Three ceilings of the loop](js--three-ceilings.md) - Serial execution; transcript-as-state; no pause button. *(Simmons)*
* [The decision lives in the structure](aio--decision-lives-in-structure.md) - Similarity search cannot answer "why." *(AI Operator)*
* [Per-hop accuracy compounds against you](aio--per-hop-decay.md) - 0.95⁵ ≈ 0.77; 0.85⁵ ≈ 0.44. *(AI Operator)*
* [Organized nonsense at industrial scale](lb--organized-nonsense.md) - Agent nodes interpret; structure can launder correlated error. *(Bouchard)*
* [Without a termination condition](ms--termination.md) - Run forever or stop arbitrarily. *(MindStudio)*
* [RAG fails on global questions](grag--rag-fails-global.md) - Corpus-level questions are not retrieval tasks. *(Microsoft Research)*
* [A buffer and a static knowledge base](neo--buffer-and-static-kb.md) - Why agent memory fails today. *(Neo4j)*
* [Overhead exceeding the problem](dl--overhead-exceeded.md) - Graph machinery taxing a linear pipeline; "structured" mistaken for "complex." *(DEV practitioner)*

# Solutions (7)

* [The graph as abstraction layer](rl--abstraction-layer.md) - Self-interpreted structure over the storage format. *(seed thread)*
* [An LLM-built graph index](grag--graph-index.md) - Entity graph + community summaries; the consumer becomes the producer. *(Microsoft Research)*
* [A temporally-aware knowledge graph engine](zep--graphiti-temporal.md) - Graphiti; typing plus time. *(Zep)*
* [Three memories, one context graph](neo--three-memories.md) - Knowledge + conversation + decision traces. *(Neo4j)*
* [OKF formalizes the LLM-wiki pattern](okf--formalizes-llm-wiki.md) - Markdown directories as portable knowledge graphs. *(Google Cloud)*
* [Send: edges unknown ahead of time](lgapi--send-unknown-edges.md) - Runtime-decided fan-out cardinality. *(LangGraph docs)*
* [Checkpointers and stores](lgdocs--checkpointers-stores.md) - Durable execution for agent graphs; the knowledge-graph gap at the API surface. *(LangGraph docs)*

# Observations (11)

* [Twelve words, 48 hours, one fabricated study](aio--twelve-words.md) - The naming event, documented. *(AI Operator)*
* [The treadmill of terms](aio--treadmill-of-terms.md) - Prompt → context → loop → graph, dated. *(AI Operator)*
* [My job is to write loops](36kr--my-job-is-to-write-loops.md) - The practice shift, first-person. *(Cherny via 36Kr)*
* [Throw the DAG away (and what happened next)](12fa--throw-the-dag-away.md) - The 2023 promise and its recorded refutation. *(12-Factor Agents)*
* [Inspired by Pregel](lg--pregel-lineage.md) - The runtime's acknowledged 2010 ancestry. *(LangGraph docs)*
* [A corpus continuously maintained by agents](spec--maintained-by-agents.md) - The OKF spec's motivating world-state, plus its five trust questions. *(OKF SPEC)*
* [Euler, 1736, and the founding of graph theory](wik--euler-1736.md) - Delete the territory, keep the map. *(Wikipedia + Britannica)*
* [Vertex-centric iteration](pre--vertex-centric.md) - Pregel's model; an agent framework minus the models. *(Malewicz et al.)*
* [Supersteps and the vote to halt](lgapi--vote-to-halt.md) - Pregel's terms of art, verbatim, in the 2026 agent runtime. *(LangGraph docs)*
* [The same two engineers, three times](tmp--shipped-it-three-times.md) - SWF → Cadence → Temporal, as employment history. *(Temporal)*
* [The blackboard, revived](bbllm--blackboard-revival.md) - 2025 LLM-agents research citing the 1970s architecture. *(Salemi et al.)*

# Inferences (6)

* [Yes and no: storage shapes retrieval](rl--yes-and-no.md) - Retrieval and representation are not separable. *(seed thread)*
* [A map of how something works](rl--map-metaphor.md) - The thread's closing distillation. *(seed thread)*
* [The constraint moved to coordination](js--coordinate-a-thousand-steps.md) - "The loop does not have verbs for" fan-out and fan-in. *(Simmons)*
* [You were already doing it](dsd--already-doing-it.md) - The installed-base argument. *(Data Science Dojo)*
* [Graphs force you to acknowledge the unmodeled](36kr--graphs-force-acknowledgment.md) - Explicitness as a legibility trade. *(Catacora via 36Kr)*
* [Loop engineering is a simple version of graphs](lgblog--loops-simple-version.md) - The one-node special case. *(LangChain)*

# Prescriptions (4)

* [Route by question type](aio--route-by-question-type.md) - Vector for lookups, graph for chains. *(AI Operator)*
* [Design loops that prompt agents](36kr--design-loops-not-prompts.md) - The loop era's core prescription, with Osmani's gloss. *(Steinberger via 36Kr)*
* [Find the simplest solution possible](anth--simplest-solution.md) - The standing counterweight. *(Anthropic)*
* [Own your control flow](12fa--own-your-control-flow.md) - Factor 8; the missing middle term. *(12-Factor Agents)*
