# Bookmarks

This folder is the bookmarks library: outside pages worth keeping, such as
articles, papers, repositories, documentation, videos and posts. It moved here
from the [investigations repository](https://github.com/markreveley/investigations/blob/main/README.md) on 2026-11-03, and
investigations cite its entries by URL. The site build will publish it; see
[SPEC-bookmark-dag-claude-opus-5-5-effort-low.md](SPEC-bookmark-dag-claude-opus-5-5-effort-low.md).
The repository's guidance is in [README.md](../README.md).

## How the library is organised

Each resource is one Markdown file in `items/`. Each topic it can be filed
under is one file in `topics/`. Both use the node format from
[artifact-dag](https://github.com/markreveley/artifact-dag), so the folder can
be checked with its validator and drawn as a graph in its viewer.

A resource file has these fields:

- `id` is `res:` followed by the file name.
- `url` is the page itself.
- `hacker_news`, when present, is the Hacker News thread that led to the
  page.
- `added` is the date the resource came in. It is intake data for us, and the site
  does not show it.
- `published`, when known, is the date the page itself was published
  (`YYYY`, `YYYY-MM` or `YYYY-MM-DD`). The site shows it and sorts by it,
  newest first, with undated resources last.
- `status` is `unread` for a resource with an overview, or `stub` for one
  whose overview still needs writing by hand.
- `tags` says what kind of thing it is, such as `paper`, `repo`, `video`,
  `docs` or `thread`.
- `topics` lists the topics it is about.

The text under the frontmatter is a short overview in our own words.

A topic is an ordinary definition node (`def:agent-sandboxes`). A narrower
topic `refines` a broader one, so Agent sandboxes sits under both AI agents
and Sandboxing. The index below lists such a topic once, under its first
parent. A resource filed under several topics appears under each of them.

## Checking and rebuilding

The site build validates the collection and publishes it; see
[ARCHITECTURE.md](../ARCHITECTURE.md). To validate it by hand, run the artifact-dag
checker from a checkout of that repository:

```sh
npm run check -- <path-to-site>/bookmarks --lint
```

The index below is generated from the files. After adding or changing a
resource, rebuild it:

```sh
python3 bookmarks/build_index.py
```

## First intake, 2026-10-23

The first batch came from the browser tabs open on 2026-10-23: 397 tabs in 17
windows, which became 258 resources under 36 topics. The intake skipped the
following:

- GitHub pages under our own accounts (markreveley, identikey and
  WorldTreeNetwork), and repository settings pages.
- Password-manager, Discord, Gmail and localhost tabs, and local files.
- Personal account and app pages, such as calendars, Drive, Photos, bookings,
  checkouts, logins, dashboards, chats and search results.
- Duplicate tabs.

Two tabs for the same document, such as an arXiv abstract and its PDF, became
one resource. A Hacker News thread and its linked page also became one
resource: the page is the `url`, and the thread is `hacker_news`.

Overviews were written from each page's text where it could be fetched. Where
the page blocked automated reading, the overview says so and relies on the
title and description. Reddit and X could not be read at all, so their 21
resources are stubs that record the post title for filling in by hand.

## Index

<!-- INDEX:START -->

### AI agents

- [Claude Duet](items/claude-duet.md)
- [Hybrid Reasoning Agents](items/hybrid-reasoning-agents.md)
- [Infrastructure for AI Agents](items/infrastructure-for-ai-agents.md)
- [live-smith](items/live-smith.md)
- [Maria Gorskikh](items/maria-gorskikh.md)
- [Meta Muse exposes users' secrets when they share conversations](items/meta-muse-exposes-users-secrets-when-they-share.md)
- [Welcome to the Era of Experience](items/welcome-to-the-era-of-experience.md)
- [What it costs to host an AI agent 24/7](items/what-it-costs-to-host-an-ai-agent-24-7.md)

#### Agent authority

- [Access management for multi-user agents (Alter demo)](items/access-management-for-multi-user-agents-alter-demo.md)
- [Alter documentation](items/alter-documentation.md)
- [Alter Vault](items/alter-vault.md)
- [Authority control plane: blast radius (Nuggets)](items/authority-control-plane-blast-radius-nuggets.md)
- [Cloudflare OS](items/cloudflare-os.md)
- [Composio](items/composio.md)
- [Enterprise AI governance framework (Nuggets)](items/enterprise-ai-governance-framework-nuggets.md)
- [Fly.io Sprites connectors](items/fly-io-sprites-connectors.md)
- [Glossary (Nuggets)](items/glossary-nuggets.md)
- [Guardrails for agentic AI](items/guardrails-for-agentic-ai.md)
- [How we're rethinking work at Cloudflare with Cloudflare OS](items/how-were-rethinking-work-at-cloudflare-with-cloudflare-os.md)
- [Infrastructure for AI Agents](items/infrastructure-for-ai-agents.md)
- [Isolate store data per user (LangSmith)](items/isolate-store-data-per-user-langsmith.md)
- [langchain-nuggets](items/langchain-nuggets.md)
- [Nuggets](items/nuggets.md)
- [Nuggets launches the Authority Control Plane](items/nuggets-launches-the-authority-control-plane.md)
- [Nuggets on LinkedIn](items/nuggets-on-linkedin.md)
- [Nuggets on X](items/nuggets-on-x.md) (stub)
- [openclaw-alter-plugin](items/openclaw-alter-plugin.md)
- [Procurement questions for evaluating AI systems (Nuggets)](items/procurement-questions-for-evaluating-ai-systems-nuggets.md)
- [Propagate identity into memory layers (Alter)](items/propagate-identity-into-memory-layers-alter.md)
- [RFC 8693: OAuth 2.0 Token Exchange](items/rfc-8693-oauth-2-0-token-exchange.md)

#### Agent frameworks

- [Cloudflare OS](items/cloudflare-os.md)
- [Composio](items/composio.md)
- [Elixir/OTP agent runtime running in 15+ companies, now open source](items/elixir-otp-agent-runtime-running-in-15-companies-now-open.md) (stub)
- [Generative user interfaces (AI SDK)](items/generative-user-interfaces-ai-sdk.md)
- [How to host a remote MCP server](items/how-to-host-a-remote-mcp-server.md)
- [Isolate store data per user (LangSmith)](items/isolate-store-data-per-user-langsmith.md)
- [langchain-nuggets](items/langchain-nuggets.md)
- [live-connector v1.0.0](items/live-connector-v1-0-0.md)
- [Model Context Protocol architecture overview](items/model-context-protocol-architecture-overview.md)
- [OpenAI Agents API](items/openai-agents-api.md)
- [Pepe](items/pepe.md)
- [Persistence and storage (Jido)](items/persistence-and-storage-jido.md)
- [TanStack AI](items/tanstack-ai.md)
- [TanStack AI 1.0 is stable (r/LLMDevs)](items/tanstack-ai-1-0-is-stable-r-llmdevs.md) (stub)
- [The runtime that was ready for AI all along](items/the-runtime-that-was-ready-for-ai-all-along.md)

#### Agent harnesses

- [A single pane of glass for all your cloud agents (Warp Oz)](items/a-single-pane-of-glass-for-all-your-cloud-agents-warp-oz.md)
- [Andrew Ng on graph engineering for agents](items/andrew-ng-on-graph-engineering-for-agents.md)
- [astra-flash-orchestrator (codex-on-crack)](items/astra-flash-orchestrator-codex-on-crack.md)
- [Effective harnesses for long-running agents](items/effective-harnesses-for-long-running-agents.md)
- [Five months treating bugs like patients and coding agents like a medical team](items/five-months-treating-bugs-like-patients-and-coding-agents.md)
- [Harness engineering for coding agent users](items/harness-engineering-for-coding-agent-users.md)
- [Have coding agents made us forget 'program to an interface'?](items/have-coding-agents-made-us-forget-program-to-an-interface.md) (stub)
- [How Claude Code is used in practice](items/how-claude-code-is-used-in-practice.md)
- [OpenAI Agents API](items/openai-agents-api.md)
- [Orchestration package that cut GPT-6 Astra usage by 98%](items/orchestration-package-that-cut-gpt-6-astra-usage-by-98.md) (stub)
- [OtoDock](items/otodock.md)
- [Paperclip](items/paperclip.md)
- [Pullboard](items/pullboard.md)
- [Testing agent skills systematically with evals](items/testing-agent-skills-systematically-with-evals.md)

#### Agent sandboxes

- [Agent sandboxes: isolated runtimes for testing agent behaviour](items/agent-sandboxes-isolated-runtimes-for-testing-agent.md)
- [AI sandbox pricing compared](items/ai-sandbox-pricing-compared.md)
- [Code interpreter pricing](items/code-interpreter-pricing.md)
- [Ephemeral vs persistent sandboxes](items/ephemeral-vs-persistent-sandboxes.md)
- [Fly.io Learn](items/fly-io-learn.md)
- [Fly.io Sprites connectors](items/fly-io-sprites-connectors.md)
- [Fly.io vs Cloudflare: agent computers vs ephemeral edge containers](items/fly-io-vs-cloudflare-agent-computers-vs-ephemeral-edge.md)
- [Fly.io vs Daytona](items/fly-io-vs-daytona.md)
- [Fly.io vs E2B](items/fly-io-vs-e2b.md)
- [Fly.io vs Modal](items/fly-io-vs-modal.md)
- [Fly.io vs Vercel Sandbox](items/fly-io-vs-vercel-sandbox.md)
- [How to run LLM-generated Python safely](items/how-to-run-llm-generated-python-safely.md)
- [OpenShell](items/openshell.md)
- [RL sandbox pricing](items/rl-sandbox-pricing.md)
- [Sprites vs E2B vs Modal vs Daytona](items/sprites-vs-e2b-vs-modal-vs-daytona.md)
- [The Sprites ecosystem](items/the-sprites-ecosystem.md)
- [VMs won't contain cyber-capable agents](items/vms-wont-contain-cyber-capable-agents.md)
- [What it costs to run Claude Code or Codex in a cloud sandbox](items/what-it-costs-to-run-claude-code-or-codex-in-a-cloud-sandbox.md)
- [Where to run agent code: sandbox providers compared](items/where-to-run-agent-code-sandbox-providers-compared.md)

### AI industry

- [A benchmark map of the US economy (Mercor)](items/a-benchmark-map-of-the-us-economy-mercor.md)
- [After automation: solo founding will be the default](items/after-automation-solo-founding-will-be-the-default.md)
- [Expanding Daybreak as the cyber defense window narrows](items/expanding-daybreak-as-the-cyber-defense-window-narrows.md)
- [How we're rethinking work at Cloudflare with Cloudflare OS](items/how-were-rethinking-work-at-cloudflare-with-cloudflare-os.md)
- [Meet the AI ethicists shaping Claude's conscience](items/meet-the-ai-ethicists-shaping-claudes-conscience.md)
- [METR lands in AI's doom debate](items/metr-lands-in-ais-doom-debate.md)
- [OpenAI cannot make AI safe on its own (letter)](items/openai-cannot-make-ai-safe-on-its-own-letter.md)
- [OpenAI is well positioned to fast-follow Jev](items/openai-is-well-positioned-to-fast-follow-jev.md)
- [Ramp AI Index, August 2026](items/ramp-ai-index-august-2026.md)
- [Software Engineer, RL Environments at AfterQuery](items/software-engineer-rl-environments-at-afterquery.md)
- [The AI industry has already spent $65 million ahead of the midterms](items/the-ai-industry-has-already-spent-65-million-ahead-of-the.md)
- [We're still underestimating what AI really means (Ryan Dahl)](items/were-still-underestimating-what-ai-really-means-ryan-dahl.md)
- [Why math dumped OpenAI](items/why-math-dumped-openai.md)

### AI safety

- ['We were looking at it wrong': the explosive claim that's upended the AI world](items/we-were-looking-at-it-wrong-the-explosive-claim-thats.md)
- [Buck Shlegeris](items/buck-shlegeris.md)
- [Human-AI partnerships are for alignment, not capability](items/human-ai-partnerships-are-for-alignment-not-capability.md)
- [Meet the AI ethicists shaping Claude's conscience](items/meet-the-ai-ethicists-shaping-claudes-conscience.md)
- [METR](items/metr.md)
- [METR lands in AI's doom debate](items/metr-lands-in-ais-doom-debate.md)
- [OpenAI cannot make AI safe on its own (letter)](items/openai-cannot-make-ai-safe-on-its-own-letter.md)
- [Redwood Research team](items/redwood-research-team.md)
- [Task-completion time horizons of frontier AI models](items/task-completion-time-horizons-of-frontier-ai-models.md)
- [The first big AI disaster is yet to happen](items/the-first-big-ai-disaster-is-yet-to-happen.md)
- [When AI builds itself](items/when-ai-builds-itself.md)
- [Would catching your AIs trying to escape convince AI developers to slow down?](items/would-catching-your-ais-trying-to-escape-convince-ai.md)

#### Interpretability

- ['We were looking at it wrong' (r/singularity)](items/we-were-looking-at-it-wrong-r-singularity.md) (stub)
- ['We were looking at it wrong': the explosive claim that's upended the AI world](items/we-were-looking-at-it-wrong-the-explosive-claim-thats.md)
- [AI interpretability is further along than I thought](items/ai-interpretability-is-further-along-than-i-thought.md)
- [ConvNeXt microscope (Neural networks are already clean)](items/convnext-microscope-neural-networks-are-already-clean.md)
- [Explosive document claims AI is not what we think (r/Futurism)](items/explosive-document-claims-ai-is-not-what-we-think-r-futurism.md) (stub)
- [Explosive document claims that AI is not what we think](items/explosive-document-claims-that-ai-is-not-what-we-think.md)
- [Neural networks are already clean](items/neural-networks-are-already-clean.md)
- [Nick Cammarata](items/nick-cammarata.md)

### AI search

- [AI optimization test: footers are back like 2003](items/ai-optimization-test-footers-are-back-like-2003.md)
- [ChatGPT built its own search index](items/chatgpt-built-its-own-search-index.md)
- [How Hacker News ranking really works](items/how-hacker-news-ranking-really-works.md)
- [Publish stats, get cited](items/publish-stats-get-cited.md)
- [Synthetic deep web: how the internet is becoming invisible](items/synthetic-deep-web-how-the-internet-is-becoming-invisible.md)
- [The recency bias that's reshaping AI search](items/the-recency-bias-thats-reshaping-ai-search.md)

### AI-assisted programming

- ['AI' is not a tool (Rich Hickey)](items/ai-is-not-a-tool-rich-hickey.md)
- [Claude Academy](items/claude-academy.md)
- [Code is clay now](items/code-is-clay-now.md)
- [Delta](items/delta.md)
- [Evolving programming languages in the AI era](items/evolving-programming-languages-in-the-ai-era.md)
- [Five months treating bugs like patients and coding agents like a medical team](items/five-months-treating-bugs-like-patients-and-coding-agents.md)
- [Grieving the loss of details](items/grieving-the-loss-of-details.md)
- [Harness engineering for coding agent users](items/harness-engineering-for-coding-agent-users.md)
- [Have coding agents made us forget 'program to an interface'?](items/have-coding-agents-made-us-forget-program-to-an-interface.md) (stub)
- [How Claude Code is used in practice](items/how-claude-code-is-used-in-practice.md)
- [How Cloudflare enforces engineering standards using AI](items/how-cloudflare-enforces-engineering-standards-using-ai.md)
- [How to read code](items/how-to-read-code.md)
- [Human-AI partnerships are for alignment, not capability](items/human-ai-partnerships-are-for-alignment-not-capability.md)
- [I am done with this (r/ClaudeAI)](items/i-am-done-with-this-r-claudeai.md) (stub)
- [I'm sorry, but you still have to think](items/im-sorry-but-you-still-have-to-think.md)
- [On the foolishness of natural language programming (1978)](items/on-the-foolishness-of-natural-language-programming-1978.md)
- [OpenSpec](items/openspec.md)
- [Per-PR preview environments for coding agents](items/per-pr-preview-environments-for-coding-agents.md)
- [Pullboard](items/pullboard.md)
- [Redesigning source control at Anthropic](items/redesigning-source-control-at-anthropic.md)
- [Replace PRs with Delta, now in public beta](items/replace-prs-with-delta-now-in-public-beta.md)
- [Rust off Rails](items/rust-off-rails.md)
- [Sean Goedecke: posts tagged ai](items/sean-goedecke-posts-tagged-ai.md)
- [Shipping 2,500 PRs in a month (talk)](items/shipping-2-500-prs-in-a-month-talk.md) (stub)
- [Software Engineering after the Vibe Shift (book)](items/software-engineering-after-the-vibe-shift-book.md)
- [Software engineers don't get to be Luddites about AI](items/software-engineers-dont-get-to-be-luddites-about-ai.md)
- [Software's centaur age may last decades](items/softwares-centaur-age-may-last-decades.md)
- [Tell agents the why, not just the how](items/tell-agents-the-why-not-just-the-how.md)
- [The compiler was supposed to end programming too](items/the-compiler-was-supposed-to-end-programming-too.md)
- [Tool or automation? You make the decision each time](items/tool-or-automation-you-make-the-decision-each-time.md)

### Cloud hosting

- [Best cloud for startups](items/best-cloud-for-startups.md)
- [Best Django hosting providers in 2026](items/best-django-hosting-providers-in-2026.md)
- [Best Docker hosting providers in 2026](items/best-docker-hosting-providers-in-2026.md)
- [Best Laravel hosting providers in 2026](items/best-laravel-hosting-providers-in-2026.md)
- [Best Python hosting providers in 2026](items/best-python-hosting-providers-in-2026.md)
- [celld](items/celld.md)
- [DeepInfer](items/deepinfer.md)
- [Deno is joining Cloudflare](items/deno-is-joining-cloudflare.md)
- [Docker is weird](items/docker-is-weird.md)
- [Fly.io Learn](items/fly-io-learn.md)
- [Fly.io vs Railway](items/fly-io-vs-railway.md)
- [Fly.io vs Render](items/fly-io-vs-render.md)
- [Golang hosting](items/golang-hosting.md)
- [How serverless hosting scales](items/how-serverless-hosting-scales.md)
- [How to host a remote MCP server](items/how-to-host-a-remote-mcp-server.md)
- [JavaScript containers (Ryan Dahl)](items/javascript-containers-ryan-dahl.md)
- [Maria Gorskikh](items/maria-gorskikh.md)
- [MicroVM vs container](items/microvm-vs-container.md)
- [NixOS is making me less afraid](items/nixos-is-making-me-less-afraid.md)
- [Node.js hosting](items/node-js-hosting.md)
- [PaaS pricing compared](items/paas-pricing-compared.md)
- [Per-PR preview environments for coding agents](items/per-pr-preview-environments-for-coding-agents.md)
- [Postgres hosting](items/postgres-hosting.md)
- [Rails hosting](items/rails-hosting.md)
- [Rust hosting](items/rust-hosting.md)
- [Taking a Lovable, Bolt or Replit app to production](items/taking-a-lovable-bolt-or-replit-app-to-production.md)
- [Top Heroku alternatives](items/top-heroku-alternatives.md)
- [What I self-host](items/what-i-self-host.md)
- [What is a Firecracker microVM?](items/what-is-a-firecracker-microvm.md)
- [What it costs to host an AI agent 24/7](items/what-it-costs-to-host-an-ai-agent-24-7.md)

### Computer science

- [Bernoulli distribution (Wikipedia)](items/bernoulli-distribution-wikipedia.md)
- [Differentiable self-organizing systems (Distill thread)](items/differentiable-self-organizing-systems-distill-thread.md)
- [Halting problem (Wikipedia)](items/halting-problem-wikipedia.md)
- [Introducing Minotaur: a GPU-less AI architecture](items/introducing-minotaur-a-gpu-less-ai-architecture.md)
- [Minotaur deep dive: reasoning without a language model](items/minotaur-deep-dive-reasoning-without-a-language-model.md)
- [Natural language processing (Wikipedia)](items/natural-language-processing-wikipedia.md)
- [On the foolishness of natural language programming (1978)](items/on-the-foolishness-of-natural-language-programming-1978.md)
- [Reinventing entropy: compression is intelligence, part 1](items/reinventing-entropy-compression-is-intelligence-part-1.md)

### Developer tools

- [A User's Guide to the Z-Shell](items/a-users-guide-to-the-z-shell.md)
- [EPOMAKER Galaxy100 QMK/VIA keyboard](items/epomaker-galaxy100-qmk-via-keyboard.md)
- [If you don't run your own LLM proxy, how do you know what's going on?](items/if-you-dont-run-your-own-llm-proxy-how-do-you-know-whats.md)
- [Learn Neovim the practical way](items/learn-neovim-the-practical-way.md)
- [My fast Zsh setup without Oh My Zsh](items/my-fast-zsh-setup-without-oh-my-zsh.md)
- [Nordwand Mono](items/nordwand-mono.md)
- [OpenAI CLI](items/openai-cli.md)
- [Pro Git](items/pro-git.md)

### Digital identity

- [banana-web](items/banana-web.md)
- [FOKS: Federated Open Key Service](items/foks-federated-open-key-service.md)
- [Identity (Stanford Encyclopedia of Philosophy)](items/identity-stanford-encyclopedia-of-philosophy.md)
- [Propagate identity into memory layers (Alter)](items/propagate-identity-into-memory-layers-alter.md)
- [The Digital Identity Event Horizon](items/the-digital-identity-event-horizon.md)
- [Woman charged with computer fraud over a scam CashApp account in her name](items/woman-charged-with-computer-fraud-over-a-scam-cashapp.md)

### Education

- [Tilden Prep part-time high school program](items/tilden-prep-part-time-high-school-program.md)

### Evals

- [A benchmark map of the US economy (Mercor)](items/a-benchmark-map-of-the-us-economy-mercor.md)
- [Asking an LLM for confidence](items/asking-an-llm-for-confidence.md)
- [Benchmarking testing in automated theorem proving](items/benchmarking-testing-in-automated-theorem-proving.md)
- [Evaluation best practices (OpenAI)](items/evaluation-best-practices-openai.md)
- [Exploring model graders for reinforcement fine-tuning](items/exploring-model-graders-for-reinforcement-fine-tuning.md)
- [FActScore](items/factscore.md)
- [Faults in our formal benchmarking](items/faults-in-our-formal-benchmarking.md)
- [JevBench](items/jevbench.md)
- [Large Language Models Pass the Turing Test](items/large-language-models-pass-the-turing-test.md)
- [Loco blog](items/loco-blog.md)
- [METR](items/metr.md)
- [OpenAI Evals is winding down; the alternatives skip the statistics](items/openai-evals-is-winding-down-the-alternatives-skip-the.md)
- [Reduced my Jev-as-a-judge calibration error](items/reduced-my-jev-as-a-judge-calibration-error.md) (stub)
- [RL sandbox pricing](items/rl-sandbox-pricing.md)
- [Sean Goedecke: posts tagged papers](items/sean-goedecke-posts-tagged-papers.md)
- [Software Engineer, RL Environments at AfterQuery](items/software-engineer-rl-environments-at-afterquery.md)
- [Task-completion time horizons of frontier AI models](items/task-completion-time-horizons-of-frontier-ai-models.md)
- [Testing agent skills systematically with evals](items/testing-agent-skills-systematically-with-evals.md)
- [The illusion of 'The Illusion of Thinking'](items/the-illusion-of-the-illusion-of-thinking.md)
- [TypeSafe workflow evals](items/typesafe-workflow-evals.md)

### Formal verification

- [About the Lean FRO](items/about-the-lean-fro.md)
- [Benchmarking testing in automated theorem proving](items/benchmarking-testing-in-automated-theorem-proving.md)
- [Care for a little more AI? (Proofs and Prompts)](items/care-for-a-little-more-ai-proofs-and-prompts.md)
- [Faults in our formal benchmarking](items/faults-in-our-formal-benchmarking.md)
- [I built the RealWorld app in Lean 4](items/i-built-the-realworld-app-in-lean-4.md)
- [Lean now ships with verified kernels](items/lean-now-ships-with-verified-kernels.md)
- [Lean, Mathlib and AI-verified math explained](items/lean-mathlib-and-ai-verified-math-explained.md)
- [LLMs are making formal software verification feasible at a much larger scale](items/llms-are-making-formal-software-verification-feasible-at-a.md)
- [On Proof and Progress in Mathematics (Thurston)](items/on-proof-and-progress-in-mathematics-thurston.md)
- [Why math dumped OpenAI](items/why-math-dumped-openai.md)

### Hardware

- [EPOMAKER Galaxy100 QMK/VIA keyboard](items/epomaker-galaxy100-qmk-via-keyboard.md)

### Language models

- ['We were looking at it wrong': the explosive claim that's upended the AI world](items/we-were-looking-at-it-wrong-the-explosive-claim-thats.md)
- [Alex Wang on X](items/alex-wang-on-x.md) (stub)
- [DeepInfer](items/deepinfer.md)
- [Dense X Retrieval: what retrieval granularity should we use?](items/dense-x-retrieval-what-retrieval-granularity-should-we-use.md)
- [Every AI model has the same controversial take on humans](items/every-ai-model-has-the-same-controversial-take-on-humans.md)
- [Hybrid Reasoning Agents](items/hybrid-reasoning-agents.md)
- [If you don't run your own LLM proxy, how do you know what's going on?](items/if-you-dont-run-your-own-llm-proxy-how-do-you-know-whats.md)
- [Large Language Models Pass the Turing Test](items/large-language-models-pass-the-turing-test.md)
- [lgit: source control for the AI era](items/lgit-source-control-for-the-ai-era.md)
- [Minotaur deep dive: reasoning without a language model](items/minotaur-deep-dive-reasoning-without-a-language-model.md)
- [Natural language processing (Wikipedia)](items/natural-language-processing-wikipedia.md)
- [Should I learn RAG as a backend dev?](items/should-i-learn-rag-as-a-backend-dev.md) (stub)
- [The illusion of 'The Illusion of Thinking'](items/the-illusion-of-the-illusion-of-thinking.md)
- [Welcome to the Era of Experience](items/welcome-to-the-era-of-experience.md)
- [WorldTUI: a 360M model that pretends to be a terminal](items/worldtui-a-360m-model-that-pretends-to-be-a-terminal.md)
- [You could have invented transformers from memory](items/you-could-have-invented-transformers-from-memory.md)

#### Decision models

- [Asking an LLM for confidence](items/asking-an-llm-for-confidence.md)
- [Build your own decision model](items/build-your-own-decision-model.md)
- [Call Jev a decision model (Maggie Appleton)](items/call-jev-a-decision-model-maggie-appleton.md) (stub)
- [Elixir client for Jev](items/elixir-client-for-jev.md) (stub)
- [Introducing System One models and Jev](items/introducing-system-one-models-and-jev.md)
- [Jeffy](items/jeffy.md)
- [Jev AI vs LLMs: when to use a decision model](items/jev-ai-vs-llms-when-to-use-a-decision-model.md)
- [Jev introduces a new shape of LLM](items/jev-introduces-a-new-shape-of-llm.md)
- [Jev meets the trolley problem](items/jev-meets-the-trolley-problem.md)
- [Jev wasn't built to make agents (Kyle Jeong)](items/jev-wasnt-built-to-make-agents-kyle-jeong.md) (stub)
- [Jev's architecture unmasked](items/jevs-architecture-unmasked.md)
- [Jev-style decisions with local Qwen](items/jev-style-decisions-with-local-qwen.md) (stub)
- [JevBench](items/jevbench.md)
- [jevchat: Jev as a (lousy) chatbot](items/jevchat-jev-as-a-lousy-chatbot.md)
- [Kev](items/kev.md)
- [OpenAI is well positioned to fast-follow Jev](items/openai-is-well-positioned-to-fast-follow-jev.md)
- [Reduced my Jev-as-a-judge calibration error](items/reduced-my-jev-as-a-judge-calibration-error.md) (stub)
- [Sean Goedecke: posts tagged ai](items/sean-goedecke-posts-tagged-ai.md)
- [SemIf](items/semif.md)
- [Six clones of Jev in two days (AINews)](items/six-clones-of-jev-in-two-days-ainews.md)
- [system-one-adapter-python](items/system-one-adapter-python.md)
- [TypeSafe AI documentation](items/typesafe-ai-documentation.md)
- [TypeSafe workflow evals](items/typesafe-workflow-evals.md)

#### Local AI

- [commonwealth-ai](items/commonwealth-ai.md)
- [Jeffy](items/jeffy.md)
- [Jev-style decisions with local Qwen](items/jev-style-decisions-with-local-qwen.md) (stub)
- [Kev](items/kev.md)
- [SemIf](items/semif.md)
- [svrn ai](items/svrn-ai.md)
- [svrnmesh releases](items/svrnmesh-releases.md)

### Linux

- [Docker is weird](items/docker-is-weird.md)
- [Linux Journey](items/linux-journey.md)
- [LWN.net weekly edition archives](items/lwn-net-weekly-edition-archives.md)
- [NixOS is making me less afraid](items/nixos-is-making-me-less-afraid.md)
- [OverTheWire wargames](items/overthewire-wargames.md)
- [Trusting-trust attack against an entire Linux distribution](items/trusting-trust-attack-against-an-entire-linux-distribution.md)

### Music technology

- [fixdenorm (Gen reference)](items/fixdenorm-gen-reference.md)
- [Gen (Max 8 documentation)](items/gen-max-8-documentation.md)
- [How I think about Instagram content (20M+ monthly views)](items/how-i-think-about-instagram-content-20m-monthly-views.md) (stub)
- [live-connector v1.0.0](items/live-connector-v1-0-0.md)
- [live-smith](items/live-smith.md)
- [YuE2: frontier music with symbolic planning](items/yue2-frontier-music-with-symbolic-planning.md)

### Networking

- [Computer Networks: A Systems Approach, Part I](items/computer-networks-a-systems-approach-part-i.md)

### Nonprofits

- [Inurement and private benefit (IRS)](items/inurement-and-private-benefit-irs.md)

### Personal writing

- [Grieving the loss of details](items/grieving-the-loss-of-details.md)
- [The desert, edge-dwellers and life-death-life cycles](items/the-desert-edge-dwellers-and-life-death-life-cycles.md)
- [The gun to your head (Nick Cammarata)](items/the-gun-to-your-head-nick-cammarata.md)
- [Things to know when you get cancer](items/things-to-know-when-you-get-cancer.md)

### Philosophy

- [Identity (Stanford Encyclopedia of Philosophy)](items/identity-stanford-encyclopedia-of-philosophy.md)
- [On Proof and Progress in Mathematics (Thurston)](items/on-proof-and-progress-in-mathematics-thurston.md)
- [Propositions (Stanford Encyclopedia of Philosophy)](items/propositions-stanford-encyclopedia-of-philosophy.md)

### Programming languages

- [Evolving programming languages in the AI era](items/evolving-programming-languages-in-the-ai-era.md)

#### Elixir

- [Elixir client for Jev](items/elixir-client-for-jev.md) (stub)
- [Elixir/OTP agent runtime running in 15+ companies, now open source](items/elixir-otp-agent-runtime-running-in-15-companies-now-open.md) (stub)
- [Evolving programming languages in the AI era](items/evolving-programming-languages-in-the-ai-era.md)
- [Mix (Elixir docs)](items/mix-elixir-docs.md)
- [Pepe](items/pepe.md)
- [Persistence and storage (Jido)](items/persistence-and-storage-jido.md)
- [The BEAM Book](items/the-beam-book.md)
- [The runtime that was ready for AI all along](items/the-runtime-that-was-ready-for-ai-all-along.md)

#### Lean

- [About the Lean FRO](items/about-the-lean-fro.md)
- [Evaluating expressions (Functional Programming in Lean)](items/evaluating-expressions-functional-programming-in-lean.md)
- [Faults in our formal benchmarking](items/faults-in-our-formal-benchmarking.md)
- [I built the RealWorld app in Lean 4](items/i-built-the-realworld-app-in-lean-4.md)
- [Lean now ships with verified kernels](items/lean-now-ships-with-verified-kernels.md)
- [Lean, Mathlib and AI-verified math explained](items/lean-mathlib-and-ai-verified-math-explained.md)
- [Let's code math in Lean 4](items/lets-code-math-in-lean-4.md)

#### Python

- [Best Django hosting providers in 2026](items/best-django-hosting-providers-in-2026.md)
- [Best Python hosting providers in 2026](items/best-python-hosting-providers-in-2026.md)
- [How to run LLM-generated Python safely](items/how-to-run-llm-generated-python-safely.md)
- [State of the art in Python 2026?](items/state-of-the-art-in-python-2026.md) (stub)
- [Think Python, 3rd edition](items/think-python-3rd-edition.md)

#### Rust

- [Building a distributed CRDT layer for Git (Conrad Irwin)](items/building-a-distributed-crdt-layer-for-git-conrad-irwin.md)
- [diamond-types](items/diamond-types.md)
- [Hello, Cargo! (The Rust Programming Language)](items/hello-cargo-the-rust-programming-language.md)
- [Loco blog](items/loco-blog.md)
- [Rust hosting](items/rust-hosting.md)
- [Rust off Rails](items/rust-off-rails.md)
- [Rustlings](items/rustlings.md)

### Security

- [Everyone in tech is panicking about security (Matt Shumer)](items/everyone-in-tech-is-panicking-about-security-matt-shumer.md) (stub)
- [Expanding Daybreak as the cyber defense window narrows](items/expanding-daybreak-as-the-cyber-defense-window-narrows.md)
- [FOKS: Federated Open Key Service](items/foks-federated-open-key-service.md)
- [Lean now ships with verified kernels](items/lean-now-ships-with-verified-kernels.md)
- [LLMs are making formal software verification feasible at a much larger scale](items/llms-are-making-formal-software-verification-feasible-at-a.md)
- [Meta Muse exposes users' secrets when they share conversations](items/meta-muse-exposes-users-secrets-when-they-share.md)
- [OverTheWire wargames](items/overthewire-wargames.md)
- [REA: Reverse Engineer Anything](items/rea-reverse-engineer-anything.md) (stub)
- [The internet is under attack (Matt Shumer)](items/the-internet-is-under-attack-matt-shumer.md) (stub)
- [The internet is under attack: how to protect yourself and your family](items/the-internet-is-under-attack-how-to-protect-yourself-and.md)
- [Trail of Bits](items/trail-of-bits.md)
- [Trusting-trust attack against an entire Linux distribution](items/trusting-trust-attack-against-an-entire-linux-distribution.md)
- [VMs won't contain cyber-capable agents](items/vms-wont-contain-cyber-capable-agents.md)
- [Woman charged with computer fraud over a scam CashApp account in her name](items/woman-charged-with-computer-fraud-over-a-scam-cashapp.md)

#### Access control

- [RFC 8693: OAuth 2.0 Token Exchange](items/rfc-8693-oauth-2-0-token-exchange.md)
- [RFC 8725: JSON Web Token Best Current Practices](items/rfc-8725-json-web-token-best-current-practices.md)

#### Sandboxing

- [How to run LLM-generated Python safely](items/how-to-run-llm-generated-python-safely.md)
- [MicroVM vs container](items/microvm-vs-container.md)
- [Software sandboxing: the basics](items/software-sandboxing-the-basics.md)
- [VMs won't contain cyber-capable agents](items/vms-wont-contain-cyber-capable-agents.md)
- [What is a Firecracker microVM?](items/what-is-a-firecracker-microvm.md)

### Version control

- [Building a distributed CRDT layer for Git (Conrad Irwin)](items/building-a-distributed-crdt-layer-for-git-conrad-irwin.md)
- [Delta](items/delta.md)
- [DeltaDB: the future of version control](items/deltadb-the-future-of-version-control.md)
- [diamond-types](items/diamond-types.md)
- [lgit: source control for the AI era](items/lgit-source-control-for-the-ai-era.md)
- [Pro Git](items/pro-git.md)
- [Redesigning source control at Anthropic](items/redesigning-source-control-at-anthropic.md)
- [Replace PRs with Delta, now in public beta](items/replace-prs-with-delta-now-in-public-beta.md)
- [The bridge to agent-scale Git infrastructure](items/the-bridge-to-agent-scale-git-infrastructure.md)

### Not yet filed under a topic

- [Beatcode](items/beatcode.md)
- [OpenReview paper BZ5a1r-kVsf](items/openreview-paper-bz5a1r-kvsf.md)

<!-- INDEX:END -->
