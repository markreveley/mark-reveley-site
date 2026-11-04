# Unprocessed bookmarks

Links that still need going through before they are published. This folder
sits outside `../dag/`, so the site build, artifact-dag's checker and the graph
viewer never read it.

Two forms are welcome here:

- A resource file in the same format as `../dag/items/`, with
  `status: unprocessed`. Its title, topics or overview may be missing or
  thin.
- A bare URL, one per line, in [inbox.md](inbox.md), for anything not yet
  looked at.

To process one: fetch the page, write the title, `tags`, `topics`,
`published` and a short overview in our own words, set `status: unread`, and
`git mv` the file into `../dag/items/`. Then run `python3 site/build.py`,
which checks the graph and stops on errors.

A processed resource must not link to a file here with `[[res:<slug>]]`: the
link would point outside the graph.
