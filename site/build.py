#!/usr/bin/env python3
"""Build the static site in site/ from the research bundle in research/.

Output is HTML + CSS only: no JavaScript, no runtime dependencies, no build
step needed to *view* the result. Run this after editing the bundle:

    python3 site/build.py
"""

import html
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("this build script needs PyYAML: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "research" / "graph-engineering"
OUT = ROOT / "site"

ROLE_ORDER = ["issue", "position", "argument", "evidence"]
REL_LABELS = {
    "responds-to": "responds to",
    "supports": "supports",
    "refines": "refines",
    "objects-to": "objects to",
    "answers": "answers",
    "exemplifies": "exemplifies",
    "precedes": "precedes",
}


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
# link resolution: bundle markdown paths -> site anchors
# --------------------------------------------------------------------------

def anchor(kind, slug):
    return {
        "excerpts": f"excerpts.html#e-{slug}",
        "references": f"sources.html#s-{slug}",
        "issues": f"views/by-issue.html#i-{slug}",
    }[kind] if kind in ("excerpts", "references", "issues") else None


def resolve(href, depth):
    """Rewrite a bundle-relative markdown link for a page `depth` dirs down.

    Returns None when the target has no page on this site, so the caller can
    render the link text as plain prose instead of a dead link.
    """
    up = "../" * depth
    if href.startswith(("http://", "https://", "mailto:")):
        return href
    href = href.split("#")[0]
    m = re.search(r"(excerpts|references|issues|views)/([\w.\-]+)\.md$", href)
    if not m:
        return None
    kind, slug = m.group(1), m.group(2)
    if slug == "index":
        page = {"excerpts": "excerpts.html", "references": "sources.html",
                "issues": "views/by-issue.html", "views": "views.html"}[kind]
        return up + page
    if kind == "views":
        return up + f"views/{slug}.html"
    return up + anchor(kind, slug)


# --------------------------------------------------------------------------
# a small markdown renderer (only the constructs the bundle actually uses)
# --------------------------------------------------------------------------

INLINE_CODE = re.compile(r"`([^`]+)`")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
ITALIC = re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])")
FOOTREF = re.compile(r"\[\^[\w.\-]+\]")


def inline(text, depth):
    text = FOOTREF.sub("", text)
    text = html.escape(text, quote=False)

    def link(m):
        label, href = m.group(1), html.unescape(m.group(2))
        target = resolve(href, depth)
        if target is None:
            return label
        ext = ' rel="noreferrer"' if target.startswith("http") else ""
        return f'<a href="{html.escape(target, quote=True)}"{ext}>{label}</a>'

    text = LINK.sub(link, text)
    text = INLINE_CODE.sub(r"<code>\1</code>", text)
    text = BOLD.sub(r"<strong>\1</strong>", text)
    text = ITALIC.sub(r"<em>\1</em>", text)
    # markdown backslash escapes (\" inside a quoted passage, \[ , ...)
    text = re.sub(r'\\([\\`*_{}\[\]()#+\-.!"\'])', r"\1", text)
    return text.strip()


def markdown(md, depth=0, heading_base=3):
    """Render a markdown fragment. Supports headings, paragraphs, lists,
    blockquotes and GFM tables — everything the bundle uses."""
    lines = [ln for ln in md.splitlines() if not re.match(r"^\[\^[\w.\-]+\]:", ln)]
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            tag = f"h{min(6, heading_base + level - 1)}"
            out.append(f"<{tag}>{inline(line.lstrip('#').strip(), depth)}</{tag}>")
            i += 1

        elif line.lstrip().startswith(("* ", "- ")) :
            items = []
            while i < len(lines) and lines[i].lstrip().startswith(("* ", "- ")):
                items.append(inline(lines[i].lstrip()[2:], depth))
                i += 1
            out.append("<ul>" + "".join(f"<li>{it}</li>" for it in items) + "</ul>")

        elif line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i].lstrip("> ").rstrip())
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(quote), depth)}</p></blockquote>")

        elif "|" in line and i + 1 < len(lines) and re.match(r"^[\s|:\-]+$", lines[i + 1]) and "-" in lines[i + 1]:
            head = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "".join(f"<th>{inline(c, depth)}</th>" for c in head)
            tbody = "".join(
                "<tr>" + "".join(f"<td>{inline(c, depth)}</td>" for c in r) + "</tr>"
                for r in rows
            )
            out.append(
                '<div class="scroll"><table><thead><tr>' + thead
                + "</tr></thead><tbody>" + tbody + "</tbody></table></div>"
            )

        else:
            para = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", ">")) \
                    and not lines[i].lstrip().startswith(("* ", "- ")):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para), depth)}</p>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# page shell
