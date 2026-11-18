#!/usr/bin/env python3
"""Build the static site from Markdown posts and definitions."""

import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
    from markdown_it import MarkdownIt
except ImportError as exc:  # pragma: no cover
    sys.exit(f"{exc}; install the build dependencies: pip install -r site/requirements.txt")



ROOT = Path(__file__).resolve().parent.parent
POST_DB = ROOT / "posts"
DEF_DB = ROOT / "defs"
OUT = ROOT / "site"
TAGS = OUT / "tags"

NAV = [("index.html", "Posts"), ("about.html", "About")]
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
# Pages from the retired quotes and bookmarks sections. The build deletes them
# so a rebuild never leaves stale copies behind; both collections now live in
# the bookmarks repository.
RETIRED = (
    "quotes.html", "quotes-expanded.html", "tags.html", "writers.html",
    "bookmarks.html", "random-quotes.js", "topics", "writers", "bookmarks",
)

def load_document(path):
    """Return YAML frontmatter and body from a Markdown record."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: frontmatter is missing its closing ---")
    meta = yaml.safe_load(text[4:end]) or {}
    if not isinstance(meta, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return meta, text[end + 5:].strip()


def load_frontmatter(path):
    """Return YAML frontmatter from a Markdown record."""
    return load_document(path)[0]


def slugify(value):
    return re.sub(r"[^a-z0-9._-]+", "-", str(value).lower()).strip("-") or "untagged"


def valid_web_url(value):
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_iso_date(value, partial=False):
    patterns = (r"\d{4}", r"\d{4}-\d{2}", r"\d{4}-\d{2}-\d{2}") if partial else (r"\d{4}-\d{2}-\d{2}",)
    if not any(re.fullmatch(pattern, value) for pattern in patterns):
        return False
    try:
        if len(value) == 4:
            date(int(value), 1, 1)
        elif len(value) == 7:
            date(int(value[:4]), int(value[5:]), 1)
        else:
            date.fromisoformat(value)
    except ValueError:
        return False
    return True


def optional_text(meta, key, path):
    value = meta.get(key)
    if value is None:
        return ""
    if not isinstance(value, (str, date)):
        raise ValueError(f"{path}: {key} must be text")
    return str(value).strip()


def build_taxonomy(records, taxonomy_path, field="tags"):
    """Load the topic hierarchy, annotate records, and aggregate each node."""
    raw_tags = {tag for record in records for tag in record[field]}
    if taxonomy_path.exists():
        definition = yaml.safe_load(taxonomy_path.read_text(encoding="utf-8")) or {}
    else:
        definition = {
            tag: {"label": tag, "tags": [tag]}
            for tag in sorted(raw_tags)
        }
    if not isinstance(definition, dict):
        raise ValueError(f"{taxonomy_path}: taxonomy must be a mapping")

    nodes = {}
    tag_nodes = {}

    def visit(branch, parent="", ancestors=()):
        if not isinstance(branch, dict):
            raise ValueError(f"{taxonomy_path}: children must be a mapping")
        for slug, value in branch.items():
            if not isinstance(slug, str) or slugify(slug) != slug:
                raise ValueError(f"{taxonomy_path}: node keys must be lowercase and hyphenated")
            if slug in nodes:
                raise ValueError(f"{taxonomy_path}: duplicate node key {slug}")
            spec = value or {}
            if not isinstance(spec, dict):
                raise ValueError(f"{taxonomy_path}: node {slug} must be a mapping")
            label = spec.get("label", slug)
            if not isinstance(label, str) or not label.strip():
                raise ValueError(f"{taxonomy_path}: node {slug} needs a text label")
            mapped_tags = spec.get("tags", [])
            if not isinstance(mapped_tags, list) or not all(
                isinstance(tag, str) and slugify(tag) == tag for tag in mapped_tags
            ):
                raise ValueError(f"{taxonomy_path}: node {slug} tags must be lowercase and hyphenated")
            children = spec.get("children", {}) or {}
            if not isinstance(children, dict):
                raise ValueError(f"{taxonomy_path}: node {slug} children must be a mapping")
            path = ancestors + (slug,)
            nodes[slug] = {
                "slug": slug,
                "label": label.strip(),
                "parent": parent,
                "children": tuple(children),
                "path": path,
            }
            for tag in mapped_tags:
                if tag in tag_nodes:
                    raise ValueError(f"{taxonomy_path}: tag {tag} is mapped more than once")
                tag_nodes[tag] = slug
            visit(children, slug, path)

    visit(definition)
    missing = sorted(raw_tags - set(tag_nodes))
    if missing:
        label = "tag(s)" if field == "tags" else field
        raise ValueError(f"{taxonomy_path}: unmapped {label}: {', '.join(missing)}")

    topic_records = {slug: [] for slug in nodes}
    for record in records:
        visible = []
        visible_slugs = set()
        memberships = set()
        for tag in record[field]:
            for slug in nodes[tag_nodes[tag]]["path"]:
                memberships.add(slug)
                if slug not in visible_slugs:
                    visible.append((slug, nodes[slug]["label"]))
                    visible_slugs.add(slug)
        record["display_topics"] = visible
        for slug in memberships:
            topic_records[slug].append(record)
    return nodes, topic_records


def collect_posts():
    records = []
    if not POST_DB.exists():
        return records
    for path in sorted(POST_DB.glob("*.md")):
        meta, body = load_document(path)
        if not meta or str(meta.get("type", "")).lower() != "post":
            continue
        missing = [
            key for key in ("title", "date_published")
            if key not in meta or meta[key] is None
            or (isinstance(meta[key], str) and not meta[key].strip())
        ]
        if missing:
            raise ValueError(f"{path}: missing required field(s): {', '.join(missing)}")
        title = optional_text(meta, "title", path)
        date_published = optional_text(meta, "date_published", path)
        excerpt = optional_text(meta, "excerpt", path)
        if not valid_iso_date(date_published):
            raise ValueError(f"{path}: date_published must be a valid YYYY-MM-DD date")
        if not body:
            raise ValueError(f"{path}: post body must not be empty")
        tags = meta.get("tags", [])
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            raise ValueError(f"{path}: tags must be a list of strings")
        if any(slugify(tag) != tag for tag in tags):
            raise ValueError(f"{path}: tags must be lowercase and hyphenated")
        if len(set(tags)) != len(tags):
            raise ValueError(f"{path}: tags must not contain duplicates")
        records.append({
            "slug": path.stem,
            "title": title,
            "date_published": date_published,
            "excerpt": excerpt,
            "body": body,
            "tags": tags,
            "first_sentence": excerpt or re.split(r"(?<=\.)\s+", body, maxsplit=1)[0],
        })
    return sorted(
        records,
        key=lambda record: (record["date_published"], record["slug"]),
        reverse=True,
    )

def definition_entries(meta, body, path):
    """Normalize legacy prose and validate definitions with per-entry sources."""
    entries = meta.get("definitions", [{"text": body}])
    if not isinstance(entries, list) or not entries:
        raise ValueError(f"{path}: definitions must be a non-empty list")
    normalized = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError(f"{path}: each definition must be a mapping")
        text = optional_text(entry, "text", path)
        if not text:
            raise ValueError(f"{path}: definition text must not be empty")
        sources = entry.get("sources", [])
        if not isinstance(sources, list):
            raise ValueError(f"{path}: sources must be a list")
        references = []
        for source in sources:
            if not isinstance(source, dict):
                raise ValueError(f"{path}: each source must be a mapping")
            reference = {
                key: optional_text(source, key, path)
                for key in ("url", "title", "author", "date")
            }
            if not valid_web_url(reference["url"]) or not reference["title"]:
                raise ValueError(f"{path}: each source needs an absolute HTTP(S) url and title")
            if reference["date"] and not valid_iso_date(reference["date"], partial=True):
                raise ValueError(f"{path}: source date must be YYYY, YYYY-MM, or YYYY-MM-DD")
            references.append(reference)
        normalized.append({"text": text, "sources": references})
    return normalized


def collect_defs():
    records = []
    for path in sorted(DEF_DB.glob("*.md")):
        meta, body = load_document(path)
        if not meta or str(meta.get("type", "")).lower() != "definition":
            continue
        term = optional_text(meta, "term", path)
        date_added = optional_text(meta, "date_added", path)
        if not term or (not body and "definitions" not in meta):
            raise ValueError(f"{path}: term and definition body must not be empty")
        if not valid_iso_date(date_added):
            raise ValueError(f"{path}: date_added must be a valid YYYY-MM-DD date")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", path.stem):
            raise ValueError(f"{path}: filename must be lowercase and hyphenated")
        categories = meta.get("categories")
        if not isinstance(categories, list) or not categories or not all(
            isinstance(category, str) and category and slugify(category) == category
            for category in categories
        ):
            raise ValueError(f"{path}: categories must be a non-empty list of lowercase slugs")
        if len(set(categories)) != len(categories):
            raise ValueError(f"{path}: categories must not contain duplicates")
        aliases = meta.get("aliases", [])
        if not isinstance(aliases, list) or not all(
            isinstance(alias, str) and alias.strip() for alias in aliases
        ):
            raise ValueError(f"{path}: aliases must be a list of non-empty strings")
        records.append({
            "slug": path.stem, "term": term, "date_added": date_added,
            "categories": categories, "body": body,
            "definitions": definition_entries(meta, body, path),
            "notes": body if "definitions" in meta else "",
            "aliases": [alias.strip() for alias in aliases],
        })
    return sorted(records, key=lambda record: (record["date_added"], record["slug"]), reverse=True)


def pretty_date(raw):
    year_match = re.fullmatch(r"\d{4}", raw)
    if year_match:
        return raw
    month_match = re.fullmatch(r"(\d{4})-(\d{2})", raw)
    if month_match:
        year, month = map(int, month_match.groups())
        return f"{MONTHS[month - 1]} {year}"
    match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", raw)
    if not match:
        return raw
    year, month, day = map(int, match.groups())
    if not 1 <= month <= 12:
        return raw
    return f"{day} {MONTHS[month - 1]} {year}"



def page(path, title, body, active=None, lede=None, random_script=False):
    depth = path.count("/")
    up = "../" * depth
    nav_items = []
    for href, label in NAV:
        nav_items.append(
            '<a href="{href}"{current}>{label}</a>'.format(
                href=up + href, label=label,
                current=' aria-current="page"' if href == active else "",
            )
        )
    nav = "".join(nav_items)
    description = (
        f'<meta name="description" content="{html.escape(lede, quote=True)}">'
        if lede else ""
    )
    post_script = (
        f'\n<script defer src="{up}random-posts.js"></script>'
        if random_script else ""
    )
    document = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Mark Reveley</title>
{description}
<link rel="stylesheet" href="{up}style.css">{post_script}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <a class="brand" href="{up}index.html">Mark Reveley</a>
  <nav class="mainnav" aria-label="Sections">{nav}</nav>
</header>
<main id="main">
{body}
</main>
</body>
</html>
"""
    destination = OUT / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(document, encoding="utf-8")

