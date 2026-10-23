"""Shape tests for skills/bs-detector/checks/. Standard library only.

A check is a contract with contributors: the skill reads every non-underscore
file in checks/, so a malformed one degrades every review. These tests fail
with the file and the missing piece named.
"""
import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKS = ROOT / "skills" / "bs-detector" / "checks"
MEASURE = ROOT / "skills" / "bs-detector" / "scripts" / "measure.py"

REQUIRED_KEYS = ("name", "summary", "signals")
REQUIRED_SECTIONS = ("Look for", "How to tell", "Not this", "When it's worst", "How it reads")
LEVELS = ("stops it", "costs trust", "slows the reader")


def _measure_fields():
    spec = importlib.util.spec_from_file_location("measure", MEASURE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return set(module.measure("").keys())


def parse(path: Path):
    """Return (frontmatter dict, list of H2 section titles, body text)."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        return {}, [], text
    meta = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    body = match.group(2)
    sections = re.findall(r"^## (.+?)\s*$", body, re.MULTILINE)
    return meta, sections, body


def check_errors(path: Path, measure_fields=None):
    """Every problem with one check file, as readable strings."""
    errors = []
    meta, sections, body = parse(path)
    if not meta:
        return ["{}: missing frontmatter".format(path.name)]
    for key in REQUIRED_KEYS:
        if not meta.get(key):
            errors.append("{}: frontmatter is missing '{}'".format(path.name, key))
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            errors.append("{}: missing section '## {}'".format(path.name, section))
    if not path.name.startswith("_"):
        if meta.get("name") and meta["name"] != path.stem:
            errors.append("{}: name '{}' should match the filename".format(path.name, meta["name"]))
        worst = body.split("## When it's worst", 1)[-1].split("\n## ", 1)[0].lower()
        if "## When it's worst" in body and not any(level in worst for level in LEVELS):
            errors.append("{}: 'When it's worst' names none of: {}".format(path.name, ", ".join(LEVELS)))
        signals = meta.get("signals", "")
        if measure_fields is not None and signals and signals != "none":
            for field in (s.strip() for s in signals.split(",")):
                if field not in measure_fields:
                    errors.append("{}: signal '{}' is not a measure.py field".format(path.name, field))
    return errors


def check_files():
    return sorted(p for p in CHECKS.glob("*.md") if not p.name.startswith("_"))


class CheckLibrary(unittest.TestCase):
    def test_library_is_not_empty(self):
        self.assertTrue(check_files(), "no check files found in {}".format(CHECKS))

    def test_every_check_has_the_contract_shape(self):
        fields = _measure_fields()
        errors = [e for p in check_files() for e in check_errors(p, fields)]
        self.assertEqual(errors, [], "\n" + "\n".join(errors))

    def test_template_has_every_section(self):
        errors = check_errors(CHECKS / "_template.md")
        self.assertEqual(errors, [], "\n" + "\n".join(errors))


class Validator(unittest.TestCase):
    """The validator itself has to catch broken checks, or the tests above prove nothing."""

    def _write(self, content):
        tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        tmp.write(content)
        tmp.close()
        return Path(tmp.name)

    def test_missing_section_is_named(self):
        path = self._write(
            "---\nname: x\nsummary: s\nsignals: none\n---\n\n"
            "## Look for\n\n## How to tell\n\n## Not this\n\n## How it reads\n"
        )
        try:
            errors = check_errors(path)
        finally:
            path.unlink()
        self.assertTrue(any("When it's worst" in e and path.name in e for e in errors), errors)

    def test_unknown_signal_is_named(self):
        path = self._write(
            "---\nname: {}\nsummary: s\nsignals: words, vibes\n---\n\n"
            "## Look for\n## How to tell\n## Not this\n## When it's worst\n- **Stops it:** x\n## How it reads\n"
            .format("PLACEHOLDER")
        )
        try:
            errors = check_errors(path, {"words"})
        finally:
            path.unlink()
        self.assertTrue(any("'vibes'" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
