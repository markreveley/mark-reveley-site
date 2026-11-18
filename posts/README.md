# Post database

Each other Markdown file in this directory is one post record and the
canonical source for its generated page.

Required frontmatter fields:

- `type: Post`
- `title`: the displayed post title
- `date_published`: an ISO date (`YYYY-MM-DD`)
- `excerpt`: optional text shown on the Posts landing-page card
- `tags`: optional list of lowercase, hyphenated category slugs, such as
  `[agent-failures, governance]`. Each must be mapped exactly once in
  [`taxonomy.yml`](taxonomy.yml), which nests them under broader categories;
  a post appears on its tags' pages and on every parent's page.

The Markdown body contains the post itself. CommonMark headings, paragraphs,
lists, blockquotes, emphasis, links, and code are rendered on the site. Raw
HTML is displayed as text rather than executed. Use level-two headings for
major sections; the post title is the page's level-one heading.
