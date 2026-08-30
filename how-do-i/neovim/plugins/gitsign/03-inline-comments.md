# Draft and submit inline review comments

Gitsigns does not implement GitHub reviews. It knows Git hunks, not PR numbers, pending reviews, or comment threads. The clean bridge is a small review document that you edit beside the source file in Neovim and submit with `gh api`.

Do not type review prose into the checked-out source file. That creates working-tree changes, changes the Gitsigns diff you are trying to inspect, and risks committing the review text. Put the document under `.git/`; Git never includes files stored there in commits.

## 1. Create the review document

From Neovim:

```vim
:vsplit .git/pr-review.json
```

Start with:

```json
{
  "comments": [
    {
      "path": "lib/example.ex",
      "line": 42,
      "side": "RIGHT",
      "body": "Could this name describe the failure case more precisely?"
    }
  ]
}
```

Keep the source file in one split and this document in the other. Add one object per inline comment.

## 2. Capture a location from the real file

Put the cursor on the line you want to discuss, then run:

```vim
:echo expand('%:.')
:echo line('.')
```

The first result is the repository-relative `path`; the second is the checked-out file's `line`. Record both in the JSON document with `"side": "RIGHT"`.

`RIGHT` means the PR's new version: added lines and unchanged context visible in the PR diff. GitHub only accepts a line if it is actually part of the displayed diff or its context. A random unchanged line elsewhere in the file will be rejected even though it has a valid file line number.

### Multi-line comments

For lines 38 through 42 on the new side:

```json
{
  "path": "lib/example.ex",
  "start_line": 38,
  "start_side": "RIGHT",
  "line": 42,
  "side": "RIGHT",
  "body": "Can this block be replaced with the existing parser helper?"
}
```

### Deleted lines

A deleted line exists only on the old, `LEFT` side. Its number is not the current buffer line number, so `line('.')` cannot identify it. Use `:Gitsigns preview_hunk` to understand the deletion, then use GitHub's Files changed view or a purpose-built PR plugin to place that comment. Do not guess the old line number.

## 3. Validate before sending

Save the document and check its syntax from a terminal:

```sh
jq empty .git/pr-review.json
git status --short
```

The second command should not show the review document and should show no accidental edits unless you intentionally changed the PR branch.

Also confirm that the PR has not moved since checkout:

```sh
git rev-parse HEAD
gh pr view --json headRefOid --jq .headRefOid
```

The two SHAs should match. If they do not, update the checked-out PR, recompute the review base, and recheck every recorded line before posting.

## 4. Create a pending GitHub review

This sends the inline comments to GitHub but keeps the review pending and visible only to you until submission:

```sh
pr_number=$(gh pr view --json number --jq .number)
head_sha=$(gh pr view --json headRefOid --jq .headRefOid)

review_id=$(
  jq --arg commit_id "$head_sha" '. + {commit_id: $commit_id}' .git/pr-review.json |
    gh api --method POST "repos/{owner}/{repo}/pulls/$pr_number/reviews" \
      --input - --jq .id
)

printf '%s\n' "$review_id"
```

The API binds the review to the current PR head SHA. Creating the review is an external write and can trigger notifications according to GitHub's API documentation, so run it only after validating the file.

Inspect the pending comments in the PR's Files changed view before submitting. GitHub lets you edit or abandon pending comments there.

## 5. Submit the pending review

Choose exactly one event:

- `COMMENT` for feedback without an approval decision;
- `APPROVE` to approve;
- `REQUEST_CHANGES` to request changes.

Submit it with an optional summary:

```sh
gh api --method POST \
  "repos/{owner}/{repo}/pulls/$pr_number/reviews/$review_id/events" \
  -f event=COMMENT \
  -f body='Inline notes are attached.'
```

This is the irreversible publishing step: collaborators can now see the review and receive normal GitHub notifications.

If you only need a general review body and no inline comments, use the simpler CLI command:

```sh
gh pr review --comment --body-file review-summary.md
```

That command does not turn line references in a Markdown file into inline comments; inline placement requires the review API fields used above.

[Next: command cheat sheet and troubleshooting](04-reference.md)

