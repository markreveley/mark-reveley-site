#!/usr/bin/env python3
"""Build the static site from the OKF-style records in quotes/."""

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
except ImportError as exc:  # pragma: no cover
    sys.exit(f"{exc}; install the build dependency: pip install -r site/requirements.txt")


ROOT = Path(__file__).resolve().parent.parent
QUOTE_DB = ROOT / "quotes"
POST_DB = ROOT / "posts"
OUT = ROOT / "site"
TOPICS = OUT / "topics"
WRITERS = OUT / "writers"

NAV = [("index.html", "Posts"), ("quotes.html", "Quotes"), ("about.html", "About")]
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
VERIFICATION_STATUSES = {"verified", "unverified", "not-found", "source-unavailable"}


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


def collect_quotes():
    records = []
    identities = {}
    if not QUOTE_DB.exists():
        return records
    for path in sorted(QUOTE_DB.glob("*.md")):
        meta = load_frontmatter(path)
        if not meta or str(meta.get("type", "")).lower() != "quote":
            continue
        missing = [
            key for key in ("resource", "quote", "date_added", "tags")
            if key not in meta or meta[key] is None
            or (isinstance(meta[key], str) and not meta[key].strip())
        ]
        if missing:
            raise ValueError(f"{path}: missing required field(s): {', '.join(missing)}")
        resource = optional_text(meta, "resource", path)
        quote = optional_text(meta, "quote", path)
        date_added = optional_text(meta, "date_added", path)
        if not valid_web_url(resource):
            raise ValueError(f"{path}: resource must be an absolute http:// or https:// URL")
        if not valid_iso_date(date_added):
            raise ValueError(f"{path}: date_added must be a valid YYYY-MM-DD date")
        tags = meta["tags"]
        if not isinstance(tags, list) or not tags or not all(isinstance(tag, str) for tag in tags):
            raise ValueError(f"{path}: tags must be a non-empty list of strings")
        normalized_tags = [slugify(tag) for tag in tags]
        if any(tag != normalized for tag, normalized in zip(tags, normalized_tags)):
            raise ValueError(f"{path}: tags must be lowercase and hyphenated")
        if len(set(normalized_tags)) != len(normalized_tags):
            raise ValueError(f"{path}: tags must not contain duplicates")

        source_date = optional_text(meta, "source_date", path)
        if source_date and not valid_iso_date(source_date, partial=True):
            raise ValueError(f"{path}: source_date must be YYYY, YYYY-MM, or YYYY-MM-DD")
        verification_status = optional_text(meta, "verification_status", path) or "unverified"
        if verification_status not in VERIFICATION_STATUSES:
            allowed = ", ".join(sorted(VERIFICATION_STATUSES))
            raise ValueError(f"{path}: verification_status must be one of: {allowed}")
        verification_date = optional_text(meta, "verification_date", path)
        if verification_date and not valid_iso_date(verification_date):
            raise ValueError(f"{path}: verification_date must be a valid YYYY-MM-DD date")
        if verification_status != "unverified" and not verification_date:
            raise ValueError(
                f"{path}: verification_date is required when verification_status is {verification_status}"
            )
        hacker_news_url = optional_text(meta, "hacker_news_url", path)
        if hacker_news_url and not valid_web_url(hacker_news_url):
            raise ValueError(f"{path}: hacker_news_url must be an absolute http:// or https:// URL")

        identity = (resource, quote)
        if identity in identities:
            raise ValueError(
                f"{path}: duplicates the URL and quote in {identities[identity]}"
            )
        identities[identity] = path
        records.append({
            "slug": path.stem,
            "resource": resource,
            "quote": quote,
            "date_added": date_added,
            "tags": normalized_tags,
            "source_title": optional_text(meta, "source_title", path),
            "source_author": optional_text(meta, "source_author", path),
            "source_date": source_date,
            "speaker": optional_text(meta, "speaker", path),
            "hacker_news_url": hacker_news_url,
            "verification_status": verification_status,
            "verification_date": verification_date,
        })
    return sorted(records, key=lambda record: (record["date_added"], record["slug"]), reverse=True)


