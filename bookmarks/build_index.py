"""Rebuild the topic index in bookmarks/README.md from the node files.

Reads topics/*.md and items/*.md (artifact-dag frontmatter) and replaces the
text between the INDEX markers in README.md. Run from anywhere:

    python3 bookmarks/build_index.py
"""

import pathlib
import re

HERE = pathlib.Path(__file__).parent
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"


def scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] == '"':
        return re.sub(r'\\(["\\])', r"\1", v[1:-1])
    return v


def front(path):
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    out = {}
    for line in m.group(1).splitlines():
        key, _, val = line.partition(":")
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            out[key] = [x.strip() for x in val[1:-1].split(",") if x.strip()]
        else:
            out[key] = scalar(val)
    return out


def main():
    topics = {}
    for p in sorted((HERE / "topics").glob("*.md")):
        f = front(p)
        topics[f["id"]] = {"title": f["title"], "parents": f.get("refines", []), "items": []}
    loose = []
    for p in sorted((HERE / "items").glob("*.md")):
        f = front(p)
        entry = (f["title"], f"items/{p.name}", f.get("status", ""))
        tops = [t for t in f.get("topics", []) if t in topics]
        for t in tops:
            topics[t]["items"].append(entry)
        if not tops:
            loose.append(entry)

    children = {t: [] for t in topics}
    roots = []
    for t, v in topics.items():
        parents = [x for x in v["parents"] if x in topics]
        # A topic with several parents is listed once, under the first.
        if parents:
            children[parents[0]].append(t)
        if not parents:
            roots.append(t)

    def line(entry):
        title, href, status = entry
        return f"- [{title}]({href})" + (" (stub)" if status == "stub" else "")

    out = []

    def section(t, depth):
        v = topics[t]
        out.append(f"{'#' * min(depth, 6)} {v['title']}\n")
        if v["items"]:
            out.extend(line(e) for e in sorted(v["items"], key=lambda e: e[0].lower()))
            out.append("")
        for c in sorted(children[t], key=lambda c: topics[c]["title"].lower()):
            section(c, depth + 1)

    for t in sorted(roots, key=lambda t: topics[t]["title"].lower()):
        section(t, 3)
    if loose:
        out.append("### Not yet filed under a topic\n")
        out.extend(line(e) for e in sorted(loose, key=lambda e: e[0].lower()))
        out.append("")

    readme = HERE / "README.md"
    text = readme.read_text()
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    body = "\n".join(out).rstrip() + "\n"
    readme.write_text(f"{head}{START}\n\n{body}\n{END}{tail}")


if __name__ == "__main__":
    main()
