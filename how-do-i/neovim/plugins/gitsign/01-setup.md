# Install and configure the review keymaps

## Requirements

- Neovim 0.11 or newer
- Git
- [GitHub CLI](https://cli.github.com/) authenticated with `gh auth login`
- [`gitsigns.nvim`](https://github.com/lewis6991/gitsigns.nvim)

For `lazy.nvim`, a review-focused plugin entry looks like this:

```lua
{
  "lewis6991/gitsigns.nvim",
  config = function()
    require("gitsigns").setup({
      on_attach = function(bufnr)
        local gitsigns = require("gitsigns")

        local function map(mode, lhs, rhs, desc)
          vim.keymap.set(mode, lhs, rhs, {
            buffer = bufnr,
            silent = true,
            desc = desc,
          })
        end

        map("n", "]c", function()
          if vim.wo.diff then
            vim.cmd.normal({ "]c", bang = true })
          else
            gitsigns.nav_hunk("next")
          end
        end, "Next Git hunk")

        map("n", "[c", function()
          if vim.wo.diff then
            vim.cmd.normal({ "[c", bang = true })
          else
            gitsigns.nav_hunk("prev")
          end
        end, "Previous Git hunk")

        map("n", "<leader>hp", gitsigns.preview_hunk, "Preview Git hunk")
        map("n", "<leader>hi", gitsigns.preview_hunk_inline, "Preview Git hunk inline")
        map("n", "<leader>hq", function()
          gitsigns.setqflist("all")
        end, "List all Git hunks")
        map("n", "<leader>hd", gitsigns.diffthis, "Diff file against review base")
      end,
    })
  end,
},
```

The `vim.wo.diff` branch preserves Neovim's built-in `[c` and `]c` behavior in a real diff window. Everywhere else, those keys call Gitsigns' current `nav_hunk` API.

This deliberately omits stage, reset, and undo mappings. They are useful while developing, but too easy to invoke accidentally during a read-only review.

Restart Neovim, then verify the plugin and commands:

```vim
:checkhealth gitsigns
:Gitsigns
```

If you do not want mappings, all tutorial steps also work as commands:

```vim
:Gitsigns nav_hunk next
:Gitsigns nav_hunk prev
:Gitsigns preview_hunk
:Gitsigns preview_hunk_inline
```

[Next: read a PR hunk by hunk](02-read-a-pr.md)