def build_taxonomy(records):
    """Load the topic hierarchy, annotate records, and aggregate each node."""
    raw_tags = {tag for record in records for tag in record["tags"]}
    taxonomy_path = QUOTE_DB / "taxonomy.yml"
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
        raise ValueError(f"{taxonomy_path}: unmapped quote tag(s): {', '.join(missing)}")

    topic_records = {slug: [] for slug in nodes}
    for record in records:
        visible = []
        visible_slugs = set()
        memberships = set()
        for tag in record["tags"]:
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
        records.append({
            "slug": path.stem,
            "title": title,
            "date_published": date_published,
            "excerpt": excerpt,
            "body": body,
        })
    return sorted(
        records,
        key=lambda record: (record["date_published"], record["slug"]),
        reverse=True,
    )


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


def page(path, title, body, active=None, lede=None, quote_controls=False):
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
    quote_script = (
        f'\n<script defer src="{up}random-quotes.js"></script>'
        if quote_controls else ""
    )
    document = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Mark Reveley</title>
{description}
<link rel="stylesheet" href="{up}style.css">{quote_script}
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
    return "../" * depth + f"topics/{slugify(tag)}.html"


def writer_href(writer, depth):
    return "../" * depth + f"writers/{slugify(writer)}.html"


def source_filter_name(record):
    """Return the best available human-readable source identity."""
    if record["source_author"]:
        return record["source_author"]
    if record["source_title"]:
        return record["source_title"]
    return urlparse(record["resource"]).netloc


def quote_filter_toggle(depth, filters_on):
    up = "../" * depth
    href = up + ("quotes.html" if filters_on else "quotes-expanded.html")
    label = "Hide quote filters" if filters_on else "Show quote filters"
    state = " is-on" if filters_on else ""
    return (
        f'<a class="filter-toggle{state}" href="{href}" '
        f'aria-label="{label}" title="{label}">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6Z"/>'
        '<circle cx="12" cy="12" r="2.75"/></svg></a>'
    )


