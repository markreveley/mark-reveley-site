# Review a pull request in Neovim with Gitsigns

If you have gitsigns.nvim (most nvim setups do): open files normally, run `:Gitsigns change_base origin/main true` once — every PR change now shows as gutter signs in the actual file, `]c` / `[c` jump hunk to hunk, `:Gitsigns preview_hunk` shows the old text. This is literally the hunk workflow, inside your editor, editing the real file.

That is the core idea. There are two details worth making explicit:

1. Gitsigns reads and navigates the diff, but it does not send review comments to GitHub.
2. `]c` and `[c` are suggested mappings, not Gitsigns defaults. Add them once in your config.

The resulting workflow is:

1. Check out the PR locally.
2. Set the Gitsigns base to the PR's merge base.
3. Read the real files, moving through hunks in the gutter.
4. Draft line-anchored comments in a separate review document under `.git/` so the PR files remain untouched.
5. Send the document as one pending GitHub review, inspect it, and submit it.

## Tutorial

- [Install and configure the review keymaps](01-setup.md)
- [Read a PR hunk by hunk](02-read-a-pr.md)
- [Draft and submit inline review comments](03-inline-comments.md)
- [Command cheat sheet and troubleshooting](04-reference.md)

If you only want to read a PR, stop after the second chapter. If you want comments attached to exact GitHub diff lines, continue through the third.

## The mental model

Gitsigns normally compares a file in your working tree with the Git index. `change_base` tells it to compare with a revision instead. Setting the change globally makes that revision apply to open buffers and files you open later.

GitHub displays a three-dot PR diff: the merge base of the base and head branches versus the PR head. Therefore `origin/main` is a useful shortcut, but the merge-base commit is the exact comparison when `main` has moved since the PR branch diverged.

Gitsigns and GitHub then have separate jobs:

| Tool | Job |
| --- | --- |
| Gitsigns | Show, preview, and navigate the PR hunks in normal file buffers |
| A `.git/pr-review.json` document | Hold comments without modifying the checked-out files |
| GitHub CLI and API | Attach those comments to GitHub diff lines and submit the review |

## Sources

- [Gitsigns README and suggested mappings](https://github.com/lewis6991/gitsigns.nvim)
- [Gitsigns command reference](https://github.com/lewis6991/gitsigns.nvim/blob/main/doc/gitsigns.txt)
- [GitHub's explanation of three-dot PR diffs](https://docs.github.com/en/pull-requests/reference/branches#three-dot-and-two-dot-git-diff-comparisons)
- [GitHub CLI pull-request commands](https://cli.github.com/manual/gh_pr)
- [GitHub review API](https://docs.github.com/en/rest/pulls/reviews)

