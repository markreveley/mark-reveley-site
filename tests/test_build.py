import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("site_build", ROOT / "site" / "build.py")
site_build = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(site_build)


def write_record(directory, name, **overrides):
    record = {
        "type": "Quote",
        "resource": "https://example.com/article",
        "quote": "A software quote.",
        "date_added": "2026-08-28",
        "tags": ["software-engineering"],
        **overrides,
    }
    frontmatter = yaml.safe_dump(record, sort_keys=False)
    (directory / name).write_text(f"---\n{frontmatter}---\n", encoding="utf-8")


def write_post(directory, name="example-post.md", **overrides):
    record = {
        "type": "Post",
        "title": "Example post",
        "date_published": "2026-08-29",
        **overrides,
    }
    frontmatter = yaml.safe_dump(record, sort_keys=False)
    (directory / name).write_text(
        f"---\n{frontmatter}---\nA post body. Another sentence.\n",
        encoding="utf-8",
    )


@contextlib.contextmanager
def isolated_site():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        quote_db = root / "quotes"
        post_db = root / "posts"
        output = root / "site"
        quote_db.mkdir()
        post_db.mkdir()
        old_db, old_posts, old_out, old_topics, old_writers = (
            site_build.QUOTE_DB,
            site_build.POST_DB,
            site_build.OUT,
            site_build.TOPICS,
            site_build.WRITERS,
        )
        try:
            site_build.QUOTE_DB = quote_db
            site_build.POST_DB = post_db
            site_build.OUT = output
            site_build.TOPICS = output / "topics"
            site_build.WRITERS = output / "writers"
            yield quote_db, output
        finally:
            site_build.QUOTE_DB, site_build.POST_DB, site_build.OUT, site_build.TOPICS, site_build.WRITERS = (
                old_db,
                old_posts,
                old_out,
                old_topics,
                old_writers,
            )


def build():
    with contextlib.redirect_stdout(io.StringIO()):
        site_build.main()