def quote_random_toggle(depth, filters_on):
    up = "../" * depth
    state = "on" if filters_on else "off"
    return (
        '<button class="random-toggle" type="button" '
        f'data-random-quote data-root="{up}" data-filters="{state}" '
        'aria-label="Load a random quote" title="Load a random quote">'
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


def quote_hero(title, lede, depth, filters_on):
    lede_html = f'\n  <p class="lede">{lede}</p>' if lede else ""
    return f"""<section class="hero">
  <div class="quote-heading">
    <h1>{html.escape(title)}</h1>
    <div class="quote-controls">
      {quote_random_toggle(depth, filters_on)}
      {quote_filter_toggle(depth, filters_on)}
    </div>
  </div>{lede_html}
</section>"""


def quote_filter_browser(feed, records, taxonomy, depth, selected_tag="", selected_source=""):
    """Wrap a quote feed with static tag and source filter rails."""
    tag_rows = []

    if selected_tag and selected_tag != "all":
        selected = taxonomy[selected_tag]
        for index, path_slug in enumerate(selected["path"]):
            node = taxonomy[path_slug]
            parent_slug = node["parent"]
            exit_href = (
                topic_href(parent_slug, depth)
                if parent_slug else "../" * depth + "quotes-expanded.html"
            )
            tag_rows.append(
                f'<li class="filter-path"><a href="{exit_href}" '
                f'aria-label="Exit {html.escape(node["label"], quote=True)} filter">'
                f'{html.escape(node["label"])}</a></li>'
            )
            if index < len(selected["path"]) - 1:
                tag_rows.append('<li class="filter-divider" aria-hidden="true"></li>')
        if selected["children"]:
            tag_rows.append('<li class="filter-divider" aria-hidden="true"></li>')
        for child_slug in selected["children"]:
            child = taxonomy[child_slug]
            tag_rows.append(
                f'<li><a href="{topic_href(child_slug, depth)}">'
                f'{html.escape(child["label"])}</a></li>'
            )
    else:
        roots = [node for node in taxonomy.values() if not node["parent"]]
        for node in sorted(roots, key=lambda item: item["label"].casefold()):
            tag_rows.append(
                f'<li><a href="{topic_href(node["slug"], depth)}">'
                f'{html.escape(node["label"])}</a></li>'
            )

    sources = sorted({source_filter_name(record) for record in records}, key=str.casefold)
    source_rows = []
    for source in sources:
        current = ' aria-current="page"' if source == selected_source else ""
        source_rows.append(
            f'<li><a href="{writer_href(source, depth)}"{current}>{html.escape(source)}</a></li>'
        )

    return f"""<section class="quote-browser" aria-label="Quote filters and results">
  <aside class="filter-rail filter-rail-tags" aria-label="Filter by tag">
    <h2>Tags</h2>
    <ul>{''.join(tag_rows)}</ul>
  </aside>
  <div class="quote-browser-feed">{feed}</div>
  <aside class="filter-rail filter-rail-sources" aria-label="Filter by author or source">
    <h2>Authors / sources</h2>
    <ul>{''.join(source_rows)}</ul>
  </aside>
</section>"""


def quote_text_html(text):
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        escaped = html.escape(paragraph).replace("\n", "<br>\n")
        paragraphs.append(f"<p>{escaped}</p>")
    return "".join(paragraphs)


def quote_card(record, depth):
    tags = "".join(
        f'<li><a href="{topic_href(slug, depth)}">{html.escape(label)}</a></li>'
        for slug, label in record["display_topics"]
    )
    resource = html.escape(record["resource"], quote=True)
    attribution_html = (
        f'  <p class="attrib">{html.escape(record["speaker"])}</p>\n'
        if record["speaker"] else ""
    )
    source_link = (
        f'<a href="{resource}" rel="noreferrer">'
        f'{html.escape(record["source_title"] or "Source")}</a>'
    )
    writer_details = []
    if record["hacker_news_url"]:
        hacker_news_url = html.escape(record["hacker_news_url"], quote=True)
        writer_details.append(
            f'<a href="{hacker_news_url}" rel="noreferrer">hn</a>'
        )
    if record["source_author"]:
        writer_details.append(
            f'<a href="{writer_href(record["source_author"], depth)}">'
            f'{html.escape(record["source_author"])}</a>'
        )
    if record["source_date"]:
        writer_details.append(pretty_date(record["source_date"]))
    source_details = " · ".join([source_link] + writer_details)
    source_title_html = f'  <p class="source-title">{source_details}</p>\n'
    record_slug = html.escape(record["slug"], quote=True)
    source_filter = source_filter_name(record)
    source_filter_label = html.escape(source_filter, quote=True)
    source_filter_url = html.escape(writer_href(source_filter, depth), quote=True)
    return f"""<article class="card quote" id="q-{record_slug}" data-quote-slug="{record_slug}" data-source-filter="{source_filter_label}" data-source-filter-href="{source_filter_url}">
  <div class="said"><blockquote>{quote_text_html(record['quote'])}</blockquote></div>
{attribution_html}{source_title_html}\
  <ul class="tags">{tags}</ul>
</article>"""


def build_random_quote_script(records):
    """Write the small client-side helper used by the random quote control."""
    OUT.mkdir(parents=True, exist_ok=True)
    slugs = json.dumps([record["slug"] for record in records], ensure_ascii=False)
    script = f"""(() => {{
  "use strict";

  const quoteSlugs = {slugs};
  const button = document.querySelector("[data-random-quote]");
  if (!button || quoteSlugs.length === 0) return;

  const root = button.dataset.root || "";
  const filtersOn = button.dataset.filters === "on";
  const pageName = filtersOn ? "quotes-expanded.html" : "quotes.html";
  const parameters = new URLSearchParams(window.location.search);
  const requestedSlug = parameters.get("quote");
  const requestedFace = Number(parameters.get("die"));
  const hasRequestedFace = Number.isInteger(requestedFace)
    && requestedFace >= 1 && requestedFace <= 6;

  function showDieFace(value) {{
    for (const face of button.querySelectorAll("[data-die-face]")) {{
      face.classList.toggle("is-visible", face.dataset.dieFace === String(value));
    }}
  }}

  if (hasRequestedFace) showDieFace(requestedFace);

  function showAssociatedFilters(card) {{
    if (!filtersOn) return;

    const tagList = document.querySelector(".filter-rail-tags ul");
    if (tagList) {{
      const rows = Array.from(card.querySelectorAll(".tags a"), (link) => {{
        const item = document.createElement("li");
        const associatedLink = link.cloneNode(true);
        associatedLink.setAttribute("aria-current", "page");
        item.append(associatedLink);
        return item;
      }});
      tagList.replaceChildren(...rows);
    }}

    const sourceList = document.querySelector(".filter-rail-sources ul");
    if (sourceList) {{
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = card.dataset.sourceFilterHref;
      link.textContent = card.dataset.sourceFilter;
      link.setAttribute("aria-current", "page");
      item.append(link);
      sourceList.replaceChildren(item);
    }}
  }}

  if (requestedSlug) {{
    const cards = Array.from(document.querySelectorAll(".card.quote"));
    const selectedCard = cards.find((card) => card.dataset.quoteSlug === requestedSlug);
    if (selectedCard) {{
      for (const card of cards) card.hidden = card !== selectedCard;
      showAssociatedFilters(selectedCard);

      const eye = document.querySelector(".filter-toggle");
      if (eye) {{
        const eyePage = filtersOn ? "quotes.html" : "quotes-expanded.html";
        const eyeParameters = new URLSearchParams({{ quote: requestedSlug }});
        if (hasRequestedFace) eyeParameters.set("die", String(requestedFace));
        eye.href = `${{root}}${{eyePage}}?${{eyeParameters}}`;
      }}
    }}
  }}

  button.addEventListener("click", () => {{
    const choices = quoteSlugs.length > 1
      ? quoteSlugs.filter((slug) => slug !== requestedSlug)
      : quoteSlugs;
    const chosen = choices[Math.floor(Math.random() * choices.length)];
    const rolledFace = Math.floor(Math.random() * 6) + 1;
    showDieFace(rolledFace);
    const nextParameters = new URLSearchParams({{
      quote: chosen,
      die: String(rolledFace),
    }});
    window.location.assign(`${{root}}${{pageName}}?${{nextParameters}}`);
  }});
}})();
"""
    (OUT / "random-quotes.js").write_text(script, encoding="utf-8")


def build_posts(records):
    cards = []
    for record in records:
        title = html.escape(record["title"])
        published = html.escape(record["date_published"], quote=True)
        date_label = html.escape(pretty_date(record["date_published"]))
        first_sentence = record["excerpt"] or re.split(r"(?<=\.)\s+", record["body"], maxsplit=1)[0]
        cards.append(f"""<article class="card post">
  <h2><a href="posts/{record['slug']}.html">{title}</a></h2>
  <p class="attrib"><time datetime="{published}">{date_label}</time></p>
  <p>{html.escape(first_sentence)}</p>
</article>""")
        post_body = f"""<article class="post-body">
  <header class="hero">
    <h1>{title}</h1>
    <p class="attrib"><time datetime="{published}">{date_label}</time></p>
  </header>
  {quote_text_html(record['body'])}
</article>"""
        page(
            f"posts/{record['slug']}.html",
            record["title"],
            post_body,
            active="index.html",
            lede=first_sentence,
        )

    post_list = "".join(cards) or '<p class="empty">No posts yet.</p>'
    body = f"""<section class="hero">
  <h1>Posts</h1>
</section>

<section class="posts">
{post_list}
</section>"""
    page("index.html", "Posts", body, active="index.html",
         lede="Mark Reveley — dev blog. Posts, quotes, and about.")


def build_quotes(records, taxonomy):
    roots = sorted(
        (node for node in taxonomy.values() if not node["parent"]),
        key=lambda node: node["label"].casefold(),
    )
    rows = "".join(
        f'<li><a href="{topic_href(node["slug"], 0)}">{html.escape(node["label"])}</a></li>'
        for node in roots
    )
    cards = "".join(quote_card(record, 0) for record in records)
    feed = cards or '<p class="empty">No quotes yet.</p>'
    lede = "A collection of decent-probability human authored quotes from selected reading, added by hand, sorted by date added"
    body = f"""{quote_hero("Quotes", lede, 0, False)}
<section class="quote-feed" aria-label="Quotes">{feed}</section>"""
    page("quotes.html", "Quotes", body, active="quotes.html",
         lede=lede, quote_controls=True)

    expanded_feed = quote_filter_browser(feed, records, taxonomy, 0)
    expanded_body = f"""{quote_hero("Quotes", lede, 0, True)}
{expanded_feed}"""
    page("quotes-expanded.html", "Quotes", expanded_body, active="quotes.html",
         lede=lede, quote_controls=True)

    tag_list = f'<ul class="topics">{rows}</ul>' if rows else '<p class="empty">No tags yet.</p>'
    tags_body = f"""<section class="hero">
  <h1>Tags</h1>
  <p class="lede">Browse the quote collection by tag.</p>
</section>
<section aria-label="All tags">{tag_list}</section>"""
    page("tags.html", "Tags", tags_body, active="quotes.html",
         lede="Browse the quote collection by tag.")


def build_writers(records, taxonomy):
    writers = {}
    for record in records:
        writers.setdefault(source_filter_name(record), []).append(record)
    rows = "".join(
        f'<li><a href="writers/{slugify(writer)}.html">{html.escape(writer)}</a></li>'
        for writer in sorted(writers, key=str.casefold)
    )
    writer_list = f'<ul class="topics">{rows}</ul>' if rows else '<p class="empty">No writers yet.</p>'
    index_body = f"""<section class="hero">
  <h1>Writer</h1>
  <p class="lede">Browse the quote collection by writer.</p>
</section>
<section aria-label="All writers">{writer_list}</section>"""
    page("writers.html", "Writer", index_body, active="quotes.html",
         lede="Browse the quote collection by writer.")

    for writer, writer_records in sorted(writers.items(), key=lambda item: item[0].casefold()):
        cards = "".join(quote_card(record, 1) for record in writer_records)
        feed = cards or '<p class="empty">No quotes yet.</p>'
        browser = quote_filter_browser(
            feed, records, taxonomy, 1, selected_source=writer
        )
        body = f"""{quote_hero(writer, "", 1, True)}
{browser}"""
        page(
            f"writers/{slugify(writer)}.html",
            f"Writer — {writer}",
            body,
            active="quotes.html",
            lede=f"Quotes by {writer}.",
            quote_controls=True,
        )


def build_topic(heading, filtered_records, all_records, taxonomy, filename, lede, selected_tag):
    cards = "".join(quote_card(record, 1) for record in filtered_records)
    if not cards:
        cards = '<p class="empty">No quotes yet.</p>'
    browser = quote_filter_browser(cards, all_records, taxonomy, 1, selected_tag=selected_tag)
    body = f"""{quote_hero(heading, lede, 1, True)}
{browser}"""
    page(
        f"topics/{filename}", heading, body, active="quotes.html",
        lede=re.sub("<[^>]+>", "", lede),
        quote_controls=True,
    )


def build_topics(records, taxonomy, topic_records):
    build_topic(
        "All quotes", records, records, taxonomy, "all.html",
        f"Every quote in the collection, {len(records)} of them, newest first.", "all",
    )
    for slug, node in sorted(
        taxonomy.items(), key=lambda item: (len(item[1]["path"]), item[1]["label"].casefold())
    ):
        count = len(topic_records[slug])
        path_label = " / ".join(taxonomy[item]["label"] for item in node["path"])
        build_topic(
            node["label"], topic_records[slug], records, taxonomy, f"{slug}.html",
            f"{count} quote{'' if count == 1 else 's'} filed under "
            f"<em>{html.escape(path_label)}</em>, newest first.",
            slug,
        )


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


def main():
    records = collect_quotes()
    posts = collect_posts()
    taxonomy, topic_records = build_taxonomy(records)
    if TOPICS.exists():
        shutil.rmtree(TOPICS)
    if WRITERS.exists():
        shutil.rmtree(WRITERS)
    build_random_quote_script(records)
    build_posts(posts)
    build_quotes(records, taxonomy)
    build_writers(records, taxonomy)
    build_topics(records, taxonomy, topic_records)
    build_about()
    pages = sorted(path.relative_to(OUT).as_posix() for path in OUT.rglob("*.html"))
    sources = len({record["resource"] for record in records})
    source_word = "source" if sources == 1 else "sources"
    print(f"{len(records)} quotes · {sources} {source_word} · {len(taxonomy)} topics")
    print(f"wrote {len(pages)} pages")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        sys.exit(str(exc))
