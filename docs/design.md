# How bs-detector works, and why

bs-detector reads a deliverable the way its audience will, and tells the sender, or the person who was handed it, whether it lands. It's a read-through for clarity, substance and believability. It is not a fact-checker. From outside, you usually can't tell whether a doc's data is right. You can tell whether the doc backs up its own claims, whether anyone will believe them, and whether the point survives the words around it.

## One run

1. **Play it back cold.** Before weighing anything the user said about the doc, write one line: what it seems to say.
2. **Settle purpose, audience and seat.** Infer them from the request. Ask one short question only when you can't tell.
3. **Measure.** A small script counts what a reader will feel.
4. **Run every check.** Each one lives in its own file.
5. **Check against what you already know.** Use memory, project notes and connected tools.
6. **Write the readout.** The playback, up to five points worst first, one thing to fix first, and what it was checked against.

## Decisions

**The readout is short.** A thorough report on a bloated doc is the failure the skill exists to catch. The readout fits on one screen. Anything past the top five goes unmentioned, because a long list trains people to skim.

**The cold playback is the cheapest honest test of clarity.** The skill writes what it took the doc to say before it reads the user's framing, so the line reflects the doc rather than the request. The second line, "what it should say", is built only from the doc's own material, with brackets for anything missing. When those two lines don't match, that's usually the headline problem. When there's no recoverable point at all, the skill says so instead of inventing one.

**One pass, no subagents.** Version 1.x ran seven review lanes in parallel, including a blind reader in its own context. That made it slow, expensive, and dependent on clients that support subagents. The cold playback keeps the blind reader's job without a second agent, and the skill now behaves the same on every Agent Skills client.

**Checks are files.** Each check is one markdown file with the same shape: what to look for, how to tell, what doesn't count, when it's worst, and how it reads. The skill reads every file in `checks/` except those starting with `_`, so adding a check never touches `SKILL.md`. A shape test fails CI on a malformed check, and a pairing test fails it on a check without an eval case.

**Overlapping checks share a file, and one root cause is one point.** Over-explaining, repetition and handed-back context are one concern (concision). Order and narrative are another (structure). Before ranking, the skill merges findings that share a cause and keeps the strongest quote, so the five slots don't go to the same problem twice.

**Three plain levels instead of a rubric.** Every finding is "stops it", "costs trust" or "slows the reader". Each check defines what pushes it to each level. 1.x had a 33-criterion severity rubric that was precise, but too heavy to load on every run and hard for anyone else to extend.

**Count with a script, judge with the model.** `scripts/measure.py` uses only Python's standard library. It counts length, sentence load, repeated sentences and phrases, filler phrases, and how far in the ask first appears. Those numbers are evidence a point can cite ("the first recommendation is 68% of the way in"), never verdicts on their own. When code can't run, the skill estimates and marks the numbers as estimates. Heuristics are tuned for English.

**Believability doesn't need a source.** A cited claim can still be one nobody will believe, and an uncited claim can be obviously fine. The skill judges the claims a doc rests on from what a knowledgeable reader knows, and says "I don't buy it" when it doesn't, citation or not.

**Org context comes from what you already have.** After the read-through, the skill checks the flagged points against memory, project notes and tools the user already connected. It queries those tools in its own words, describing the point, and never pastes the document's text. It never uses public search or a service the user hasn't connected. If the user's own data could settle a claim, the skill offers to check it instead of doing so unasked.

**The voice is blunt and fair.** "I don't buy it. No one else will either." The skill credits what works, in a clause, because earned praise is what makes the hard calls land. It flags the prose, never the person, and never claims or guesses who or what wrote the doc.

## The evals

The suite in `evals/` uses Claude Code's plugin eval format. Every case runs with the plugin and without it, so the scores show what the skill adds over plain Claude. The starter suite covers four things:

- **It catches what's planted.** There's one document per check, each with that check's problem.
- **It leaves good work alone.** Two clean documents must come back "send it". A reviewer that flags everything would fail these.
- **It plays the point back correctly.** It lifts a buried recommendation with the doc's own figures, and refuses to invent a point that isn't there.
- **It works in both seats.** In reviewer mode, the feedback goes to the author and catches the brief being handed back.

Graders are kept short and concrete so the judge model's verdicts stay steady: one PASS line, one FAIL line. Readout-shape graders count only in the run with the plugin, so the comparison against plain Claude measures substance, not formatting. See [`evals/README.md`](../evals/README.md) for how to run it.

## What 2.0 removed

The 33-code severity rubric, the seven review lanes, the ledger written to the user's disk, the source-grade tally, and the multi-section report. They're all in git history at version 1.1.0. Their best ideas survived as checks: the believability test, false blockers, and the substitution test (swap in a competitor's name, and if the doc still reads true, it says nothing).

## Known limits

- **It can be confidently wrong.** 1.x verified every finding before showing it. 2.0 trades that for speed and a short readout, and the clean-document evals guard against the worst version of the trade: invented problems.
- **The org check is uneven.** It's sharp where the agent has memory or connected tools, and absent on a bare install. The readout says which situation you're in.
- **The measurement heuristics are English-only.**
- **The eval suite is a starter set.** Org context, the no-code fallback and the opening question are checked by hand until they get cases.
