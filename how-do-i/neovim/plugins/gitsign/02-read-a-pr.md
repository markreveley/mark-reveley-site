# Read a PR hunk by hunk

The aim is to check out the PR head while making Gitsigns display the same conceptual diff as GitHub's **Files changed** view.

## 1. Check out the PR

Start with a clean working tree because checkout changes branches:

```sh
git status --short
gh auth status
gh pr checkout 123
```

Replace `123` with the PR number or URL. Confirm that the current branch belongs to the expected PR:

```sh
gh pr view --json number,title,baseRefName,headRefName,url
```

## 2. Fetch the base branch and find the merge base

The portable shell sequence is:

```sh
base_branch=$(gh pr view --json baseRefName --jq .baseRefName)
git fetch origin "$base_branch"
git merge-base HEAD "origin/$base_branch"
```

Copy the SHA printed by `git merge-base`, then open Neovim at the repository root:

```sh
nvim .
```

Set that SHA as the global Gitsigns base:

```vim
:Gitsigns change_base THE_MERGE_BASE_SHA true
```

For example:

```vim
:Gitsigns change_base a1b2c3d4 true
```

The final `true` matters: it applies the base to all attached buffers and to files opened later.

### The fast form

For a PR into `main`, this is often close enough:

```vim
:Gitsigns change_base origin/main true
```

Use the merge-base form when accuracy matters. GitHub's PR view uses a three-dot comparison, while comparing directly with `origin/main` is effectively a two-endpoint comparison. If the base branch advanced after the PR diverged, the direct form can show unrelated base-branch changes.

## 3. Open the complete hunk list

Run:

```vim
:Gitsigns setqflist all
```

Gitsigns populates and opens Neovim's quickfix list with hunks from all modified files in the repository. In the quickfix window:

- press `<CR>` to open the selected hunk;
- use `:cnext` and `:cprevious` to move between entries;
- use `:cclose` when you want the file to fill the screen again.

With the setup from chapter one, `<leader>hq` opens the same list.

## 4. Use the review loop

Once a file is open:

1. Read enough surrounding code to understand the file, not just the patch.
2. Press `]c` to jump to the next changed hunk.
3. Run `:Gitsigns preview_hunk` or press `<leader>hp` to see removed lines and the old text.
4. Press `q` to leave the preview.
5. Follow definitions and references using your normal LSP motions.
6. Return and continue with `]c`; use `[c` when you need to backtrack.

Useful alternate views:

```vim
:Gitsigns preview_hunk_inline
:Gitsigns diffthis
:Gitsigns toggle_word_diff
```

`preview_hunk_inline` inserts the deleted side as virtual lines inside the current buffer. `diffthis` opens a normal Neovim diff against the configured review base. Word diff highlights the smaller changed regions within changed lines.

## 5. Check that the file set matches GitHub

These commands should describe the same PR-shaped change:

```sh
git diff --name-only "origin/$base_branch...HEAD"
gh pr view --json files --jq '.files[].path'
```

If the lists disagree, fetch the base branch again, recompute the merge base, and rerun `change_base`. Also check whether you have edited any files locally with `git status --short`.

## 6. Reset Gitsigns after the review

To return every buffer to Gitsigns' normal index comparison:

```vim
:Gitsigns reset_base true
```

You can leave the review base active while drafting comments; reset it when you finish or switch tasks.

[Next: draft and submit inline comments](03-inline-comments.md)

