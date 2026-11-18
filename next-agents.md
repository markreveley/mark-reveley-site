---
type: handoff
audience: agent
updated: 2026-11-17
---

# Next steps for the agent

Read with [`next-operator.md`](next-operator.md). Rewrite both at the end of each thread; delete finished steps.

## State

- The site has two sections, Posts and About. Definitions still build at `defs.html` but stay out of the navigation.
- **Quotes and bookmarks moved out** on 2026-11-17, to the private [bookmarks repository](https://github.com/markreveley/bookmarks). Before removing them here, every site bookmark (1265, counting `unprocessed/`) and every quote (85, with both Hacker News excerpts) was checked against that repo by URL and quote text; the only three not matched by URL are duplicates that repo merged on purpose (listed in its `ignored.txt`). The bookmark topic tree moved to its `topics/`, and its page now keeps its own copy of the old stylesheet, so it no longer reads this repo.
- **Posts** carry `tags`, mapped to nested categories in `posts/taxonomy.yml`. The die opens a random post; the eye shows the tag rail on the left (`index-expanded.html`). How they work is in [ARCHITECTURE.md](ARCHITECTURE.md).
- Cloudflare Pages serves the committed `site/` folder from `main`.

## Environment facts

- **Publishing a post:** the build reads only top-level `posts/*.md`, so `posts/drafts/` and `posts/roughs/` are never published. When formatting the operator's draft, fix plain typos, keep their phrasing, fragments and odd commas, and list the fixes in the reply. Give it `tags` from `posts/taxonomy.yml`, adding a category there if none fits.
- **Build and test:** `python3 site/build.py` and `python3 -m unittest discover -s tests` (needs PyYAML and markdown-it-py; `uv run --no-project --with-requirements site/requirements.txt -- python site/build.py` works without installing them).
- **Google Tasks** through `gws`: the token expired; see `next-operator.md`.

## Next, in order

1. **(blocked on operator)** Google Tasks through `gws`.

## Pending operator decisions

- Whether to publish the `dirtwire-touring-gws` OAuth consent screen, so tokens stop expiring every 7 days.
