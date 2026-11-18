# mark-reveley

A static personal site with posts and an about page. Definitions are built too,
at `defs.html`, but are left out of the navigation.

Quotes and bookmarks used to be sections of this site. On 2026-11-17 they moved
to the private [bookmarks repository](https://github.com/markreveley/bookmarks),
which is now the only place they are kept (each quote sits on the bookmark of
the page it came from). Their records and pages were removed from here; git
history has them.

## Investigate a future post

Keep sources, analysis, working instructions, experiments, and rough drafts in
the [investigations repository](https://github.com/markreveley/investigations).
Follow its README and AGENTS.md, including a source walkthrough that explains
and checks each claim before drawing wider conclusions. Publish completed posts
by adding records to this repository's `posts/` directory.

## Add a post

Create a Markdown record under [`posts/`](posts/) with a title, publication
date, tags, and body, then rebuild the site. See [`posts/README.md`](posts/README.md)
for the schema. Every tag must be mapped in [`posts/taxonomy.yml`](posts/taxonomy.yml).

## Browse posts

The Posts heading carries two controls:

- **The die** opens a random post (never the one you are on), and shows the
  face it rolled. It is on the Posts feed, the tag pages and every post page.
- **The eye** shows the tag rail to the left of the feed
  (`index-expanded.html`), in the nested format the quotes section used.
  Pressing it again hides the rail. From a post page, the eye opens the feed
  showing just that post's card, with the rail listing its tags.

Each tag has a page, `tags/<tag>.html`, listing the posts filed under it or
any narrower tag.

## Add a definition

Create a Markdown record under [`defs/`](defs/) with a term, date added,
categories, and definition body, then rebuild. See [`defs/README.md`](defs/README.md)
for the schema and nested category format.

## Run and rebuild the site

The generated pages are committed, so they can be opened directly or served:

    python3 -m http.server -d site 8000

To rebuild:

    pip install -r site/requirements.txt
    python3 site/build.py

Run the tests with:

    python3 -m unittest discover -s tests -v
