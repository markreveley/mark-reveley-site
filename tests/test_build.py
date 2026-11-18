import contextlib
import importlib.util
import io
import re
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("site_build", ROOT / "site" / "build.py")
site_build = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(site_build)


def write_post(directory, name="example-post.md", **overrides):
    body = overrides.pop("body", "A post body. Another sentence.")
    record = {
        "type": "Post",
        "title": "Example post",
        "date_published": "2026-08-29",
        **overrides,
    }
    frontmatter = yaml.safe_dump(record, sort_keys=False)
    (directory / name).write_text(
        f"---\n{frontmatter}---\n{body}\n",
        encoding="utf-8",
    )


TAXONOMY = """agents:
  label: Agents
  children:
    agent-failures:
      label: Agent failures
      tags: [agent-failures]
    governance:
      label: Governance
      tags: [governance]
philosophy:
  label: Philosophy
  tags: [philosophy]
"""


@contextlib.contextmanager
def isolated_site():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        post_db = root / "posts"
        def_db = root / "defs"
        output = root / "site"
        post_db.mkdir()
        def_db.mkdir()
        saved = (site_build.POST_DB, site_build.DEF_DB, site_build.OUT, site_build.TAGS)
        try:
            site_build.POST_DB = post_db
            site_build.DEF_DB = def_db
            site_build.OUT = output
            site_build.TAGS = output / "tags"
            yield post_db, output
        finally:
            site_build.POST_DB, site_build.DEF_DB, site_build.OUT, site_build.TAGS = saved


def build():
    with contextlib.redirect_stdout(io.StringIO()):
        site_build.main()


def navigation(page):
    return page.split('<nav class="mainnav"', 1)[1].split("</nav>", 1)[0]


