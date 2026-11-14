---
type: Post
title: "The Governance Spiral"
date_published: "2026-11-13"
excerpt: "Rules about rules. Plans within plans. The problem and the solution are often indistinguishable."
---
The governance spiral is a state of entropic bureaucratic feedback that LLMs tend to reach without proper guardrails. Somewhat unfortunately, the only solution is, more guardrails. The governance spiral is experienced as a continuous flow of seemingly self-referential rules about rules. Plans within plans. The problem and the solution are often indistinguishable.

Agents have no constancy. They are very powerful and very literal. They can seem scarily intuitive about certain things while wildly unintuitive about others. They cannot develop intuition about a system in the way a human would, so they can seem to require explicit guidelines. They certainly like to give them to themselves.

Let’s say you’ve asked an agent to list all available fruits at an online fruit store. The agent goes to the site, extracts the names of all the fruits, and lists them. One of the fruits is a fruit bar. Another is a jar of jam with “real fruit”. You point this out to the agent, which corrects the list, and creates a policy: “C01: referencing fruit by a product is not enough - it must be a real fruit.”

You do another intake with a fresh agent, the policy guard exists, and the fruit list is correct now - except that it is not listing fresh squeezed orange juice, which is not a product, it is actually literally only fruit, it’s just squeezed and comes in a bottle. You tell this to the agent, which creates a new policy, linked to C01, that reads “C02: fruit juice is considered a fruit, always make sure to list any and all fruit juice.”

Then, you do a new intake with a fresh third agent. This agent includes in the list a fruit bar, which advertises that it’s “sweetened with fruit juice.” You tell the agent, do not include fruit bars sweetened with fruit juice. Agent creates C03: “Do not include fruit bars sweetened with fruit juice.” Or significantly worse, the agent writes this guardrail into the agents.md.

And, you have begun the governance spiral. Further dependent rules will be authored built upon these, and if you’re very lucky, will be stored in the same place, but in all likelihood, will be scattered across several documents.

How to solve the governance spiral is a topic for another blog. But the first challenge is even recognizing that you are in it.
