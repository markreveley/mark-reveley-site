#!/usr/bin/env python3
"""Build the static site in site/ from the research bundle in research/.

The site has one object: the quote. Every verbatim excerpt in the bundle
becomes one card — the quote text, a note, its date, the URL it came from, and
its labels. Sources, views and the level hierarchy are not rendered as pages of
their own.

Quotes are reached by topic. quotes.html lists every topic in the corpus;
topics/<tag>.html holds the quotes carrying that tag, and topics/all.html holds
the lot. A quote carries several tags, so it appears under each of them.

Output is HTML + CSS only: no JavaScript, nothing to run to *view* the
result. Building it needs PyYAML and Python-Markdown:

    pip install pyyaml markdown
    python3 site/build.py
"""

import html
import re
import sys
from pathlib import Path

try:
    import yaml
    from markdown import Extension, Markdown
    from markdown.preprocessors import Preprocessor
    from markdown.treeprocessors import Treeprocessor
    from xml.etree import ElementTree as etree
except ImportError as exc:  # pragma: no cover
    sys.exit(f"{exc}; this build script needs: pip install pyyaml markdown")

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "research" / "graph-engineering"
OUT = ROOT / "site"

# Directories and pages the build clears first, so a rebuild leaves no orphans:
# the topic pages (a tag dropped from the bundle should lose its page) and the
# pages an older, level-structured version of this site generated.
STALE = ["topics", "reading.html", "sources.html", "excerpts.html",
         "views.html", "views"]


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------

def load(path):
    """Split a bundle document into (frontmatter dict, body text)."""
    text = path.read_text(encoding="utf-8")
    meta = {}
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            raw, body = text[4:end], text[end + 5:]
            try:
                meta = yaml.safe_load(raw) or {}
            except yaml.YAMLError:
                meta = dict(re.findall(r"^(\w+): (.+)$", raw, re.M))
    return meta, body


def sections(body):
    """Map '# Heading' -> the markdown under it (top-level headings only)."""
    out, name, buf = {}, None, []
    for line in body.splitlines():
        if line.startswith("# "):
            if name is not None:
                out[name] = "\n".join(buf).strip()
            name, buf = line[2:].strip(), []
        else:
            buf.append(line)
    if name is not None:
        out[name] = "\n".join(buf).strip()
    return out


def sec(doc, *names):
    """First matching body section — headings vary (Quote vs Quotes)."""
    for n in names:
        if n in doc["sec"]:
            return doc["sec"][n]
    return ""


def collect(dirname):
    docs = {}
    for path in sorted((BUNDLE / dirname).glob("*.md")):
        if path.name == "index.md":
            continue
        meta, body = load(path)
        docs[path.stem] = {
            "slug": path.stem,
            "path": f"{dirname}/{path.name}",
            "meta": meta,
            "body": body,
            "sec": sections(body),
            "title": meta.get("title") or path.stem,
            "description": meta.get("description", ""),
            "tags": meta.get("tags") or [],
        }
    return docs


# --------------------------------------------------------------------------
# dates
#
# The bundle writes source dates as free text: an ISO date, sometimes a year
# only, sometimes with a parenthetical ("2010 (SIGMOD, pp. 135-146)"), and
# sometimes no date at all ("living document"). Read the leading date off the
# front for display and sorting; keep the rest as-is when there is none.
# --------------------------------------------------------------------------

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

LEAD_DATE = re.compile(r"^\s*(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?")


def parse_date(raw):
    """(y, m, d) as ints with 0 for the parts a date string omits, or None."""
    m = LEAD_DATE.match(str(raw or ""))
    if not m:
        return None
    y, mo, d = m.group(1), m.group(2), m.group(3)
    return int(y), int(mo or 0), int(d or 0)


def pretty_date(raw):
    """'2026-07-04' -> '4 July 2026'; '2026-04' -> 'April 2026'; '2026' -> '2026'.

    A string with no leading date ('living document') is shown as written.
    """
    parts = parse_date(raw)
    if not parts:
        return str(raw or "").strip()
    y, mo, d = parts
    if d:
        return f"{d} {MONTHS[mo - 1]} {y}"
    if mo:
        return f"{MONTHS[mo - 1]} {y}"
    return str(y)


def date_key(raw):
    """Sort key, newest first; undated entries sort to the end."""
    parts = parse_date(raw)
    if not parts:
        return (0, 0, 0, 0)
    y, mo, d = parts
    return (1, y, mo, d)