def topic_href(tag, depth):
    return "../" * depth + f"tags/{slugify(tag)}.html"



def taxonomy_filter_rows(taxonomy, selected_slug, depth, href_builder, terminal_rows=()):
    """Render a taxonomy rail at its root or at one selected drill-down node."""
    if not selected_slug:
        roots = sorted(
            (node for node in taxonomy.values() if not node["parent"]),
            key=lambda node: node["label"].casefold(),
        )
        return [
            f'<li><a href="{href_builder(node["slug"], depth)}">'
            f'{html.escape(node["label"])}</a></li>'
            for node in roots
        ]

    selected = taxonomy[selected_slug]
    rows = []
    for index, path_slug in enumerate(selected["path"]):
        node = taxonomy[path_slug]
        parent_slug = node["parent"]
        exit_href = (
            href_builder(parent_slug, depth)
            if parent_slug else "../" * depth + "index-expanded.html"
        )
        rows.append(
            f'<li class="filter-path"><a href="{exit_href}" '
            f'aria-label="Exit {html.escape(node["label"], quote=True)} filter">'
            f'{html.escape(node["label"])}</a></li>'
        )
        if index < len(selected["path"]) - 1:
            rows.append('<li class="filter-divider" aria-hidden="true"></li>')

    if selected["children"] or terminal_rows:
        rows.append('<li class="filter-divider" aria-hidden="true"></li>')
    for child_slug in selected["children"]:
        child = taxonomy[child_slug]
        rows.append(
            f'<li><a href="{href_builder(child_slug, depth)}">'
            f'{html.escape(child["label"])}</a></li>'
        )
    rows.extend(terminal_rows)
    return rows


