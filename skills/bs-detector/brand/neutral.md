# Brand: Neutral

No name, no logo, system fonts, slate and blue. Use it when a readout shouldn't carry anyone's brand, or as the starting point for your own.

## Voice

**Whose voice:** a plain, experienced reviewer. First person, talking to the author, with no signature phrases.

**Phrases that fit:**

- "I don't think this holds up, and here's why…"
- "I don't find this credible, and I don't think your reader will either."
- "This isn't clear enough. After two passes I still can't state what you're asking for."
- "Three paragraphs for one point. Keep the point."
- "This is well written and says very little."
- "This is treated as a blocker, and nothing here shows that it is one."
- "I can't get your numbers to add up."
- "This part works. Keep it."

## Readout labels

| Placeholder | Value |
|---|---|
| `{{VERDICT_STOP}}` | Not ready to send |
| `{{VERDICT_WARN}}` | Fix these first |
| `{{VERDICT_GO}}` | Ready to send |
| `{{LABEL_READ}}` | Reading this as |
| `{{LABEL_SAYS}}` | What it seems to say |
| `{{LABEL_SHOULD}}` | What it should say |
| `{{LABEL_LENGTH}}` | Length |
| `{{LABEL_FIX_FIRST}}` | Fix first |
| `{{LABEL_CHECKED}}` | Checked against |
| `{{LABEL_NO_CONTEXT}}` | No org context was available to check this against. |
| `{{REVIEWER_OPENER}}` | To {author}, re: {doc} |
| `{{LEVEL_STOPS}}` | Blocks it |
| `{{LEVEL_COSTS}}` | Costs trust |
| `{{LEVEL_SLOWS}}` | Slows the reader |

## Page identity

| Placeholder | Value |
|---|---|
| `{{WORDMARK}}` | `BS TEST` |
| `{{TILE_LETTER}}` | none. Delete the tile `<div>`. |
| `{{REPORT_LABEL}}` | empty. Delete the `<span>` inside `.word`. |
| `{{PROMPT}}` | `$` |
| `{{FOOTER_CREDIT}}` | `bs-detector` |
| `{{FONTS_FAMILY}}` | none. Delete the two `preconnect` links and the Google Fonts stylesheet link. |

## Tokens

Paste this into `{{BRAND_TOKENS}}`. Keep both dark blocks identical. Keep `--red` and `--amber` for "stops it" and "costs trust".

```css
:root{
  --display:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --body:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --bg:#FFFFFF; --surface:#F8FAFC; --surface-2:#EEF1F5; --line:#E2E8F0;
  --ink:#0F172A; --muted:#475569; --faint:#5B6474;
  --brand:#3B6EF0; --brand-ink:#1D4ED8; --brand-soft:#EEF3FF;
  --tile:#0F172A; --tile-ink:#FFFFFF; --quote-bg:#F8FAFC;
  --red:#B42318; --red-soft:#FEF3F2; --amber:#B54708; --amber-soft:#FFFAEB;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
  --bg:#0B1220; --surface:#162033; --surface-2:#1E2A40; --line:#26334D;
  --ink:#E2E8F0; --muted:#A7B1C2; --faint:#94A3B8;
  --brand-ink:#93B4FF; --brand-soft:rgba(59,110,240,.16);
  --tile:#93B4FF; --tile-ink:#0B1220; --quote-bg:#111A2B;
  --red:#F97066; --red-soft:rgba(249,112,102,.12); --amber:#FDB022; --amber-soft:rgba(253,176,34,.12)}}
:root[data-theme="dark"]{color-scheme:dark;
  --bg:#0B1220; --surface:#162033; --surface-2:#1E2A40; --line:#26334D;
  --ink:#E2E8F0; --muted:#A7B1C2; --faint:#94A3B8;
  --brand-ink:#93B4FF; --brand-soft:rgba(59,110,240,.16);
  --tile:#93B4FF; --tile-ink:#0B1220; --quote-bg:#111A2B;
  --red:#F97066; --red-soft:rgba(249,112,102,.12); --amber:#FDB022; --amber-soft:rgba(253,176,34,.12)}
```
