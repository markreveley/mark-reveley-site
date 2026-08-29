# mark-reveley

A static personal site with posts, selected quotes, and an about page.

## Add a quote

Invoke the repository skill and provide the resource URL and exact quote text:

    $quote

The skill asks only for whichever of those two inputs is missing. It inspects
the source, verifies the quotation when possible, records supported source
metadata, assigns topics, writes an OKF-style Markdown record under
[`quotes/`](quotes/), and rebuilds and tests the site.

The URL is intentionally not unique. Different quotes may point to the same
resource; only an exact repeat of both URL and quote is rejected.

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