def post_inline_html(text, render_text=html.escape):
    """Render escaped post text with safe Markdown-style web links."""
    fragments = []
    cursor = 0
    for match in re.finditer(r"\[([^\]\n]+)\]\((https?://[^\s)]+)\)", text):
        fragments.append(render_text(text[cursor:match.start()]))
        label, url = match.groups()
        if valid_web_url(url):
            fragments.append(
                f'<a href="{html.escape(url, quote=True)}" rel="noreferrer">'
                f'{html.escape(label)}</a>'
            )
        else:
            fragments.append(html.escape(match.group(0)))
        cursor = match.end()
    fragments.append(render_text(text[cursor:]))
    return "".join(fragments).replace("\n", "<br>\n")


def post_text_html(text):
    """Render post Markdown while keeping embedded HTML inert."""
    markdown = MarkdownIt("commonmark", {"html": False, "breaks": True})
    tokens = markdown.parse(text)
    for token in tokens:
        for child in token.children or []:
            if child.type == "link_open":
                child.attrSet("rel", "noreferrer")
    return markdown.renderer.render(tokens, markdown.options, {})




def post_filter_toggle(depth, filters_on):
    up = "../" * depth
    href = up + ("index.html" if filters_on else "index-expanded.html")
    label = "Hide post tags" if filters_on else "Show post tags"
    state = " is-on" if filters_on else ""
    return (
        f'<a class="filter-toggle{state}" href="{href}" '
        f'aria-label="{label}" title="{label}">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6Z"/>'
        '<circle cx="12" cy="12" r="2.75"/></svg></a>'
    )


