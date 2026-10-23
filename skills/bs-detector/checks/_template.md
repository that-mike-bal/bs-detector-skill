---
name: example-check
summary: One line saying what this check catches.
signals: none
---

Copy this file to `checks/<name>.md`, keep every heading, and fill each section in a few lines. The skill skips files whose names start with `_`. Add an eval case under `evals/checks/<name>/` in the same change. `signals` lists the `measure.py` fields this check may cite, comma-separated, or `none`.

## Look for

What the problem looks like on the page. Two to five concrete shapes.

## How to tell

The test you run to confirm it, in a sentence or two.

## Not this

What looks similar but isn't a finding. Prose you'd have written differently is taste, and taste never counts.

## When it's worst

What makes it **stops it**, **costs trust**, or **slows the reader**.

## How it reads

One example line in the readout, in the brand's voice.
