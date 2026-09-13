# Definition collection

Each other Markdown file is the canonical source for one term's card. Use a
lowercase, hyphenated filename as its stable permalink identifier.

```yaml
---
type: Definition
term: Program
date_added: "2026-09-11"
categories: [operating-systems]
---
The definition goes here, followed by optional explanatory paragraphs and
Markdown web links to references.
```

All fields shown are required. Supply a non-empty body or a `definitions` list
as described below. `date_added` must be
a valid ISO date. The feed and category pages sort by date added, newest
first; matching dates sort by filename in reverse alphabetical order, as
with quotes. Editing a definition does not change its date added.

## Multiple definitions and sources

Use `definitions` in frontmatter to feature multiple definitions of the same
term on one card. Each definition has required `text` and an optional `sources`
list. Sources appear directly beneath the text they support, in recorded order;
multiple definitions are separated within the card. A reference identifies the
source, without implying that the definition is a verbatim quotation.

```yaml
definitions:
  - text: A first definition of the term.
    sources:
      - title: Source article
        url: https://example.com/article#section
        author: Example Author
        date: "2026-09-12"
      - title: Supporting reference
        url: https://example.org/reference
  - text: An alternative definition of the same term.
    sources:
      - title: Another perspective
        url: https://example.net/perspective
```

Each source requires a `title` and absolute HTTP(S) `url`; URL fragments are
preserved. Optional `author` can name an individual or organization. Optional
`date` is the source publication date at known precision (`YYYY`, `YYYY-MM`,
or `YYYY-MM-DD`), independent of the card's date added. Omit unknown metadata.

With `definitions` present, the Markdown body is optional and serves as shared
notes below the definitions. Existing body-only records remain supported as
one definition without structured sources. Term links apply to each definition
and shared notes; source titles and attribution retain their source links.

## Term links and categories

Every occurrence of an entry's term in definition prose links to its card,
including occurrences in its own definition. Matching ignores capitalization,
uses whole words, and prefers the longest matching phrase. Existing Markdown
links retain their destinations. Optional `aliases` lists alternate phrases
or plurals, for example `aliases: [execution state]`. Terms and aliases must
not refer to multiple entries. Links work across category pages, and new
entries become link targets throughout the collection on the next rebuild.

`taxonomy.yml` defines the nested categories shown to the left of the feed
(above it on smaller screens). It uses the same format as the quote taxonomy:
stable node keys, `label`, `children`, and `tags` mapping record category slugs
to nodes. Each assigned category must be mapped exactly once. Parent pages
include all descendant definitions, without duplicates. Multiple categories
may be assigned to a definition.

Run `python3 site/build.py` from the repository root after changes. The builder
generates `site/defs.html` and `site/defs/categories/<category>.html`.
