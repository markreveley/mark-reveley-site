---
type: Quote
resource: "https://arxiv.org/pdf/2605.27361"
quote: |-
  Modern retrieval agents expose many configuration choices—LLM, retriever, number of documents, number of hops, and synthesis strategy—each shaping both
  answer quality and serving cost. Today, these pipelines are typically hand-tuned
  once per workload, leaving substantial per-query optimization untapped. We formulate Query2Conf : given a natural-language query and either an accuracy or
  a budget target, select from a predefined pipeline catalog the configuration that
  minimizes cost (or maximizes accuracy) at inference time. We propose BRANE
  which uses an LLM to convert each query into workload-specific characteristics,
  then trains a lightweight per-configuration predictor that estimates whether the
  pipeline will answer the query correctly. At inference time, BRANE selects the
  configuration that maximizes predicted correctness penalized by cost, exposing a
  tunable cost–quality tradeoff without retraining. Across MuSiQue, BrowseCompPlus, and FinanceBench, BRANE consistently pushes the cost–quality Pareto
  frontier, matches the best fixed configuration’s accuracy at up to 89% lower cost,
  and outperforms LLM-routing, rule-based, and fine-tuned Qwen3-4B baselines.
  These results show that per-query configuration of the full retrieval pipeline is a
  practical alternative to static workload-level tuning.
date_added: "2026-09-17"
tags:
  - retrieval-augmented-generation
  - model-routing
  - inference-costs
  - evaluation
source_title: "Natural Language Query to Configuration for Retrieval Agents"
source_department: "UC Berkeley · University of Washington · Microsoft Azure Research - Systems"
source_author: "Melissa Z. Pan, Negar Arabzadeh, Mathew Jacob, Fiodar Kazhamiaka, Esha Choukse, and Matei Zaharia"
source_date: "2026-05-26"
verification_status: "not-found"
verification_date: "2026-09-17"
# Exact-match difference: supplied "BrowseCompPlus" is "BrowseComp-Plus" in the source.
---
