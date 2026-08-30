# Command cheat sheet and troubleshooting

## One-screen review sequence

```sh
gh pr checkout 123
base_branch=$(gh pr view --json baseRefName --jq .baseRefName)
git fetch origin "$base_branch"
git merge-base HEAD "origin/$base_branch"
nvim .
```

Then in Neovim, substituting the printed SHA:

```vim
:Gitsigns change_base THE_MERGE_BASE_SHA true
:Gitsigns setqflist all
```

Review motions:

| Action | Mapping | Command |
| --- | --- | --- |
| Next hunk | `]c` | `:Gitsigns nav_hunk next` |
| Previous hunk | `[c` | `:Gitsigns nav_hunk prev` |
| Preview old text | `<leader>hp` | `:Gitsigns preview_hunk` |
| Inline preview | `<leader>hi` | `:Gitsigns preview_hunk_inline` |
| All repository hunks | `<leader>hq` | `:Gitsigns setqflist all` |
| Full-file diff | `<leader>hd` | `:Gitsigns diffthis` |
| Restore normal base | — | `:Gitsigns reset_base true` |

## What the gutter signs mean

The exact characters and colors depend on your colorscheme and Gitsigns configuration. Semantically they mark:

- added lines;
- changed lines;
- deleted lines, represented beside a neighboring surviving line;
- staged variants, if your configuration displays them.

During PR review the signs describe the comparison with the base passed to `change_base`, plus any uncommitted edits you make on top of the checked-out PR.

## `]c` and `[c` do nothing

Gitsigns does not install those mappings by default. Add the `on_attach` mappings from [the setup chapter](01-setup.md), restart Neovim, and check:

```vim
:verbose nmap ]c
:verbose nmap [c
```

The output identifies the configuration that owns each mapping.

## No signs appear

Check, in order:

```vim
:checkhealth gitsigns
:Gitsigns debug_messages
:set signcolumn?
```

Then verify in a shell that the current file really differs from the selected base:

```sh
git diff THE_MERGE_BASE_SHA -- path/to/file
```

Common causes are opening Neovim outside the repository, using a stale or incorrect base, reviewing an untracked file while `attach_to_untracked` is disabled, or exceeding Gitsigns' configured maximum file length.

## The signs include changes that are not on GitHub

First check for local edits:

```sh
git status --short
```

If the working tree is clean, you probably compared directly with the current `origin/main` instead of the PR merge base. Fetch the actual base branch, run `git merge-base`, and pass that SHA to `change_base`.

## The signs vanish in files opened later

The global argument was omitted. Run:

```vim
:Gitsigns change_base THE_MERGE_BASE_SHA true
```

## GitHub rejects an inline comment with HTTP 422

Usually one of these is true:

- the `path` is not relative to the repository root;
- the line is not present in the PR diff or its displayed context;
- `RIGHT` was used for a deleted line that belongs on `LEFT`;
- the PR head changed after the line numbers were recorded;
- a multi-line comment is missing `start_line` or `start_side`.

Refresh the PR, verify its `headRefOid`, and re-anchor the comment instead of retrying guessed coordinates.

## Gitsigns is showing the index again

`change_base` lasts for the Neovim session, not forever. Re-run it after restarting Neovim. This is desirable: ordinary editing should return to the normal working-tree-versus-index view automatically.

