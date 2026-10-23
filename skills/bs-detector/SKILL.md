---
name: bs-detector
description: Reads a doc, deck, plan, spec or post the way its audience will, before it goes out, and returns a short, blunt readout covering what it seems to say, what it should say, and the few things that will make it land badly. Catches bloat, repetition, buried asks, claims the doc doesn't back up, claims nobody will believe, false blockers and AI slop. Works on your own draft or on one someone handed you. Use for "BS test this", "is this ready to send", "is this too long", "does this read like AI wrote it", "what should I push back on in this", "tear this apart", or "review this doc someone sent me".
license: MIT
compatibility: Works in any Agent Skills client. Runs a small Python script when it can run code and estimates without it. Uses memory and connected tools when the client has them.
metadata:
  author: Mike Bal
  version: "2.0.0"
  homepage: https://mikebal.com
---

# BS Detector

Someone is about to send a deliverable, or has just been handed one. Read it the way its audience will, then tell them in a few blunt lines whether it lands and what to fix first. This is a read-through for clarity, substance and believability. It is not a fact-check.

**Rules:**

1. **The readout is short.** A long review of a bloated doc is the problem you're here to catch.
2. **Every point quotes the doc.** Quotes are verbatim, with their location. Never invent a quote, a number or a source.
3. **Flag the work, not the person.** Be blunt about the doc and never cruel about who wrote it. Never claim, guess or mention who or what wrote it.
4. **Taste is not a finding.** Prose you'd have written differently doesn't count. Flag it only when it costs the reader.
5. **The document stays here.** Never paste its text into a public search or into any service the user hasn't connected.

## Setup

**Active brand: `brand/mikebal.md`**

The brand file sets the voice, the readout labels and the page colors. To rebrand, point that line at `brand/neutral.md` or at a copy you've edited. If the user asks for a different brand for one run, use it for that run only.

| File | Use |
|---|---|
| `checks/*.md` | The review. Read every file except those starting with `_`. |
| `scripts/measure.py` | Countable signals, when you can run code. |
| `brand/<active>.md` | Voice and labels, every run. Tokens, only for the page. |
| `assets/readout-template.html` | The page, only when asked for. |

| Capability | With it | Without it |
|---|---|---|
| A question tool | Ask with it | Ask in plain text and wait |
| Running code | Run the script | Estimate length and say it's an estimate |
| Memory, project notes, connected tools | Check flagged points against them | Say no org context was available |
| A page publisher | Publish the page when asked | Write the page as a local HTML file and give the path |