# --------------------------------------------------------------------------

NAV = [("index.html", "Posts"), ("reading.html", "Reading"), ("about.html", "About")]
SUBNAV = [("reading.html", "Overview"),
          ("sources.html", "Level 1 · Sources"),
          ("excerpts.html", "Level 2 · Excerpts"),
          ("views.html", "Level 3 · Views")]


def page(path, title, body, subnav=None, active=None, lede=None):
    depth = path.count("/")
    up = "../" * depth
    nav = "".join(
        '<a href="{href}"{cur}>{label}</a>'.format(
            href=up + href, label=label,
            cur=' aria-current="page"' if href == active or (
                active in dict(SUBNAV) and href == "reading.html") else "")
        for href, label in NAV)
    sub = ""
    if subnav:
        sub = '<nav class="subnav" aria-label="Reading">' + "".join(
            '<a href="{href}"{cur}>{label}</a>'.format(
                href=up + href, label=label,
                cur=' aria-current="page"' if href == active else "")
            for href, label in SUBNAV) + "</nav>"
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
{sub}
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


def tags_html(tags, depth=0):
    if not tags:
        return ""
    up = "../" * depth
    return '<ul class="tags">' + "".join(
        f'<li><a href="{up}views/by-tag.html#t-{html.escape(str(t))}">{html.escape(str(t))}</a></li>'
        for t in tags) + "</ul>"


def badge(kind, value):
    return f'<span class="badge badge-{kind}">{html.escape(str(value))}</span>'


# --------------------------------------------------------------------------
# index the bundle
# --------------------------------------------------------------------------

refs = collect("references")
excs = collect("excerpts")
issues = collect("issues")

# excerpt -> its sources; source -> its excerpts
for e in excs.values():
    e["src"] = []
    for s in (e["meta"].get("sources") or []):
        m = re.search(r"references/([\w.\-]+)\.md", str(s.get("resource", "")))
        if m and m.group(1) in refs:
            e["src"].append(m.group(1))
for r in refs.values():
    r["excerpts"] = [s for s, e in excs.items() if r["slug"] in e["src"]]

# typed edges, forward and backward
for e in excs.values():
    e["out"], e["back"] = [], []
for e in excs.values():
    for d in (e["meta"].get("deps") or []):
        target = str(d.get("concept", ""))
        rel = d.get("rel", "relates-to")
        m = re.search(r"(excerpts|issues)/([\w.\-]+)\.md", target)
        if not m:
            continue
        kind, slug = m.group(1), m.group(2)
        e["out"].append((rel, kind, slug))
        if kind == "excerpts" and slug in excs:
            excs[slug]["back"].append((rel, e["slug"]))
        elif kind == "issues" and slug in issues:
            issues[slug].setdefault("positions", []).append((rel, e["slug"]))

# tag -> documents
tag_index = {}
for coll, kind in ((excs, "excerpts"), (refs, "references"), (issues, "issues")):
    for d in coll.values():
        for t in d["tags"]:
            tag_index.setdefault(
                str(t), {"excerpts": [], "references": [], "issues": []}
            )[kind].append(d["slug"])


