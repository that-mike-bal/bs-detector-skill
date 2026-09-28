# Brand: Neutral

No name, no logo, system fonts, slate and blue. Use it when a report shouldn't carry anyone's brand, or as the starting point for your own.

## Identity

| Placeholder | Value |
|---|---|
| `{{WORDMARK}}` | `BS TEST` |
| `{{TILE_LETTER}}` | none. Delete the tile `<div>`. |
| `{{REPORT_LABEL}}` | empty. Delete the `<span>` inside `.word`. |
| `{{PROMPT}}` | `$` |
| `{{FOOTER_CREDIT}}` | `bs-detector` |
| `{{FONTS_FAMILY}}` | none. Delete the two `preconnect` links and the Google Fonts stylesheet link. |

## Voice

**Whose voice:** a plain, experienced reviewer. First person, talking to the author, with no signature phrases.

**Phrases that fit:**

- "I don't think this holds up, and here's why…"
- "This one will stop the conversation if you send it as is."
- "I can't get your numbers to add up."
- "Someone reading closely will ask about this."
- "This part works. Keep it."

**Severity chip labels** (`{{SEVERITY_LABEL}}`). Keep these out of the prose of other flags so the chip and the text never disagree:

| Level | Label |
|---|---|
| `kill` | Deal-breaker |
| `hurt` | Costs you trust |
| `quick` | Quick fix |

When a `kill` only applies to one of several audiences, name it: "Deal-breaker for investors".

**Labels and titles:**

| Placeholder | Value |
|---|---|
| `{{LABEL_CAUGHT}}` | What caught my eye |
| `{{LABEL_WHY}}` | Why it doesn't hold |
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
| `go` | Ready to send | Ready for &lt;audience&gt; |

## Tokens

Paste this into `{{BRAND_TOKENS}}`. Keep both dark blocks identical. Keep `--red` and `--amber` semantic.

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
