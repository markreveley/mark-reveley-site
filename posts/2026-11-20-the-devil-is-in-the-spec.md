---
type: Post
title: "The Devil Is in the Spec"
date_published: "2026-11-20"
excerpt: "Docs used to trail the code. Now the natural language spec drives it, and the details that matter have moved."
tags: [specification, comprehension]
---
One of the effects of having an agent at your disposal is you have to begin thinking in terms of how to delegate. This seems obvious, but how you do that is not always clear.

What aspects of your thinking, what aspects of a system of organization and processing, what aspects of evaluating what you've built can safely be delegated is not always easy to specify.

The challenge is keeping a representative mental model of what you are building top of mind that allows you to drive and delegate without that mental model drifting from what has actually been built. Which is nearly inevitable.

To truly understand the system on the level the agent does, you would have to build the system. With code, you have to be actually writing the code in the same way software developers traditionally have. This is no longer tenable, unless you are very good, working on very critical software, or programming as creative expression. Otherwise the incentives are off.

We accept the downside, the downstream negative effects of cognitive drift across the system as being the price we will pay to employ fanatical legions of amnesiac coding agents.

You cannot definitively test for system comprehension over a codebase. But you can test the functionality of the code. Similar to code, you cannot test for how intention maps to instructions, doctrine, policy, and process specifications that are written in natural language. Dissimilar to code, you cannot test for the accuracy and effectiveness of markdown, at least not without an obscene number of evals.

Traditionally, docs were often out of step with the code, considered to be a trailing artifact where drift was a forgivable sin. Code defined, docs referenced.

That relationship has inverted. Natural language specification and intention capturing is what orients and drives the agent, and how the agent approaches creating the code which defines the project. The devil was in the details of the code, it's now in the details of the spec.