def link_exc(slug, depth, cls=""):
    if slug not in excs:
        return html.escape(slug)
    up = "../" * depth
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{up}excerpts.html#e-{slug}">{html.escape(excs[slug]["title"])}</a>'


def link_issue(slug, depth):
    up = "../" * depth
    title = issues[slug]["title"] if slug in issues else slug
    return f'<a href="{up}views/by-issue.html#i-{slug}">{html.escape(title)}</a>'


def link_ref(slug, depth):
    up = "../" * depth
    return f'<a href="{up}sources.html#s-{slug}">{html.escape(refs[slug]["title"])}</a>'


def relation_list(e, depth):
    rows = []
    for rel, kind, slug in e["out"]:
        target = link_issue(slug, depth) if kind == "issues" else link_exc(slug, depth)
        rows.append(f'<li><span class="rel">{REL_LABELS.get(rel, rel)}</span> {target}</li>')
    for rel, slug in sorted(e["back"]):
        rows.append(f'<li><span class="rel rel-in">{REL_LABELS.get(rel, rel)} this</span> {link_exc(slug, depth)}</li>')
    if not rows:
        return '<p class="none">No typed edges.</p>'
    return f'<ul class="edges">{"".join(rows)}</ul>'


def excerpt_card(e, depth=0, show_source=True):
    quote = markdown(sec(e, "Quote", "Quotes"), depth)
    note = markdown(sec(e, "Note"), depth)
    meta = e["meta"]
    bits = [badge("role", meta.get("role", "—")), badge("subtype", meta.get("subtype", "—"))]
    if meta.get("speaker"):
        bits.append(f'<span class="speaker">{html.escape(str(meta["speaker"]))}</span>')
    src = ""
    if show_source and e["src"]:
        src = '<p class="from">From ' + " · ".join(link_ref(s, depth) for s in e["src"]) + "</p>"
    return f"""<article class="card excerpt" id="e-{e['slug']}">
  <h3><a class="self" href="{'../' * depth}excerpts.html#e-{e['slug']}">{html.escape(e['title'])}</a></h3>
  <p class="badges">{''.join(bits)}</p>
  {quote}
  <div class="note">{note}</div>
  {src}
  <details class="edges-box"><summary>Typed edges</summary>{relation_list(e, depth)}</details>
  {tags_html(e['tags'], depth)}
</article>"""


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

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
    <p class="badges"><time datetime="2026-09-01">1 September 2026</time></p>
    <p>One-paragraph summary.</p>
  </article>

  -->
  <p class="empty">No posts yet.</p>
  <p class="empty-note">Nothing published so far. In the meantime, the
  <a href="reading.html">reading</a> section has what I have been going through.</p>
</section>"""
    page("index.html", "Posts", body, active="index.html",
         lede="Mark Reveley — dev blog. Posts, reading notes, and about.")


def build_reading():
    n_views = 5
    body = f"""<section class="hero">
  <h1>Reading</h1>
  <p class="lede">What I read gets decomposed into three levels: the
  <strong>sources</strong> themselves, the <strong>excerpts</strong> pulled
  verbatim out of them, and the <strong>views</strong> that arrange those
  excerpts into something you can read end to end. Each level links down to the
  next and back up again.</p>
</section>

<section class="levels">
  <article class="card level">
    <p class="level-no">Level 1</p>
    <h2><a href="sources.html">Sources</a></h2>
    <p>{len(refs)} primary and secondary sources — essays, papers, docs, threads
    — each with what it is, when it was published, and whether I could actually
    fetch it.</p>
    <p class="down">Down to the quotes taken from each one.</p>
  </article>

  <article class="card level">
    <p class="level-no">Level 2</p>
    <h2><a href="excerpts.html">Excerpts</a></h2>
    <p>{len(excs)} verbatim quotes, one idea each, typed by the part they play in
    the argument (issue, position, argument, evidence) and wired to one another
    with typed edges.</p>
    <p class="down">Up to its source, across to the quotes it answers.</p>
  </article>

  <article class="card level">
    <p class="level-no">Level 3</p>
    <h2><a href="views.html">Views</a></h2>
    <p>{n_views} arrangements over the excerpts — by date, by open question, by
    role, by tag, by edge. A view selects and orders; it does not conclude.</p>
    <p class="down">Down into the excerpts it composes.</p>
  </article>