# --------------------------------------------------------------------------
# link resolution
#
# A link between two excerpts becomes an anchor on topics/all.html, the one
# page that is guaranteed to hold every quote — a topic page holds only its own.
# A link to anything else — a source record, an issue, a view, the bundle README
# — has no page here, so it keeps its text and loses its href rather than going
# dead.
# --------------------------------------------------------------------------

def resolve(href, depth, base=None):
    if href.startswith(("http://", "https://", "mailto:")):
        return href
    href = href.split("#")[0]
    m = re.search(r"(?:(excerpts|references|issues|views)/)?([\w.\-]+)\.md$", href)
    if not m:
        return None
    kind, slug = m.group(1) or base, m.group(2)
    if kind != "excerpts" or slug == "index" or slug not in excs:
        return None
    return "../" * depth + f"topics/all.html#q-{slug}"


# --------------------------------------------------------------------------
# markdown rendering — Python-Markdown, plus tree passes that adapt its output
# to this site: bundle links become site anchors, headings are shifted under
# the page's own <h1>, and tables get a scroll wrapper.
# --------------------------------------------------------------------------

FOOTNOTE_REF = re.compile(r"\[\^[\w.\-]+\]")
FOOTNOTE_DEF = re.compile(r"^\[\^[\w.\-]+\]:.*$", re.M)


class StripFootnotes(Preprocessor):
    """Drop footnote markers and definitions.

    Every excerpt footnotes its own source, which the card already links at
    the bottom; rendering them again per card would repeat that a hundred
    times.
    """

    def run(self, lines):
        text = FOOTNOTE_DEF.sub("", "\n".join(lines))
        return [ln.rstrip() for ln in FOOTNOTE_REF.sub("", text).splitlines()]


class RewriteLinks(Treeprocessor):
    """Point bundle markdown links at their anchor on this site."""

    def __init__(self, md, depth, base):
        super().__init__(md)
        self.depth, self.base = depth, base

    def run(self, root):
        for a in root.iter("a"):
            href = a.get("href", "")
            if href.startswith(("http://", "https://", "mailto:")):
                a.set("rel", "noreferrer")
                continue
            target = resolve(href, self.depth, self.base)
            if target is None:
                a.tag = "span"
                a.attrib.pop("href", None)
            else:
                a.set("href", target)


class ShiftHeadings(Treeprocessor):
    """Renumber headings so a section's `#` sits under the page's own <h1>."""

    def __init__(self, md, base):
        super().__init__(md)
        self.base = base

    def run(self, root):
        for el in root.iter():
            if len(el.tag) == 2 and el.tag[0] == "h" and el.tag[1].isdigit():
                el.tag = f"h{min(6, self.base + int(el.tag[1]) - 1)}"


class WrapTables(Treeprocessor):
    """Let a wide table scroll inside its own box instead of the page."""

    def run(self, root):
        for i, child in enumerate(list(root)):
            if child.tag == "table":
                box = etree.Element("div", {"class": "scroll"})
                box.append(child)
                root[i] = box


class SplitQuotes(Treeprocessor):
    """Give each statement its own quote mark.

    An excerpt that quotes its source twice writes two blockquotes separated
    by a blank line; Python-Markdown folds those into one. Split them back
    apart so the card shows two quotations, not one two-paragraph quotation.
    """

    def run(self, root):
        children = []
        for child in root:
            paras = list(child)
            if child.tag == "blockquote" and len(paras) > 1 and \
                    all(p.tag == "p" for p in paras):
                for para in paras:
                    quote = etree.Element("blockquote")
                    quote.append(para)
                    children.append(quote)
            else:
                children.append(child)
        root[:] = children


class BundleExtension(Extension):
    def __init__(self, depth, heading_base, base):
        self.depth, self.heading_base, self.base = depth, heading_base, base
        super().__init__()

    def extendMarkdown(self, md):
        # \" is a markdown escape in the bundle's quoted passages; Python-
        # Markdown's own escape set predates that convention.
        if '"' not in md.ESCAPED_CHARS:
            md.ESCAPED_CHARS.append('"')
        md.preprocessors.register(StripFootnotes(md), "strip_footnotes", 40)
        md.treeprocessors.register(RewriteLinks(md, self.depth, self.base), "bundle_links", 4)
        md.treeprocessors.register(ShiftHeadings(md, self.heading_base), "shift_headings", 3)
        md.treeprocessors.register(WrapTables(md), "wrap_tables", 2)
        md.treeprocessors.register(SplitQuotes(md), "split_quotes", 1)


