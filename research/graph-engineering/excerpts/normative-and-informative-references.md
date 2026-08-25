---
type: Excerpt
subtype: definition
role: evidence
title: "Normative and informative references"
description: The RFC Editor's test for sorting an RFC's own references — essential to implementing or understanding it, or merely additional.
tags: [definitions, standards]
speaker: "RFC 7322, RFC Style Guide (RFC Editor)"
sources:
  - id: ietf
    resource: /references/ietf-rfc7322.md
    title: "RFC 7322: RFC Style Guide"
generated: { by: research_agent/claude-code, at: 2026-08-25T12:00:00Z }
verified: { by: "process:curl-quote-check", at: 2026-08-25T12:00:00Z }
status: stable
---

# Quotes

> "Reference lists must indicate whether each reference is normative or informative, where normative references are essential to implementing or understanding the content of the RFC and informative references provide additional information." [^ietf]

# Note

Section 4.8.6, "References Section." Unlike ISO/IEC and W3C, the IETF frames the distinction at the level of a document's *references* rather than its own body text — a cited RFC is normative if the one citing it cannot be implemented or understood without it, informative otherwise. When a document has both, the RFC Editor requires the reference list itself to be split into two labeled subsections.

[^ietf]: RFC 7322, RFC Style Guide, September 2014, §4.8.6