</section>

<section class="current">
  <h2>Currently reading</h2>
  <p><strong>Graph engineering</strong> — where the term came from, and whether
  the 2026 version of it is a new discipline or a rename of workflow
  engineering. {len(refs)} sources, {len(excs)} excerpts, {len(issues)} open
  questions.</p>
  <p>Start with the <a href="views/timeline.html">timeline</a> if you want the
  shape of it, or the <a href="views/by-issue.html">open questions</a> if you
  want the disagreements.</p>
</section>"""
    page("reading.html", "Reading", body, subnav=True, active="reading.html",
         lede="Three levels: sources, excerpts, views.")


def build_sources():
    by_letter = {}
    for r in sorted(refs.values(), key=lambda d: d["title"].lower()):
        by_letter.setdefault(r["title"].lstrip('"').upper()[0], []).append(r)
    jump = '<nav class="jump" aria-label="Jump to letter">' + "".join(
        f'<a href="#l-{L}">{L}</a>' for L in sorted(by_letter)) + "</nav>"

    blocks = []
    for L in sorted(by_letter):
        blocks.append(f'<h2 class="letter" id="l-{L}">{L}</h2>')
        for r in by_letter[L]:
            m = r["meta"]
            head = html.escape(r["title"])
            if m.get("resource"):
                head = (f'<a href="{html.escape(str(m["resource"]), quote=True)}" '
                        f'rel="noreferrer">{head}</a>')
            meta_bits = []
            if m.get("source_author"):
                meta_bits.append(html.escape(str(m["source_author"])))
            if m.get("source_date"):
                meta_bits.append(html.escape(str(m["source_date"])))
            if m.get("availability"):
                meta_bits.append(badge("avail", m["availability"]))
            kids = r["excerpts"]
            kid_html = (
                '<details class="edges-box" open><summary>'
                f'{len(kids)} excerpt{"s" if len(kids) != 1 else ""} from this source'
                '</summary><ul class="edges">'
                + "".join(f"<li>{link_exc(s, 0)}</li>" for s in sorted(
                    kids, key=lambda s: excs[s]["title"].lower()))
                + "</ul></details>"
            ) if kids else '<p class="none">No excerpts taken from this one yet.</p>'
            about = markdown(sec(r, "About"), 0)
            blocks.append(f"""<article class="card source" id="s-{r['slug']}">
  <h3>{head}</h3>
  <p class="badges">{' · '.join(meta_bits)}</p>
  <p class="desc">{inline(r['description'], 0)}</p>
  <div class="about">{about}</div>
  {kid_html}
  {tags_html(r['tags'], 0)}
</article>""")

    body = f"""<section class="hero">
  <h1>Level 1 · Sources</h1>
  <p class="lede">{len(refs)} sources, alphabetical. Each links out to the
  original and down to the excerpts taken from it. <em>Availability</em> records
  whether the text could be fetched and quoted directly, or whether the quotes
  came through a mirror.</p>
