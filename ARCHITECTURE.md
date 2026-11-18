# Architecture

## Records in, pages out

The site is static. Each kind of content is a folder of Markdown records with
YAML frontmatter, and those folders are the only source of truth:

| Folder | Record | Pages |
|---|---|---|
| `posts/` | `type: Post` | `index.html`, `index-expanded.html`, `posts/*.html`, `tags/*.html` |
| `defs/` | `type: definition` | `defs.html`, `defs/categories/` |

`site/build.py` reads the folders and writes every page into the repo's
`site/` folder, next to `style.css` and `assets/`. The generated pages are
committed, so the folder can be opened from disk or served by any static host
(Cloudflare Pages serves it). Rebuild and commit them after changing a record.

Build needs: Python with `site/requirements.txt`.

## Post tags

A post's `tags` are mapped to nested categories by `posts/taxonomy.yml`, read
by the same `build_taxonomy` that reads `defs/taxonomy.yml`. A post filed
under a narrower tag also appears on each broader tag's page. The tag rail
uses `taxonomy_filter_rows`: at the root it lists the top-level categories;
on a tag page it shows the path down to that tag, then its children.

## The die and the eye

`random-posts.js` is generated with the list of post slugs. The die picks a
post other than the current one and opens `posts/<slug>.html?die=<face>`; the
`die` parameter only keeps the rolled face showing on the next page. The eye is
a plain link between `index.html` and `index-expanded.html` (and from a tag
page back to `index.html`). On a post page the script adds `?post=<slug>`
to the eye's link, and on the feed that parameter hides every card but that
post's, with the rail narrowed to its tags.

## Retired: quotes and bookmarks

Until 2026-11-17 the site also published `quotes/` (quote records with a
topic and source taxonomy) and `bookmarks/` (artifact-dag nodes, validated and
drawn with a pinned artifact-dag checkout). Both now live in the
[bookmarks repository](https://github.com/markreveley/bookmarks): every quote
is kept on the bookmark of its source page, with its Hacker News excerpts, and
the bookmark topic tree moved to that repo's `topics/`. The records, build
code and pages were removed from here. `build.py` deletes the old output paths
listed in `RETIRED`, so a rebuild never leaves stale pages behind.
