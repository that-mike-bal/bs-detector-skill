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
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
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

    def test_every_check_has_an_eval_case(self):
        evals = ROOT / "evals" / "checks"
        missing = [
            p.stem for p in check_files()
            if not (evals / p.stem / "prompt.md").exists() or not (evals / p.stem / "graders" / "criteria.md").exists()
        ]
        self.assertEqual(
            missing, [],
            "add evals/checks/<name>/prompt.md and graders/criteria.md for: " + ", ".join(missing),
        )


VALID_BODY = (
    "## Look for\n\nx\n\n## How to tell\n\nx\n\n## Not this\n\nx\n\n"
    "## When it's worst\n\n- **Stops it:** x\n\n## How it reads\n\nx\n"
)


class Validator(unittest.TestCase):
    """The validator itself has to catch broken checks, or the tests above prove nothing."""

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)

    def _write(self, name, content):
        path = Path(self.dir.name) / name
        path.write_text(content, encoding="utf-8")
        return path

    def _frontmatter(self, name="good", signals="none"):
        return "---\nname: {}\nsummary: s\nsignals: {}\n---\n\n".format(name, signals)

    def test_a_valid_check_has_no_errors(self):
        path = self._write("good.md", self._frontmatter() + VALID_BODY)
        self.assertEqual(check_errors(path, {"words"}), [])

    def test_missing_section_is_named(self):
        body = VALID_BODY.split("## When it's worst")[0] + "## How it reads\n\nx\n"
        path = self._write("good.md", self._frontmatter() + body)
        errors = check_errors(path)
        self.assertTrue(any("When it's worst" in e and "good.md" in e for e in errors), errors)

    def test_unknown_signal_is_named(self):
        path = self._write("good.md", self._frontmatter(signals="words, vibes") + VALID_BODY)
        self.assertEqual(check_errors(path, {"words"}), ["good.md: signal 'vibes' is not a measure.py field"])

    def test_name_must_match_filename(self):
        path = self._write("good.md", self._frontmatter(name="other") + VALID_BODY)
        self.assertEqual(check_errors(path), ["good.md: name 'other' should match the filename"])

    def test_worst_section_must_name_a_level(self):
        body = VALID_BODY.replace("- **Stops it:** x", "- Bad things happen.")
        path = self._write("good.md", self._frontmatter() + body)
        errors = check_errors(path)
        self.assertTrue(any("names none of" in e for e in errors), errors)

    def test_missing_frontmatter_is_named(self):
        path = self._write("good.md", VALID_BODY)
        self.assertEqual(check_errors(path), ["good.md: missing frontmatter"])

    def test_template_is_exempt_from_name_and_level_rules(self):
        path = self._write("_template.md", self._frontmatter(name="anything") + VALID_BODY.replace("Stops it", "Level"))
        self.assertEqual(check_errors(path), [])


if __name__ == "__main__":
    unittest.main()