class SiteBuildTests(unittest.TestCase):
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
        with isolated_site() as (quote_db, output):
            write_post(
                quote_db.parent / "posts",
                excerpt="A custom post-card excerpt.",
            )
            build()

            landing = (output / "index.html").read_text(encoding="utf-8")
            post = (output / "posts" / "example-post.html").read_text(encoding="utf-8")
            self.assertIn('<a href="posts/example-post.html">Example post</a>', landing)
            self.assertIn("A custom post-card excerpt.", landing)
            self.assertIn("A post body. Another sentence.", post)

    def test_builds_enriched_quotes_and_allows_a_repeated_resource(self):
        with isolated_site() as (quote_db, output):
            write_record(
                quote_db,
                "first.md",
                source_title="An example article",
                source_author="Example Author",
                source_date="2026-08-20",
                hacker_news_url="https://news.ycombinator.com/item?id=12345678",
                verification_status="verified",
                verification_date="2026-08-28",
            )
            write_record(
                quote_db,
                "second.md",
                quote="Design <systems> carefully.",
                tags=["design", "systems"],
                speaker="Example Speaker",
                verification_status="source-unavailable",
                verification_date="2026-08-28",
            )
            build()

            landing = (output / "quotes.html").read_text(encoding="utf-8")
            tags_page = (output / "tags.html").read_text(encoding="utf-8")
            writers_page = (output / "writers.html").read_text(encoding="utf-8")
            writer_page = (output / "writers" / "example-author.html").read_text(encoding="utf-8")
            expanded = (output / "quotes-expanded.html").read_text(encoding="utf-8")
            topic_page = (output / "topics" / "software-engineering.html").read_text(encoding="utf-8")
            all_quotes = (output / "topics" / "all.html").read_text(encoding="utf-8")
            self.assertIn(
                "A collection of decent-probability human authored quotes from selected reading, "
                "added by hand, sorted by date added",
                landing,
            )
            self.assertNotIn('<a href="tags.html">Tags</a>', landing)
            self.assertNotIn('<a href="writers.html">Writer</a>', landing)
            self.assertIn('class="quote-feed"', landing)
            self.assertIn('class="filter-toggle"', landing)
            self.assertIn('href="quotes-expanded.html"', landing)
            self.assertNotIn('class="filter-rail ', landing)
            self.assertIn('class="filter-toggle is-on"', expanded)
            self.assertIn('href="quotes.html"', expanded)
            self.assertIn('class="filter-rail filter-rail-tags"', expanded)
            self.assertIn('class="filter-rail filter-rail-sources"', expanded)
            self.assertNotIn('>all</a>', expanded)
            self.assertLess(
                landing.index("Design &lt;systems&gt; carefully."),
                landing.index("A software quote."),
            )
            self.assertNotIn('<a href="quotes.html">Quotes</a>', tags_page)
            self.assertIn('<ul class="topics">', tags_page)
            self.assertIn("software-engineering", tags_page)
            self.assertNotIn('<article class="card quote"', tags_page)
            self.assertNotIn("A software quote.", tags_page)
            self.assertIn('<a href="writers/example-author.html">Example Author</a>', landing)
            self.assertIn('<a href="writers/example-author.html">Example Author</a>', writers_page)
            self.assertIn("<h1>Example Author</h1>", writer_page)
            self.assertIn("A software quote.", writer_page)
            self.assertNotIn('<a href="../quotes.html">Quotes</a>', writer_page)
            self.assertIn('class="filter-toggle is-on"', writer_page)
            self.assertIn('aria-current="page">Example Author</a>', writer_page)
            self.assertIn(
                'href="../quotes-expanded.html" '
                'aria-label="Exit software-engineering filter">software-engineering</a>',
                topic_page,
            )
            self.assertIn("Design &lt;systems&gt; carefully.", all_quotes)
            self.assertNotIn('>all</a>', all_quotes)
            self.assertIn("Example Speaker", all_quotes)
            self.assertIn("An example article", all_quotes)
            self.assertIn("Example Author", all_quotes)
            self.assertIn(
                '<a href="https://example.com/article" rel="noreferrer">An example article</a>',
                all_quotes,
            )
            source_link = '<a href="https://example.com/article" rel="noreferrer">An example article</a>'
            hn_link = '<a href="https://news.ycombinator.com/item?id=12345678" rel="noreferrer">hn</a>'
            author_link = '<a href="../writers/example-author.html">Example Author</a>'
            self.assertIn(f"{source_link} · {hn_link} · {author_link}", all_quotes)
            self.assertNotIn(">https://example.com/article</a>", all_quotes)
            self.assertNotIn("source unavailable", all_quotes)
            self.assertNotIn('class="record-meta"', all_quotes)
            self.assertNotIn('<a class="self"', all_quotes)
            self.assertTrue((output / "topics" / "software-engineering.html").exists())

    def test_builds_a_drill_down_topic_taxonomy(self):
        with isolated_site() as (quote_db, output):
            write_record(
                quote_db,
                "architecture.md",
                quote="Agent architecture matters.",
                tags=["agent-architecture"],
            )
            write_record(
                quote_db,
                "instructions.md",
                resource="https://example.com/instructions",
                quote="Agent instructions matter.",
                tags=["agent-instructions"],
            )
            (quote_db / "taxonomy.yml").write_text(
                """agent:
  label: agent
  children:
    agent-architecture:
      label: architecture
      tags: [agent-architecture]
    agent-instructions:
      label: instruction
      tags: [agent-instructions]
software:
  label: software
""",
                encoding="utf-8",
            )
            build()

            landing = (output / "quotes.html").read_text(encoding="utf-8")
            expanded = (output / "quotes-expanded.html").read_text(encoding="utf-8")
            agent_page = (output / "topics" / "agent.html").read_text(encoding="utf-8")
            architecture_page = (
                output / "topics" / "agent-architecture.html"
            ).read_text(encoding="utf-8")

            self.assertIn(
                '<a href="topics/agent.html">agent</a></li>'
                '<li><a href="topics/agent-architecture.html">architecture</a>',
                landing,
            )
            expanded_tags = expanded.split('class="filter-rail filter-rail-tags"', 1)[1].split(
                "</aside>", 1
            )[0]
            self.assertIn('href="topics/agent.html">agent</a>', expanded_tags)
            self.assertIn('href="topics/software.html">software</a>', expanded_tags)
            self.assertNotIn('>architecture</a>', expanded_tags)

            agent_tags = agent_page.split('class="filter-rail filter-rail-tags"', 1)[1].split(
                "</aside>", 1
            )[0]
            self.assertIn(
                'href="../quotes-expanded.html" aria-label="Exit agent filter">agent</a>',
                agent_tags,
            )
            self.assertEqual(agent_tags.count('class="filter-divider"'), 1)
            self.assertIn('>architecture</a>', agent_tags)
            self.assertIn('>instruction</a>', agent_tags)
            self.assertNotIn('>software</a>', agent_tags)

            architecture_tags = architecture_page.split(
                'class="filter-rail filter-rail-tags"', 1
            )[1].split("</aside>", 1)[0]
            self.assertIn(
                'href="../topics/agent.html" aria-label="Exit architecture filter">architecture</a>',
                architecture_tags,
            )
            self.assertIn(
                'href="../quotes-expanded.html" aria-label="Exit agent filter">agent</a>',
                architecture_tags,
            )
            self.assertEqual(architecture_tags.count('class="filter-divider"'), 1)
            self.assertNotIn('>instruction</a>', architecture_tags)

    def test_rejects_an_exact_url_and_quote_duplicate(self):
        with isolated_site() as (quote_db, _):
            write_record(quote_db, "first.md")
            write_record(quote_db, "duplicate.md", tags=["another-tag"])
            with self.assertRaisesRegex(ValueError, "duplicates the URL and quote"):
                build()

    def test_rejects_invalid_required_fields(self):
        cases = (
            ({"resource": "example.com/article"}, "resource must be an absolute"),
            ({"date_added": "2026-02-30"}, "date_added must be a valid"),
            ({"tags": []}, "tags must be a non-empty"),
            ({"tags": ["Software Engineering"]}, "lowercase and hyphenated"),
            ({"hacker_news_url": "news.ycombinator.com/item?id=123"}, "hacker_news_url must be an absolute"),
        )
        for overrides, message in cases:
            with self.subTest(overrides=overrides), isolated_site() as (quote_db, _):
                write_record(quote_db, "invalid.md", **overrides)
                with self.assertRaisesRegex(ValueError, message):
                    build()

    def test_requires_a_date_for_attempted_verification(self):
        with isolated_site() as (quote_db, _):
            write_record(quote_db, "missing-date.md", verification_status="verified")
            with self.assertRaisesRegex(ValueError, "verification_date is required"):
                build()


if __name__ == "__main__":
    unittest.main()
