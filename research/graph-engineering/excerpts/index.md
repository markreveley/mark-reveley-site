# Level 2 — Excerpts

Verbatim quotes, one OKF concept each. Since v3 (IBIS-hybrid) every excerpt carries two facets: a `role` in the dialectic (issue / position / argument / evidence) and a `subtype` speech-act flavor (question / claim / definition / problem / solution / observation / inference / prescription), plus tags, a speaker, provenance into `../references/`, and typed `deps` forming a DAG rooted in [`../issues/`](../issues/index.md). Grouped here by role; the subtype is noted per entry.

# Issue statements (1)

* [The skeptic's question: just fancier retrieval?](rl--just-fancier-retrieval.md) - The seed thread's OP names the trend's legibility problem and poses the reduction that the whole bundle answers — are graphs merely a fancier retrieval mechanism? *(question)*

# Positions (33)

* [Own your control flow](12fa--own-your-control-flow.md) - Factor 8 — build your own control structures around the loop; good agents are mostly just software. *(prescription)*
* [Design loops that prompt agents](36kr--design-loops-not-prompts.md) - Steinberger's loop-era standing reminder — stop prompting agents yourself; design the loops that do — with Osmani's definitional gloss. *(prescription)*
* [A graph is two things: nodes and edges](aio--nodes-and-edges.md) - The field guide's buzzword-free minimal definition, cast in knowledge terms — the things you know about, and the connections between them. *(definition)*
* [Route by question type](aio--route-by-question-type.md) - The practitioner consensus — vector for lookups, graph for chains; hybrid, not conversion. *(prescription)*
* [An untyped edge is one bit](aio--typed-edges-one-bit.md) - The typed-edge distinction — "related" carries one bit of information; supersedes / depends_on / decided_by / caused carry the meaning. *(claim)*
* [Find the simplest solution possible](anth--simplest-solution.md) - The standing counterweight to graph maximalism — add complexity only when needed; use agents only where paths can't be hardcoded. *(prescription)*
* [Workflows vs agents](anth--workflows-vs-agents.md) - The December 2024 distinction both 2026 camps descend from — predefined code paths versus LLMs directing their own process, in a loop. *(definition)*
* [Autonomy versus reliability](da--autonomy-reliability-tradeoff.md) - The spectrum stated plainly — more autonomy, more potential value, less reliability; determinism for sensitive or preset workflows. *(claim)*
* [Maximal determinism, encoded in topology](da--maximal-determinism.md) - LangChain's own characterization of LangGraph — domain knowledge encoded in the graph's shape instead of left to the model's judgment. *(claim)*
* [The edge type IS the knowledge](ft--edge-type-is-knowledge.md) - The maximal typed-edge thesis — relatedness is trivial to detect; the typed edge is what answers "why did this change? *(claim)*
* [Explicit graphs an agent can traverse](ft--explicit-graphs-definition.md) - Flowtivity's definition uniting both senses — entities, decisions, and concepts as nodes; typed edges; traversal by the agent — plus the concurrency argument against loops. *(definition)*
* [Loops live inside the nodes](gd--loops-inside-graphs.md) - The nesting claim — important nodes still contain loops; the graph organizes, constrains, and connects them. Plus the restraint prescription: graph only the necessary relationships. *(claim)*
* [The AI moves within a pre-designed map](gd--pre-designed-map.md) - Gao Dalie's determinist definition — humans design the objectives, criteria, and the entire path; the AI does not wander. *(definition)*
* [Three tiers of reliability](gd--three-tier-reliability.md) - The cleanest layering claim in the corpus — prompt engineering makes a call reliable, loop engineering an agent, graph engineering a group of agents. *(claim)*
* [Structurization for agents](gmaa--structurization.md) - The academic survey's thesis — graphs are the natural data paradigm for structuring the intricate information agent capabilities depend on. *(claim)*
* [An LLM-built graph index](grag--graph-index.md) - GraphRAG's mechanism — derive an entity knowledge graph from documents, pre-generate community summaries, answer global questions by map-reduce over communities. *(solution)*
* [RAG fails on global questions](grag--rag-fails-global.md) - The GraphRAG paper's problem statement — retrieval cannot answer questions about a corpus as a whole, because they are summarization tasks, not retrieval tasks. *(problem)*
* [The loop exposed its own ceiling](js--loop-exposed-its-ceiling.md) - The genesis thesis (July 4, 2026) — loop engineering succeeded, which moved the bottleneck to a place shaped like a graph. *(claim)*
* [Boring nodes, typed edges, checkpointed state](js--nodes-edges-state.md) - Simmons' three commitments — the definitional core of graph engineering in its orchestration sense. *(definition)*
* [Compiled once, kept current](ka--compiled-once.md) - Karpathy's LLM-wiki principle — knowledge as a persistent, compounding, cross-referenced artifact the model maintains, not something re-derived per query. *(claim)*
* [Graphs contain loops](lb--graphs-contain-loops.md) - Bouchard's containment claim — the graph is not a replacement for the loop but an extra layer of delegated trust above it. *(claim)*
* [This week's name for an orchestrated system of loops](lb--this-weeks-name.md) - Bouchard's deflationary definition — graph engineering as the newest label on a rename treadmill, for a practice that already existed. *(definition)*
* [Stack and extend loops](lc--stack-and-extend-loops.md) - Loop engineering defined as loop composition — agent, verification, event-driven, and hill-climbing loops stacked into systems. *(definition)*
* [Loop engineering is a simple version of graphs](lgblog--loops-simple-version.md) - LangChain's formal subsumption — loops are the one-node special case, and production agents need cycles anyway. *(inference)*
* [We've been doing it for three years](lgblog--three-years.md) - LangChain's retro-claim on the viral term — sardonic about the name, possessive about the practice. *(claim)*
* [A buffer and a static knowledge base](neo--buffer-and-static-kb.md) - Neo4j's diagnosis of agent unreliability — memory that is only a conversation buffer plus a static store, losing the plan across loops. *(problem)*
* [Three memories, one context graph](neo--three-memories.md) - Neo4j's proposal — long-term knowledge, short-term conversation, and reasoning memory for decision traces, unified in a graph grounded in the data's entities. *(solution)*
* [The graph as abstraction layer](rl--abstraction-layer.md) - The commenter's constructive move — a graph plus the code that interprets it is a self-defined abstraction layer over the storage format, freeing representation from the format's limits. *(solution)*
* [Legible to humans and machines](rl--humans-and-machines.md) - The commenter's opening definition — graphs express complex information in a form both humans and machines can understand, and convert easily to visualization. *(definition)*
* [A map of how something works](rl--map-metaphor.md) - The commenter's closing distillation — the graph is a map you create of how something works, then read back. *(inference)*
* [Yes and no: storage shapes retrieval](rl--yes-and-no.md) - The commenter's direct answer to the reduction question — graphs are about data complexity, and the storage method determines the retrieval method. *(inference)*
* [Making links, so a person or machine can explore](tbl--making-links.md) - Berners-Lee's 2006 statement of the linked-data vision — the Semantic Web is about links that let people and machines explore a web of data. *(claim)*
* [A temporally-aware knowledge graph engine](zep--graphiti-temporal.md) - Zep's Graphiti — agent memory as a temporal knowledge graph synthesizing conversation and business data while keeping historical relationships. *(solution)*

# Arguments (10)

* [Graphs force you to acknowledge the unmodeled](36kr--graphs-force-acknowledgment.md) - Luis Catacora's double-edged observation — loops are fault-tolerant precisely because they are vague; graphs surface how much of the workflow was never really modeled. *(inference)*
* [The decision lives in the structure](aio--decision-lives-in-structure.md) - The field guide's case against similarity search — the ten most similar chunks cannot explain a decision whose meaning is carried by relationships. *(problem)*
* [Per-hop accuracy compounds against you](aio--per-hop-decay.md) - The arithmetic that kills graph projects — at 95% per-hop accuracy a 5-hop chain is 77% trustworthy; at 85%, 44%. *(problem)*
* [Overhead exceeding the problem](dl--overhead-exceeded.md) - A practitioner's exit report — the graph framework taxed a linear pipeline; "structured" mistaken for "complex. *(problem)*
* [You were already doing it](dsd--already-doing-it.md) - The frameworks argument — anyone using LangGraph, Microsoft Agent Framework, ADK, or CrewAI was doing "graph engineering" before the name existed. *(inference)*
* [The constraint moved to coordination](js--coordinate-a-thousand-steps.md) - Why now — model capability moved the binding constraint from step competence to system coordination, and coordination is a graph problem. *(inference)*
* [Three ceilings of the loop](js--three-ceilings.md) - Simmons' bill of particulars against the single agent loop — serial execution, transcript-as-state, and no pause button. *(problem)*
* [Organized nonsense at industrial scale](lb--organized-nonsense.md) - The graph era's characteristic failure mode — agent nodes interpret rather than execute, so a graph of agents checking agents can compound error with perfect structure. *(problem)*
* [Without a termination condition](ms--termination.md) - The loop's definitional hazard — agents that run forever or stop arbitrarily. *(problem)*
* [Decision trees don't fit CSV rows](rl--decision-trees-vs-csv.md) - The concrete failure case — decision structures for 10,000 behaviors can be flattened into linked rows, but reading and retrieval degrade because the encoding fights the shape of the data. *(problem)*

# Evidence (30)

* [Throw the DAG away (and what happened next)](12fa--throw-the-dag-away.md) - The 2023-era promise recorded by 12-factor-agents — give the agent a goal and skip the graph — followed immediately by the verdict: it doesn't quite work. *(observation)*
* [My job is to write loops](36kr--my-job-is-to-write-loops.md) - Boris Cherny's first-person report of the practice shift — running loops that prompt Claude and decide what to do next. *(observation)*
* [The treadmill of terms](aio--treadmill-of-terms.md) - The dated genealogy — prompt (2023), context (mid-2025), loop (June 2026), graph (July 2026) — each naming a real shift, each turned into content slop within weeks. *(observation)*
* [Twelve words, 48 hours, one fabricated study](aio--twelve-words.md) - The documented anatomy of the naming event — Steinberger's joke tweet, three competing definitions within 48 hours, and a viral study that does not exist. *(observation)*
* [Specialists at a blackboard](bb--specialists-at-a-blackboard.md) - The 1970s coordination architecture — independent knowledge sources cooperating through shared state under a control shell, with a moderator to keep them from trampling each other. *(definition)*
* [The blackboard, revived](bbllm--blackboard-revival.md) - A 2025 LLM multi-agent paper explicitly inspired by the classical blackboard architecture — the ancestry acknowledged from inside current research. *(observation)*
* [Activities, gateways, events — and human tasks](bpmn--graphical-processes.md) - BPMN — the workflow-engine era's standardized process graphs, version 2.0 released January 2011. *(definition)*
* [Managers, contractors, and bids](cnp--manager-and-contractors.md) - Smith's 1980 Contract Net Protocol — task announcement, bidding, delegation, and recursive subcontracting among autonomous agents. *(definition)*
* [Goldens: a pending test case](deepeval--goldens.md) - Evals' own term of art — a golden is an input plus expected output recorded before any model has run, so it can be replayed across models and prompt versions. *(definition)*
* [Things, not strings](gkg--things-not-strings.md) - Google's 2012 slogan — an intelligent model, "in geek-speak, a graph," of real-world entities and their relationships. *(definition)*
* [Issues, positions, arguments](ibis--wicked-problems.md) - Kunz & Rittel's IBIS — typed argumentation graphs for wicked problems (1960s–1970), made graphical hypertext by Conklin's gIBIS in the late 1980s. *(definition)*
* [Normative and informative references](ietf--normative-informative-references.md) - The RFC Editor's test for sorting an RFC's own references — essential to implementing or understanding it, or merely additional. *(definition)*
* [Normative and informative elements](iso--normative-informative-elements.md) - ISO/IEC's own terms-and-definitions entries for what makes part of a standard normative versus informative. *(definition)*
* [A model calling tools in a loop until done](lc--model-calling-tools-in-loop.md) - The loop era's minimal definition of an agent, from LangChain's June 2026 loop-engineering piece. *(definition)*
* [Inspired by Pregel](lg--pregel-lineage.md) - The acknowledged descent of the era's dominant agent runtime from Google's 2010 graph-processing system. *(observation)*
* [Deterministic and agentic steps in one graph](lg--stateful-orchestration.md) - LangGraph's self-definition — a low-level orchestration runtime whose core strength is mixing hand-coded and LLM-driven steps in a single stateful graph. *(claim)*
* [Send: edges unknown ahead of time](lgapi--send-unknown-edges.md) - LangGraph's Send API — dynamic map-reduce fan-out where the number of branches is not known when the graph is written. *(solution)*
* [Supersteps and the vote to halt](lgapi--vote-to-halt.md) - LangGraph's execution semantics are Pregel's, verbatim — supersteps, message passing, and termination by inactive-node vote. *(observation)*
* [Checkpointers and stores](lgdocs--checkpointers-stores.md) - LangGraph's persistence — thread-scoped checkpoints for interrupts, time travel, and fault tolerance; cross-thread stores for durable knowledge. *(solution)*
* [Act, observe, decide, repeat](ms--act-observe-repeat.md) - MindStudio's definition of the loop and of loop engineering, with the ReAct lineage claim. *(definition)*
* [OKF formalizes the LLM-wiki pattern](okf--formalizes-llm-wiki.md) - Google's June 2026 answer to knowledge-for-agents — an open spec turning directories of markdown into portable, interoperable graphs. *(solution)*
* [Anatomy of the agent loop](ora--anatomy-of-the-loop.md) - The harness-level definition — assemble context, reason, act, repeat until stop — and why loops exist at all. *(definition)*
* [Places, transitions, tokens](pet--places-transitions.md) - The 1962 formalism — Petri nets as directed bipartite graphs whose token flow models concurrency, later specialized into workflow nets. *(definition)*
* [Vertex-centric iteration](pre--vertex-centric.md) - Pregel's computational model (2010) — programs as iterations in which vertices receive messages, send messages, and mutate state — the systems ancestor of agent-graph runtimes. *(observation)*
* [A corpus continuously maintained by agents](spec--maintained-by-agents.md) - The OKF spec's motivating observation — knowledge is no longer authored once and read; agents write it continuously, which makes provenance, trust, freshness, lifecycle, and attestation first-class problems. *(observation)*
* [Deciders, workers, durable state — 2012](swf--durable-state-2012.md) - Amazon SWF (announced February 2012) — coordinate distributed tasks, track state durably, and let a decider program choose each next step. *(definition)*
* [Durable Execution](tmp--durable-execution.md) - The abstraction the workflow lineage converged on — automatically preserving a workflow's full state so execution survives failure. *(definition)*
* [The same two engineers, three times](tmp--shipped-it-three-times.md) - The personnel continuity of the workflow lineage — Amazon (SWF) → Microsoft (Durable Task) → Uber (Cadence) → Temporal. *(observation)*
* [Normative and informative text](w3c--normative-informative.md) - The W3C glossary definition every technical specification's conformance sections rest on. *(definition)*
* [Euler, 1736, and the founding of graph theory](wik--euler-1736.md) - The deep origin — Euler's formalization and impossibility proof for the Königsberg bridges founded graph theory and foreshadowed topology. *(observation)*
