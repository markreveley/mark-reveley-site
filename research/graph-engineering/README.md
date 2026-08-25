---
type: Guide
title: "How this bundle works"
description: Method, OKF conventions, extension fields, subtype enum, tag taxonomy, and open questions for the graph-engineering research bundle.
tags: [meta, method]
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
status: stable
---

# What this is

A research push on **graph engineering** — as defined historically, and as the term re-emerged in June–July 2026 alongside *loop engineering* in AI-agent practice. The bundle has three levels of artifacts, as requested by the repository owner:

| Level | Directory | Contents |
|---|---|---|
| 1 | [`references/`](references/index.md) | Links to resources: one OKF concept per source, with availability, dates, and credibility notes |
| 2 | [`excerpts/`](excerpts/index.md) | Verbatim quotes from those sources, persisted as OKF concepts with a `role` in the dialectic, a `subtype` speech-act flavor, tags, and typed `deps` |
| 2 | [`issues/`](issues/index.md) | Root issue nodes (v3): the questions the position excerpts respond to |
| 3 | [`views/`](views/index.md) | Non-narrative compositions over the quote DAG (currently: the timeline). Explicit synthesis moved to [`ob6to8/direction`](https://github.com/ob6to8/direction/blob/main/mark_reveley/2026-08-25-graph-engineering-synthesis/README.md) under the house rule below |

**House rule (2026-08-25, operator-directed).** This repository contains only primary sources and the typed DAG of quotes extracted from them, plus non-narrative views over that DAG. Positions may be taken only *implicitly* — in which quotes are selected and how they are composed and connected. Explicit synthesis lives in `ob6to8/direction` (`mark_reveley/2026-08-25-graph-engineering-synthesis/`), so conclusions are drawn in the operator's own writing, and presentation stays composable. Accordingly, in the v3 migration (2026-08-25) excerpt `# Analysis` prose was replaced by short provenance-and-connection `# Note`s; the removed interpretive prose survives only in the direction synthesis docs.

# OKF conformance

This bundle targets **OKF v0.2** as specified in [`okf/SPEC.md`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) of Google's `knowledge-catalog` repository (read at commit `9a15b13`, 2026-08-24). OKF — the **Open Knowledge Format** — was introduced by Google Cloud on 2026-06-12; see the [source reference](references/okf-spec.md). Conformance choices:

- Every non-reserved `.md` file carries YAML frontmatter with a required `type` (§4.1). Types used here: `Source Reference`, `Excerpt`, `Issue`, `Guide`.
- `index.md` and `log.md` follow §8 and §9.
- Provenance uses the `sources` family (§5.1); per-claim attribution uses footnotes keyed to `sources[].id` (§5.1). Excerpt concepts point their `sources[].resource` at the Level-1 reference concept (bundle-relative), and each reference concept's `resource` is the external URL — so lineage recursion (§5.1) works: excerpt → reference → external source.
- Trust uses `generated` / `verified` (§5.2) with the actor convention (§7). `generated.by` is `research_agent/claude-code`. `verified.by` is `process:curl-quote-check` (quote fragments mechanically matched against raw fetched page text), `process:local-clone-read` / `process:local-file-extract` (quotes taken directly from a locally cloned file or extracted PDF), `process:transcript-match` (quotes matched against the operator-supplied transcript), or `human:mreveley` (the repository owner's in-session attestation of that transcript, given twice). Concepts whose source pages could not be re-fetched raw have **no** `verified` key — per §5.3 they are honestly *unverified* rather than silently trusted.
- In frontmatter, cross-concept paths use the bundle-absolute form (`/excerpts/...`, §6.1 recommended). In body prose, links are relative so they also render on GitHub.

# Extension fields (producer-defined, per §4.1 "Extensions")

| Field | On | Meaning |
|---|---|---|
| `role` | Excerpt, Issue | **Primary facet (v3, IBIS-hybrid, adopted 2026-08-25)**: the unit's place in the dialectic. Enum: `issue` \| `position` \| `argument` \| `evidence` (see the v3 section below) |
| `subtype` | Excerpt | Secondary facet: the quote's speech-act flavor. Enum (v2): `question` \| `claim` \| `definition` \| `problem` \| `solution` \| `observation` \| `inference` \| `prescription` (definitions below) |
| `speaker` | Excerpt | Who said/wrote the quoted words (may differ from the page author, e.g. a quoted tweet) |
| `deps` | Excerpt | Typed relations forming the corpus DAG: list of `{ concept, rel }`. IBIS core: `responds-to` (position → issue) \| `supports` \| `objects-to`. Retained genealogy layer (non-IBIS): `answers` (directly addresses/resolves) \| `refines` \| `exemplifies` \| `precedes` |
| `availability` | Source Reference | `fetched` \| `blocked` \| `user-supplied` \| `local-clone` |
| `source_author`, `source_date` | Source Reference | Author and publication date of the external source |
| `retrieved` | Source Reference | When this research accessed it |

A concept's frontmatter `subtype` classifies its **primary** quote. Where a concept carries closely-coupled secondary quotes from the same source, each secondary quote is labeled with its own subtype inline in the body.

## The subtype enum (v2)

- **question** — an interrogative unit: the quote's work is to open an issue, not settle one.
- **claim** — an assertion about how things are.
- **definition** — a statement whose primary work is to fix what a term or thing *is* (including deflationary and functional definitions).
- **problem** — an articulated limitation, failure mode, or difficulty.
- **solution** — a built or proposed remedy: a system, format, or design answering a problem.
- **observation** — a report of events or states of affairs (empirical or historical) without a strong causal/normative thesis.
- **inference** — a conclusion explicitly reasoned from other statements; the reasoning step is the point of the quote.
- **prescription** — normative guidance: what one *should* do.

v1 of this enum lacked `question` and `definition`; both were added 2026-08-24 at the maintainer's direction and the corpus re-typed (12 claims → `definition`; the seed thread's OP → `question`). The tag `definition` now marks *only* concepts whose primary subtype is something else but which contain definitional content (currently: [typed-edges-one-bit](excerpts/aio--typed-edges-one-bit.md), [three-tier-reliability](excerpts/gd--three-tier-reliability.md), [abstraction-layer](excerpts/rl--abstraction-layer.md)). The dual-role caveat stands: a prescription usually implies a claim; the primary subtype is a judgment call recorded per-concept, with secondary roles labeled inline in multi-quote bodies.

## The role facet and issue layer (v3, IBIS-hybrid)

Adopted 2026-08-25 at the operator's direction, after the format discussion: the grammar of IBIS — Kunz & Rittel's issue-based information systems (1970; gIBIS 1988 — see [the excerpt](excerpts/ibis--wicked-problems.md), which documents this schema's own ancestry) — carried on the OKF markdown+frontmatter substrate, with OKF's provenance and trust fields retained in full.

- **issue** — an open question. Root issue nodes live in [`issues/`](issues/index.md) (`type: Issue`); an excerpt may also carry `role: issue` when a source states the question verbatim (currently one: [the skeptic's question](excerpts/rl--just-fancier-retrieval.md)). Issue nodes state questions and list positions; they never take a side.
- **position** — a contestable stance responding to an issue (`responds-to`). Competing definitions are competing positions.
- **argument** — reasoning offered for or against a position (`supports` / `objects-to`).
- **evidence** — descriptive, historical, or documentary material (consensus definitions, capability documentation, dated events). Evidence attaches to positions via `supports`/`objects-to`/`exemplifies`, or bears on issues through the genealogy layer (`precedes`) and the views.

Assignment heuristic: contested → position; consensus or historical → evidence; interrogative → issue; reasoning that attacks or supports → argument. The IBIS attachment discipline is enforced for `responds-to` (positions to issues); the retained genealogy relations may connect any roles, and are what pure IBIS cannot express (see the format discussion's downside list — this hybrid is the answer to it). One deviation from classic IBIS is deliberate: like the original, this corpus **never concludes** — verdict prose lives in `ob6to8/direction`, per the house rule.

# Tag taxonomy (the "like sorting mechanism")

Tags group perspectives across sources so a consumer can synthesize a tag view by scanning frontmatter (SPEC §3.1).

- **Topic**: `knowledge-representation`, `retrieval`, `memory`, `orchestration`, `control-flow`, `typed-edges`, `temporal`, `concurrency`, `legibility`, `determinism`, `verification`
- **Discourse**: `term-genealogy`, `hype-cycle`, `skepticism`, `practice`, `evaluation`, `risk`, `simplicity`
- **Discipline**: `loop-engineering`, `graph-engineering`, `standards`, `tooling`, `multi-agent`, `history`, `academic`, `workflow-engines`, `durable-execution`, `argumentation` (the last three added in research push #2 for the workflow-engine and coordination lineages)

**A tag has to divide the corpus.** Two families were dropped on 2026-08-25 (operator-directed) because they did not:

- The **practice era** family — `era-agentic`, `era-classical`, `era-knowledge-graph`. `era-agentic` sat on 60 of 70 excerpts, which is not a sorting mechanism but a restatement of what the bundle is about. The period distinction it was meant to draw is already carried by `history` (on all ten former `era-classical` excerpts) and by each source's `source_date`.
- The **speech-act echoes** — `definition`, `prescription`, `solution`, `prescription-hybrid`. These duplicated values of the `subtype` enum, which every excerpt already carries as a first-class field; `prescription` and `solution` were never in this taxonomy to begin with. Sort by `subtype` instead.

Expect the surviving tags to stay lopsided toward this bundle's subject — that is what a single research push produces. The test is not evenness but whether a tag splits the corpus into a set worth reading on its own.

# Verification

Quote fidelity is the core risk of a bundle like this (quotes were initially extracted by an LLM-assisted fetcher). Mitigation: every persisted quote was re-checked by fetching the source page **raw** (curl) and mechanically matching normalized quote fragments against the normalized page text (whitespace collapsed; curly/straight quotes and dash variants unified). Only fragments that matched exactly earned `verified: { by: process:curl-quote-check }`. Outcomes:

- Verified verbatim: all excerpts from 34 of 38 sources (research push #2 — the [paradigm-or-hype investigation](https://github.com/ob6to8/direction/blob/main/mark_reveley/2026-08-25-graph-engineering-synthesis/paradigm-or-hype.md) — added 10 sources and 15 excerpts on 2026-08-24; all 10 new sources curl-verified).
- **Unverified** (no `verified` key): [Oracle blog](references/oracle-agent-loop-decoded.md) (firewall page on raw fetch) and [Britannica](references/britannica-graph-theory.md) (bot challenge). Their quotes are as extracted on first fetch, flagged in each excerpt's analysis.
- **User-attested, twice, and matched**: the seed [Reddit thread transcript](references/reddit-llmdevs-graph-trend.md) (reddit.com is unfetchable from this environment) was supplied verbatim in-session by the repository owner on 2026-08-24 and re-supplied identically on 2026-08-25; the two supplies and all six seed excerpts were mechanically matched (`process:transcript-match`), so the seed excerpts now carry machine-confirmed stamps atop the double human attestation.
- **Local-clone**: [OKF SPEC.md](references/okf-spec.md) (commit `9a15b13`) and [12-factor-agents](references/humanlayer-12-factor-agents.md) (commit `d20c728`) — quoted directly from files on disk.

# Open questions for the maintainer

1. **OKF fidelity vs. extensions.** ~~Keep OKF, extend, or migrate?~~ Resolved 2026-08-25: **IBIS-hybrid adopted (v3)** — IBIS grammar (roles + core relations) on the OKF carrier, trust fields retained, genealogy relations kept as a marked non-IBIS layer.
2. **Enum coverage.** ~~Should the enum grow `question` and `definition`?~~ Resolved 2026-08-24: maintainer directed the extension; corpus re-typed to the eight-value enum (v2 above).
3. **"Historically."** The exact phrase "graph engineering" had no stable pre-2026 identity; the history here is organized as three lineages (mathematical, knowledge-representation, systems/orchestration) that the 2026 term collapses together — see the [synthesis](https://github.com/ob6to8/direction/blob/main/mark_reveley/2026-08-25-graph-engineering-synthesis/graph-engineering.md). If "historically" was meant to target one specific prior sense (e.g. knowledge-graph engineering as an ontology-engineering discipline, or graph *data* engineering), the reference set can be deepened in that direction.
4. **Granularity.** One concept per quote (with rare same-source secondary quotes). Alternative: one concept per source with quote lists. Current choice optimizes the tag/dep graph; say the word to re-shard.
5. **Inaccessible sources.** The two Reddit threads (seed + FLARE) and X/Twitter posts are unreachable from this environment; tweet texts are recorded *as reported by* secondary sources, with the discrepancies noted (e.g. "nine words" vs "twelve words", 2.6M vs 2.9M views). Supply transcripts/screenshots to upgrade them to attested.
