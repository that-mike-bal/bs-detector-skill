---
description: A long document driving a tiny decision.
tags: [checks]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

BS test this before I send it. It goes to our finance approver, who just needs to approve or reject the renewal. It's my draft.

---

# Diagramming Tool Subscription: Renewal Review

## Summary
This document reviews our diagramming tool subscription ahead of its renewal on April 1 and recommends that we renew it.

## Background
We first bought the diagramming tool in 2021, when the design team needed a shared place to sketch user flows. At the time, flows lived in a mix of slide decks, whiteboard photos and personal files, and nobody could find the current version of anything. The design team trialed three tools over a month and chose this one because it was the easiest for non-designers to pick up. Over the next year, product managers started using it for roadmap sketches, and engineering adopted it for architecture diagrams. By 2023 it had become the default place for any diagram that more than one person needed to see.

## How teams use it today
Design uses it for user flows and journey maps. Most new features start as a flow in the tool before anything is mocked up. Product uses it for roadmap sketches and for the diagrams that go into planning documents. Engineering uses it for system architecture, sequence diagrams and incident timelines, and several runbooks link directly to diagrams in the tool. Support uses it for troubleshooting decision trees that agents follow on live tickets. Marketing has started using it to plan campaign flows. In short, it has spread well beyond the team that first bought it, and diagrams from it are embedded in many of the documents people use every day.

## Alternatives we looked at
We looked at three alternatives before recommending renewal.

The first is a general-purpose whiteboard tool that several teams already use for workshops. It is good for freeform sketching and real-time collaboration, but its diagramming shapes are limited, and it has no way to keep diagrams consistent across a document library. Moving to it would mean redrawing architecture diagrams by hand.

The second is the diagramming feature built into our documentation platform. It is included at no extra cost, which is attractive. However, it supports only basic shapes and connectors, has no templates for sequence diagrams, and can't import our existing files. Engineering tried it for two weeks and went back.

The third is an open-source diagramming tool that we could self-host. It is free to license and has strong diagram features. But self-hosting would put maintenance, upgrades and security reviews on the platform team, and it lacks the single sign-on integration our security team requires for internal tools.

## Feature comparison
- Templates for user flows, architecture and sequence diagrams: current tool yes; whiteboard partial; docs platform no; open source yes.
- Import of our existing files: current tool yes; whiteboard no; docs platform no; open source partial.
- Single sign-on: current tool yes; whiteboard yes; docs platform yes; open source no.
- Embeds in our documentation platform: current tool yes; whiteboard yes; docs platform yes; open source partial.
- Real-time collaboration: all four yes.

## Usage data
Over the last 90 days, 42 people across six teams edited at least one diagram. The library holds about 1,300 diagrams, of which roughly 400 were edited in the last six months. About 150 diagrams are embedded in runbooks, planning documents and support playbooks.

## Security and compliance
The vendor supports single sign-on through our identity provider, holds a current SOC 2 Type II report, and stores data in the US region we require. Security reviewed the vendor last year and had no findings.

## Migration considerations
Moving off the tool would require redrawing or converting about 1,300 diagrams, re-embedding about 150 of them, and retraining six teams. We estimate that at several weeks of combined effort, spread across teams that have other commitments this quarter.

## Cost
The renewal is $4,800 for one year, the same price as last year.

## Recommendation
Renew the diagramming tool subscription for one year at $4,800.

---
