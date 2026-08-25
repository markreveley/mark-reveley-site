# mark-reveley

Working repository for research artifacts.

## Contents

- [`site/`](site/) — the website: a static dev blog (posts, quotes, about) in
  HTML and CSS only. Its quotes section is a front door onto the research
  bundle below — one card per quote, reached by topic, the levels left behind.
  Open `site/index.html`, or see [`site/README.md`](site/README.md).
- [`research/graph-engineering/`](research/graph-engineering/) — evidence bundle on **graph engineering**: primary sources and the typed DAG of verbatim quotes extracted from them (OKF v0.2 carrier). Per the house rule, explicit synthesis lives in `ob6to8/direction`.
  - **Level 1** — [`references/`](research/graph-engineering/references/): annotated links to primary sources.
  - **Level 2** — [`excerpts/`](research/graph-engineering/excerpts/): verbatim quotes decomposed into typed, tagged, cross-linked knowledge units.
  - **Level 3** — [`views/`](research/graph-engineering/views/): non-narrative compositions over the quote DAG (synthesis documents live in `ob6to8/direction`).

Start at [`research/graph-engineering/index.md`](research/graph-engineering/index.md).

## Running the site locally

The built pages are committed, so opening `site/index.html` in a browser is
enough to read it. To serve it over HTTP instead:

    python3 -m http.server -d site 8000     # then open http://localhost:8000/

To regenerate the pages from the research bundle:

    pip install -r site/requirements.txt    # PyYAML, Python-Markdown
    python3 site/build.py

Those two packages are needed only to build the site, never to view it. See
[`site/README.md`](site/README.md) for what the build does.
