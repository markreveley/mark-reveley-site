---
type: Quote
resource: "https://tailscale.com/blog/how-tailscale-works"
quote: |-
  Note that the private key never, ever leaves its node. This is important because the private key is the only thing that could potentially be used to impersonate that node when negotiating a WireGuard session. As a result, only the two nodes that are communicating with each other are able to encrypt or decrypt packets for that WireGuard session. It’s important to keep that in mind: Tailscale node connections are end-to-end encrypted (a concept called “zero trust networking”).

  Unlike a hub-and-spoke network, unencrypted packets never need to be sent over a wire, and no intermediary can inspect them. (The exception is if you use subnet routes, which are useful for incremental deployment, which Tailscale supports. You can create a hybrid network that combines new-style mesh connections with zero or more old-style “hubs” that decrypt packets, then forward them to legacy physical networks.)
date_added: "2026-09-20"
tags: ["peer-to-peer-networking", "software-security"]
source_title: "How Tailscale works"
source_author: "Avery Pennarun"
source_date: "2020-03-20"
verification_status: "verified"
verification_date: "2026-09-20"
---
