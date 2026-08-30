#!/usr/bin/env python3
"""Build the static site from the OKF-style records in quotes/."""

import html
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


def page(path, title, body, active=None, lede=None):
    depth = path.count("/")
    up = "../" * depth
    nav = "".join(
        '<a href="{href}"{current}>{label}</a>'.format(
            href=up + href, label=label,
            current=' aria-current="page"' if href == active else "",
        )
        for href, label in NAV
    )
    description = (
        f'<meta name="description" content="{html.escape(lede, quote=True)}">'
        if lede else ""
    )
    document = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Mark Reveley</title>
{description}
<link rel="stylesheet" href="{up}style.css">
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


def quote_text_html(text):
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        escaped = html.escape(paragraph).replace("\n", "<br>\n")
        paragraphs.append(f"<p>{escaped}</p>")
    return "".join(paragraphs)


def quote_card(record, depth):
    tags = "".join(
        f'<li><a href="{topic_href(tag, depth)}">{html.escape(tag)}</a></li>'
        for tag in record["tags"]
    )
    tags += f'<li><a href="{"../" * depth}topics/all.html">all</a></li>'
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
    return f"""<article class="card quote" id="q-{record['slug']}">
  <div class="said"><blockquote>{quote_text_html(record['quote'])}</blockquote></div>
{attribution_html}{source_title_html}\
  <ul class="tags">{tags}</ul>
</article>"""


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


def build_quotes(records, topics):
    topic_order = sorted(topics, key=lambda tag: (-len(topics[tag]), tag))
    rows = "".join(
        f'<li><a href="{topic_href(tag, 0)}">{html.escape(tag)}</a></li>'
        for tag in topic_order
    )
    cards = "".join(quote_card(record, 0) for record in records)
    feed = cards or '<p class="empty">No quotes yet.</p>'
    lede = "A collection of decent-probability human authored quotes from selected reading, added by hand, sorted by date added"
    body = f"""<section class="hero">
  <h1>Quotes</h1>
  <p class="lede">{lede}</p>
</section>
<section class="quote-feed" aria-label="Quotes">{feed}</section>"""
    page("quotes.html", "Quotes", body, active="quotes.html",
         lede=lede)

    tag_list = f'<ul class="topics">{rows}</ul>' if rows else '<p class="empty">No tags yet.</p>'
    tags_body = f"""<section class="hero">
  <h1>Tags</h1>
  <p class="lede">Browse the quote collection by tag.</p>
</section>
<section aria-label="All tags">{tag_list}</section>"""
    page("tags.html", "Tags", tags_body, active="quotes.html",
         lede="Browse the quote collection by tag.")


def build_writers(records):
    writers = {}
    for record in records:
        if record["source_author"]:
            writers.setdefault(record["source_author"], []).append(record)
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
        selected = html.escape(writer)
        cards = "".join(quote_card(record, 1) for record in writer_records)
        body = f"""<section class="hero">
  <h1>{selected}</h1>
</section>
{cards or '<p class="empty">No quotes yet.</p>'}"""
        page(
            f"writers/{slugify(writer)}.html",
            f"Writer — {writer}",
            body,
            active="quotes.html",
            lede=f"Quotes by {writer}.",
        )


def build_topic(heading, records, filename, lede):
    cards = "".join(quote_card(record, 1) for record in records)
    if not cards:
        cards = '<p class="empty">No quotes yet.</p>'
    body = f"""<section class="hero">
  <h1>{html.escape(heading)}</h1>
  <p class="lede">{lede}</p>
</section>
{cards}"""
    page(f"topics/{filename}", heading, body, active="quotes.html", lede=re.sub("<[^>]+>", "", lede))


def build_topics(records, topics):
    build_topic("All quotes", records, "all.html",
                f"Every quote in the collection, {len(records)} of them, newest first.")
    for tag in sorted(topics, key=lambda value: (-len(topics[value]), value)):
        count = len(topics[tag])
        build_topic(
            tag, topics[tag], f"{slugify(tag)}.html",
            f"{count} quote{'' if count == 1 else 's'} tagged <em>{html.escape(tag)}</em>, newest first.",
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
    topics = {}
    for record in records:
        for tag in record["tags"]:
            topics.setdefault(tag, []).append(record)
    if TOPICS.exists():
        shutil.rmtree(TOPICS)
    if WRITERS.exists():
        shutil.rmtree(WRITERS)
    build_posts(posts)
    build_quotes(records, topics)
    build_writers(records)
    build_topics(records, topics)
    build_about()
    pages = sorted(path.relative_to(OUT).as_posix() for path in OUT.rglob("*.html"))
    sources = len({record["resource"] for record in records})
    source_word = "source" if sources == 1 else "sources"
    print(f"{len(records)} quotes · {sources} {source_word} · {len(topics)} topics")
    print(f"wrote {len(pages)} pages")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        sys.exit(str(exc))
