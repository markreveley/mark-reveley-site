# Definition collection

Each other Markdown file is the canonical source for one definition. Use a
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

All fields shown are required, as is a non-empty body. `date_added` must be
a valid ISO date. The feed and category pages sort by date added, newest
first; matching dates sort by filename in reverse alphabetical order, as
with quotes. Editing a definition does not change its date added.

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
