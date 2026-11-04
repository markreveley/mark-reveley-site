---
type: handoff
audience: operator
updated: 2026-11-03
---

# Next steps for the operator

Read with [`next-agents.md`](next-agents.md).

## 1. Re-authorise the Google Workspace CLI (only when you want Google Tasks)

The saved `gws` token is rejected (`token_error: "Bad Request"`). In a Claude Code prompt, run:

```
! /opt/homebrew/bin/fnm exec --using=22 gws auth login --account dirtwiretouring@gmail.com --scopes https://www.googleapis.com/auth/gmail.modify,https://www.googleapis.com/auth/spreadsheets,https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/calendar,https://www.googleapis.com/auth/tasks
! cp ~/.config/gws/credentials.ZGlydHdpcmV0b3VyaW5nQGdtYWlsLmNvbQ.enc ~/.config/gws/credentials.enc
```

Then tell the agent it's done, and which Google account holds the tasks you mean.

## Questions

- **Bookmarks UI:** how to keep 1172 bookmarks from overwhelming readers. Options:
  - (a) a collapsed-topic graph view in artifact-dag;
  - (b) paging or per-topic landing pages on the site;
  - (c) splitting the biggest topics;
  - some combination.
- **elixir-mind:** should its `/bookmarks` skill now write to `site/bookmarks/unprocessed/`, with `survey/bookmarks.md` frozen?
- **Consent screen:** publish the `dirtwire-touring-gws` OAuth consent screen to production, so `gws` tokens stop expiring weekly?
