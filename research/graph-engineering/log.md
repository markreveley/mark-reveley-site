# Bundle Update Log

## 2026-08-24

* **Creation**: Research push #2 (paradigm-or-hype, at the maintainer's direction): added 10 source references (Petri nets, blackboard/Hearsay-II, Contract Net, IBIS/gIBIS, BPMN, AWS SWF, the Temporal lineage, the LLM-blackboard paper, Deep Agents, a LangGraph exit report), 15 excerpts, and the [Paradigm or hype train?](synthesis/paradigm-or-hype.md) synthesis; extended the [timeline](synthesis/timeline.md) with 1962/1970/1970s/1980/2011/2012/2019 entries. Corpus now 38 sources / 70 excerpts.
* **Update**: Extended the subtype enum to v2 at the maintainer's direction — added `question` and `definition` — and re-typed the corpus: 12 concepts `claim` → `definition`, [the skeptic's question](excerpts/rl--just-fancier-retrieval.md) `problem` → `question`. New distribution: 1 question, 11 claims, 12 definitions, 8 problems, 5 solutions, 8 observations, 6 inferences, 4 prescriptions. The `definition` tag now marks definitional content on non-definition subtypes only. See [README](README.md) § The subtype enum (v2).
* **Initialization**: Created the bundle structure (references / excerpts / synthesis) per OKF v0.2.
* **Creation**: Registered 28 source references, including the seed Reddit thread supplied verbatim by the repository owner ([reddit-llmdevs-graph-trend](references/reddit-llmdevs-graph-trend.md)).
* **Creation**: Decomposed 55 verbatim excerpts across the sources (23 claims, 9 problems, 5 solutions, 8 observations, 6 inferences, 4 prescriptions); quotes checked against raw page text by `process:curl-quote-check` where pages were reachable (see [README](README.md) § Verification).
* **Creation**: Wrote the [main synthesis](synthesis/graph-engineering.md) and the [timeline](synthesis/timeline.md).
* **Note**: reddit.com is not fetchable from this environment; the seed thread's transcript was supplied in-session by the repository owner and is attested as such. The Oracle and Britannica pages could not be re-fetched raw, so their excerpts carry no `verified` field (OKF trust tier: unverified).