def post_random_toggle(depth):
    up = "../" * depth
    return (
        '<button class="random-toggle" type="button" '
        f'data-random-post data-root="{up}" '
        'aria-label="Load a random post" title="Load a random post">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<rect x="3" y="3" width="18" height="18" rx="2.5"/>'
        '<g class="die-face" data-die-face="1"><circle cx="12" cy="12" r="1"/></g>'
        '<g class="die-face" data-die-face="2"><circle cx="8" cy="8" r="1"/><circle cx="16" cy="16" r="1"/></g>'
        '<g class="die-face" data-die-face="3"><circle cx="8" cy="8" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="16" cy="16" r="1"/></g>'
        '<g class="die-face" data-die-face="4"><circle cx="8" cy="8" r="1"/><circle cx="16" cy="8" r="1"/><circle cx="8" cy="16" r="1"/><circle cx="16" cy="16" r="1"/></g>'
        '<g class="die-face is-visible" data-die-face="5"><circle cx="8" cy="8" r="1"/><circle cx="16" cy="8" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="8" cy="16" r="1"/><circle cx="16" cy="16" r="1"/></g>'
        '<g class="die-face" data-die-face="6"><circle cx="8" cy="7.5" r="1"/><circle cx="16" cy="7.5" r="1"/><circle cx="8" cy="12" r="1"/><circle cx="16" cy="12" r="1"/><circle cx="8" cy="16.5" r="1"/><circle cx="16" cy="16.5" r="1"/></g>'
        '</svg></button>'
    )


