# site/

A static dev blog: HTML and CSS, no JavaScript, no framework, no runtime
dependencies. Open `site/index.html` in a browser, or serve the directory:

    python3 -m http.server -d site 8000

## Sections

| Page | What it is |
|---|---|
| `index.html` | **Posts** — the blog itself. No posts yet; the markup for one is in an HTML comment on that page. |
| `quotes.html` | **Quotes** — the topic list: every tag in the corpus, most-used first. |
| `topics/<tag>.html` | The quotes carrying one tag. `topics/all.html` is the whole corpus. |
| `about.html` | **About** — one sentence. |

## Quotes

The quote is the only object the site has: no source pages, no view pages, no
levels. Every excerpt in
[`research/graph-engineering/excerpts/`](../research/graph-engineering/excerpts/)
becomes one card.

Quotes are reached by topic. `quotes.html` is the landing page and holds
nothing but the sentence and the topic list — every tag in the corpus with the
number of quotes carrying it, most-used first. Each entry links to
`topics/<tag>.html`, which lists those quotes; `topics/all.html` lists all of
them. Quotes are ordered newest first everywhere, by the publication date of
the source they came from. A quote carries four to six tags, so it appears
under each of them.

Each card holds, in this order:

1. the statement it makes, as a small heading — also its anchor, `#q-<slug>`;
2. **the quote text**, verbatim, set as the largest thing on the card;
3. the note on it;
4. speaker and date;
5. the URL it came from — the whole of what used to be the source record;
6. its labels: what kind of statement it is, then its topics — each linking to
   that topic's page.

Everything that describes the quote sits below the quote, so nothing competes
with the text itself.

Two things the bundle carries are deliberately not rendered: the typed edges
between quotes, and the issues they answer. Both are graph structure rather
than quotes, and the pages that displayed them are gone.

### Labels

The bundle types each excerpt on two facets — a `role` in the dialectic
(issue / position / argument / evidence) and a `subtype` speech act (question /
claim / definition / problem / solution / observation / inference /
prescription). They are not orthogonal: only 14 of the 32 possible pairs occur,
and most subtypes appear under a single role. The site shows `subtype` alone,
since `role` is a fact about a quote's position in the argument graph, which
this site no longer draws.

The bundle's other tags are the site's topics, and are read off the quotes
alone — a source's own tags describe the source, which this site no longer
renders.

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

* **`RewriteLinks`** — turns a link between two excerpts into its anchor on
  `topics/all.html`, the one page guaranteed to hold every quote. A link with no
  page here — a source record, an issue, a view, the bundle README — keeps its
  text and loses its href rather than going dead.
* **`ShiftHeadings`** — renumbers a fragment's headings so its `#` lands under
  the page's own `<h1>`.
* **`WrapTables`** — puts each table in an `overflow-x` box so a wide one
  scrolls itself instead of the page.
* **`SplitQuotes`** — an excerpt quoting its source twice writes two
  blockquotes; Python-Markdown folds those into one, so this splits them back
  apart into two quotations.

Plus a preprocessor that drops footnote markers (every excerpt footnotes its
own source, which each card already links), and `"` added to the escape set,
since the bundle writes `\"` inside quoted passages.

Source dates in the bundle are free text — an ISO date, a bare year, sometimes
a parenthetical, sometimes `living document`. `build.py` reads the leading date
off the front for display and ordering, and shows anything undated as written.

`build.py` clears `topics/` before each run, along with the pages the earlier,
level-structured version of this site generated, so a tag dropped from the
bundle loses its page and a rebuild leaves no orphans behind.