_converters = {}


def _converter(depth, heading_base, base):
    key = (depth, heading_base, base)
    if key not in _converters:
        _converters[key] = Markdown(
            extensions=["tables", BundleExtension(depth, heading_base, base)],
            output_format="html")
    return _converters[key].reset()


def markdown(text, depth=0, heading_base=3, base=None):
    """Render a bundle markdown fragment as HTML for a page `depth` dirs down.

    `base` names the collection the fragment came from, for sibling links.
    """
    return _converter(depth, heading_base, base).convert(text.strip())


def inline(text, depth=0, base=None):
    """Render a one-line fragment (a description, a label) without the <p>."""
    out = markdown(text, depth, base=base)
    m = re.fullmatch(r"<p>(.*)</p>", out, re.S)
    return m.group(1) if m else out


# --------------------------------------------------------------------------
# page shell
# --------------------------------------------------------------------------

NAV = [("index.html", "Posts"), ("quotes.html", "Quotes"), ("about.html", "About")]


def page(path, title, body, active=None, lede=None):
    depth = path.count("/")
    up = "../" * depth
    nav = "".join(
        '<a href="{href}"{cur}>{label}</a>'.format(
            href=up + href, label=label,
            cur=' aria-current="page"' if href == active else "")
        for href, label in NAV)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Mark Reveley</title>
{'<meta name="description" content="' + html.escape(lede or "", quote=True) + '">' if lede else ''}
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
<footer class="foot">
  <p>Static HTML and CSS. No JavaScript, no tracking, nothing to run.</p>
</footer>
</body>
</html>
"""
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc, encoding="utf-8")
    return dest


def topic_href(tag, depth):
    """Where a topic lives. Tags are already slug-shaped; this only guards it."""
    slug = re.sub(r"[^a-z0-9._-]+", "-", str(tag).lower()).strip("-") or "untagged"
    return "../" * depth + f"topics/{slug}.html"


def tags_html(kind, tags, depth):
    """The card's bottom row: what kind of statement it is, then its topics."""
    items = [f'<li class="kind">{html.escape(str(kind))}</li>'] if kind else []
    items += [f'<li><a href="{topic_href(t, depth)}">{html.escape(str(t))}</a></li>'
              for t in tags]
    return f'<ul class="tags">{"".join(items)}</ul>' if items else ""


# --------------------------------------------------------------------------
# index the bundle
# --------------------------------------------------------------------------

refs = collect("references")
excs = collect("excerpts")

# quote -> the sources it was taken from
for e in excs.values():
    e["src"] = []
    for s in (e["meta"].get("sources") or []):
        m = re.search(r"references/([\w.\-]+)\.md", str(s.get("resource", "")))
        if m and m.group(1) in refs:
            e["src"].append(m.group(1))
    # A quote is dated by the source it came from — the first one it cites.
    e["date"] = refs[e["src"][0]]["meta"].get("source_date", "") if e["src"] else ""

# Newest first; undated quotes ("living document") fall to the end.
ORDER = sorted(excs.values(),
               key=lambda e: (tuple(-n for n in date_key(e["date"])),
                              e["title"].lower()))

# topic -> its quotes, in that same order. Topics come off the quotes alone:
# a source's own tags describe the source, which this site no longer renders.
topics = {}
for e in ORDER:
    for tag in e["tags"]:
        topics.setdefault(str(tag), []).append(e)

# Most-used first, alphabetical within a count — the order the old by-tag view
# used, and the one that puts the useful topics at the top of the list.
TOPIC_ORDER = sorted(topics, key=lambda tg: (-len(topics[tg]), tg))


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

def source_links(e):
    """The URLs this quote came from, one per line, bare."""
    rows = []
    for slug in e["src"]:
        url = str(refs[slug]["meta"].get("resource", "")).strip()
        if not url:
            continue
        safe = html.escape(url, quote=True)
        if url.startswith(("http://", "https://")):
            rows.append(f'<li><a href="{safe}" rel="noreferrer">{html.escape(url)}</a></li>')
        else:
            rows.append(f"<li>{html.escape(url)}</li>")
    return f'<ul class="src">{"".join(rows)}</ul>' if rows else ""


