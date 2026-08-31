---
name: quote
description: Add a selected quotation to this site's quote collection from exact quote text and its URL. Use when the user asks to save, collect, intake, or add a quote; research its source metadata, classify it, author the OKF-style record, and rebuild the site. Do not use for general quotation lookup or unrelated research.
---

# Quote

Treat the skill invocation as the only intake interface. The intake order is:

1. Exact quote text
2. Resource URL

Accept legacy URL-first input when its meaning is already clear; ask only for
whichever of the two values is missing. Author the Markdown record directly—do
not call or recreate an intake CLI.

Before writing, read `quotes/README.md` for the current schema and inspect the
existing records in `quotes/` for vocabulary and duplicates.

## Intake workflow

1. Preserve the supplied quote exactly, apart from removing accidental outer
   whitespace. Never silently correct spelling, punctuation, typography, or
   wording.
2. Check for an existing record with the same complete `resource` and `quote`.
   If found, report its path and stop. The same URL with a different quote is
   valid.
3. Open the resource and collect only metadata supported by the page or another
   authoritative representation of it: source title, author, publication date,
   and the quoted speaker when distinct from the author.
4. Compare the supplied quote with accessible source text. Use `verified` only
   for a match after harmless whitespace normalization. Use `not-found` when
   the source is accessible but does not contain the quote,
   `source-unavailable` when it cannot be inspected, and `unverified` when no
   check was attempted. Do not repair a mismatch or invent missing metadata.
5. Assign one to five specific subject tags. Prefer suitable tags already in
   the collection, but add a new tag when it describes the quote materially
   better. Tags must be lowercase, hyphenated, distinct, and useful for finding
   related quotes; avoid catchalls such as `ideas`, `misc`, or `quotes`.
6. Use the current local date for `date_added` and, when a source check was
   attempted, `verification_date`. Preserve only the known precision of
   `source_date`: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`.
7. Write one file under `quotes/`, named
   `YYYY-MM-DD-<concise-quote-slug>.md`. If that name exists, make the slug more
   specific rather than overwriting it. Use valid YAML frontmatter and no
   duplicated quote body.
8. Run `python3 site/build.py` and
   `python3 -m unittest discover -s tests -v`. Fix record errors before
   finishing; do not weaken validation to admit a bad record.

Report the record path, assigned tags, verification result, and any source
metadata that remains unknown.
