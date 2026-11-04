# Architecture

## Records in, pages out

The site is static. Each kind of content is a folder of Markdown records with
YAML frontmatter, and those folders are the only source of truth:

| Folder | Record | Pages |
|---|---|---|
| `posts/` | `type: Post` | `index.html`, `posts/*.html` |
| `quotes/` | `type: Quote` | `quotes.html`, `quotes-expanded.html`, `topics/`, `writers/`, `tags.html` |
| `defs/` | `type: definition` | `defs.html`, `defs/categories/` |
| `bookmarks/` | artifact-dag nodes (`resource`, `definition`) | `bookmarks.html`, `bookmarks/topics/`, `bookmarks/graph.html` |

`site/build.py` reads the folders and writes every page into `site/site/`,
next to `style.css` and `assets/`. The generated pages are committed, so the
folder can be opened from disk or served by any static host. Rebuild and
commit them after changing a record.

Build needs: Python with `site/requirements.txt`. For bookmarks it also needs
`git` and `node`, and network access the first time (see below).

## Bookmarks

`bookmarks/` uses the [artifact-dag](https://github.com/markreveley/artifact-dag)
node format, not the site's own record format, so the same files can be checked
and drawn by artifact-dag's tools. Its schema is artifact-dag's `SCHEMA.md`,
"Resource". In short:

- `dag/items/*.md` are bookmarks: `type: resource`, `id: res:<slug>`, `url`,
  and `topics` naming the topics they are filed under.
- `dag/topics/*.md` are topics: `type: definition` tagged `topic`. A narrower
  topic names its broader ones in `refines`.
- `unprocessed/*.md` are links still to be gone through. They sit outside
  `dag/` because artifact-dag's checker and viewer read every Markdown file
  under the folder they are given and cannot exclude a subfolder. Nothing in
  `unprocessed/` is checked or published. Processing a file means writing its
  overview and topics, then `git mv` into `dag/items/`.

The folder's own [README](bookmarks/README.md) covers adding entries; the
[spec](bookmarks/SPEC-bookmark-dag-claude-opus-5-5-effort-low.md) covers where
the collection is going.

The build does three things with it:

1. **Topic pages, in the site's style.** `collect_bookmarks` and
   `build_bookmarks` in `build.py` read the nodes with PyYAML and write
   `bookmarks.html` and one page per topic. A topic page lists the bookmarks
   filed under it or any narrower topic. In the topic tree, a topic with
   several parents appears under its first one.
2. **Validation.** artifact-dag's `dagcheck --lint` runs over `bookmarks/dag/`.
   Errors stop the build. Warnings and info are printed only when it fails.
3. **Graph page.** artifact-dag's `build-viewer` turns `bookmarks/dag/` into one
   self-contained HTML page, configured by `bookmarks/dag-viewer.json`, and
   the build writes it to `bookmarks/graph.html`. The page loads dagre and
   fonts from CDNs. Without a network it falls back to a simpler layout.

Steps 2 and 3 run only when `bookmarks/dag/items/` exists. All three read
`bookmarks/dag/` only.

### artifact-dag is pinned to a recorded commit

`bookmarks/artifact-dag.rev` holds one full commit hash of artifact-dag. On
first use, `artifact_dag_checkout` in `build.py` shallow-fetches exactly that
commit into `.cache/artifact-dag/`, which is gitignored. Later builds reuse
it, and fetch again only when the hash changes. artifact-dag has no npm
dependencies, so nothing is installed: `node` runs its scripts directly.

- **Upgrade:** write the new hash into `artifact-dag.rev`, rebuild, check
  `bookmarks.html` and `bookmarks/graph.html`, and commit the hash with the
  rebuilt pages.
- **Try a local viewer:** `ARTIFACT_DAG_DIR=../artifact-dag python3
  site/build.py` uses that checkout as it is and ignores the pin. Do not
  commit pages built that way, unless the checkout is at the pinned commit.

**Why a recorded commit.** The pin keeps a published page from changing
because of an unrelated artifact-dag commit, and it makes each build
reproducible. A git submodule would pin just as well. It was not chosen
because:

- a clone needs `--recurse-submodules` or `git submodule update --init`, and
  without that the folder is silently empty;
- submodules are awkward across branches and in worktrees, and these repos
  use worktrees constantly;
- this repository stays an ordinary repository. The cost is a few lines of
  fetch code, and network access on the first build.

A sibling checkout (`../artifact-dag`) was not chosen as the default either:
the build would use whatever happened to be checked out there.

### Why the data lives here

The bookmarks moved here from the investigations repository on 2026-11-03.
They are published content, like quotes and definitions, and every other
published record set lives in this repository. If something other than the
site ever needs to write to them, they can move to a repository of their own,
and the build would fetch them the same way it fetches artifact-dag.
