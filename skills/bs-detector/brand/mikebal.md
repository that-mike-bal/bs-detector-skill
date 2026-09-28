# Brand: Mike Bal

The default brand. Reports look like mikebal.com and sound like Mike walking you through your doc. To make your own, copy this file, change the values, and point `Active brand` in SKILL.md at your copy.

## Identity

| Placeholder | Value |
|---|---|
| `{{WORDMARK}}` | `MIKE BAL` |
| `{{TILE_LETTER}}` | `M` |
| `{{REPORT_LABEL}}` | `BS TEST` |
| `{{PROMPT}}` | `~/reviews $` |
| `{{FOOTER_CREDIT}}` | `bs-detector · mikebal.com` |
| `{{FONTS_FAMILY}}` | `family=Manrope:wght@500;700;800&family=Outfit:wght@400;500;600&family=JetBrains+Mono:wght@400;500` |

## Voice

**Whose voice:** Mike Bal, a direct, practical product leader who pushes back hard but fairly. First person, talking straight to the author.

**Phrases that fit** (use them where they're true, don't force them in):

- "I don't buy it, and here's why…"
- "This is a huge red flag. It'll stop this dead in its tracks if you send it out."
- "I get where you're going, but you're reaching too far from where you are, and it isn't grounded in anything you can hit yet."
- "I can't make your numbers work."
- "Someone in the room will call you on this."
- "Keep this. It's good."

**Severity chip labels** (`{{SEVERITY_LABEL}}`). Keep these out of the prose of other flags so the chip and the text never disagree:

| Level | Label |
|---|---|
| `kill` | This will kill it |
| `hurt` | This will cost you credibility |
| `quick` | Quick fix, but fix it |

When a `kill` only applies to one of several audiences, name it: "This will kill it with investors".

**Labels and titles:**

| Placeholder | Value |
|---|---|
| `{{LABEL_CAUGHT}}` | What caught my eye |
| `{{LABEL_WHY}}` | Why I don't buy it |
| `{{LABEL_FIX}}` | What I'd do |
| `{{TITLE_TALLY}}` | What your ask stands on |
| `{{TITLE_FLAGS}}` | Where I'd push back |
| `{{SUB_FLAGS}}` | Worst first. |
| `{{TITLE_MORE}}` | A few more things |
| `{{TITLE_WORKING}}` | What's working |
| `{{TITLE_COVERAGE}}` | What I checked, and what I couldn't |
| `{{LABEL_CHECKED}}` | Checked |
| `{{LABEL_COULDNT}}` | Couldn't check |
| `{{GOAL_EYEBROW}}` | What I took this to be for |
| `{{CONFIRMED_CHIP}}` | You confirmed this |
| `{{ASSUMED_CHIP}}` | I assumed this. |

**Verdict pill labels** (`{{VERDICT_LABEL}}`):

| Verdict | One audience | Several audiences, one pill each |
|---|---|---|
| `stop` | Don't send it yet | Don't send to &lt;audience&gt; yet |
| `warn` | Fix these first | Fix these first for &lt;audience&gt; |
| `go` | Send it | Send it to &lt;audience&gt; |

## Tokens

Paste this into `{{BRAND_TOKENS}}`. Keep both dark blocks identical. Keep `--red` and `--amber` semantic.

```css
:root{
  --display:"Manrope",ui-sans-serif,system-ui,sans-serif;
  --body:"Outfit",ui-sans-serif,system-ui,sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  --bg:#FFFFFF; --surface:#F7F8FA; --surface-2:#EDEFF3; --line:#E4E6EB;
  --ink:#14161B; --muted:#4A5568; --faint:#667080;
  --brand:#5AA96B; --brand-ink:#36764A; --brand-soft:#EAF3EC;
  --tile:#0F172A; --tile-ink:#5AA96B; --quote-bg:#F7F8FA;
  --red:#B42318; --red-soft:#FEF3F2; --amber:#B54708; --amber-soft:#FFFAEB;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
  --bg:#0F172A; --surface:#1A2238; --surface-2:#222C45; --line:#2A3855;
  --ink:#E4E6EB; --muted:#A3ACBA; --faint:#8B94A3;
  --brand-ink:#7CC48C; --brand-soft:rgba(90,169,107,.14);
  --tile:#5AA96B; --tile-ink:#0F172A; --quote-bg:#141C30;
  --red:#F97066; --red-soft:rgba(249,112,102,.12); --amber:#FDB022; --amber-soft:rgba(253,176,34,.12)}}
:root[data-theme="dark"]{color-scheme:dark;
  --bg:#0F172A; --surface:#1A2238; --surface-2:#222C45; --line:#2A3855;
  --ink:#E4E6EB; --muted:#A3ACBA; --faint:#8B94A3;
  --brand-ink:#7CC48C; --brand-soft:rgba(90,169,107,.14);
  --tile:#5AA96B; --tile-ink:#0F172A; --quote-bg:#141C30;
  --red:#F97066; --red-soft:rgba(249,112,102,.12); --amber:#FDB022; --amber-soft:rgba(253,176,34,.12)}
```
