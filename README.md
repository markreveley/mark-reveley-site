# mark-reveley

A static personal site with posts, selected quotes, definitions, and an about page.

## Add a definition

Create a Markdown record under [`defs/`](defs/) with a term, date added,
categories, and definition body, then rebuild. See [`defs/README.md`](defs/README.md)
for the schema and nested category format.

## Add a post

Create a Markdown record under [`posts/`](posts/) with a title, publication
date, and body, then rebuild the site. See [`posts/README.md`](posts/README.md)
for the schema.

## Add a quote

Invoke the repository skill and provide the resource URL and exact quote text:

    $quote

The skill asks only for whichever of those two inputs is missing. It inspects
the source, verifies the quotation when possible, records supported source
metadata, assigns topics, writes an OKF-style Markdown record under
[`quotes/`](quotes/), and rebuilds and tests the site.

The URL is intentionally not unique. Different quotes may point to the same
resource; only an exact repeat of both URL and quote is rejected.

Quotes with a `hacker_news_url` may also include `child_quotes`, an ordered
list of exact excerpts from that HN discussion. Keep the article URL in
`resource` and its excerpt in `quote`; save discussion excerpts on the same
record, not as separate quotes. They appear below the article details on the
card, indented under an HN discussion link, without commenter attribution.
Preserve each excerpt verbatim and check it against the linked discussion.
The parent verification fields describe the article quote only. Child quotes
inherit the parent card's topics and do not count as separate quote records.

```yaml
hacker_news_url: "https://news.ycombinator.com/item?id=12345678"
child_quotes:
  - "An exact excerpt from the discussion."
  - |-
    Another discussion excerpt, with multiple paragraphs.

    Its second paragraph.
```

## Quote records

The Markdown files in [`quotes/`](quotes/) are the quote database and the only
source of truth. Each record has these YAML frontmatter attributes:

```yaml
---
type: Quote
resource: "https://example.com/article"
quote: "The selected passage."
date_added: "2026-08-28"
tags: ["example-topic"]
source_title: "Example article"
source_author: "Example Author"
source_date: "2026-08-20"
verification_status: "verified"
verification_date: "2026-08-28"
---
```

See [`quotes/README.md`](quotes/README.md) for the complete schema. The
repository-scoped skill lives at
[`quote/SKILL.md`](.agents/skills/quote/SKILL.md).

The former graph-engineering research bundle and its demo quotes are preserved
under [`removed/research/`](removed/research/).

## Run and rebuild the site

The generated pages are committed, so they can be opened directly or served:

    python3 -m http.server -d site 8000

To rebuild without adding a quote:

    pip install -r site/requirements.txt
    python3 site/build.py

Run the tests with:

    python3 -m unittest discover -s tests -v
