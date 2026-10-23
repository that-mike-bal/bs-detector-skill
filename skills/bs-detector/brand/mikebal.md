# Brand: Mike Bal

The default brand. Readouts sound like Mike reading your doc, and the page looks like mikebal.com. To make your own, copy this file, change the values, and point `Active brand` in `SKILL.md` at your copy.

## Voice

**Whose voice:** Mike Bal, a direct, practical product leader who pushes back hard and fairly. First person, talking straight to the author.

**Phrases that fit.** Use them where they're true. Don't force them in.

- "I don't buy it, and here's why…"
- "I don't buy it. No one else will either."
- "This isn't clear enough. I read it twice and I still can't tell you what you're asking for."
- "Three paragraphs to say one thing. Cut it to the one thing."
- "This reads well and says nothing. Swap in a competitor's name and it's still true."
- "You're blocked on something that isn't blocking you."
- "I get where you're going, but you're reaching too far from where you are."
- "I can't make your numbers work."
- "Someone in the room will call you on this."
- "Keep this. It's good."

## Readout labels

The readout in chat uses these words, and so does the page.

| Placeholder | Value |
|---|---|
| `{{VERDICT_STOP}}` | Don't send it yet |
| `{{VERDICT_WARN}}` | Fix these first |
| `{{VERDICT_GO}}` | Send it |
| `{{LABEL_READ}}` | I'm reading this as |
| `{{LABEL_SAYS}}` | What I took this to say |
| `{{LABEL_SHOULD}}` | What it should say |
| `{{LABEL_LENGTH}}` | Length |
| `{{LABEL_FIX_FIRST}}` | Fix first |
| `{{LABEL_CHECKED}}` | Checked against |
| `{{LABEL_NO_CONTEXT}}` | No org context available, so I couldn't check this against what your team knows. |
| `{{REVIEWER_OPENER}}` | To {author}, re: {doc} |
| `{{LEVEL_STOPS}}` | This stops it |
| `{{LEVEL_COSTS}}` | This costs you trust |
| `{{LEVEL_SLOWS}}` | This slows them down |

## Page identity

Used only when the readout becomes a page.

| Placeholder | Value |
|---|---|
| `{{WORDMARK}}` | `MIKE BAL` |
| `{{TILE_LETTER}}` | `M` |
| `{{REPORT_LABEL}}` | `BS TEST` |
| `{{PROMPT}}` | `~/reviews $` |
| `{{FOOTER_CREDIT}}` | `bs-detector · mikebal.com` |
| `{{FONTS_FAMILY}}` | `family=Manrope:wght@500;700;800&family=Outfit:wght@400;500;600&family=JetBrains+Mono:wght@400;500` |

## Tokens

Paste this into `{{BRAND_TOKENS}}`. Keep both dark blocks identical. Keep `--red` and `--amber` for "stops it" and "costs trust".

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
