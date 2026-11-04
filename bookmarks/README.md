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

## Second intake, 2026-11-03

The second batch came from 513 open tabs in 35 windows. 306 were already in the
collection, counting matches on a resource's Hacker News thread, and 8 more were
repeats of other tabs. The intake skipped the same kinds of page as the first,
plus music and local-news pages, and kept certification and career-study pages,
public GitHub repositories under our own accounts, and one book's store page.
That added 74 resources and two topics, Knowledge management and Technical
writing.

The 21 stubs from the first intake now have overviews. X posts were read in the
browser, and Reddit posts through Reddit's RSS feeds, since the browser
extension does not open Reddit. An overview can point to another resource with
an artifact-dag wikilink, `[[res:<slug>]]`, which the site renders as a link.

## Index

<!-- INDEX:START -->

### AI agents

- [AI agents and the impact on cybersecurity (Cisco)](items/ai-agents-and-the-impact-on-cybersecurity-cisco.md)
- [Claude Duet](items/claude-duet.md)
- [Giving Opus 5.5 some free time on a cron job (r/claudexplorers)](items/giving-opus-5-5-some-free-time-on-a-cron-job-r-claudexplorer.md)
- [Hybrid Reasoning Agents](items/hybrid-reasoning-agents.md)
- [Infrastructure for AI Agents](items/infrastructure-for-ai-agents.md)
- [live-smith](items/live-smith.md)
- [Maria Gorskikh](items/maria-gorskikh.md)
- [Meta Muse exposes users' secrets when they share conversations](items/meta-muse-exposes-users-secrets-when-they-share.md)
- [Welcome to the Era of Experience](items/welcome-to-the-era-of-experience.md)
- [What it costs to host an AI agent 24/7](items/what-it-costs-to-host-an-ai-agent-24-7.md)

#### Agent authority

- [Access management for multi-user agents (Alter demo)](items/access-management-for-multi-user-agents-alter-demo.md)
- [Agent identity and access management: can SPIFFE work? (Solo.io)](items/agent-identity-and-access-management-can-spiffe-work-solo-io.md)
- [Agent identity series (Christian Posta)](items/agent-identity-series-christian-posta.md)
- [Agentic AI identity: why your IAM stack isn't ready](items/agentic-ai-identity-why-your-iam-stack-isnt-ready.md)
- [Alter documentation](items/alter-documentation.md)
- [Alter Vault](items/alter-vault.md)
- [Authority control plane: blast radius (Nuggets)](items/authority-control-plane-blast-radius-nuggets.md)
- [Cloudflare OS](items/cloudflare-os.md)
- [Composio](items/composio.md)
- [Do AI agents need their own identity? (Christian Posta)](items/do-ai-agents-need-their-own-identity-christian-posta.md)
- [Enterprise AI governance framework (Nuggets)](items/enterprise-ai-governance-framework-nuggets.md)
- [Fly.io Sprites connectors](items/fly-io-sprites-connectors.md)
- [Giving AI agents identities: delegation, not borrowing](items/giving-ai-agents-identities-delegation-not-borrowing.md)
- [Glossary (Nuggets)](items/glossary-nuggets.md)
- [Guardrails for agentic AI](items/guardrails-for-agentic-ai.md)
- [How we're rethinking work at Cloudflare with Cloudflare OS](items/how-were-rethinking-work-at-cloudflare-with-cloudflare-os.md)
- [Infrastructure for AI Agents](items/infrastructure-for-ai-agents.md)
- [Isolate store data per user (LangSmith)](items/isolate-store-data-per-user-langsmith.md)
- [langchain-nuggets](items/langchain-nuggets.md)
- [Nuggets](items/nuggets.md)
- [Nuggets launches the Authority Control Plane](items/nuggets-launches-the-authority-control-plane.md)
- [Nuggets on LinkedIn](items/nuggets-on-linkedin.md)
- [Nuggets on X](items/nuggets-on-x.md)
- [openclaw-alter-plugin](items/openclaw-alter-plugin.md)
- [Procurement questions for evaluating AI systems (Nuggets)](items/procurement-questions-for-evaluating-ai-systems-nuggets.md)
- [Propagate identity into memory layers (Alter)](items/propagate-identity-into-memory-layers-alter.md)
- [RFC 8693: OAuth 2.0 Token Exchange](items/rfc-8693-oauth-2-0-token-exchange.md)
- [Solving the identity crisis for AI agents (Uber)](items/solving-the-identity-crisis-for-ai-agents-uber.md)
- [What is agent identity? (Solo.io)](items/what-is-agent-identity-solo-io.md)

#### Agent frameworks

- [Cloudflare OS](items/cloudflare-os.md)
- [Composio](items/composio.md)
- [Elixir/OTP agent runtime running in 15+ companies, now open source](items/elixir-otp-agent-runtime-running-in-15-companies-now-open.md)
- [Generative user interfaces (AI SDK)](items/generative-user-interfaces-ai-sdk.md)
- [How to host a remote MCP server](items/how-to-host-a-remote-mcp-server.md)
- [Isolate store data per user (LangSmith)](items/isolate-store-data-per-user-langsmith.md)
- [kagent](items/kagent.md)
- [langchain-nuggets](items/langchain-nuggets.md)
- [live-connector v1.0.0](items/live-connector-v1-0-0.md)
- [Model Context Protocol architecture overview](items/model-context-protocol-architecture-overview.md)
- [OpenAI Agents API](items/openai-agents-api.md)
- [Pepe](items/pepe.md)
- [Persistence and storage (Jido)](items/persistence-and-storage-jido.md)
- [TanStack AI](items/tanstack-ai.md)
- [TanStack AI 1.0 is stable (r/LLMDevs)](items/tanstack-ai-1-0-is-stable-r-llmdevs.md)
- [The runtime that was ready for AI all along](items/the-runtime-that-was-ready-for-ai-all-along.md)

#### Agent harnesses

- [7 core components for building a software factory (Warp)](items/7-core-components-for-building-a-software-factory-warp.md)
- [A single pane of glass for all your cloud agents (Warp Oz)](items/a-single-pane-of-glass-for-all-your-cloud-agents-warp-oz.md)
- [Andrew Ng on graph engineering for agents](items/andrew-ng-on-graph-engineering-for-agents.md)
- [astra-flash-orchestrator (codex-on-crack)](items/astra-flash-orchestrator-codex-on-crack.md)
- [Building a coding agent from scratch (course)](items/building-a-coding-agent-from-scratch-course.md)
- [Effective harnesses for long-running agents](items/effective-harnesses-for-long-running-agents.md)
- [Entire](items/entire.md)
- [Five months treating bugs like patients and coding agents like a medical team](items/five-months-treating-bugs-like-patients-and-coding-agents.md)
- [Harness engineering for coding agent users](items/harness-engineering-for-coding-agent-users.md)
- [Have coding agents made us forget 'program to an interface'?](items/have-coding-agents-made-us-forget-program-to-an-interface.md)
- [Herdr](items/herdr.md)
- [How Claude Code is used in practice](items/how-claude-code-is-used-in-practice.md)
- [I took apart Claude Code, OpenCode and Pi (r/LLMDevs)](items/i-took-apart-claude-code-opencode-and-pi-r-llmdevs.md)
- [OpenAI Agents API](items/openai-agents-api.md)
- [Orchestration package that cut GPT-6 Astra usage by 98%](items/orchestration-package-that-cut-gpt-6-astra-usage-by-98.md)
- [OtoDock](items/otodock.md)
- [Paperclip](items/paperclip.md)
- [Pullboard](items/pullboard.md)
- [Testing agent skills systematically with evals](items/testing-agent-skills-systematically-with-evals.md)
- [tuios](items/tuios.md)

#### Agent sandboxes

- [Agent sandboxes: isolated runtimes for testing agent behaviour](items/agent-sandboxes-isolated-runtimes-for-testing-agent.md)
- [AI sandbox pricing compared](items/ai-sandbox-pricing-compared.md)
- [Code interpreter pricing](items/code-interpreter-pricing.md)
- [Ephemeral vs persistent sandboxes](items/ephemeral-vs-persistent-sandboxes.md)
- [Fly.io Learn](items/fly-io-learn.md)
- [Fly.io Sprites alternatives for AI agent sandboxes (Blaxel)](items/fly-io-sprites-alternatives-for-ai-agent-sandboxes-blaxel.md)
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
- [An AI breakthrough has made decades of computer science research 'irrelevant' (WIRED)](items/an-ai-breakthrough-has-made-decades-of-computer-science-rese.md)
- [Expanding Daybreak as the cyber defense window narrows](items/expanding-daybreak-as-the-cyber-defense-window-narrows.md)
- [Global Cybersecurity Outlook 2026 (World Economic Forum)](items/global-cybersecurity-outlook-2026-world-economic-forum.md)
- [How we're rethinking work at Cloudflare with Cloudflare OS](items/how-were-rethinking-work-at-cloudflare-with-cloudflare-os.md)
- [I make six figures and AI does all my work (r/accelerate)](items/i-make-six-figures-and-ai-does-all-my-work-r-accelerate.md)
- [Infisical raises a $40 million Series B (Start with Identity)](items/infisical-raises-a-40-million-series-b-start-with-identity.md)
- [Meet the AI ethicists shaping Claude's conscience](items/meet-the-ai-ethicists-shaping-claudes-conscience.md)
- [METR lands in AI's doom debate](items/metr-lands-in-ais-doom-debate.md)
- [OpenAI cannot make AI safe on its own (letter)](items/openai-cannot-make-ai-safe-on-its-own-letter.md)
- [OpenAI is well positioned to fast-follow Jev](items/openai-is-well-positioned-to-fast-follow-jev.md)
- [Ramp AI Index, August 2026](items/ramp-ai-index-august-2026.md)
- [Software Engineer, RL Environments at AfterQuery](items/software-engineer-rl-environments-at-afterquery.md)
- [The AI industry has already spent $65 million ahead of the midterms](items/the-ai-industry-has-already-spent-65-million-ahead-of-the.md)
- [The Atlassian engineer who posted his systems breakdown is now at Tesla (r/AgentsOfAI)](items/the-atlassian-engineer-who-posted-his-systems-breakdown-is-n.md)
- [The bubble is not popping (r/antiai)](items/the-bubble-is-not-popping-r-antiai.md)
- [The rise and fall of agent civilizations (Dwarkesh Patel)](items/the-rise-and-fall-of-agent-civilizations-dwarkesh-patel.md)
- [We're still underestimating what AI really means (Ryan Dahl)](items/were-still-underestimating-what-ai-really-means-ryan-dahl.md)
- [Why math dumped OpenAI](items/why-math-dumped-openai.md)

### AI safety

- ['We were looking at it wrong': the explosive claim that's upended the AI world](items/we-were-looking-at-it-wrong-the-explosive-claim-thats.md)
- [Buck Shlegeris](items/buck-shlegeris.md)
- [Claude poisoning another AI through harmless-looking stories (r/pwnhub)](items/claude-poisoning-another-ai-through-harmless-looking-stories.md)
- [fair-witness-framework](items/fair-witness-framework.md)
- [Human-AI partnerships are for alignment, not capability](items/human-ai-partnerships-are-for-alignment-not-capability.md)
- [I asked 100 agents to hack me (Shrivu Shankar)](items/i-asked-100-agents-to-hack-me-shrivu-shankar.md)
- [Jailbreaking LLMs: a comprehensive guide (Promptfoo)](items/jailbreaking-llms-a-comprehensive-guide-promptfoo.md)
- [Meet the AI ethicists shaping Claude's conscience](items/meet-the-ai-ethicists-shaping-claudes-conscience.md)
- [METR](items/metr.md)
- [METR lands in AI's doom debate](items/metr-lands-in-ais-doom-debate.md)
- [OpenAI cannot make AI safe on its own (letter)](items/openai-cannot-make-ai-safe-on-its-own-letter.md)
- [Redwood Research team](items/redwood-research-team.md)
- [Task-completion time horizons of frontier AI models](items/task-completion-time-horizons-of-frontier-ai-models.md)
- [The first big AI disaster is yet to happen](items/the-first-big-ai-disaster-is-yet-to-happen.md)
- [The rise and fall of agent civilizations (Dwarkesh Patel)](items/the-rise-and-fall-of-agent-civilizations-dwarkesh-patel.md)
- [When AI builds itself](items/when-ai-builds-itself.md)
- [Would catching your AIs trying to escape convince AI developers to slow down?](items/would-catching-your-ais-trying-to-escape-convince-ai.md)

#### Interpretability

- ['We were looking at it wrong' (r/singularity)](items/we-were-looking-at-it-wrong-r-singularity.md)
- ['We were looking at it wrong': the explosive claim that's upended the AI world](items/we-were-looking-at-it-wrong-the-explosive-claim-thats.md)
- [AI interpretability is further along than I thought](items/ai-interpretability-is-further-along-than-i-thought.md)
- [ConvNeXt microscope (Neural networks are already clean)](items/convnext-microscope-neural-networks-are-already-clean.md)
- [Explosive document claims AI is not what we think (r/Futurism)](items/explosive-document-claims-ai-is-not-what-we-think-r-futurism.md)
- [Explosive document claims that AI is not what we think](items/explosive-document-claims-that-ai-is-not-what-we-think.md)
- [heretic](items/heretic.md)
- [Neural networks are already clean](items/neural-networks-are-already-clean.md)
- [Nick Cammarata](items/nick-cammarata.md)
- [Qwen 3.8 27B on my laptop can interpret model weights, too (Simon Willison)](items/qwen-3-8-27b-on-my-laptop-can-interpret-model-weights-too-si.md)
- [Sparks of weight-space programming](items/sparks-of-weight-space-programming.md)
- [The 'Astra can read and write weights' post is misleading (Matthew Honnibal)](items/the-astra-can-read-and-write-weights-post-is-misleading-matt.md)
- [tutorials](items/tutorials.md)
- [Uncensor any LLM with abliteration (Maxime Labonne)](items/uncensor-any-llm-with-abliteration-maxime-labonne.md)

### AI search

- [AI optimization test: footers are back like 2003](items/ai-optimization-test-footers-are-back-like-2003.md)
- [ChatGPT built its own search index](items/chatgpt-built-its-own-search-index.md)
- [How Hacker News ranking really works](items/how-hacker-news-ranking-really-works.md)
- [Publish stats, get cited](items/publish-stats-get-cited.md)
- [Synthetic deep web: how the internet is becoming invisible](items/synthetic-deep-web-how-the-internet-is-becoming-invisible.md)
- [The recency bias that's reshaping AI search](items/the-recency-bias-thats-reshaping-ai-search.md)

### AI-assisted programming

- ['AI' is not a tool (Rich Hickey)](items/ai-is-not-a-tool-rich-hickey.md)
- [7 core components for building a software factory (Warp)](items/7-core-components-for-building-a-software-factory-warp.md)
- [Claude Academy](items/claude-academy.md)
- [Code is clay now](items/code-is-clay-now.md)
- [Delta](items/delta.md)
- [Don't review agent code, interrogate it (r/codex)](items/dont-review-agent-code-interrogate-it-r-codex.md)
- [Evolving programming languages in the AI era](items/evolving-programming-languages-in-the-ai-era.md)
- [Five months treating bugs like patients and coding agents like a medical team](items/five-months-treating-bugs-like-patients-and-coding-agents.md)
- [Grieving the loss of details](items/grieving-the-loss-of-details.md)
- [Harness engineering for coding agent users](items/harness-engineering-for-coding-agent-users.md)
- [Have coding agents made us forget 'program to an interface'?](items/have-coding-agents-made-us-forget-program-to-an-interface.md)
- [How Claude Code is used in practice](items/how-claude-code-is-used-in-practice.md)
- [How Cloudflare enforces engineering standards using AI](items/how-cloudflare-enforces-engineering-standards-using-ai.md)
- [How I use OpenCode and AI in Neovim](items/how-i-use-opencode-and-ai-in-neovim.md)
- [How to read code](items/how-to-read-code.md)
- [Human-AI partnerships are for alignment, not capability](items/human-ai-partnerships-are-for-alignment-not-capability.md)
- [I am done with this (r/ClaudeAI)](items/i-am-done-with-this-r-claudeai.md)
- [I'm sorry, but you still have to think](items/im-sorry-but-you-still-have-to-think.md)
- [Karpathy is right: your attention is the new bottleneck](items/karpathy-is-right-your-attention-is-the-new-bottleneck.md)
- [On the foolishness of natural language programming (1978)](items/on-the-foolishness-of-natural-language-programming-1978.md)
- [OpenSpec](items/openspec.md)
- [Per-PR preview environments for coding agents](items/per-pr-preview-environments-for-coding-agents.md)
- [Pullboard](items/pullboard.md)
- [Redesigning source control at Anthropic](items/redesigning-source-control-at-anthropic.md)
- [Replace PRs with Delta, now in public beta](items/replace-prs-with-delta-now-in-public-beta.md)
- [Rust off Rails](items/rust-off-rails.md)
- [Sean Goedecke: posts tagged ai](items/sean-goedecke-posts-tagged-ai.md)
- [Shipping 2,500 PRs in a month (talk)](items/shipping-2-500-prs-in-a-month-talk.md)
- [sidekick.nvim](items/sidekick-nvim.md)
- [Software Engineering after the Vibe Shift (book)](items/software-engineering-after-the-vibe-shift-book.md)
- [Software engineers don't get to be Luddites about AI](items/software-engineers-dont-get-to-be-luddites-about-ai.md)
- [Software's centaur age may last decades](items/softwares-centaur-age-may-last-decades.md)
- [Superrepos and why Claude Code is the best worktree manager (cmux)](items/superrepos-and-why-claude-code-is-the-best-worktree-manager.md)
- [Tell agents the why, not just the how](items/tell-agents-the-why-not-just-the-how.md)
- [The compiler was supposed to end programming too](items/the-compiler-was-supposed-to-end-programming-too.md)
- [Tool or automation? You make the decision each time](items/tool-or-automation-you-make-the-decision-each-time.md)
- [unslop](items/unslop.md)

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
- [kagent](items/kagent.md)
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

- [An AI breakthrough has made decades of computer science research 'irrelevant' (WIRED)](items/an-ai-breakthrough-has-made-decades-of-computer-science-rese.md)
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
- [Herdr](items/herdr.md)
- [How I use OpenCode and AI in Neovim](items/how-i-use-opencode-and-ai-in-neovim.md)
- [If you don't run your own LLM proxy, how do you know what's going on?](items/if-you-dont-run-your-own-llm-proxy-how-do-you-know-whats.md)
- [Learn Neovim the practical way](items/learn-neovim-the-practical-way.md)
- [My fast Zsh setup without Oh My Zsh](items/my-fast-zsh-setup-without-oh-my-zsh.md)
- [My first day with the Rex beta (r/Ghostty)](items/my-first-day-with-the-rex-beta-r-ghostty.md)
- [My minimal Zsh setup is ridiculously good](items/my-minimal-zsh-setup-is-ridiculously-good.md)
- [Nordwand Mono](items/nordwand-mono.md)
- [OpenAI CLI](items/openai-cli.md)
- [Pro Git](items/pro-git.md)
- [Rex: public testing is beginning (Superlogical)](items/rex-public-testing-is-beginning-superlogical.md)
- [sidekick.nvim](items/sidekick-nvim.md)
- [The Ghostty team just replaced their own terminal?](items/the-ghostty-team-just-replaced-their-own-terminal.md)
- [The Ghostty team just replaced their own terminal? (r/Ghostty)](items/the-ghostty-team-just-replaced-their-own-terminal-r-ghostty.md)
- [The Neovim setup I use every day](items/the-neovim-setup-i-use-every-day.md)
- [The Zen of cmux](items/the-zen-of-cmux.md)
- [Tmux is still better than Herdr](items/tmux-is-still-better-than-herdr.md)
- [tuios](items/tuios.md)
- [You don't need plugins in Neovim (full IDE setup)](items/you-dont-need-plugins-in-neovim-full-ide-setup.md)

### Digital identity

- [Agent identity and access management: can SPIFFE work? (Solo.io)](items/agent-identity-and-access-management-can-spiffe-work-solo-io.md)
- [Agent identity series (Christian Posta)](items/agent-identity-series-christian-posta.md)
- [Agentic AI identity: why your IAM stack isn't ready](items/agentic-ai-identity-why-your-iam-stack-isnt-ready.md)
- [banana-web](items/banana-web.md)
- [Do AI agents need their own identity? (Christian Posta)](items/do-ai-agents-need-their-own-identity-christian-posta.md)
- [FOKS: Federated Open Key Service](items/foks-federated-open-key-service.md)
- [How to get an IAM job (Start with Identity)](items/how-to-get-an-iam-job-start-with-identity.md)
- [identikey-core](items/identikey-core.md)
- [identikey-protocol](items/identikey-protocol.md)
- [Identity (Stanford Encyclopedia of Philosophy)](items/identity-stanford-encyclopedia-of-philosophy.md)
- [Identity vendor directory (Start with Identity)](items/identity-vendor-directory-start-with-identity.md)
- [Moving into IAM: why workforce identity comes first](items/moving-into-iam-why-workforce-identity-comes-first.md)
- [Propagate identity into memory layers (Alter)](items/propagate-identity-into-memory-layers-alter.md)
- [Solving the identity crisis for AI agents (Uber)](items/solving-the-identity-crisis-for-ai-agents-uber.md)
- [Study guide for Exam SC-300 (Microsoft Identity and Access Administrator)](items/study-guide-for-exam-sc-300-microsoft-identity-and-access-ad.md)
- [The Digital Identity Event Horizon](items/the-digital-identity-event-horizon.md)
- [What is agent identity? (Solo.io)](items/what-is-agent-identity-solo-io.md)
- [Woman charged with computer fraud over a scam CashApp account in her name](items/woman-charged-with-computer-fraud-over-a-scam-cashapp.md)
- [World Tree Network (GitHub)](items/world-tree-network-github.md)

### Education

- [Building a coding agent from scratch (course)](items/building-a-coding-agent-from-scratch-course.md)
- [How to get an IAM job (Start with Identity)](items/how-to-get-an-iam-job-start-with-identity.md)
- [I took apart Claude Code, OpenCode and Pi (r/LLMDevs)](items/i-took-apart-claude-code-opencode-and-pi-r-llmdevs.md)
- [Moving into IAM: why workforce identity comes first](items/moving-into-iam-why-workforce-identity-comes-first.md)
- [Oregon Cyber Trails](items/oregon-cyber-trails.md)
- [Professor Messer (YouTube)](items/professor-messer-youtube.md)
- [Professor Messer's Security+ SY0-701 course](items/professor-messers-security-sy0-701-course.md)
- [Study guide for Exam SC-300 (Microsoft Identity and Access Administrator)](items/study-guide-for-exam-sc-300-microsoft-identity-and-access-ad.md)
- [The Little Book of Deep Learning (François Fleuret)](items/the-little-book-of-deep-learning-fran-ois-fleuret.md)
- [The Little Book of Generative AI Foundations](items/the-little-book-of-generative-ai-foundations.md)
- [Tilden Prep part-time high school program](items/tilden-prep-part-time-high-school-program.md)
- [tutorials](items/tutorials.md)
- [Understanding the OSI model (Professor Messer, Network+)](items/understanding-the-osi-model-professor-messer-network.md)

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
- [Reduced my Jev-as-a-judge calibration error](items/reduced-my-jev-as-a-judge-calibration-error.md)
- [RL sandbox pricing](items/rl-sandbox-pricing.md)
- [Sean Goedecke: posts tagged papers](items/sean-goedecke-posts-tagged-papers.md)
- [Software Engineer, RL Environments at AfterQuery](items/software-engineer-rl-environments-at-afterquery.md)
- [Task-completion time horizons of frontier AI models](items/task-completion-time-horizons-of-frontier-ai-models.md)
- [Testing agent skills systematically with evals](items/testing-agent-skills-systematically-with-evals.md)
- [The illusion of 'The Illusion of Thinking'](items/the-illusion-of-the-illusion-of-thinking.md)
- [tutorials](items/tutorials.md)
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

### Knowledge management

- [Google's Open Knowledge Format, an implementation for real-life problems (r/LLMDevs)](items/googles-open-knowledge-format-an-implementation-for-real-lif.md)
- [okf (wmahfoudh)](items/okf-wmahfoudh.md)

### Language models

- ['We were looking at it wrong': the explosive claim that's upended the AI world](items/we-were-looking-at-it-wrong-the-explosive-claim-thats.md)
- [DeepInfer](items/deepinfer.md)
- [Dense X Retrieval: what retrieval granularity should we use?](items/dense-x-retrieval-what-retrieval-granularity-should-we-use.md)
- [Every AI model has the same controversial take on humans](items/every-ai-model-has-the-same-controversial-take-on-humans.md)
- [heretic](items/heretic.md)
- [How you could have invented the transformer from memory (Alex Wang)](items/alex-wang-on-x.md)
- [Hybrid Reasoning Agents](items/hybrid-reasoning-agents.md)
- [If you don't run your own LLM proxy, how do you know what's going on?](items/if-you-dont-run-your-own-llm-proxy-how-do-you-know-whats.md)
- [Large Language Models Pass the Turing Test](items/large-language-models-pass-the-turing-test.md)
- [lgit: source control for the AI era](items/lgit-source-control-for-the-ai-era.md)
- [LLM Engineer's Handbook (Iusztin and Labonne)](items/llm-engineers-handbook-iusztin-and-labonne.md)
- [Minotaur deep dive: reasoning without a language model](items/minotaur-deep-dive-reasoning-without-a-language-model.md)
- [Natural language processing (Wikipedia)](items/natural-language-processing-wikipedia.md)
- [Should I learn RAG as a backend dev?](items/should-i-learn-rag-as-a-backend-dev.md)
- [Sparks of weight-space programming](items/sparks-of-weight-space-programming.md)
- [The illusion of 'The Illusion of Thinking'](items/the-illusion-of-the-illusion-of-thinking.md)
- [The Little Book of Deep Learning (François Fleuret)](items/the-little-book-of-deep-learning-fran-ois-fleuret.md)
- [The Little Book of Generative AI Foundations](items/the-little-book-of-generative-ai-foundations.md)
- [Uncensor any LLM with abliteration (Maxime Labonne)](items/uncensor-any-llm-with-abliteration-maxime-labonne.md)
- [Welcome to the Era of Experience](items/welcome-to-the-era-of-experience.md)
- [WorldTUI: a 360M model that pretends to be a terminal](items/worldtui-a-360m-model-that-pretends-to-be-a-terminal.md)
- [You could have invented transformers from memory](items/you-could-have-invented-transformers-from-memory.md)

#### Decision models

- [Asking an LLM for confidence](items/asking-an-llm-for-confidence.md)
- [Build your own decision model](items/build-your-own-decision-model.md)
- [Call Jev a decision model (Maggie Appleton)](items/call-jev-a-decision-model-maggie-appleton.md)
- [Elixir client for Jev](items/elixir-client-for-jev.md)
- [Introducing System One models and Jev](items/introducing-system-one-models-and-jev.md)
- [Jeffy](items/jeffy.md)
- [Jev AI vs LLMs: when to use a decision model](items/jev-ai-vs-llms-when-to-use-a-decision-model.md)
- [Jev introduces a new shape of LLM](items/jev-introduces-a-new-shape-of-llm.md)
- [Jev meets the trolley problem](items/jev-meets-the-trolley-problem.md)
- [Jev wasn't built to make agents (Kyle Jeong)](items/jev-wasnt-built-to-make-agents-kyle-jeong.md)
- [Jev's architecture unmasked](items/jevs-architecture-unmasked.md)
- [Jev-style decisions with local Qwen](items/jev-style-decisions-with-local-qwen.md)
- [JevBench](items/jevbench.md)
- [jevchat: Jev as a (lousy) chatbot](items/jevchat-jev-as-a-lousy-chatbot.md)
- [Kev](items/kev.md)
- [OpenAI is well positioned to fast-follow Jev](items/openai-is-well-positioned-to-fast-follow-jev.md)
- [Reduced my Jev-as-a-judge calibration error](items/reduced-my-jev-as-a-judge-calibration-error.md)
- [Sean Goedecke: posts tagged ai](items/sean-goedecke-posts-tagged-ai.md)
- [SemIf](items/semif.md)
- [Six clones of Jev in two days (AINews)](items/six-clones-of-jev-in-two-days-ainews.md)
- [system-one-adapter-python](items/system-one-adapter-python.md)
- [TypeSafe AI documentation](items/typesafe-ai-documentation.md)
- [TypeSafe API reference (System One)](items/typesafe-api-reference-system-one.md)
- [TypeSafe workflow evals](items/typesafe-workflow-evals.md)

#### Local AI

- [commonwealth-ai](items/commonwealth-ai.md)
- [Jeffy](items/jeffy.md)
- [Jev-style decisions with local Qwen](items/jev-style-decisions-with-local-qwen.md)
- [Kev](items/kev.md)
- [Qwen 3.8 27B on my laptop can interpret model weights, too (Simon Willison)](items/qwen-3-8-27b-on-my-laptop-can-interpret-model-weights-too-si.md)
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

- [beatcode (GitHub)](items/beatcode-github.md)
- [beatcode-lean](items/beatcode-lean.md)
- [fixdenorm (Gen reference)](items/fixdenorm-gen-reference.md)
- [Gen (Max 8 documentation)](items/gen-max-8-documentation.md)
- [How I think about Instagram content (20M+ monthly views)](items/how-i-think-about-instagram-content-20m-monthly-views.md)
- [live-connector v1.0.0](items/live-connector-v1-0-0.md)
- [live-smith](items/live-smith.md)
- [YuE2: frontier music with symbolic planning](items/yue2-frontier-music-with-symbolic-planning.md)

### Networking

- [BayMe.sh documentation](items/bayme-sh-documentation.md)
- [Computer Networks: A Systems Approach, Part I](items/computer-networks-a-systems-approach-part-i.md)
- [Professor Messer (YouTube)](items/professor-messer-youtube.md)
- [Understanding the OSI model (Professor Messer, Network+)](items/understanding-the-osi-model-professor-messer-network.md)
- [World Tree Network (GitHub)](items/world-tree-network-github.md)

### Nonprofits

- [Inurement and private benefit (IRS)](items/inurement-and-private-benefit-irs.md)

### Personal writing

- [Grieving the loss of details](items/grieving-the-loss-of-details.md)
- [The desert, edge-dwellers and life-death-life cycles](items/the-desert-edge-dwellers-and-life-death-life-cycles.md)
- [The gun to your head (Nick Cammarata)](items/the-gun-to-your-head-nick-cammarata.md)
- [Things to know when you get cancer](items/things-to-know-when-you-get-cancer.md)

### Philosophy

- [fair-witness-framework](items/fair-witness-framework.md)
- [Identity (Stanford Encyclopedia of Philosophy)](items/identity-stanford-encyclopedia-of-philosophy.md)
- [On Proof and Progress in Mathematics (Thurston)](items/on-proof-and-progress-in-mathematics-thurston.md)
- [Propositions (Stanford Encyclopedia of Philosophy)](items/propositions-stanford-encyclopedia-of-philosophy.md)

### Programming languages

- [Evolving programming languages in the AI era](items/evolving-programming-languages-in-the-ai-era.md)

#### Elixir

- [Elixir client for Jev](items/elixir-client-for-jev.md)
- [Elixir/OTP agent runtime running in 15+ companies, now open source](items/elixir-otp-agent-runtime-running-in-15-companies-now-open.md)
- [Evolving programming languages in the AI era](items/evolving-programming-languages-in-the-ai-era.md)
- [Mix (Elixir docs)](items/mix-elixir-docs.md)
- [Pepe](items/pepe.md)
- [Persistence and storage (Jido)](items/persistence-and-storage-jido.md)
- [The BEAM Book](items/the-beam-book.md)
- [The runtime that was ready for AI all along](items/the-runtime-that-was-ready-for-ai-all-along.md)

#### Lean

- [About the Lean FRO](items/about-the-lean-fro.md)
- [beatcode-lean](items/beatcode-lean.md)
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
- [State of the art in Python 2026?](items/state-of-the-art-in-python-2026.md)
- [Think Python, 3rd edition](items/think-python-3rd-edition.md)

#### Rust

- [Building a distributed CRDT layer for Git (Conrad Irwin)](items/building-a-distributed-crdt-layer-for-git-conrad-irwin.md)
- [diamond-types](items/diamond-types.md)
- [Hello, Cargo! (The Rust Programming Language)](items/hello-cargo-the-rust-programming-language.md)
- [identikey-core](items/identikey-core.md)
- [Loco blog](items/loco-blog.md)
- [Rust hosting](items/rust-hosting.md)
- [Rust off Rails](items/rust-off-rails.md)
- [Rustlings](items/rustlings.md)

### Security

- [AI agents and the impact on cybersecurity (Cisco)](items/ai-agents-and-the-impact-on-cybersecurity-cisco.md)
- [AI web app pentesting: everything you need to know (Intruder)](items/ai-web-app-pentesting-everything-you-need-to-know-intruder.md)
- [Everyone in tech is panicking about security (Matt Shumer)](items/everyone-in-tech-is-panicking-about-security-matt-shumer.md)
- [Expanding Daybreak as the cyber defense window narrows](items/expanding-daybreak-as-the-cyber-defense-window-narrows.md)
- [FOKS: Federated Open Key Service](items/foks-federated-open-key-service.md)
- [Global Cybersecurity Outlook 2026 (World Economic Forum)](items/global-cybersecurity-outlook-2026-world-economic-forum.md)
- [I asked 100 agents to hack me (Shrivu Shankar)](items/i-asked-100-agents-to-hack-me-shrivu-shankar.md)
- [Infisical](items/infisical.md)
- [Infisical (GitHub)](items/infisical-github.md)
- [Jailbreaking LLMs: a comprehensive guide (Promptfoo)](items/jailbreaking-llms-a-comprehensive-guide-promptfoo.md)
- [Lean now ships with verified kernels](items/lean-now-ships-with-verified-kernels.md)
- [LLMs are making formal software verification feasible at a much larger scale](items/llms-are-making-formal-software-verification-feasible-at-a.md)
- [Meta Muse exposes users' secrets when they share conversations](items/meta-muse-exposes-users-secrets-when-they-share.md)
- [OpenBao](items/openbao.md)
- [Oregon Cyber Trails](items/oregon-cyber-trails.md)
- [OverTheWire wargames](items/overthewire-wargames.md)
- [Professor Messer (YouTube)](items/professor-messer-youtube.md)
- [Professor Messer's Security+ SY0-701 course](items/professor-messers-security-sy0-701-course.md)
- [REA: Reverse Engineer Anything](items/rea-reverse-engineer-anything.md)
- [The internet is under attack (Matt Shumer)](items/the-internet-is-under-attack-matt-shumer.md)
- [The internet is under attack: how to protect yourself and your family](items/the-internet-is-under-attack-how-to-protect-yourself-and.md)
- [Trail of Bits](items/trail-of-bits.md)
- [Trusting-trust attack against an entire Linux distribution](items/trusting-trust-attack-against-an-entire-linux-distribution.md)
- [VMs won't contain cyber-capable agents](items/vms-wont-contain-cyber-capable-agents.md)
- [Woman charged with computer fraud over a scam CashApp account in her name](items/woman-charged-with-computer-fraud-over-a-scam-cashapp.md)

#### Access control

- [Giving AI agents identities: delegation, not borrowing](items/giving-ai-agents-identities-delegation-not-borrowing.md)
- [Infisical](items/infisical.md)
- [Infisical (GitHub)](items/infisical-github.md)
- [Infisical raises a $40 million Series B (Start with Identity)](items/infisical-raises-a-40-million-series-b-start-with-identity.md)
- [OpenBao](items/openbao.md)
- [RFC 8693: OAuth 2.0 Token Exchange](items/rfc-8693-oauth-2-0-token-exchange.md)
- [RFC 8725: JSON Web Token Best Current Practices](items/rfc-8725-json-web-token-best-current-practices.md)
- [Study guide for Exam SC-300 (Microsoft Identity and Access Administrator)](items/study-guide-for-exam-sc-300-microsoft-identity-and-access-ad.md)

#### Sandboxing

- [How to run LLM-generated Python safely](items/how-to-run-llm-generated-python-safely.md)
- [MicroVM vs container](items/microvm-vs-container.md)
- [Software sandboxing: the basics](items/software-sandboxing-the-basics.md)
- [VMs won't contain cyber-capable agents](items/vms-wont-contain-cyber-capable-agents.md)
- [What is a Firecracker microVM?](items/what-is-a-firecracker-microvm.md)

### Technical writing

- [ASD-STE100 Simplified Technical English, Issue 9](items/asd-ste100-simplified-technical-english-issue-9.md)

### Version control

- [Building a distributed CRDT layer for Git (Conrad Irwin)](items/building-a-distributed-crdt-layer-for-git-conrad-irwin.md)
- [Delta](items/delta.md)
- [DeltaDB: the future of version control](items/deltadb-the-future-of-version-control.md)
- [diamond-types](items/diamond-types.md)
- [Entire](items/entire.md)
- [lgit: source control for the AI era](items/lgit-source-control-for-the-ai-era.md)
- [Pro Git](items/pro-git.md)
- [Redesigning source control at Anthropic](items/redesigning-source-control-at-anthropic.md)
- [Replace PRs with Delta, now in public beta](items/replace-prs-with-delta-now-in-public-beta.md)
- [Superrepos and why Claude Code is the best worktree manager (cmux)](items/superrepos-and-why-claude-code-is-the-best-worktree-manager.md)
- [The bridge to agent-scale Git infrastructure](items/the-bridge-to-agent-scale-git-infrastructure.md)

### Not yet filed under a topic

- [Beatcode](items/beatcode.md)
- [OpenReview paper BZ5a1r-kVsf](items/openreview-paper-bz5a1r-kvsf.md)

<!-- INDEX:END -->
