---
type: Quote
resource: "https://news.ycombinator.com/item?id=48542480"
quote: |-
  If you're new to Iroh, my mental model is roughly "Tailscale at the application layer instead of the network layer".
  If your question is, "why not just use Tailscale?", look at it from an app developer's perspective. If you want to release an app and have instances of your app be able to easily connect to each other, you could theoretically embeded Tailscale functionality into your app, but then the users of your app need Tailscale accounts, and your app is dependent on Tailscale.
  Iroh lets you embed this functionality directly, and provides public fallback relays. If your app gets too big for the public relays, using your own relays is the flip of a switch.
date_added: "2026-09-14"
tags:
  - peer-to-peer-networking
  - developer-tools
  - vendor-lock-in
source_title: "Iroh 1.0"
source_author: "apitman"
source_date: "2026-06-15"
hacker_news_url: "https://news.ycombinator.com/item?id=48546782"
verification_status: "verified"
verification_date: "2026-09-14"
---
