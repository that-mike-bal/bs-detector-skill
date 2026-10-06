# Changelog

## 1.1.0 (2026-10-06)

The review was too dependent on sourcing. A claim could be unsourced and perfectly fine, or cited and still something nobody would believe, and only the first of those got caught. This release adds the second axis and three kinds of detection that never needed a source.

- **Believability, judged separately from sourcing.** Every load-bearing claim is now marked believable, a stretch, or doesn't pass, from the reviewer's own read against general knowledge — no source, no search. A claim that doesn't pass is a `kill` whatever its grade, including a verified one, and a no-source claim nobody would question drops to a note. New codes `K8`, `H10`, `H11`, and a calibration check that fails a review whose flags are all citation complaints.
- **Overclaiming and unexamined assumptions.** Judgment calls, estimates and open debates presented as decided or proven, and the premises an argument rests on that are never stated or tested.
- **False blockers.** Things stated as blocked, required, impossible or not allowed where nothing shows that they are. A `kill` (`K9`) when the ask rests on one, `hurt` (`H12`) when the plan merely bends around it. Also catches the mirror: "done" or "unblocked" on something still open.
- **A Clarity lane**, running at every depth including quick. Whether the point can be stated in one line, words that carry nothing, repetition, vague quantifiers where a real number exists, sentences that need a second pass, and the ask buried in prose. New codes `K10`, `H13`, `Q7`–`Q9`.
- **AI overwriting** as its own pattern set (`H14`): symmetrical scaffolding, filler transitions, lines that still read true with a competitor's name swapped in, confident phrasing with no object under it. It flags the prose, never the author or the tool.
- **A blunter voice.** Flat rejection when something doesn't hold: "I don't buy it. No one else will either." "This isn't clear enough." No softening of the call itself. Crediting what works stays, because it's what makes the hard calls land as earned.
- **Guardrails against the obvious failure modes:** bloat is a defect only when it costs the reader, prose you'd have written differently is taste and gets dropped, and blunt never means cruel.

## 1.0.2 (2026-10-05)

- Plugin icon for the directory listing: the mikebal.com laser gun, rendered from the theme's `assets/svg/laser-gun.svg` onto the brand's night/green tile at 1024x1024. Set as `icon` in `plugin.json`.

## 1.0.1 (2026-09-28)

- The document no longer leaves the review. Evidence and breadth lanes search the public fact behind a claim, in their own words, and never the document's own sentence or an unreleased figure, price, vendor, customer or date. A claim that can't be checked without exposing something private is graded "couldn't check", with the internal source to connect named instead. Applies to every lane, including lanes run without subagents.

## 1.0.0 (2026-09-25)

First public release.

- Goal checkpoint, blind read, six review lanes, and verification before any flag is shown.
- One severity scale (kill, hurt, quick, note) backed by a written rubric with criteria codes, patterns and worked examples.
- Seven evidence grades, including "couldn't check" for sources that exist but can't be reached.
- Fallbacks for clients without subagents, web search, connected apps or a page publisher.
- Report layout split into a template, and branding into swappable brand files (Mike Bal default, neutral preset).
- Claude Code plugin and marketplace manifests, Codex metadata, and a zip build for Claude apps.