def post_controls(depth, filters_on):
    return f"""<div class="section-controls">
      {post_random_toggle(depth)}
      {post_filter_toggle(depth, filters_on)}
    </div>"""


def post_hero(title, lede, depth, filters_on):
    lede_html = f'\n  <p class="lede">{lede}</p>' if lede else ""
    return f"""<section class="hero">
  <div class="section-heading">
    <h1>{html.escape(title)}</h1>
    {post_controls(depth, filters_on)}
  </div>{lede_html}
</section>"""


def post_tag_list(record, depth):
    return "".join(
        f'<li><a href="{topic_href(slug, depth)}">{html.escape(label)}</a></li>'
        for slug, label in record["display_topics"]
    )


def post_card(record, depth):
    up = "../" * depth
    title = html.escape(record["title"])
    published = html.escape(record["date_published"], quote=True)
    slug = html.escape(record["slug"], quote=True)
    tags = post_tag_list(record, depth)
    tags_html = f'\n  <ul class="tags">{tags}</ul>' if tags else ""
    return f"""<article class="card post" id="p-{slug}" data-post-slug="{slug}">
  <h2><a href="{up}posts/{slug}.html">{title}</a></h2>
  <p class="attrib"><time datetime="{published}">{html.escape(pretty_date(record["date_published"]))}</time></p>
  <p>{html.escape(record["first_sentence"])}</p>{tags_html}
</article>"""


def post_filter_browser(feed, taxonomy, depth, selected_tag=""):
    """Wrap a post feed with the tag rail on the left, as the quotes section had."""
    rows = taxonomy_filter_rows(taxonomy, selected_tag, depth, topic_href)
    return f"""<section class="post-browser" aria-label="Post tags and posts">
  <aside class="filter-rail filter-rail-tags" aria-label="Filter by tag">
    <h2>Tags</h2>
    <ul>{''.join(rows)}</ul>
  </aside>
  <div class="post-browser-feed">{feed}</div>
</section>"""


def build_random_post_script(records):
    """Write the client-side helper behind the dice and the eye."""
    OUT.mkdir(parents=True, exist_ok=True)
    slugs = json.dumps([record["slug"] for record in records], ensure_ascii=False)
    script = f"""(() => {{
  "use strict";

  const postSlugs = {slugs};
  const button = document.querySelector("[data-random-post]");
  if (!button) return;

  const root = button.dataset.root || "";
  const parameters = new URLSearchParams(window.location.search);
  const postBody = document.querySelector(".post-body[data-post-slug]");
  const currentSlug = postBody ? postBody.dataset.postSlug : parameters.get("post");
  const requestedFace = Number(parameters.get("die"));
  const hasRequestedFace = Number.isInteger(requestedFace)
    && requestedFace >= 1 && requestedFace <= 6;

  function showDieFace(value) {{
    for (const face of button.querySelectorAll("[data-die-face]")) {{
      face.classList.toggle("is-visible", face.dataset.dieFace === String(value));
    }}
  }}

  if (hasRequestedFace) showDieFace(requestedFace);

  // index.html?post=<slug> and index-expanded.html?post=<slug> show one post's
  // card; with the eye on, the tag rail lists only that post's tags.
  const requestedSlug = parameters.get("post");
  if (requestedSlug) {{
    const cards = Array.from(document.querySelectorAll(".card.post"));
    const selectedCard = cards.find((card) => card.dataset.postSlug === requestedSlug);
    if (selectedCard) {{
      for (const card of cards) card.hidden = card !== selectedCard;
      const tagList = document.querySelector(".filter-rail-tags ul");
      if (tagList) {{
        const rows = Array.from(selectedCard.querySelectorAll(".tags a"), (link) => {{
          const item = document.createElement("li");
          const tagLink = link.cloneNode(true);
          tagLink.setAttribute("aria-current", "page");
          item.append(tagLink);
          return item;
        }});
        tagList.replaceChildren(...rows);
      }}
    }}
  }}

  // Carry the shown post through the eye, so toggling keeps the same post.
  const eye = document.querySelector(".filter-toggle");
  if (eye && currentSlug && postSlugs.includes(currentSlug)) {{
    const eyeUrl = new URL(eye.getAttribute("href"), window.location.href);
    eyeUrl.searchParams.set("post", currentSlug);
    if (hasRequestedFace) eyeUrl.searchParams.set("die", String(requestedFace));
    eye.href = eyeUrl.href;
  }}

  if (postSlugs.length === 0) {{
    button.disabled = true;
    return;
  }}

  button.addEventListener("click", () => {{
    const choices = postSlugs.length > 1
      ? postSlugs.filter((slug) => slug !== currentSlug)
      : postSlugs;
    const chosen = choices[Math.floor(Math.random() * choices.length)];
    const rolledFace = Math.floor(Math.random() * 6) + 1;
    showDieFace(rolledFace);
    const next = new URLSearchParams({{ die: String(rolledFace) }});
    window.location.assign(`${{root}}posts/${{encodeURIComponent(chosen)}}.html?${{next}}`);
  }});
}})();
"""
    (OUT / "random-posts.js").write_text(script, encoding="utf-8")


