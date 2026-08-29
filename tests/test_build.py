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


@contextlib.contextmanager
def isolated_site():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        quote_db = root / "quotes"
        output = root / "site"
        quote_db.mkdir()
        old_db, old_out, old_topics = site_build.QUOTE_DB, site_build.OUT, site_build.TOPICS
        try:
            site_build.QUOTE_DB = quote_db
            site_build.OUT = output
            site_build.TOPICS = output / "topics"
            yield quote_db, output
        finally:
            site_build.QUOTE_DB, site_build.OUT, site_build.TOPICS = old_db, old_out, old_topics


def build():
    with contextlib.redirect_stdout(io.StringIO()):
        site_build.main()


class SiteBuildTests(unittest.TestCase):
    def test_builds_enriched_quotes_and_allows_a_repeated_resource(self):
        with isolated_site() as (quote_db, output):
            write_record(
                quote_db,
                "first.md",
                source_title="An example article",
                source_author="Example Author",
                source_date="2026-08-20",
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
            all_quotes = (output / "topics" / "all.html").read_text(encoding="utf-8")
            self.assertIn("2 quotes from 1 source", landing)
            self.assertIn("Design &lt;systems&gt; carefully.", all_quotes)
            self.assertIn("Example Speaker", all_quotes)
            self.assertIn("An example article", all_quotes)
            self.assertIn("Example Author", all_quotes)
            self.assertIn("source unavailable", all_quotes)
            self.assertTrue((output / "topics" / "software-engineering.html").exists())

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
