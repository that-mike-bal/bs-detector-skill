---
description: An update that over-explains basics and repeats its one point.
tags: [checks]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

BS test this. It's an update for our engineering leads about the API versioning change, and it's my draft.

---

# API Versioning Update

As many of you know, an API, or application programming interface, is the way that different software systems talk to each other. When one system wants data from another, it sends a request to the API, and the API sends back a response. APIs are very important to how our product works, because our customers' integrations use them every day.

Versioning is the practice of giving each set of changes to an API a version number. This lets customers keep using an older version while they move to a newer one. Versioning is important because it means changes don't break customers' integrations.

The key point of this update is that we are moving to date-based API versions starting March 1. In other words, starting March 1, our API versions will be based on dates. To put it simply, versions will be named by date from March 1 onward.

Each customer will be pinned to the version that is current when they create their API key. Old versions will be supported for 12 months after a new one ships.

To summarize: we are moving to date-based versioning on March 1, customers are pinned to their version, and old versions get 12 months of support. Again, the main change is that versions will be named by date starting March 1.

---