def build_posts(records, taxonomy, tag_records):
    lede = "Mark Reveley — dev blog. Posts and about."
    for record in records:
        title = html.escape(record["title"])
        published = html.escape(record["date_published"], quote=True)
        date_label = html.escape(pretty_date(record["date_published"]))
        tags = post_tag_list(record, 1)
        tags_html = f'\n  <ul class="tags">{tags}</ul>' if tags else ""
        post_body = f"""<article class="post-body" data-post-slug="{html.escape(record['slug'], quote=True)}">
  <header class="hero">
    <div class="section-heading">
      <h1>{title}</h1>
      {post_controls(1, False)}
    </div>
    <p class="attrib"><time datetime="{published}">{date_label}</time></p>
  </header>
  {post_text_html(record['body'])}{tags_html}
</article>"""
        page(
            f"posts/{record['slug']}.html",
            record["title"],
            post_body,
            active="index.html",
            lede=record["first_sentence"],
            random_script=True,
        )

    feed = "".join(post_card(record, 0) for record in records) or '<p class="empty">No posts yet.</p>'
    body = f"""{post_hero("Posts", "", 0, False)}

<section class="posts">
{feed}
</section>"""
    page("index.html", "Posts", body, active="index.html", lede=lede, random_script=True)

    expanded = f"""{post_hero("Posts", "", 0, True)}
{post_filter_browser(feed, taxonomy, 0)}"""
    page("index-expanded.html", "Posts", expanded, active="index.html",
         lede=lede, random_script=True)

    for slug, node in taxonomy.items():
        filtered = tag_records[slug]
        count = len(filtered)
        path_label = " / ".join(taxonomy[item]["label"] for item in node["path"])
        tag_lede = (
            f"{count} post{'' if count == 1 else 's'} filed under "
            f"<em>{html.escape(path_label)}</em>, newest first."
        )
        tag_feed = "".join(post_card(record, 1) for record in filtered)
        tag_feed = tag_feed or '<p class="empty">No posts yet.</p>'
        body = f"""{post_hero(node['label'], tag_lede, 1, True)}
{post_filter_browser(tag_feed, taxonomy, 1, slug)}"""
        page(f"tags/{slug}.html", node["label"], body, active="index.html",
             lede=re.sub("<[^>]+>", "", tag_lede), random_script=True)

