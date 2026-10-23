# Evals

These cases test whether bs-detector does its job. They're written in Claude Code's [plugin eval format](https://code.claude.com/docs/en/plugin-evals): each case is a folder with a `prompt.md` (a realistic request with the document pasted in) and a `graders/` folder of pass/fail checks.

## What the suite proves

| Proof | Cases |
|---|---|
| It catches what's planted | `checks/`: one document per check, each with that check's problem planted in it |
| It leaves good work alone | `clean/`: a tight memo and a long reference page that should both come back "send it" |
| It plays the point back correctly | `playback/`: a buried recommendation it should lift, and a doc with no point it shouldn't invent one for |
| It behaves in both seats | `seats/`: reviewer mode, where the readout goes to the author and catches the restated brief |

`readout/` checks that one root cause becomes one point, not two.

Every case has four graders:

- `criteria`: a judge model checks the planted problem against concrete PASS and FAIL conditions.
- `readout-shape`: the readout has its playback lines.
- `five-points-max`: no more than five points.
- `skill-fired`: the skill actually ran.

The shape graders count only in the run with the plugin loaded, so the plain-Claude comparison measures substance, not formatting.

## Run it

You need Claude Code v2.1.269 or later and git 2.31 or later. Run from the repository root.

Every case runs three times with the plugin and three times without it, and every run is a real model call on your account. Start with one group:

```bash
claude plugin eval . --tag checks --threshold 0.8 --max-cost-usd 10
```

Iterate on one case cheaply with a single run and no comparison:

```bash
claude plugin eval . --case false-blockers --runs 1 --ablation none
```

Run the whole suite with pinned models before recording scores:

```bash
claude plugin eval . --threshold 0.8 --model claude-sonnet-5 --judge-model claude-sonnet-5 --max-cost-usd 40
```

Results land in `evals/results/`, which git ignores.

## Add a check's case

1. Add the check as `skills/bs-detector/checks/<name>.md`.
2. Copy any folder under `evals/checks/` to `evals/checks/<name>/`.
3. Replace the document in `prompt.md` with one that plants your check's problem, and nothing else that's dramatic.
4. Rewrite `graders/criteria.md` as one PASS line and one FAIL line naming that problem.

`tests/test_checks.py` fails until every check has a case, so CI catches a check without one.

## Not covered yet

These are checked by hand for now: org context from memory or connected tools, the unattended data claim, the measurement script versus the no-code fallback, the opening question, missing figures in the playback, and reviewer mode without a brief. Each becomes a case when it breaks.

## Latest scores

Not yet run through `claude plugin eval`, so there's no scored run and no comparison against plain Claude yet.

As a first pass, each case was given once to a fresh agent with only `SKILL.md` and the user's message, then checked against its PASS and FAIL conditions by hand. 14 of 15 passed. `no-point` failed because its "what it should say" line picked a winner the doc never chose. `SKILL.md` was tightened so the skill never decides for a doc that doesn't. After that, `no-point`, `buried-point`, `support` and the README example were run again, and all of them passed. The first pass also showed the original `long-reference-doc` fixture had real contradictions in its retry rules, which the skill caught. The fixture was fixed.
