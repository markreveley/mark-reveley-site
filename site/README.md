# site/

A static dev blog: HTML and CSS, no JavaScript, no framework, no runtime
dependencies. Open `site/index.html` in a browser, or serve the directory:

    python3 -m http.server -d site 8000

## Sections

| Page | What it is |
|---|---|
| `index.html` | **Posts** — the blog itself. No posts yet; the markup for one is in an HTML comment on that page. |
| `reading.html` | **Reading** — the hub for the three-level research bundle. |
| `about.html` | **About** — one sentence. |

## The three levels

`reading.html` is a front door onto [`research/graph-engineering/`](../research/graph-engineering/),
which keeps sources, excerpts and views as separate levels. Each level page
links down to the next and back up again:

* **Level 1 — `sources.html`** — every source, alphabetical, linking out to the
  original and down to the excerpts taken from it.
* **Level 2 — `excerpts.html`** — every verbatim excerpt, grouped under its
  source, with its role, subtype, tags, and its typed edges to other excerpts
  and to the open questions (collapsed behind `<details>`, which needs no
  script).
* **Level 3 — `views.html`** — compositions over the excerpt graph.

An excerpt that cites two sources is filed under the first and cross-referenced
from the others, so every anchor id is unique.

## Views

`views/timeline.html` is rendered from the bundle's own view document. The other
four are **demo views** — labelled as such on the page — built from the same
corpus to show what the level is for:

| View | Arranged by |
|---|---|
| `views/timeline.html` | date (from `research/graph-engineering/views/timeline.md`) |
| `views/by-issue.html` | the seven open questions, with the positions on record |
| `views/by-role.html` | role in the argument: issue, position, argument, evidence |
| `views/by-tag.html` | tag, most-used first |
| `views/edges.html` | typed relation: supports, refines, objects-to, precedes… |

## Rebuilding

Every page except `style.css` is generated from the bundle by `build.py`, so
the site and the research never drift apart. Edit the markdown, then:

    pip install -r site/requirements.txt   # PyYAML, Python-Markdown
    python3 site/build.py

Editing the HTML directly works too, but the next build overwrites it — put
lasting changes in `build.py` (structure) or `style.css` (never generated).

### How build.py renders

Markdown goes through [Python-Markdown](https://python-markdown.github.io/)
with the `tables` extension. Four passes adapt its output to this site:

* **`RewriteLinks`** — turns a bundle link (`../excerpts/foo.md`, or a bare
  `foo.md` written between siblings) into the anchor for its page here. A link
  with no page on this site — the bundle README, the update log — keeps its
  text and loses its href rather than going dead.
* **`ShiftHeadings`** — renumbers a fragment's headings so its `#` lands under
  the page's own `<h1>`.
* **`WrapTables`** — puts each table in an `overflow-x` box so a wide one
  scrolls itself instead of the page.
* **`SplitQuotes`** — an excerpt quoting its source twice writes two
  blockquotes; Python-Markdown folds those into one, so this splits them back
  apart into two quotations.

Plus a preprocessor that drops footnote markers (every excerpt footnotes its
own source, which each card already names), and `"` added to the escape set,
since the bundle writes `\"` inside quoted passages.
