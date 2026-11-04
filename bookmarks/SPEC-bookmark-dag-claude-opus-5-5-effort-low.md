# Spec: a DAG of bookmarks (2026-11-03)

## Decision

Use the **artifact-dag** node format (`artifact-dag/SCHEMA.md`, "Resource")
as the source of truth. Do not use OKF for this collection. If something ever
needs OKF, write a one-way exporter.

Why not OKF:

- OKF's topic structure is the folder tree, so a bookmark sits in one place.
  Topics here need several parents: Agent sandboxes `refines` both AI agents
  and Sandboxing. artifact-dag has typed edges and checks them for cycles;
  OKF has neither.
- artifact-dag already has the tools: `dagcheck` validates and lints, and
  `build-viewer` draws the graph. Both run on this folder today with no
  errors.
- The ids are global (`def:evals`), so this graph can be merged in the viewer
  with other artifact-dag collections (worldtree, identikey) on shared terms.
- The fields map across almost one to one (table below), so choosing
  artifact-dag now leaves OKF open later.

## State today

`site/bookmarks/` already is the DAG. It moved here from `investigations/resources/` on 2026-11-03:

- 258 `resource` nodes in `items/` and 36 topic nodes in `topics/`. Each topic
  is a `definition` tagged `topic`.
- Edges: resource →`topics`→ def, and def →`refines`→ broader def (13 topics
  have a parent).
- `npm run check -- ../site/bookmarks --lint` reports no errors and
  no warnings. The info findings are 23 `dead_end_definition` (root topics,
  which have nothing to point to) and 2 `untopiced_resource`
  (`items/beatcode.md`, `items/openreview-paper-bz5a1r-kvsf.md`).
- `npm run build -- --dag ../site/bookmarks --title Bookmarks`
  builds a 180 KB page.

So the work is to tighten the collection and fold in the other collections.
Nothing new has to be built.

## Node model

| Node | Type | Id | Role |
|---|---|---|---|
| Bookmark | `resource` | `res:<slug>` | one outside page; required: `id`, `type`, `title`, `url` |
| Topic | `definition`, `tags: [topic]` | `def:<slug>` | a subject a bookmark is filed under |

Edges:

- `topics: [def:…]` on a resource says what it is about. Every resource needs
  at least one.
- `refines: [def:…]` on a topic gives its broader topic or topics. This is
  where the hierarchy comes from.
- `[[res:…]]` or `[[def:…]]` in an overview adds a `mentions` edge, for "see
  also" between bookmarks. No new edge kind is needed.

**Tags and topics are kept apart.** `tags` says what *kind* of thing a
resource is, from a closed list (`paper`, `repo`, `docs`, `video`, `thread`,
`post`, `tool`, `research`, `course`). `topics` says what it is *about*. A
new subject becomes a topic file, never a tag.

Other fields kept in frontmatter: `hacker_news`, `added`, `status`
(`unread | read | promoted`; `unprocessed` for files in `bookmarks/unprocessed/`, outside the graph). The parser ignores fields it does not
know, which is allowed.

## Rules (`site/bookmarks/lint.dl`)

The checker reads extra rules from `<folder>/lint.dl`. Add:

1. Do not report `dead_end_definition` for a definition tagged `topic`,
   because a root topic has no broader topic to point to. Check whether a
   rule can suppress a built-in finding. If it cannot, record these findings
   in a baseline file with `--baseline` instead.
2. A resource tag outside the closed list is a warn (`unknown_kind_tag`).
3. A resource with no `topics` is raised from info to warn.

Use `--baseline` so the rules can be switched on before every old finding is
fixed.

## Bringing in the other collections

| Source | Size | Overlap with this library | Plan |
|---|---|---|---|
| `elixir-mind/survey/bookmarks.md` | about 721 unique URLs, 741 entries | 4 URLs | convert by script, one `res:` file per entry |
| `elixir-mind/survey/channels.md` | 56 URLs | — | convert if they are bookmarks; otherwise leave |
| `_do/resources/links/`, `_do/links/` | about 10 URLs | — | convert by hand |
| `elixir-mind/deprecated/intake/intake.md` | about 433 raw URLs | not measured | skip; it is the raw list that came before the survey register |

How to convert `bookmarks.md`. Each entry is `### [title](url)` followed by
`Added · Status · Tags` and a one-line summary.

- `title`, `url` and `added` carry straight over. The summary becomes the
  overview.
- `status: surveyed` becomes `unread`. `promoted → <link>` becomes `promoted`,
  and the overview links to the elixir-mind reference.
- **Tags.** The file has 1364 distinct free-form tags, and 988 of them appear
  only once. They are not topics. Map them to topics this way: the section
  heading (`### AI Agents & Orchestration`) plus the tags go through a mapping
  table (`tag-map.json`, tag → `def:` topic). Write the table once, by hand
  with an agent's help. Map only the frequent tags; an entry whose tags are
  unmapped is filed by its heading. Do not carry the free-form tags over;
  they stay in the elixir-mind source.
- Remove duplicates by normalised URL (no scheme, no `www.`, no trailing `/`).
  When a URL is already present, the existing item is kept.
- Mark where each item came from with a `source: elixir-mind-survey` field.

When the conversion is done, stop adding to `elixir-mind/survey/bookmarks.md`,
and point `/bookmarks` at `site/bookmarks/unprocessed/` (new links) and `site/bookmarks/dag/items/` (processed). That is a
separate change in elixir-mind.

## Topic hierarchy

Currently 13 of 36 topics have a parent. Before the merge, which roughly
triples the item count:

- Settle on about 8–12 root topics, such as AI, Software engineering,
  Security, Networking, Music, Philosophy and Society. Give every other topic
  a `refines` to a root.
- Split a topic once it has more than about 25 items. Merge any topic that
  has fewer than 3.
- A topic's body is a one-sentence scope note saying what is filed there, as
  `agent-sandboxes.md` does now.

## Viewer

- Done 2026-11-03. `site/build.py` publishes the collection as
  `bookmarks.html` with one page per topic, in the site's own style, and as
  `bookmarks/graph.html`, the artifact-dag viewer. It runs `dagcheck --lint`
  first and stops on errors. artifact-dag is pinned to a recorded commit. How
  this works and why is in [ARCHITECTURE.md](../ARCHITECTURE.md).
- A useful later feature for artifact-dag: an option that shows the topic
  hierarchy with item counts and draws resources only when a topic is
  expanded. With about 1000 resources, the full graph becomes unreadable.

## Optional: OKF export

If an OKF bundle is ever needed, a script maps the fields as follows and
writes each item into `<root-topic>/<topic>/` folders. An item with several
topics goes in its first topic's folder.

| artifact-dag | OKF |
|---|---|
| `id` | `id` |
| `type: resource` | `type: reference` |
| `title` | `title` |
| `url` | `resource` |
| first line of the overview | `description` |
| `added` | `timestamp` |
| `tags` + topic slugs | `tags` |

## Steps

1. Give topics to the 2 resources that have none. Add `lint.dl` and a
   baseline.
2. Settle the root topics and `refines` (the topic hierarchy section above).
3. Write `tag-map.json` and the converter script for elixir-mind bookmarks.
   Do a dry run, check it, then write the files.
4. Convert the `_do` link files by hand.
5. Run `build_index.py` and `dagcheck --lint`, then build the viewer and look
   at it.
6. Point elixir-mind's `/bookmarks` at the new collection; freeze
   `survey/bookmarks.md`.