</section>
{jump}
{''.join(blocks)}"""
    page("sources.html", "Sources", body, subnav=True, active="sources.html",
         lede=f"{len(refs)} primary and secondary sources.")


def build_excerpts():
    ordered = sorted(refs.values(), key=lambda d: d["title"].lower())
    jump = '<nav class="jump wrap" aria-label="Jump to source">' + "".join(
        f'<a href="#g-{r["slug"]}">{html.escape(r["title"])}</a>'
        for r in ordered if r["excerpts"]) + "</nav>"

    blocks, seen = [], set()
    for r in ordered:
        if not r["excerpts"]:
            continue
        kids = sorted(r["excerpts"], key=lambda s: excs[s]["title"].lower())
        # An excerpt can cite two sources; it is filed under the first and
        # cross-referenced from the rest, so every id stays unique.
        own = [s for s in kids if excs[s]["src"][0] == r["slug"]]
        shared = [s for s in kids if s not in own]
        seen.update(own)
        cross = ""
        if shared:
            cross = ('<p class="group-meta">Also draws on: ' + " · ".join(
                link_exc(s, 0) for s in shared) + "</p>")
        blocks.append(f"""<section class="group" id="g-{r['slug']}">
  <h2>{html.escape(r['title'])}</h2>
  <p class="group-meta">{len(kids)} excerpt{"s" if len(kids) != 1 else ""} ·
    <a href="sources.html#s-{r['slug']}">source record</a></p>
  {cross}
  {''.join(excerpt_card(excs[s], 0, show_source=len(excs[s]["src"]) > 1) for s in own)}
</section>""")
    orphans = [s for s in sorted(excs) if s not in seen]
    if orphans:
        blocks.append('<section class="group" id="g-other"><h2>Unattached</h2>'
                      + "".join(excerpt_card(excs[s]) for s in orphans) + "</section>")

    roles = {r: sum(1 for e in excs.values() if e["meta"].get("role") == r) for r in ROLE_ORDER}
    counts = " · ".join(f"{n} {r}" for r, n in roles.items() if n)
    body = f"""<section class="hero">
  <h1>Level 2 · Excerpts</h1>
  <p class="lede">{len(excs)} verbatim quotes, grouped under the source they came
  from. Each carries a <strong>role</strong> in the argument and a
  <strong>subtype</strong> saying what kind of move it makes, plus typed edges to
  the quotes and questions it touches — open <em>Typed edges</em> on any card to
  walk sideways.</p>
  <p class="counts">{counts}</p>
  <p class="counts">Other ways in:
    <a href="views/by-role.html">by role</a> ·
    <a href="views/by-issue.html">by open question</a> ·
    <a href="views/by-tag.html">by tag</a></p>
</section>
{jump}
{''.join(blocks)}"""
    page("excerpts.html", "Excerpts", body, subnav=True, active="excerpts.html",
         lede=f"{len(excs)} verbatim excerpts, typed and cross-linked.")


VIEWS = [
    ("timeline.html", "Timeline: 1736 → 2026",
     "The dated genealogy — Euler to the July 2026 naming events — with every "
     "row linked to the excerpt that evidences it.", False),
    ("by-issue.html", "By open question",
     "The root questions the corpus disagrees about, each with the positions on "
     "record and no verdict.", True),
    ("by-role.html", "By role in the argument",
     "The same excerpts sorted into issues, positions, arguments and evidence — "
     "the shape of the debate rather than its chronology.", True),
    ("by-tag.html", "By tag",
     "Every tag in the corpus, with the excerpts and sources carrying it. The "
     "cross-cutting index.", True),
    ("edges.html", "By typed edge",
     "The DAG flattened into an edge list, grouped by relation: what supports, "
     "refines, objects to or precedes what.", True),
]

DEMO = ('<p class="demo"><strong>Demo view.</strong> Composed for this site out of '
        'the corpus, to show what the views level can hold — the bundle itself '
        'ships one hand-written view, the <a href="timeline.html">timeline</a>.</p>')


def view_page(filename, title, body, lede, demo=True):
    head = f"""<section class="hero">
  <h1>{html.escape(title)}</h1>
  <p class="lede">{lede}</p>
  {DEMO if demo else ''}