def quote_card(e, depth):
    quote = markdown(sec(e, "Quote", "Quotes"), depth, base="excerpts")
    note = markdown(sec(e, "Note"), depth, base="excerpts")
    speaker = str(e["meta"].get("speaker", "")).strip()
    when = pretty_date(e["date"])
    line = " · ".join(x for x in (html.escape(speaker), html.escape(when)) if x)
    return f"""<article class="card quote" id="q-{e['slug']}">
  <h2><a class="self" href="#q-{e['slug']}">{html.escape(e['title'])}</a></h2>
  <div class="said">{quote}</div>
  <div class="note">{note}</div>
  <p class="attrib">{line}</p>
  {source_links(e)}
  {tags_html(e['meta'].get('subtype'), e['tags'], depth)}
</article>"""


def build_posts():
    body = """<section class="hero">
  <h1>Posts</h1>
  <p class="lede">Notes on building things — agents, graphs, and the occasional
  detour through a sampler. Written when there is something worth writing down.</p>
</section>

<section class="posts">
  <!-- A post goes here. Copy this block, fill it in, newest first:

  <article class="card post">
    <h2><a href="posts/slug.html">Post title</a></h2>
    <p class="attrib"><time datetime="2026-09-01">1 September 2026</time></p>
    <p>One-paragraph summary.</p>
  </article>

  -->
  <p class="empty">No posts yet.</p>
  <p class="empty-note">Nothing published so far. In the meantime, the
  <a href="quotes.html">quotes</a> section has what I have been reading.</p>
</section>"""
    page("index.html", "Posts", body, active="index.html",
         lede="Mark Reveley — dev blog. Posts, quotes, and about.")


def build_quotes():
    """The landing page: the sentence, then the list of topics."""
    n_src = len({s for e in excs.values() for s in e["src"]})
    rows = "".join(
        f'<li><a href="{topic_href(tg, 0)}">{html.escape(tg)}</a>'
        f'<span class="count">{len(topics[tg])}</span></li>'
        for tg in TOPIC_ORDER)
    body = f"""<section class="hero">
  <h1>Quotes</h1>
  <p class="lede">A collection of quotes from selected reading.</p>
  <p class="counts">{len(ORDER)} quotes from {n_src} sources, tagged with
  {len(TOPIC_ORDER)} topics. Pick one below, or
  <a href="topics/all.html">read them all</a>.</p>
</section>

<h2 class="topics-head">Topics</h2>
<ul class="topics">{rows}</ul>"""
    page("quotes.html", "Quotes", body, active="quotes.html",
         lede="A collection of quotes from selected reading.")


def build_topic(heading, quotes, filename, lede):
    body = f"""<section class="hero">
  <h1>{html.escape(heading)}</h1>
  <p class="lede">{lede}</p>
  <p class="counts"><a href="../quotes.html">All topics</a></p>
</section>
{''.join(quote_card(e, 1) for e in quotes)}"""
    page(f"topics/{filename}", heading, body, active="quotes.html", lede=lede)


def build_topics():
    build_topic("All quotes", ORDER, "all.html",
                f"Every quote in the corpus, {len(ORDER)} of them, newest first.")
    for tg in TOPIC_ORDER:
        quotes = topics[tg]
        n = len(quotes)
        build_topic(tg, quotes, Path(topic_href(tg, 0)).name,
                    f"{n} quote{'' if n == 1 else 's'} tagged "
                    f"<em>{html.escape(tg)}</em>, newest first.")


def build_about():
    body = """<section class="hero">
  <h1>About</h1>
  <p class="lede">Mark Reveley is a musician developer living in Berkeley.</p>
</section>

<section class="about-more">
  <p>This site is three things: <a href="index.html">posts</a> when there are
  any, a <a href="quotes.html">quotes</a> section — one quote per statement,
  each with the date and the URL it came from — and this page.</p>
  <p>It is static HTML and CSS — no JavaScript, no framework, no analytics.</p>
</section>"""
    page("about.html", "About", body, active="about.html",
         lede="Mark Reveley is a musician developer living in Berkeley.")


def clean():
    """Remove pages the level-structured version of this site used to write."""
    for name in STALE:
        target = OUT / name
        if target.is_dir():
            for child in sorted(target.rglob("*"), reverse=True):
                child.unlink() if child.is_file() else child.rmdir()
            target.rmdir()
        elif target.exists():
            target.unlink()


def main():
    clean()
    build_posts()
    build_quotes()
    build_topics()
    build_about()
    pages = sorted(p.relative_to(OUT).as_posix() for p in OUT.rglob("*.html"))
    print(f"{len(excs)} quotes · {len(refs)} sources indexed · "
          f"{len(TOPIC_ORDER)} topics")
    print(f"wrote {len(pages)} pages")


if __name__ == "__main__":
    main()
