# Severity rubric

Use this to set and justify every finding's severity. Every finding in the ledger gets a level **and** the criterion code it met (for example `hurt · H1`). If you can't name a code, the finding isn't ready to show anyone.

Codes stay in the ledger. The report shows the level in the brand's plain words, never the code.

## 1. Four questions set the level

1. **Is it a defect?** Taste, style you'd do differently, and "I'd structure it another way" are not defects. Drop them.
2. **Would a knowledgeable reader believe it?** Separate question from where it came from. A cited claim can still be unbelievable, and an uncited one can be obviously fine. See section 3.
3. **Does it touch the ask?** A claim is load-bearing if the decision, the ask, or the reader's next move would change were it false.
4. **What does the deciding reader do if they find it?** Say no or "come back later" (kill), keep going but trust the rest less (hurt), notice and move on (quick or note).

## 2. The levels

| Level | Plain test | Where it goes | Effect on that audience's verdict |
|---|---|---|---|
| `kill` | If the deciding reader finds this, the answer is no or "come back later." | Flag | stop |
| `hurt` | The answer might still be yes, but every other number now gets discounted. | Flag | warn |
| `quick` | A careful reader notices. The fix is a line edit or one check, and nothing else depends on it. | Flag if it's in the worst 7 and changes a line, otherwise A few more things | warn |
| `note` | Real, small, worth a line. | A few more things | none |
| drop | Taste, a claim the document doesn't make, or silence treated as contradiction. | Nowhere | none |

## 3. Believability, separate from sourcing

A source grade answers "where did this come from". It does not answer "would anyone believe it". Both matter, and the second catches what the first misses.

Judge every load-bearing claim on both. Believability is your own read as someone who knows the territory, against general knowledge, the document's own figures, and what the audience already knows. It needs no source and no search.

| Mark | Test |
|---|---|
| **Believable** | A knowledgeable reader nods and moves on. |
| **A stretch** | They don't reject it, but they want the working before they act on it. |
| **Doesn't pass** | They don't buy it. Nothing in the document would change their mind, and a citation doesn't rescue it. |

**"Doesn't pass" is a finding on its own, whatever the grade.** A verified number supporting a conclusion it doesn't reach still doesn't pass. Say that plainly instead of hunting for a sourcing technicality to hang it on.

**Unsourced is not the same as unbelievable.** A no-source claim every reader would accept ("most of our traffic is mobile", at a company whose traffic is mobile) is a note at most. Don't manufacture severity out of a missing citation when nobody would question the substance.

**A citation doesn't buy a pass.** Check what the source actually supports before the grade does any work for the author.

## 4. Criteria

A finding needs to meet **one** criterion at its level.

### kill

| Code | Criterion |
|---|---|
| K1 | A load-bearing claim is **contradicted** (grade E) by a source the audience trusts, or by the document's own figures. |
| K2 | A load-bearing claim has **no source** (grade D) and it's the justification for the ask. |
| K3 | **The ask is missing or unpriced** for an audience that decides: no amount, no owner, no date, or no decision named. |
| K4 | **The math doesn't work** on a load-bearing figure, and the corrected number changes the conclusion. |
| K5 | **The premise is gone.** The gap, problem or market the document is built on has changed. |
| K6 | **Wrong room.** It asks for a decision this reader can't make, or one that's already been made. |
| K7 | **Exposure in public copy.** An unsupported superlative, health, safety, pricing or legal claim a regulator, a competitor or a customer could hold you to. |
| K8 | **Nobody will buy it.** A load-bearing claim doesn't pass the straight-face test, whatever its grade. The reader stops trusting the document at that line. |
| K9 | **A false blocker.** Something is stated as blocked, impossible, required or not allowed, it isn't, and the ask rests on it: more time, more budget, a cut, an exception, a different path. |
| K10 | **The point never lands.** After a full read, the deciding reader still can't say what's being asked or why. No decision can be made from it. |

### hurt

