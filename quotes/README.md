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
- `source_date`: publication date at known ISO precision
- `speaker`: quoted speaker when distinct from the source author
- `hacker_news_url`: Hacker News discussion URL for the source
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

## Intake

Invoke `$quote` and provide the exact quote text first, followed by its URL. The repository skill reads
the source, assigns tags, records supported metadata and verification state,
authors the Markdown file directly, then rebuilds and tests the site.
