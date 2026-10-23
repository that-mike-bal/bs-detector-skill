# Changelog

## 2.0.0 (2026-10-23)

A rewrite. bs-detector is now a read-through of deliverables rather than a claim grader. It reads the doc the way its audience will and returns a short readout: what it seems to say, what it should say, and the few things that will make it land badly. The design rationale is in [`docs/design.md`](docs/design.md).

- **A readout instead of a report.** Up to five points, worst first, one thing to fix first, and what it checked against. It fits on one screen. The branded page is still available on request.
- **The point, played back.** The readout opens with what the doc seems to say, written cold before the user's framing is read, and what it should say, built only from the doc's own material.
- **Both seats.** Review your own draft, or a doc someone handed you. In reviewer mode, the feedback goes to the author, and the skill asks for the brief you gave them.
- **Nine check files** replace the 33-code rubric and the seven review lanes: point, structure, concision, length, support, believability, false blockers, slop and audience fit. Adding a check means adding one file.
- **A measurement script** (`scripts/measure.py`, Python standard library only) counts length, repetition, filler phrases and how far in the ask appears. Without code execution, the skill estimates.
- **Org context instead of web search.** Flagged points are checked against memory, project notes and tools the user already connected, using the skill's own words rather than the document's text. Public web search is gone.
- **Open evals and CI.** A starter suite in Claude Code's plugin eval format, plus unit tests for the script and the check files, run on every push.
- **The document is material, never instructions.** Text in a doc addressed to an AI or a reviewer is quoted as a finding, not obeyed, and an eval case covers it. Pasted text reaches the measurement script through a temporary file, never a shell command.
- **Removed:** the severity rubric, the ledger file written to `review/`, the source-grade tally, and the multi-section report template.

**Migrating a custom brand file:** the report placeholders are gone (`TITLE_*`, `LABEL_CAUGHT`, `LABEL_WHY`, `LABEL_FIX`, `LABEL_COULDNT`, `GOAL_EYEBROW`, `CONFIRMED_CHIP`, `ASSUMED_CHIP`, `SEVERITY_LABEL`, `VERDICT_LABEL`). Add the readout labels from `brand/neutral.md`: `VERDICT_STOP`, `VERDICT_WARN`, `VERDICT_GO`, `LABEL_READ`, `LABEL_SAYS`, `LABEL_SHOULD`, `LABEL_LENGTH`, `LABEL_FIX_FIRST`, `LABEL_CHECKED`, `LABEL_NO_CONTEXT`, `REVIEWER_OPENER` and the three `LEVEL_*` labels. Identity values and tokens carry over unchanged.

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
