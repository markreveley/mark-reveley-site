---
id: res:the-perils-of-uuid-primary-keys-in-sqlite-anders-murphy
type: resource
title: "The perils of UUID primary keys in SQLite (Anders Murphy)"
url: "https://andersmurphy.com/2026/06/05/the-perils-of-uuid-primary-keys-in-sqlite.html"
hacker_news: "https://news.ycombinator.com/item?id=48419571"
added: 2026-07-23
source: [elixir-mind-processed]
published: 2026-06-05
status: unread
tags: [article]
topics: [def:databases]
---
Benchmarks showing random UUIDv4 primary keys make SQLite inserts 14-16x
slower than sequential keys, recommending UUIDv7 or rowid.
