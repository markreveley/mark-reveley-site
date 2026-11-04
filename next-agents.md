---
type: handoff
audience: agent
updated: 2026-11-03
---

# Next steps for the agent

Read with [`next-operator.md`](next-operator.md). Rewrite both at the end of each thread; delete finished steps.

## State

- `main` is at the merge of PR #11, pushed, and deployed by Cloudflare Pages, which serves the committed `site/` folder. No other branches or worktrees from the bookmarks work remain.
- **Bookmarks:**
  - `bookmarks/dag/items/` holds 1172 published resources, under 50 topics in `bookmarks/dag/topics/`. `dagcheck` reports 0 errors and 0 warnings.
  - The site publishes them as `bookmarks.html`, one page per topic, and the artifact-dag viewer at `bookmarks/graph.html`. How the build works is in [ARCHITECTURE.md](ARCHITECTURE.md). Fields and intake history are in [bookmarks/README.md](bookmarks/README.md).
- **Unprocessed:** `bookmarks/unprocessed/` holds 93 entries that sit outside the graph and are never published. 19 are Reddit link posts or removed posts; most of the rest are YouTube videos and pages with too little text to describe. `inbox.md` there is empty. How to process an entry is in [bookmarks/unprocessed/README.md](bookmarks/unprocessed/README.md).
- **Collections imported:** every resource has a private `source` list, which the site does not display. All of these are in: the Chrome tab intakes of 2026-10-23 and 2026-11-03, and elixir-mind's survey register, raw intake list and `knowledge/` references. Investigations no longer holds a bookmarks library.
- **Pin:** artifact-dag is pinned to `e9a6c2a…` in `bookmarks/artifact-dag.rev`.
- **Plan:** the working plan is [bookmarks/SPEC-bookmark-dag-claude-opus-5-5-effort-low.md](bookmarks/SPEC-bookmark-dag-claude-opus-5-5-effort-low.md).

## Environment facts

- **Build dependencies:** PyYAML and markdown-it are not installed globally. Build and test with:
  - `uv run --no-project --with-requirements site/requirements.txt -- python site/build.py`
  - `... -- python -m unittest discover -s tests`

  The bookmarks step also needs `node` and `git`. The first build fetches artifact-dag into `.cache/`.
- **Checking the graph:** run `npm run check -- ../site/bookmarks/dag --lint` from a checkout of artifact-dag. Point it at `bookmarks/dag`, not `bookmarks`.
- **Lint warnings:** an incidental mention of a topic word ("written in Rust") raises `unlinked_term`. Resolve it with `not_links: [def:x]` on that resource.
- **Reading pages:**
  - Claude in Chrome refuses reddit.com. Read Reddit posts from `https://www.reddit.com/r/<sub>/comments/<id>/.rss`. Reddit returns 429 quickly, so fetch slowly with backoff, in the background.
  - X posts can be read in Chrome. Pull the post text and `time` from the `article` element.
  - An X post's date can be computed from its ID: `((id >> 22) + 1288834974657)` ms.
- **Listing Chrome tabs:** Claude in Chrome cannot see the user's own tabs. List them read-only with AppleScript (`tell application "Google Chrome"`). AppleScript variable names are case-insensitive and `tab` is a Chrome class, so don't name a variable `t` or `tab`.
- **Visit dates:** Chrome history (`~/Library/Application Support/Google/Chrome/<profile>/History`, copied first) gives first-visit dates. The operator chose to publish `published` only.
- **Intake exclusions** (operator's choices): own AI sessions (Perplexity, Kimi, claude.ai), Gmail, accounts and transactions, private repos, local and music news, and sensitive personal pages. Included: public repos under the operator's own accounts, and certification and career-study pages.

## Next, in order

1. **(blocked on operator)** Discuss how to keep 1172 bookmarks from overwhelming readers before building anything. The graph page is about 750 KB, and `bookmarks.html` lists everything on one page. Options:
   - an artifact-dag viewer mode that collapses topics and shows counts (spec, "Viewer");
   - paging or per-topic landing on the site;
   - splitting large topics: `ai-assisted-programming` has about 200 items, against the spec's limit of 25.
2. Process `bookmarks/unprocessed/`. Read thin YouTube and other pages in Chrome where a fetch gave nothing, write overviews, and `git mv` them into `dag/items/`. Leave Reddit link posts until there is a way to read their targets.
3. **(ask operator)** Point elixir-mind's `/bookmarks` skill at `site/bookmarks/unprocessed/` and freeze `elixir-mind/survey/bookmarks.md` (spec, last step). This is a change in the elixir-mind repo.
4. The spec's remaining tidy-ups:
   - `bookmarks/dag/lint.dl` with a closed list of kind tags, and a warn for a resource with no topics;
   - choose 8–12 root topics and give every other topic a parent (many have none);
   - merge topics with fewer than 3 items.
5. **(blocked on operator)** Google Tasks through `gws`. Its token expired; see `next-operator.md`.

## Pending operator decisions

- The overwhelm-avoiding UI approach (step 1).
- Whether to repoint elixir-mind's `/bookmarks` (step 3).
- Whether to publish the `dirtwire-touring-gws` OAuth consent screen, so tokens stop expiring every 7 days.