class SiteBuildTests(unittest.TestCase):
    def write_definition(self, name="program", body="A definition.", **overrides):
        meta = {
            "type": "Definition", "term": name.title(),
            "date_added": "2026-09-11", "categories": ["systems"], **overrides,
        }
        (site_build.DEF_DB / f"{name}.md").write_text(
            f"---\n{yaml.safe_dump(meta)}---\n{body}\n", encoding="utf-8"
        )

    def test_definitions_order_categories_and_navigation(self):
        with isolated_site() as (_, output):
            (site_build.DEF_DB / "taxonomy.yml").write_text(
                "computing:\n  label: Computing\n  children:\n"
                "    systems:\n      label: Systems\n      tags: [systems]\n"
                "    languages:\n      label: Languages\n      tags: [languages]\n"
            )
            self.write_definition("old", date_added="2026-09-10")
            self.write_definition("alpha", categories=["languages"])
            self.write_definition("zeta", categories=["systems", "languages"],
                                  body='Safe <script> & [reference](https://example.com).')
            build()
            feed = (output / "defs.html").read_text()
            parent = (output / "defs/categories/computing.html").read_text()
            child = (output / "defs/categories/systems.html").read_text()
            self.assertLess(feed.index('id="d-zeta"'), feed.index('id="d-alpha"'))
            self.assertLess(feed.index('id="d-alpha"'), feed.index('id="d-old"'))
            self.assertEqual(parent.count('id="d-zeta"'), 1)
            self.assertIn('id="d-old"', child)
            self.assertNotIn('id="d-alpha"', child)
            self.assertIn('href="../../defs.html#d-zeta"', child)
            self.assertIn('href="../../defs.html">All definitions', child)
            self.assertIn('href="../../defs/categories/systems.html" aria-current="page"', child)
            self.assertIn('Safe &lt;script&gt; &amp;', feed)
            self.assertIn('href="https://example.com"', feed)
            self.assertIn('<time datetime="2026-09-11">11 September 2026</time>', feed)
            for filename in ("index.html", "defs.html", "defs/categories/systems.html"):
                navigation = (output / filename).read_text().split('<nav class="mainnav"', 1)[1].split('</nav>', 1)[0]
                self.assertNotIn('defs.html', navigation)
            # Removing a category must remove the generated page on the next build.
            (site_build.DEF_DB / "taxonomy.yml").unlink()
            build()
            self.assertFalse((output / "defs/categories/computing.html").exists())

    def test_definition_validation_and_empty_feed(self):
        with isolated_site() as (_, output):
            build()
            self.assertIn("No definitions yet.", (output / "defs.html").read_text())
        cases = (
            ({"date_added": "2026-02-30"}, "date_added must"),
            ({"term": ""}, "term and definition body"),
            ({"body": ""}, "term and definition body"),
            ({"categories": []}, "categories must"),
            ({"categories": ["Bad Category"]}, "categories must"),
            ({"categories": ["systems", "systems"]}, "duplicates"),
        )
        for overrides, message in cases:
            with self.subTest(overrides=overrides), isolated_site():
                self.write_definition(**overrides)
                with self.assertRaisesRegex(ValueError, message):
                    build()
        with isolated_site():
            self.write_definition()
            (site_build.DEF_DB / "taxonomy.yml").write_text("computing: {}\n")
            with self.assertRaisesRegex(ValueError, "unmapped categories"):
                build()

    def test_definition_links_match_terms_aliases_and_preserve_existing_links(self):
        with isolated_site() as (_, output):
            self.write_definition("process", aliases=["processes"])
            self.write_definition("process-execution-state", term="Process execution state",
                                  aliases=["execution state"])
            self.write_definition("program", body=(
                "Process execution state; EXECUTION STATE; process; processes; process's; "
                "processor; preprocessing. <process> & program.\n\n"
                "[process reference](https://example.com/process)"
            ))
            build()
            for path, prefix in (("defs.html", ""), ("defs/categories/systems.html", "../../")):
                page = (output / path).read_text()
                self.assertIn(f'<a href="{prefix}defs.html#d-process-execution-state">Process execution state</a>', page)
                self.assertIn(f'<a href="{prefix}defs.html#d-process-execution-state">EXECUTION STATE</a>', page)
                self.assertIn(f'<a href="{prefix}defs.html#d-process">processes</a>', page)
                self.assertIn(f'<a href="{prefix}defs.html#d-process">process</a>&#x27;s', page)
                self.assertIn('processor; preprocessing.', page)
                self.assertIn(f'&lt;<a href="{prefix}defs.html#d-process">process</a>&gt; &amp;', page)
                self.assertIn('<a href="https://example.com/process" rel="noreferrer">process reference</a>', page)
                self.assertIn(f'<a href="{prefix}defs.html#d-program">program</a>', page)

    def test_definition_links_reject_ambiguous_targets(self):
        with isolated_site():
            self.write_definition("process")
            self.write_definition("other", aliases=["PROCESS"])
            with self.assertRaisesRegex(ValueError, "ambiguous definition term or alias"):
                build()

    def test_multiple_definitions_keep_sources_with_their_text(self):
        with isolated_site() as (_, output):
            self.write_definition("program")
            self.write_definition("agent", body="Notes about a program.", definitions=[
                {"text": "First: a program.", "sources": [
                    {"title": "First <source>", "url": "https://example.com/one?a=1&b=2#part",
                     "author": "Author & Team", "date": "2026-02-18"},
                    {"title": "Supporting source", "url": "https://example.com/two"},
                ]},
                {"text": "Second: another program.", "sources": [
                    {"title": "Other source", "url": "https://example.org/three", "date": "2025"},
                ]},
            ])
            build()
            for filename, prefix in (("defs.html", ""), ("defs/categories/systems.html", "../../")):
                page = (output / filename).read_text()
                card = page.split('id="d-agent">', 1)[1].split('</article>', 1)[0]
                self.assertEqual(card.count('class="definition-entry"'), 2)
                self.assertLess(card.index('First &lt;source&gt;'), card.index('Second:'))
                self.assertLess(card.index('Supporting source'), card.index('Second:'))
                self.assertGreater(card.index('Other source'), card.index('Second:'))
                self.assertIn('https://example.com/one?a=1&amp;b=2#part', card)
                self.assertIn('Author &amp; Team', card)
                self.assertIn('<time datetime="2026-02-18">18 February 2026</time>', card)
                self.assertEqual(card.count(f'href="{prefix}defs.html#d-program"'), 3)
                self.assertIn('class="definition-notes"', card)

    def test_structured_definition_validation(self):
        cases = [
            ([], "definitions must"),
            (["text"], "definition must be a mapping"),
            ([{"text": ""}], "definition text must"),
            ([{"text": "Valid", "sources": {}}], "sources must be a list"),
            ([{"text": "Valid", "sources": ["source"]}], "source must be a mapping"),
            ([{"text": "Valid", "sources": [{"url": "https://example.com"}]}], "url and title"),
            ([{"text": "Valid", "sources": [{"title": "Bad", "url": "javascript:alert(1)"}]}], "url and title"),
            ([{"text": "Valid", "sources": [{"title": "Bad", "url": "https://example.com", "date": "2026-02-30"}]}], "source date must"),
        ]
        for definitions, message in cases:
            with self.subTest(definitions=definitions), isolated_site():
                self.write_definition(body="", definitions=definitions)
                with self.assertRaisesRegex(ValueError, message):
                    build()
        with isolated_site() as (_, output):
            self.write_definition(body="", definitions=[{"text": "A definition without a source."}])
            build()
            self.assertIn("A definition without a source.", (output / "defs.html").read_text())

    def test_about_links_to_social_profiles_with_icons(self):
        with isolated_site() as (_, output):
            build()

            about = (output / "about.html").read_text(encoding="utf-8")
            profiles = {
                "Substack": "https://substack.com/@markreveley1",
                "GitHub": "https://github.com/markreveley",
                "X": "https://x.com/markreveley",
                "LinkedIn": "https://www.linkedin.com/in/mark-r-9aab133/",
            }
            for service, profile in profiles.items():
                with self.subTest(service=service):
                    self.assertIn(f'href="{profile}"', about)
                    self.assertIn(f'aria-label="{service}"', about)
            self.assertEqual(about.count('rel="me noreferrer"'), len(profiles))
            self.assertIn('class="about-heading"', about)
            self.assertIn('class="about-social-links"', about)
            self.assertEqual(about.count('class="social-icon"'), len(profiles))
            self.assertNotIn("Elsewhere", about)
    def test_builds_posts_from_markdown_records(self):
        with isolated_site() as (posts, output):
            write_post(
                posts,
                excerpt="A custom post-card excerpt.",
                body=(
                    "A post body with an [example](https://example.com/path?a=1&b=2). "
                    "Another sentence."
                ),
            )
            build()

            landing = (output / "index.html").read_text(encoding="utf-8")
            post = (output / "posts" / "example-post.html").read_text(encoding="utf-8")
            self.assertIn('<a href="posts/example-post.html">Example post</a>', landing)
            self.assertIn("A custom post-card excerpt.", landing)
            self.assertIn(
                '<a href="https://example.com/path?a=1&amp;b=2" rel="noreferrer">example</a>',
                post,
            )
            self.assertNotIn("[example]", post)

    def test_post_markdown_formats_transcript_and_keeps_html_inert(self):
        with isolated_site() as (posts, output):
            write_post(
                posts,
                body=(
                    "## Transcript\n\n### Assistant\n\n"
                    "**History check** with *emphasis* and `git log --all`.\n\n"
                    "- First finding\n- Second finding\n\n"
                    "> Exact quoted wording.\n\n"
                    "```text\n<routes ref=\"/policy.md\">\n```\n\n"
                    "<script>alert('test')</script>\n\n"
                    "[unsafe](javascript:alert(1))"
                ),
            )
            build()
            post = (output / "posts" / "example-post.html").read_text()
            for fragment in (
                "<h2>Transcript</h2>", "<h3>Assistant</h3>",
                "<strong>History check</strong>", "<em>emphasis</em>",
                "<code>git log --all</code>", "<ul>\n<li>First finding</li>",
                "<blockquote>\n<p>Exact quoted wording.</p>",
                '<pre><code class="language-text">&lt;routes',
                "&lt;script&gt;",
            ):
                self.assertIn(fragment, post)
            self.assertNotIn("<script>", post)
            self.assertNotIn('href="javascript:', post)

    def test_navigation_has_only_posts_and_about(self):
        with isolated_site() as (posts, output):
            write_post(posts)
            build()
            for filename in ("index.html", "index-expanded.html", "about.html",
                             "posts/example-post.html", "defs.html"):
                links = re.findall(r'>([^<]+)</a>', navigation((output / filename).read_text()))
                self.assertEqual(links, ["Posts", "About"], filename)

    def test_retired_quote_and_bookmark_pages_are_removed(self):
        with isolated_site() as (_, output):
            for name in ("quotes.html", "bookmarks.html", "tags.html", "random-quotes.js"):
                (output / name).parent.mkdir(parents=True, exist_ok=True)
                (output / name).write_text("old")
            for folder in ("topics", "writers", "bookmarks/topics"):
                (output / folder).mkdir(parents=True, exist_ok=True)
                (output / folder / "x.html").write_text("old")
            build()
            for name in ("quotes.html", "bookmarks.html", "tags.html", "random-quotes.js",
                         "topics", "writers", "bookmarks"):
                self.assertFalse((output / name).exists(), name)

    def test_post_tags_build_a_rail_and_tag_pages(self):
        with isolated_site() as (posts, output):
            (posts / "taxonomy.yml").write_text(TAXONOMY)
            write_post(posts, "old.md", title="Old", date_published="2026-09-01",
                       tags=["philosophy"])
            write_post(posts, "new.md", title="New", date_published="2026-10-01",
                       tags=["governance", "agent-failures"])
            write_post(posts, "untagged.md", title="Untagged", date_published="2026-08-01")
            build()
            landing = (output / "index.html").read_text()
            expanded = (output / "index-expanded.html").read_text()
            parent = (output / "tags/agents.html").read_text()
            child = (output / "tags/governance.html").read_text()
            post = (output / "posts/new.html").read_text()

            # Cards carry their tags, broader categories first.
            card = landing.split('id="p-new"', 1)[1].split("</article>", 1)[0]
            self.assertLess(card.index('href="tags/agents.html">Agents'),
                            card.index('href="tags/governance.html">Governance'))
            self.assertIn('href="tags/agent-failures.html">Agent failures', card)
            # The plain feed has no rail; the eye's page has it on the left, roots only.
            self.assertNotIn("filter-rail", landing)
            self.assertIn('class="filter-rail filter-rail-tags"', expanded)
            rail = expanded.split('<h2>Tags</h2>', 1)[1].split("</aside>", 1)[0]
            self.assertIn('href="tags/agents.html">Agents', rail)
            self.assertIn('href="tags/philosophy.html">Philosophy', rail)
            self.assertNotIn("governance", rail)
            # Tag pages include narrower tags' posts once and drill down.
            self.assertEqual(parent.count('id="p-new"'), 1)
            self.assertNotIn('id="p-old"', parent)
            self.assertIn('href="../tags/governance.html">Governance', parent.split("</aside>", 1)[0])
            self.assertIn('href="../index-expanded.html" aria-label="Exit Agents filter"', child)
            self.assertIn("1 post filed under <em>Agents / Governance</em>", child)
            # A post page lists its tags.
            self.assertIn('href="../tags/governance.html">Governance', post)
            # Removing a tag removes its page on the next build.
            (posts / "taxonomy.yml").write_text(TAXONOMY.replace(
                "philosophy:\n  label: Philosophy\n  tags: [philosophy]\n", ""))
            (posts / "old.md").unlink()
            build()
            self.assertFalse((output / "tags/philosophy.html").exists())

    def test_post_tags_are_validated(self):
        cases = (
            ("Bad Tag", "lowercase and hyphenated"),
            (["dup", "dup"], "duplicates"),
            ("not-a-list", "list of strings"),
            (["unmapped"], "unmapped tag"),
        )
        for tags, message in cases:
            with self.subTest(tags=tags), isolated_site() as (posts, _):
                (posts / "taxonomy.yml").write_text("dup: {tags: [dup]}\n")
                write_post(posts, tags=tags if isinstance(tags, list) or tags == "not-a-list" else [tags])
                with self.assertRaisesRegex(ValueError, message):
                    build()

    def test_dice_and_eye_are_on_posts_pages(self):
        with isolated_site() as (posts, output):
            (posts / "taxonomy.yml").write_text(TAXONOMY)
            write_post(posts, "one.md", title="One", tags=["governance"])
            write_post(posts, "two.md", title="Two")
            build()
            expectations = {
                "index.html": ('href="index-expanded.html"', 'data-root=""', False),
                "index-expanded.html": ('href="index.html"', 'data-root=""', True),
                "tags/governance.html": ('href="../index.html"', 'data-root="../"', True),
                "posts/one.html": ('href="../index-expanded.html"', 'data-root="../"', False),
            }
            for filename, (eye_href, root, on) in expectations.items():
                with self.subTest(page=filename):
                    page = (output / filename).read_text()
                    self.assertIn("data-random-post", page)
                    self.assertIn('aria-label="Load a random post"', page)
                    self.assertIn(root, page)
                    eye = page.split('class="filter-toggle', 1)[1].split(">", 1)[0]
                    self.assertIn(eye_href, eye)
                    self.assertEqual(" is-on" in eye[:7], on)
                    self.assertIn("random-posts.js", page)
            self.assertIn('data-post-slug="one"', (output / "posts/one.html").read_text())
            script = (output / "random-posts.js").read_text()
            self.assertIn('["two", "one"]', script)
            self.assertIn("posts/${encodeURIComponent(chosen)}.html", script)
            self.assertNotIn("random-toggle", (output / "about.html").read_text())


if __name__ == "__main__":
    unittest.main()