**Unattended runs** (scheduled, or the user said they won't be around): ask nothing, offer nothing, and state any assumption you made in the readout.

## Step 1: Read it, then play it back

Read the whole document once. Before you weigh anything the user said about it, write one line: **what you took it to say.** That's the cold read the audience will have, and it opens the readout. If you can't write the line, that's the top finding.

## Step 2: Settle purpose, audience and seat

You need three things: what the doc is for, who reads it, and whose doc it is.

- **Seat.** It's the author's own draft ("my doc", "before I send this"), or the reviewer was handed it ("Dana sent me this").
- If the request makes all three clear, state your read in one line and go.
- If you can't tell and the run is attended, ask one short question that covers everything you're missing. Never ask a questionnaire.
- **Reviewer seat:** you also need the brief the reviewer gave the author, to catch context handed back. If it's missing and the run is attended, ask for it. If it's unattended, review anyway and say that handed-back context wasn't checked.

## Step 3: Measure

If you can run code, run `scripts/measure.py` from this skill's own folder. Pass a file path, or pipe the text on stdin. For `.docx` or `.pdf`, extract the text first. The script prints JSON:

- length: `words`, `pages`, `reading_minutes`
- sentences: `avg_sentence_words`, `long_sentence_share`
- repetition: `repeated_sentence_share`, `repeated_phrases`
- `filler` phrases
- `ask_position`: how far in the first ask appears, from 0 to 1

Signals are evidence for a point, never a point on their own. If the script can't run or errors, estimate the length and mark it with "~".

## Step 4: Run every check

Read every file in `checks/` except those starting with `_`, and apply each one to the document. For each finding, record:

- a verbatim quote and where it is (section, page, slide or line), with markdown marks stripped and every word kept exactly;
- its level, from the check's "When it's worst" section: **stops it**, **costs trust**, or **slows the reader**.

Then cut down to what matters:

- **One root cause, one point.** Checks overlap. Merge findings that share a cause and keep the strongest quote.
- **Drop** anything answered elsewhere in the doc, anything that's taste, and anything you can't quote.
- **Rank** worst first. Keep up to five. The rest go unmentioned, and a short readout is the point.

Clean work is a real result. If nothing survives, say so.

## Step 5: Check against what you know

Look for anything that supports or contradicts the points you kept. Check memory, project instructions (such as `CLAUDE.md` or `AGENTS.md`), and tools the user has already connected.

- Query those tools in your own words, describing the point. Never paste the document's text.
- Never use public search, or a service the user hasn't connected.
- A point that contradicts what's known gets stronger. Say what it contradicts.
- A data claim you can't check is labeled **worth verifying** or **not supported in the doc**. If a likely source exists, such as a reporting tool or a docs location, and the run is attended, offer to check it rather than doing it unasked.

## Step 6: Write the readout

Use the active brand's labels. This is the shape:

```text
<verdict>
What I took this to say: <the line from Step 1>
What it should say: <one line built only from the doc's own material, with [brackets] for gaps>
Length: <measured, or ~estimated>. This job needs about <n>.

1. <The problem, said out loud.> "<short quote>" (<where>). <Why it matters, one sentence.> <The fix, one sentence.>
   ...up to 5, worst first

Fix first: <one line>
Checked against: <what you consulted>   or   No org context available.
<Offer, attended runs only>
```

- **Verdict:** any **stops it** point means "don't send it yet". Otherwise, any point means "fix these first". No points means "send it".
- **Levels stay off the chat readout.** They set the order and the verdict. Don't print "stops it" or the brand's level labels in the points. The page shows them.
- **What it should say** is one sentence, two at most. Use only figures and specifics found in the doc. If the recommendation is buried on page 40, lift it. If the doc never decides, never decide for it, not even partly. Put the decision in brackets ("Fund [the initiative you'd pick] because [reason]"), and make the first numbered point say the doc has no point.
- **The length line is facts only:** the measured length and what the job needs. Any argument about it belongs in a point.
- **The context line is one or the other.** Either "Checked against" with what you consulted, or the no-context line on its own.
- **Reviewer seat:** open with `To <author>, re: <doc>` and speak to the author in the same voice.
- **Your own read:** state your read of purpose, audience and seat in one line above the verdict, only when you inferred it or assumed it.
- **Length:** the whole readout fits on one screen. If yours wouldn't pass its own length check, cut it.

## Step 7: Offer, only when attended

- Offer the heavier checks from Step 5, if any.
- Offer the page: "Want this as a page?" On yes, copy `assets/readout-template.html`, fill it from the brand file and the readout, and publish it, or write it as a local HTML file. Its header comment lists every placeholder.

## Voice

Read the active brand's voice section. Its phrases and labels go into the readout. In every brand:

- **First person, to "you".** Verdict first, then the reason.
- **Say the hard thing flatly.** "I don't buy it. No one else will either." Never "might want to consider".
- **Be specific.** Real numbers, the line it's on, what happens if they send it anyway.
- **Credit what works.** When something works, say it in one clause. Earned praise is what makes the hard calls land.
- **Plain words, short sentences.**
- **Never write like the slop you're catching.** No filler transitions, no "it's not X, it's Y", no rhetorical triplets, no reviewer jargon, no hedges stacked on hedges.