</section>"""
    page(f"views/{filename}", title, head + body, subnav=True,
         active="views.html", lede=lede)


def build_views_index():
    cards = []
    for filename, title, blurb, demo in VIEWS:
        tag = '<span class="badge badge-demo">demo</span>' if demo else \
              '<span class="badge badge-real">in the bundle</span>'
        cards.append(f"""<article class="card view">
  <h2><a href="views/{filename}">{html.escape(title)}</a></h2>
  <p class="badges">{tag}</p>
  <p>{blurb}</p>
</article>""")
    body = f"""<section class="hero">
  <h1>Level 3 · Views</h1>
  <p class="lede">A view arranges excerpts — by date, by question, by role, by
  edge — without adding conclusions. Whatever position a view takes is implicit
  in what it selects and how it orders it.</p>
  <p class="counts">One view ships with the research bundle; the rest are demos
  built from the same corpus to show what this level is for.</p>
</section>
{''.join(cards)}"""
    page("views.html", "Views", body, subnav=True, active="views.html",
         lede="Compositions over the excerpt graph.")


def build_timeline():
    meta, body = load(BUNDLE / "views" / "timeline.md")
    rendered = markdown(re.sub(r"^# .+\n", "", body.lstrip(), count=1), depth=1, heading_base=2)
    view_page("timeline.html", meta.get("title", "Timeline"), rendered,
              "The dated genealogy of graph engineering, every row linked to the "
              "excerpt that evidences it. Rendered from the bundle's own view "
              "document.", demo=False)


def build_by_issue():
    blocks = []
    for slug in sorted(issues, key=lambda s: issues[s]["title"].lower()):
        it = issues[slug]
        positions = sorted(it.get("positions", []), key=lambda p: excs[p[1]]["title"].lower())
        rows = "".join(
            f'<li><span class="rel">{REL_LABELS.get(rel, rel)}</span> '
            f'{link_exc(s, 1)}<span class="say">{inline(excs[s]["description"], 1)}</span></li>'
            for rel, s in positions) or '<li class="none">Nothing on record yet.</li>'
        blocks.append(f"""<article class="card issue" id="i-{slug}">
  <h2>{html.escape(it['title'])}</h2>
  <p class="badges">{badge('role', 'issue')}{badge('status', it['meta'].get('status', 'open'))}
    <span class="speaker">{len(positions)} on record</span></p>
  <div class="about">{markdown(sec(it, 'Issue'), 1)}</div>
  <ul class="edges answers">{rows}</ul>
  {tags_html(it['tags'], 1)}
</article>""")
    view_page("by-issue.html", "By open question", "".join(blocks),
              f"The {len(issues)} root questions the corpus argues about. Each "
              "lists the excerpts that answer it and takes no side.")


def build_by_role():
    blocks = []
    blurbs = {
        "issue": "A question the corpus is arguing about.",
        "position": "An answer someone puts on record.",
        "argument": "A move made in support of, or against, a position.",
        "evidence": "Something observed, dated, or shipped.",
    }
    for role in ROLE_ORDER:
        members = sorted((e for e in excs.values() if e["meta"].get("role") == role),
                         key=lambda e: e["title"].lower())
        rows = "".join(
            f'<li>{badge("subtype", e["meta"].get("subtype", "—"))} {link_exc(e["slug"], 1)}'
            f'<span class="say">{inline(e["description"], 1)}</span></li>' for e in members)
        blocks.append(f"""<section class="group">
  <h2>{role.title()} <span class="count">{len(members)}</span></h2>
  <p class="group-meta">{blurbs[role]}</p>
  <ul class="edges roll">{rows}</ul>
