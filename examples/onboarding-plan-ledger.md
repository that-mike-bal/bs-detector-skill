# Ledger: Onboarding Relaunch: Q1 Plan

Document: examples/onboarding-plan.md (explicitly fictional example)
Reviewed: 25 Sep 2026 · Full depth (exec audience, ask rests on several numbers)
Run mode: unattended (goal assumed, no checkpoint, Step 7 skipped)
Fallbacks: no subagents (lanes run in one pass, in order claims, audience, voice, evidence, breadth; Step 1 notes stand in for the blind lane); no question tool needed (unattended); no connected system of record for Ledgerly (internal figures graded X); no page publisher (local HTML file).

## Assumed goal

- What it's for: get Ledgerly's leadership team to approve the Q1 onboarding relaunch (five-email sequence plus in-app checklist).
- Who's reading it: the leadership team. They know the business and its numbers; they will do the math.
- What you want them to do: approve a January start.
- Depth: Full.
- Checked against: the document itself, the web for the one claim about the outside world. No internal sources available.
- Under a different goal: if this is an early heads-up rather than a request for sign-off, flag 01 (no price) drops from kill to hurt and the verdict moves to warn; the rest stand.

## Claims

| ID | Verbatim quote | Location | Type | Load-bearing | Grade | Checked against |
|---|---|---|---|---|---|---|
| C1 | "Ledgerly is the only bookkeeping app built for freelancers." | Summary, para 1 | Superlative | No | E | QuickBooks Solopreneur page (https://quickbooks.intuit.com/solopreneur/): "designed for self-employed individuals running a one-person business"; Xero page titled "Self-Employed Accounting Software for Freelancers" (https://www.xero.com/us/small-businesses/xero-for-self-employed/); Zapier roundup of 8 self-employed accounting apps (https://zapier.com/blog/accounting-bookkeeping-software-freelance/). Checked 25 Sep 2026. |
| C2 | "only 22% of new signups connect a bank account in their first week" | Summary, para 1 | Figure | Yes | X | Implies product analytics; not connected. Also conflicts with C10 inside the document. |
| C3 | "customers who connect a bank account are 3x more likely to still be paying after six months" | Summary, para 1 | Figure | Yes | X | Implies retention/billing data; not connected. |
| C4 | "Connecting a bank account is what keeps customers." | Summary, para 1 | Inference (correlation stated as cause) | Yes | C | Document only. C3 is a real association read as cause; nothing shows cause. |
| C5 | "The new sequence will lift first-week activation from 22% to 40% by the end of Q2." | Summary, para 2 | Forecast | Yes | U | Document's own figures: best cohort ever 35% (C8); 31% open the first email (C7). Not graded E: the checklist's reach isn't quantified, so the document's figures don't strictly rule 40% out. |
| C6 | "Signups: about 9,000 per month." | What we know | Figure | No | X | Product analytics; not connected. |
| C7 | "31% of new signups open the first onboarding email." | What we know | Figure | No | X | Email platform; not connected. |
| C8 | "our highest-activating cohort ever (the October 2025 webinar cohort) reached 35% activation." | What we know | Figure | No | X | Product analytics; not connected. |
| C9 | "Customers love the checklist idea. NPS rose from 38 to 47 after we previewed the checklist in the September newsletter." | What we know | Attributed claim + inference | Yes | C | NPS asks how likely someone is to recommend the product/company overall (Bain, https://www.bain.com/insights/introducing-the-net-promoter-system-loyalty-insights/). A rise measured after the preview is a timing link, not a checklist measure. NPS survey itself: X. |
| C10 | "Activation today: 22% (see summary). Activation for the most recent full month was 24%." | What we know | Figure | No (but it moves the baseline under C5 and C12) | X | Analytics; not connected. Internal conflict with C2. "(see summary)" cites the document itself. |
| C11 | "roughly 1,600 more activated customers every month (9,000 × 18%)" | Impact | Calculation | No | A | Recomputed: 9,000 × 0.18 = 1,620. Correct. |
| C12 | "At our average of $19 per month, that's about $365K in new annual recurring revenue (ARR) per monthly cohort." | Impact | Calculation + unstated assumption | Yes | C | Arithmetic holds (1,600 × $19 × 12 = $364,800). But it counts every newly activated signup as a paying customer for 12 months. The document never says what share of signups pay, and C3 implies activated customers still churn. Activations stand in for revenue. $19 average: X. |
| C13 | "Engineering will pick this up once the billing migration ships." | The plan, step 2 | Dependency / unstated assumption | No | D | No ship date for the billing migration anywhere in the document. Step 2 starts in week 2, so the plan assumes it ships by then. |
| C14 | "Our biggest problem is activation" | Summary, para 1 | Assertion / superlative | No | D | Nothing compares activation with other problems. |
| C15 | "We'll share final costs once the design work is scoped." | Ask | Missing figure | n/a (the ask itself) | n/a | No amount, no owner beyond "From: Growth". |

Load-bearing tally (6): A 0, B 0, C 3 (C4, C9, C12), D 0, E 0, U 1 (C5), X 2 (C2, C3).

Derived numbers (from the document's own figures only):
- 40% of 9,000 = 3,600 activated a month; 35% (best ever) = 3,150.
- 31% of 9,000 = 2,790 open the first email. If the emails carry the lift, 1,620 more activations = 58% of those openers newly connecting a bank.
- Baseline 24% instead of 22%: lift is 16 points, 9,000 × 16% = 1,440 more a month, × $19 × 12 = $328,320 (about $328K). Difference vs. the document: 160 customers a month against its stated 1,600 (180 against the unrounded 1,620), about $37K ARR per cohort.

## Findings

| ID | Claim ID or "none" | Lane | Level + code | Kept or dropped, and why |
|---|---|---|---|---|
| F1 | C15 | Audience / breadth | kill · K3 | Kept, flag 01. The ask is unpriced and has no named owner; leadership is asked to approve with costs to follow. |
| F2 | C5 | Claims / voice | hurt · H2 | Kept, flag 02. "will" on a forecast; 40% is above the best cohort ever (35%, self-selected webinar cohort); email reach math (58% of openers) not addressed. Not K2/K4: forecast grade U tops out at hurt · H2 unless the document's figures rule it out, and the checklist leg isn't quantified. Headline placement noted but can't adjust into kill. |
| F3 | C12 | Claims | hurt · H1 | Kept, flag 03. Activations stand in for paying, retained customers. Not K4: arithmetic is right and there's no cost to compare against, so I can't say the corrected number flips the answer. |
| F4 | C4, C3 | Claims / breadth | hurt · H2 | Kept, flag 04 (merged with F5 and F6: same root, association read as cause, and the plan can't test it). |
| F5 | C9 | Evidence | hurt · H1 | Merged into flag 04. NPS measures overall recommend-likelihood, not the checklist. |
| F6 | none | Breadth | hurt · H5 | Merged into flag 04. "launch to 100% of new signups" leaves no comparison group; activation already moved 22% to 24% without the relaunch. |
| F7 | C2, C10 | Claims | hurt · H6 | Kept, flag 05. Two baselines, and the gap moves the lift by about 160 customers a month and about $37K of ARR per cohort. |
| F8 | C13 | Breadth / audience | hurt · H5 | Kept, flag 06. Hidden dependency with no date; checklist build week 2 assumes the migration has shipped. |
| F9 | C1 | Evidence | hurt · H3 (H4 also fits) | Kept, flag 07. Contradicted by QuickBooks Solopreneur and Xero pages; first sentence of the summary; checkable in under a minute. Up-one adjustment can't reach kill. Not K7: internal document, not public copy. |
| F10 | C14 | Blind / voice | note | Kept, A few more things. |
| F11 | C5 | Blind | note | Kept, A few more things. Summary credits "the new sequence" alone for the lift while the plan has two parts. |
| F12 | C11 | Claims | drop | Arithmetic checks out (1,620, rounded to 1,600). $365K vs. $369K from unrounded figures is rounding, not a defect. |
| F13 | C7 | Evidence | drop | 31% open rate is an input, not used as proof of activation; no proxy-metric problem on its own. Used inside F2. |
| F14 | none | Audience | drop | No checkpoint between week 12 and the end-of-Q2 target. Structural preference; the document does name a metric and a date. |
| F15 | C10 | Blind | drop (merged) | "(see summary)" cites itself; folded into F7. |

Calibration: one kill (F1), stands on its own. Seven flags, no overflow after merging F4-F6. Verdict for the one deciding audience (leadership): stop.

## Lane notes

### Blind (Step 1 notes, standing in for the blind lane)

- Playback: Growth wants leadership to approve an onboarding relaunch (five emails plus an in-app checklist) starting in January. They say it takes first-week bank connection from 22% to 40% by end of Q2 and adds about $365K ARR per monthly cohort.
- Doesn't make sense: which is today's number, 22% or 24%? 40% beats the best cohort ever (35%); why? Summary credits "the new sequence" but the plan has two parts. When does the billing migration ship? What does it cost?
- Only makes sense if you already know: the billing migration's timeline; whether signups are paying customers or a free tier.
- Smell test: big number, no price, depends on another team's unfinished work, target above anything you've ever done.

### Claims
- Steelman: activation is a real, measurable problem; bank connection is a plausible lever for a bookkeeping app; the impact math is shown and reproducible.
- Held up: 9,000 × 18% = 1,620; 1,600 × $19 × 12 = $364,800. The plan's week sequence is internally ordered.

### Audience
- Steelman: short, decision stated at the top, clear metric and date.
- First question: what does it cost and who owns it? Question that sinks it: why should we believe 40% when the best you've ever done is 35%?
- Held up: the "Decision needed" line is unambiguous.

### Voice
- Steelman: plain, short, no jargon beyond ARR, which is defined.
- Problems: "will lift", "Customers love", "is what keeps customers", "the only". Confidence runs ahead of support throughout.

### Evidence
- Steelman: internal figures are the kind a growth team would have in its analytics.
- Held up: nothing external contradicts the internal figures; they're simply unreachable (X). The one external claim (C1) is contradicted.

### Breadth
- Steelman: a two-lever plan (email plus in-product) is a reasonable shape.
- Missing: cost and owner; billing-migration date and fallback; a comparison group; what share of activated signups pay.