def def_category_href(slug, depth):
    return "../" * depth + f"defs/categories/{slug}.html"


def definition_linker(records):
    """Match whole terms and explicit aliases, preferring the longest phrase."""
    targets = {}
    for record in records:
        for term in [record["term"], *record.get("aliases", [])]:
            key = term.lower()
            if key in targets and targets[key] != record["slug"]:
                raise ValueError(f"ambiguous definition term or alias: {term}")
            targets[key] = record["slug"]
    pattern = re.compile(
        r"(?<!\w)(?:" + "|".join(
            re.escape(term) for term in sorted(targets, key=lambda term: (-len(term), term))
        ) + r")(?!\w)", re.IGNORECASE,
    ) if targets else None

    def render(text, depth):
        if pattern is None:
            return html.escape(text)
        fragments = []
        cursor = 0
        for match in pattern.finditer(text):
            fragments.append(html.escape(text[cursor:match.start()]))
            slug = targets[match.group().lower()]
            href = "../" * depth + f"defs.html#d-{slug}"
            fragments.append(f'<a href="{html.escape(href, quote=True)}">{html.escape(match.group())}</a>')
            cursor = match.end()
        fragments.append(html.escape(text[cursor:]))
        return "".join(fragments)

    return render


def def_card(record, depth, link_text):
    slug = html.escape(record["slug"], quote=True)
    permalink = "../" * depth + f"defs.html#d-{slug}"
    categories = "".join(
        f'<li><a href="{def_category_href(category, depth)}">{html.escape(label)}</a></li>'
        for category, label in record["display_topics"]
    )
    def prose(text):
        return "".join(
            f'<p>{post_inline_html(paragraph, lambda text: link_text(text, depth))}</p>'
            for paragraph in re.split(r"\n\s*\n", text.strip())
        )

    entries = []
    for entry in record["definitions"]:
        references = []
        for source in entry["sources"]:
            details = [f'<a href="{html.escape(source["url"], quote=True)}" rel="noreferrer">'
                       f'{html.escape(source["title"])}</a>']
            if source["author"]:
                details.append(html.escape(source["author"]))
            if source["date"]:
                details.append(f'<time datetime="{source["date"]}">{pretty_date(source["date"])}</time>')
            references.append(f'<li>{" · ".join(details)}</li>')
        attribution = (
            '<div class="definition-sources"><span>Sources</span>'
            f'<ul>{"".join(references)}</ul></div>' if references else ""
        )
        entries.append(f'<div class="definition-entry">{prose(entry["text"])}{attribution}</div>')
    body = "".join(entries)
    if record["notes"]:
        body += f'<div class="definition-notes">{prose(record["notes"])}</div>'
    return f"""<article class="card definition" id="d-{slug}">
  <h2><a href="{permalink}">{html.escape(record['term'])}</a></h2>
  {body}
  <p class="attrib">Added <time datetime="{record['date_added']}">{pretty_date(record['date_added'])}</time></p>
  <ul class="tags">{categories}</ul>
</article>"""


