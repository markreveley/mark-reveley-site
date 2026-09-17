# Quote database

Each other Markdown file in this directory is one quote record and the
canonical source for the generated site.

## Schema

Required OKF-style frontmatter fields:

- `type: Quote`
- `resource`: an absolute HTTP(S) URL
- `quote`: the selected quotation
- `date_added`: an ISO date (`YYYY-MM-DD`)
- `tags`: one or more lowercase, hyphenated topics

Optional enriched fields:

- `source_title`: title of the page or work
- `source_author`: author of the source
- `source_department`: card attribution for formal papers with multiple authors;
  use verified departments/research groups, or institutions when departments are
  unspecified. Keep all names in `source_author` for records and author indexes.
- `source_date`: publication date at known ISO precision
- `speaker`: quoted speaker when distinct from the source author
- `source-taxonomy.yml`: maps source hosts to the source-format hierarchy used by the Writers index
- `hacker_news_url`: Hacker News discussion URL for the source
- `related_links`: optional list of `{title, url}` mappings for extra resources
  shown with the card's source details. Each needs a non-empty title and an
  absolute HTTP(S) URL; the main source remains in `resource`.
- `child_quotes`: optional ordered list of non-empty discussion excerpt strings;
  requires `hacker_news_url` on `news.ycombinator.com`. Preserve exact text.
  These render below the article details, without commenter attribution, on
  every quote card. They share the parent's topics and are not separate records.
  Check them against the discussion; parent verification fields apply only to
  the main quote. See the root README for a YAML example.
- `verification_status`: `verified`, `unverified`, `not-found`, or
  `source-unavailable`
- `verification_date`: required when a source check was attempted

```yaml
---
type: Quote
resource: "https://example.com/article"
quote: "The exact selected passage."
date_added: "2026-08-28"
tags: ["design", "systems"]
source_title: "Example article"
source_author: "Example Author"
source_date: "2026-08-20"
speaker: "Example Speaker"
hacker_news_url: "https://news.ycombinator.com/item?id=12345678"
verification_status: "verified"
verification_date: "2026-08-28"
---
```

The URL is not a key: several records may point to the same resource. The
combination of complete URL and exact quote text must be unique.

## Taxonomy

`taxonomy.yml` maps the flat tags stored in quote records onto the hierarchy
shown by the site. Each raw tag must appear exactly once in a node's `tags`
list. Node keys are stable page slugs; `label` is the shorter name displayed
on quote cards and in the drill-down filter.

`source-taxonomy.yml` maps each quote source host to a source format used by
the Writers index. Add a new host to the most specific existing format, or add
a new format when needed, before building the site.

## Intake

Invoke `$quote` and provide the exact quote text first, followed by its URL. The repository skill reads
the source, assigns tags, records supported metadata and verification state,
authors the Markdown file directly, then rebuilds and tests the site.