</section>""")
    view_page("by-role.html", "By role in the argument", "".join(blocks),
              "The corpus sorted by the part each excerpt plays — issue, "
              "position, argument, evidence — rather than by where it came from.")


def build_by_tag():
    size = lambda t: sum(len(v) for v in tag_index[t].values())
    order = sorted(tag_index, key=lambda t: (-size(t), t))
    jump = '<nav class="jump wrap" aria-label="Jump to tag">' + "".join(
        f'<a href="#t-{html.escape(t)}">{html.escape(t)} '
        f'<span class="count">{size(t)}</span></a>'
        for t in order) + "</nav>"
    blocks = []
    for t in order:
        e_slugs = sorted(tag_index[t]["excerpts"], key=lambda s: excs[s]["title"].lower())
        r_slugs = sorted(tag_index[t]["references"], key=lambda s: refs[s]["title"].lower())
        i_slugs = sorted(tag_index[t]["issues"], key=lambda s: issues[s]["title"].lower())
        parts = []
        if i_slugs:
            parts.append("<h3>Questions</h3><ul class=\"edges\">" + "".join(
                f"<li>{link_issue(s, 1)}</li>" for s in i_slugs) + "</ul>")
        if e_slugs:
            parts.append("<h3>Excerpts</h3><ul class=\"edges\">" + "".join(
                f"<li>{link_exc(s, 1)}</li>" for s in e_slugs) + "</ul>")
        if r_slugs:
            parts.append("<h3>Sources</h3><ul class=\"edges\">" + "".join(
                f"<li>{link_ref(s, 1)}</li>" for s in r_slugs) + "</ul>")
        blocks.append(f"""<article class="card tag-block" id="t-{html.escape(t)}">
  <h2>{html.escape(t)} <span class="count">{size(t)}</span></h2>
  {''.join(parts)}
</article>""")
    view_page("by-tag.html", "By tag", jump + "".join(blocks),
              f"All {len(order)} tags in the corpus, most-used first, with "
              "everything carrying each one.")


def build_edges():
    grouped = {}
    for e in excs.values():
        for rel, kind, slug in e["out"]:
            grouped.setdefault(rel, []).append((e["slug"], kind, slug))
    blocks = []
    for rel in sorted(grouped, key=lambda r: -len(grouped[r])):
        rows = "".join(
            f'<li>{link_exc(a, 1)}<span class="arrow" aria-hidden="true">→</span>'
            f'{link_issue(b, 1) if kind == "issues" else link_exc(b, 1)}</li>'
            for a, kind, b in sorted(grouped[rel], key=lambda p: excs[p[0]]["title"].lower()))
        blocks.append(f"""<section class="group">
  <h2>{REL_LABELS.get(rel, rel)} <span class="count">{len(grouped[rel])}</span></h2>
  <ul class="edges pairs">{rows}</ul>
</section>""")
    total = sum(len(v) for v in grouped.values())
    view_page("edges.html", "By typed edge", "".join(blocks),
              f"All {total} typed edges in the corpus, grouped by relation. "
              "Reading down a group is one way to see what the argument rests on.")


def build_about():
    body = """<section class="hero">
  <h1>About</h1>
  <p class="lede">Mark Reveley is a musician developer living in Berkeley.</p>
</section>

<section class="about-more">
  <p>This site is three things: <a href="index.html">posts</a> when there are
  any, a <a href="reading.html">reading</a> section that keeps sources, excerpts
  and views as separate levels, and this page.</p>
  <p>It is static HTML and CSS — no JavaScript, no framework, no analytics.</p>
</section>"""
    page("about.html", "About", body, active="about.html",
         lede="Mark Reveley is a musician developer living in Berkeley.")


def main():
    build_posts()
    build_reading()
    build_sources()
    build_excerpts()
    build_views_index()
    build_timeline()
    build_by_issue()
    build_by_role()
    build_by_tag()
    build_edges()
    build_about()
    pages = sorted(p.relative_to(OUT).as_posix() for p in OUT.rglob("*.html"))
    print(f"{len(refs)} sources · {len(excs)} excerpts · {len(issues)} issues")
    print(f"wrote {len(pages)} pages: " + ", ".join(pages))


if __name__ == "__main__":
    main()