def build_defs(records, taxonomy, category_records):
    link_text = definition_linker(records)
    def render(filename, selected=""):
        depth = filename.count("/")

        def category_tree(parent=""):
            rows = []
            children = sorted(
                (node for node in taxonomy.values() if node["parent"] == parent),
                key=lambda node: node["label"].casefold(),
            )
            for node in children:
                slug = node["slug"]
                current = ' aria-current="page"' if selected == slug else ""
                rows.append(
                    f'<li><a href="{def_category_href(slug, depth)}"{current}>'
                    f'{html.escape(node["label"])} <span class="category-count">'
                    f'({len(category_records[slug])})</span></a>{category_tree(slug)}</li>'
                )
            return f'<ul>{"".join(rows)}</ul>' if rows else ""

        current = ' aria-current="page"' if not selected else ""
        all_link = f'<a href="{"../" * depth}defs.html"{current}>All definitions ({len(records)})</a>'
        filtered = category_records[selected] if selected else records
        title = taxonomy[selected]["label"] if selected else "Defs"
        lede = "Definitions, newest added first."
        if selected:
            lede = " / ".join(taxonomy[slug]["label"] for slug in taxonomy[selected]["path"])
            lede += " — newest added first."
        feed = "".join(def_card(record, depth, link_text) for record in filtered)
        feed = feed or '<p class="empty">No definitions yet.</p>'
        body = f"""<section class="hero">
  <h1>{html.escape(title)}</h1>
  <p class="lede">{html.escape(lede)}</p>
</section>
<section class="defs-browser" aria-label="Definitions and categories">
  <aside class="filter-rail defs-categories" aria-label="Definition categories">
    <h2>Categories</h2>
    <nav aria-label="Filter definitions">{all_link}{category_tree()}</nav>
  </aside>
  <div class="defs-feed">{feed}</div>
</section>"""
        page(filename, title, body, active="defs.html", lede=lede)

    category_output = OUT / "defs" / "categories"
    if category_output.exists():
        shutil.rmtree(category_output)
    render("defs.html")
    for slug in taxonomy:
        render(f"defs/categories/{slug}.html", slug)


def build_about():
    body = """<section class="hero">
  <div class="about-heading">
    <h1>About</h1>
    <nav class="about-social-links" aria-label="Mark Reveley elsewhere">
      <a href="https://substack.com/@markreveley1" rel="me noreferrer" aria-label="Substack" title="Substack"><svg class="social-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M22.539 8.242H1.46V5.406h21.08v2.836zM1.46 10.812V24L12 18.11 22.54 24V10.812H1.46zM22.54 0H1.46v2.836h21.08V0z"/></svg></a>
      <a href="https://github.com/markreveley" rel="me noreferrer" aria-label="GitHub" title="GitHub"><svg class="social-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a>
      <a href="https://x.com/markreveley" rel="me noreferrer" aria-label="X" title="X"><svg class="social-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z"/></svg></a>
      <a href="https://www.linkedin.com/in/mark-r-9aab133/" rel="me noreferrer" aria-label="LinkedIn" title="LinkedIn"><svg class="social-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 1 1 0-4.124 2.062 2.062 0 0 1 0 4.124zM7.119 20.452H3.555V9H7.12v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
    </nav>
  </div>
  <p class="lede">Hi I'm Mark. I'm a musician developer living in Berkeley. I'm currently working on a textual musical compiler (Beatcode) and associated benchmark (Beatbench). I'm also a member of the band Dirtwire. I write here about AI, agents, dev, and music.</p>
</section>

<section class="about-more">
  <img class="about-photo" src="assets/mark-headshot.jpg" alt="Mark Reveley">
</section>"""
    page("about.html", "About", body, active="about.html",
         lede="Hi I'm Mark. I'm a musician developer living in Berkeley. I'm currently working on a textual musical compiler (Beatcode) and associated benchmark (Beatbench). I'm also a member of the band Dirtwire. I write here about AI, agents, dev, and music.")


def remove_retired_pages():
    for name in RETIRED:
        path = OUT / name
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


def main():
    posts = collect_posts()
    post_taxonomy, tag_records = build_taxonomy(posts, POST_DB / "taxonomy.yml")
    definitions = collect_defs()
    def_taxonomy, category_records = build_taxonomy(
        definitions, DEF_DB / "taxonomy.yml", field="categories"
    )
    remove_retired_pages()
    if TAGS.exists():
        shutil.rmtree(TAGS)
    build_random_post_script(posts)
    build_posts(posts, post_taxonomy, tag_records)
    build_defs(definitions, def_taxonomy, category_records)
    build_about()
    pages = sorted(path.relative_to(OUT).as_posix() for path in OUT.rglob("*.html"))
    print(f"{len(posts)} posts · {len(post_taxonomy)} tags")
    print(f"wrote {len(pages)} pages")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        sys.exit(str(exc))
