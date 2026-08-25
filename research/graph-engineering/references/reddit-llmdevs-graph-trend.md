---
type: Source Reference
title: "r/LLMDevs: What's up with new trend with graphs?"
description: The seed source — a Reddit exchange in which an OP asks why graphs are suddenly everywhere and a commenter defends graphs as representation, not just retrieval.
resource: https://www.reddit.com/r/LLMDevs/comments/1vwixw5/whats_up_with_new_trend_with_graphs/
tags: [level-1, skepticism, knowledge-representation, community]
source_author: "anonymous Reddit users (OP + one responding commenter)"
source_date: "2026 (thread id 1vwixw5)"
retrieved: "2026-08-24"
availability: user-supplied
generated: { by: research_agent/claude-code, at: 2026-08-24T23:00:00Z }
verified:
  - { by: "human:mreveley", at: 2026-08-24T00:00:00Z }
  - { by: "human:mreveley", at: 2026-08-25T00:00:00Z }
  - { by: "process:transcript-match", at: 2026-08-25T02:05:00Z }
status: stable
---

# About

The prompt for this whole bundle. An OP asks what the graph trend is for; a commenter answers in four moves: graphs are legible to humans *and* machines; storage shape determines retrieval; complex things (processes, decisions, relationships, sequences) are not "a singular data point"; and a graph plus the code that interprets it is an abstraction layer — "a map of how something works," read back.

reddit.com is not fetchable from this research environment. The full exchange was supplied **verbatim in-session by the repository owner** (`human:mreveley`) — twice: on 2026-08-24 with the original research request, and again, word-for-word identically, on 2026-08-25. The two supplies were mechanically compared (`process:transcript-match`): zero word-level differences; the only variances are typographic (the OP's lines carry curly apostrophes, the responder's straight — preserved below as supplied; excerpt quotes normalize apostrophes). The transcript below reproduces the 2026-08-25 supply's paragraph structure exactly, including the embedded link to the [FLARE thread](reddit-flare-ide.md) (previously elided to a bracket note). Trust rests on the double human attestation, not on an independent fetch.

# Transcript (as supplied)

> OP: What’s up with new trend with graphs?
>
> Response: Sure, graphs are a way to express complex information in a way where both humans and machines can understand it.
>
> I assuming that we're talking about computational graphs and not visual charts.
>
> But, obviously a graph can be converted into a visualization very easily and humans love to see information visualized because it helps to understand it.
>
> So, it makes complete sense to work with graphs for certain things. Especially ERD like graphs for understanding a process.
>
> As an example: If you look in this screen shot, I hope you can see why we need the information to be visualized, there's a ton of it.
>
> https://old.reddit.com/r/ArtificialInteligence/comments/1vwazom/flare_a_graphfirst_ide_for_agentic_coding_watch/
>
> OP: Thanks, for such an eloquent response, however I still don’t understand the purpose. It it just fancier way to do retrieval?
>
> Response: Well yes and no. It's a way to store data that complex systems use, but obviously the storage method directly impacts the retrieval method. It's more about the data complexity honestly. We are just trying to work with things that are not well described by a singular data point. So, you have all of this data, and you want to store it in a way that represents what it is, very well. So, we're trying to build decision making trees for 10,000 different things our system does, that's not something that is described well in a traditional CSV data format.
>
> I suppose you could break each decision node down and encode in into rows that are linked together. But, then the data wouldn't be easy to read and you would have to hop and skip around because of the links. Then retrieving it would be slower than it needs to be, because it's encoded across multiple rows, instead of just 1.
>
> Where as with a graph: You can do whatever you want including redefine the coordinate system. Your graph maybe has 3 axis instead of 2. You're only limited by whatever you implement. The limitation of the data structure itself goes away. So, you're building an abstraction layer on top of the data format basically, which is your code that interprets your own graph. So, now you have a way to represents complex things well, so things like processes, functionality, relationships, sequences, and tons more. A graph is inherently just an abstract way to represent information.
>
> Edit: The concept to me, is like you're creating a map of how something works, and then reading it back.

# Excerpts in this bundle

- [The skeptic's question: just fancier retrieval?](../excerpts/rl--just-fancier-retrieval.md)
- [Legible to humans and machines](../excerpts/rl--humans-and-machines.md)
- [Yes and no: storage shapes retrieval](../excerpts/rl--yes-and-no.md)
- [Decision trees don't fit CSV rows](../excerpts/rl--decision-trees-vs-csv.md)
- [The graph as abstraction layer](../excerpts/rl--abstraction-layer.md)
- [A map of how something works](../excerpts/rl--map-metaphor.md)