| Code | Criterion |
|---|---|
| H1 | A load-bearing claim rests on a **sideways source** (grade C): a real number that measures something else. |
| H2 | **Confidence beyond the evidence**: "will" on a forecast, "proven" on a pilot, a sample stated as everyone, correlation stated as cause. |
| H3 | A **non-load-bearing claim is wrong**, and a reader will spot it. |
| H4 | An **unproven superlative** ("only", "first", "every competitor", "industry-leading") in internal material. If a source contradicts it, use H3 (or K1 if it's load-bearing). |
| H5 | The **obvious first question has no answer**: the cost side, a dependency, a risk, or how success is measured. |
| H6 | **The document argues with itself**: the same figure or fact differs between sections, and the difference matters. |
| H7 | **Bad news is buried or softened**: "softer than planned" for a 30% miss, or the risk in an appendix. |
| H8 | **A flattering window or baseline**: a comparison period or peer set picked because it looks good. |
| H9 | A load-bearing claim has **no source** (grade D), but it isn't the justification for the ask. |
| H10 | **Settled when it's open.** A judgment call, an estimate, or a live debate presented as decided, proven or definitive. |
| H11 | **An unexamined assumption carries the argument.** The case rests on a premise that's never stated, never tested, and wouldn't survive a direct question. |
| H12 | **A constraint is asserted, not shown.** A blocker, dependency, requirement or limit stated as fact with nothing behind it, and the plan bends around it. K9 when the ask rests on it. |
| H13 | **Bloat hides the point.** The substance is in there, but the reader has to dig it out. Length, repetition or scaffolding is doing the damage. |
| H14 | **Composed, not thought through.** Machine-written prose: symmetrical scaffolding, filler transitions, lines that would fit any company, confident phrasing with nothing specific under it. |

### quick

All three must hold: the fix is a line edit or one check, nothing else depends on it, and a careful reader would notice.

| Code | Criterion |
|---|---|
| Q1 | A minor figure, date, name or link is wrong or unsourced. |
| Q2 | An acronym or term this audience won't know is used without a definition. |
| Q3 | Units or periods are missing or mixed (monthly vs. annual, gross vs. net), but the conclusion survives. |
| Q4 | More precision than the data supports ("37.4%" from 40 responses). |
| Q5 | The ask is there but buried below the first screen or page. |
| Q6 | Stacked hedges or weasel words that blur what's actually being claimed. |
| Q7 | **Half the words do nothing.** A passage survives a serious cut with nothing lost. |
| Q8 | **Vague where a number exists.** "significantly", "a number of", "substantially", "most", where the real figure is available. |
| Q9 | **Read-it-twice sentence.** The meaning only arrives on the second pass. |

### note

Anything real that doesn't meet a quick criterion: a typo that changes nothing, an inconsistency in naming, a small structural stumble the blind read hit.

## 5. Moving a level up or down

**Up one level when:**

- the audience is external (investors, board, customers, press) or checks for a living (finance, legal);
- the claim sits in the headline, exec summary, first slide, or the ask itself;
- the same pattern shows up three or more times, so it reads as carelessness rather than a slip;
- a reader could check it in under a minute.

**Down one level when:**

- the document already labels the uncertainty ("early read", "directional", "assumes X");
- the audience already has the context and won't be misled;
- the user confirmed it's a working draft meant to invite pushback.

**How adjustments combine:** net the ups and downs, then move at most one level in total.

**Never:**

- reach `kill` by adjustment. A finding is `kill` only when it meets a K criterion. Adjustments can take a `kill` down to `hurt`, never a `hurt` up to `kill`;
- raise anything on taste;
- treat a "can't know yet" (U) or "couldn't check" (X) grade as a defect on its own. A load-bearing U stated as fact tops out at `hurt · H2`, and the fix is to present it as a bet;
- treat a silent source as a contradiction.

## 6. Grade and believability to default level

A starting point, before the adjustments in section 5.

| Grade | Load-bearing | Not load-bearing |
|---|---|---|
| A verified | none | none |
| B backed, small gap | quick or note | none |
| C sideways source | hurt (H1) | note |
| D no source | kill (K2) if it justifies the ask, otherwise hurt (H9) | quick (Q1) or note |
| E contradicted | kill (K1) | hurt (H3) if a reader will spot it, otherwise quick |
| U can't know yet | hurt (H2) if stated as certain, otherwise none | none |
| X couldn't check | none. List it under "couldn't check" and name the source to connect. | none |

Then apply believability, which can raise a level on its own:

| Mark | Load-bearing | Not load-bearing |
|---|---|---|
| Believable | no change. On a D grade nobody would question, drop to note. | no change |
| A stretch | at least hurt (H10 or H11) | note |
| Doesn't pass | kill (K8), whatever the grade says | hurt (H3) |

**D or X?** D means the document gives no source and you can't find one. X means the document names or clearly implies a source (a dashboard, a report, a survey) that you can't reach. An internal figure with a named source you can't open is X, not D.

**Inferences:** a conclusion drawn from a real number, such as cause read into a correlation, is C (the number is real but doesn't show what's claimed). That lands at `hurt · H1` or `H2`, not `kill · K2`.

**Forecasts:** a forecast can't be verified, so it starts at U. But check whether the document's own figures can reach it. If they can't, grade it E: the document contradicts itself.

## 7. Patterns to hunt

What each lane should be scanning for, with the check to run and the usual landing spot.

### Numbers

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Orphan number | "a 40% lift" with nothing behind it | Trace it to a source or the document's own data | K2 / Q1 |
| Proxy metric | Email opens cited as proof of activation | Ask what the source actually counts | H1 |
| Doesn't reconcile | Parts don't sum; percentages of different bases added together | Recompute from the document's own figures | K4 / H6 |
| Impossible target | The goal needs a conversion rate nothing in the document supports | Work backward to the rate required and compare it to the best one shown | K4 |
| Base-rate leap | A forecast far above the document's own history | Compare to the highest past result in the document. If the document's own figures can't reach the forecast, grade it E. | H2, or K4 when it's the reason for the ask and E |
| Annualized spike | One good week times 52 | Check the period behind the run rate | H2 / K4 |
| Double counting | The same revenue credited to two levers | Sum the levers against the stated total | K4 / H6 |
| Unit or period drift | Monthly cost against annual benefit | Normalize and recompute | Q3, or K4 if it flips the answer |
| Precision theater | Decimals on a small sample | Check the sample size | Q4 |
| Flattering window | Compared to the worst month on record | Look for the default comparison period | H8 |

### Logic

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Correlation as cause | "Members spend 2x, so membership drives spend" | Ask whether big spenders were the ones who joined | H2 |
| Sample as everyone | Five interviews become "customers want" | Find the sample size | H2 |
| Survivorship | Only the customers who stayed were surveyed | Ask who was left out | H2 |
| No counterfactual | "Revenue rose 12% after launch" | Ask what it would have done anyway | H2 |
| Impossible sequence | Phase 2 needs an output from Phase 3 | Walk the timeline in order | K4 / H5 |

### Belief

Run these without a source and without a search. They're your own read.

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Straight-face failure | A result far outside anything this team, product or market has produced | Compare it to the best real outcome you know of, inside the document or outside it | K8 |
| Cited but absurd | A real source attached to a conclusion it doesn't reach | Read what the source actually measured | K8 / H1 |
| Too clean | Every number round, every risk tidily mitigated, no mess anywhere | Ask what the messy version looks like, and why none of it appears | H10 / H11 |
| Unexamined premise | "Since customers obviously want X…" | Ask what's left of the argument if the premise is false | H11 |
| Definitive on a judgment call | "The right approach is…" on a genuine fork | Look for the alternatives considered and why they lost | H10 |
| Settled language on open work | "proven", "validated", "we know", on a pilot or an estimate | Find what closed the question. If nothing did, it's open. | H10 |

### Blockers and constraints

The document says something can't happen. Check whether that's true before the plan bends around it.

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| False blocker | "We can't ship until legal signs off", where nothing requires it | Find the rule, owner or system that actually imposes it | K9 / H12 |
| Invented requirement | "The platform requires…", "Policy says…", with no policy named | Name the policy and read it | K9 / H12 |
| Phantom dependency | A blocking handoff to a team that was never asked | Check whether the dependency was ever raised with that team | H12 / H5 |
| Blocker as excuse | A missed date explained by a blocker that cleared weeks ago | Date the blocker against the timeline | K9 |
| Unblocked as claimed | "Unblocked", "done", "approved", on something still open | Find the evidence it actually cleared | K1 / H3 |
| Constraint with no owner | "We only have two engineers" with no decision behind it | Ask who set the limit and whether it can move | H12 |

### Claims about the world

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Stale premise | "No competitor offers this" | Search for current offers as of today | K5 |
| Unproven superlative | "The only platform built for…" | Search for counterexamples | H4, or K7 in public copy |
| Borrowed authority | "Research shows…" with no citation | Find the actual study and what it measured | K2 / H1 |

### The ask and the plan

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Missing price tag | "We recommend investing in…" with no amount | Find the amount, owner and date | K3 |
| One-sided ledger | Benefits listed, costs absent | Look for cost, effort, and what gets dropped | H5 |
| Hidden dependency | Needs a team or system that's committed elsewhere | List what has to be true for the plan to start | H5 |
| No finish line | No metric or date that says it worked | Look for the success measure | H5 / Q5 |

### Voice

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Forecast as fact | "This will deliver $2M" | Is the source a plan or a result? | H2 |
| Softened bad news | "Came in below expectations" for a 30% miss | Find the actual number | H7 |
| Insider language | Acronyms the reader won't know | Picture the least-briefed reader in the room | Q2 |
| Certainty borrowed from nowhere | "Clearly", "obviously", "without question", on a contested point | Ask what makes it obvious. If nothing does, the word is doing the work. | H10 |

### Clarity and bloat

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Can't say it back | You've read it twice and still can't state the point in one line | Try writing that line. If you can't, neither can the reader. | K10 / H13 |
| Buried point | The ask arrives on page 3 | Find the first sentence that states the ask | K10 / Q5 |
| Throat-clearing | Two paragraphs of context before anything is claimed | Delete the opening and check what's lost | Q7 / H13 |
| Said three times | The same point in the summary, the body and the close | Count the restatements | H13 / Q7 |
| Vague quantifier | "significantly improved", "a number of customers" | Ask for the number. If it exists, it belongs there. | Q8 |
| Abstraction stack | A sentence of nouns with no actor | Ask who does what to whom | Q9 |
| Hedge pile | "could potentially help to possibly improve" | Say what's actually claimed | Q6 |

### AI overwriting

Prose that was composed rather than thought through. Hunt the shape, not the author.

| Pattern | Looks like | Check | Usually |
|---|---|---|---|
| Symmetrical scaffolding | Three sections, three bullets each, every bullet the same length | Ask whether the content really divides that evenly | H14 |
| Filler transitions | "It's worth noting", "Importantly", "In today's landscape" | Delete them and check nothing is lost | Q7 / H14 |
| Substitution test | Swap in a competitor's name and it still reads true | Run the swap | H14 |
| Confident and empty | Strong verbs with no object: "drives meaningful impact" | Ask impact on what, measured how | H14 / H10 |
| Polish over substance | Reads beautifully, says little | Strip it to claims and count them | H13 / H14 |
| Restated brief | The document answers the ask by restating the ask | Compare it to the original request | H13 |

**Bloat is a defect only when it costs the reader.** Prose you'd have written differently is taste; drop it. The test is whether the point is harder to find, not whether the sentences are longer than yours.

## 8. Worked examples

Each example states the grade, the code, and why it isn't one level higher or lower.

### kill

**"The new SMS welcome flow will grow loyalty sign-ups from 15% to 30% of first-time buyers."** (p. 2)
Page 1 says 20% of first-time buyers opt in to texts, and the best campaign on page 3 converted 40% of the people who got it. If the flow only reaches people who opt in, 30% overall needs about 90% of them to sign up (0.20 × 90% + 0.80 × 15% = 30%). Nothing in the document gets close to 90%.
Grade E: the document's own figures can't reach its forecast. `kill · K4`. It's the headline number and the reason for the ask. Not merely hurt, because the corrected figure changes the ask.

**"No national retailer offers free in-home consultations."** (exec summary)
A major competitor launched free in-home consultations this spring, with a dated announcement.
`kill · K5`. The whole proposal is built on the gap. Not hurt, because the premise itself is gone, not just weakened.

**"Moving to the new stack will cut support tickets by 60% in the first quarter."** (p. 1)
No source, and none needed to reject it: a platform migration raises tickets before it lowers them, and nothing in the document names a ticket driver the migration removes.
Believability: doesn't pass. `kill · K8`. Not K2, because the problem isn't the missing citation — a citation wouldn't fix it. The reader stops trusting the rest of the page here.

**"We can't launch in Q3 because the brand refresh has to ship first."** (timeline slide)
Nothing ties launch to the refresh. The dependency was assumed, never agreed, and the refresh team has no date for it.
`kill · K9`. The whole ask is a quarter's delay resting on this. Not H12, because the delay is the ask.

**"This document outlines our strategic approach to the evolving landscape and the initiatives we believe will position us for sustainable growth."** (the opening, and the closest thing to a thesis in nine pages)
Nine pages, four initiatives, no recommendation, no amount, no owner. A cold reader finishes it unable to say what decision is wanted.
`kill · K10`. Not H13, because there's no buried point to dig out — there's no point.

### hurt

**"Customers love the new checkout. NPS is up 12 points."** (slide 3)
The NPS survey goes to every customer and asks about the brand overall, not about checkout.
`hurt · H1`. Sideways source on a claim that supports the rollout. Not kill, because the conversion data on slide 5 also supports the rollout and is sound.

**"We're the only scheduling tool built for small clinics."** (internal strategy doc)
Two direct competitors say the same thing on their homepages.
`hurt · H4`. Not kill internally, because nothing is decided on it. The same line on the public homepage is `kill · K7`.

**"Research validates that self-serve onboarding is the right model for this segment."** (p. 4)
The research is six user interviews, all with customers who already self-served. It's a reasonable direction, stated as a closed question.
`hurt · H10`. Not K8, because the direction is believable — only the certainty is wrong. The fix is to call it a bet and name what would prove it.

**"Enterprise buyers in this category expect SSO on day one, so SSO leads the roadmap."** (roadmap doc)
Nothing establishes the expectation. The entire sequencing argument rests on it, and it's never examined.
`hurt · H11`. Not K8, because it's plausible — plenty of enterprise buyers do. Not K2, because the defect is the unexamined premise, not the missing citation.

**Three pages of context before the recommendation on page 4.** (exec memo)
The recommendation is sound and the evidence is there. An exec reading the first page learns nothing they can act on.
`hurt · H13`. Not K10, because the point does land eventually. Not Q5, because the problem is three pages of material, not a misplaced line.

**"Our platform leverages best-in-class capabilities to drive meaningful outcomes across the customer journey."** (the product section, in full)
Swap in any competitor's name and it still reads true. No capability named, no outcome measured.
`hurt · H14`. Not a note, because this is the section meant to say what the product does.

### quick

**"CAC: $42"** (p. 1) vs. **"CAC: $44"** (appendix)
The appendix is the newer pull, and the $2 gap doesn't change the payback conclusion.
`quick · Q1`. Not H6, because H6 needs a difference that matters. It stays a flag because a finance reader will ask which one is right.

**"Q3 NRR held at 104%."** (store-ops audience)
This audience doesn't use "NRR".
`quick · Q2`. Define it in five words on first use.

**"Adoption improved significantly after the redesign."** (p. 2)
The dashboard figure is in the appendix: 11% to 19%.
`quick · Q8`. The number exists and is better than the adjective. Not H13, because one line changes it.

### note

"As we discussed above" with nothing above it. A heading style that changes halfway through. Neither changes what the reader believes or does.

### drop

- "I'd lead with the customer story." That's taste.
- "The market study doesn't mention this risk, so it's contradicted." Silence isn't contradiction.
- "The plan ignores international expansion." The document never claims to cover it, and the goal doesn't include it.
- "These sentences are longer than they need to be." The point is easy to find anyway. Bloat counts when it costs the reader, not when it offends you.

## 9. Calibration before publishing

- **Every flag has a code** in the ledger. No code, no flag.
- **The source-bias check:** read your own flag list. If every flag is a complaint about citations, you ran half the review. Go back for belief (section 3), blockers, and clarity.
- **The one-line test:** state the document's point in one line without looking at it. If you can't, that's `K10` or `H13`, and it outranks most of what else you found.
- **Inflation check:** would the deciding reader actually say no over this one thing? If you have to argue for it, it's `hurt`.
- **Deflation check:** if the reader found it and you'd rated it `quick`, would you be embarrassed? Then move it up.
- **More than two kills?** Check that each would stop the decision on its own. Merge the ones with the same root cause.
- **Verdict matches the flags:** stop only with at least one kill for that audience; go only with no kill, hurt or quick flags.
- **An empty flag list on sound work is a real result.** Don't pad it.
