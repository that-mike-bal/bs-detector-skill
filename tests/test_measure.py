"""Tests for skills/bs-detector/scripts/measure.py. Standard library only."""
import importlib.util
import json
import subprocess
import sys
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "bs-detector" / "scripts" / "measure.py"

_spec = importlib.util.spec_from_file_location("measure", SCRIPT)
measure = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(measure)

FILLER_WORDS = (
    "Teams ship work when owners know the goal and the date. "
    "Our support queue grew after the pricing change in March. "
    "Most tickets asked how seats are counted on annual plans. "
    "The billing page explains monthly plans but skips annual ones. "
    "Sales also answers the same seat question several times a week. "
)


def words_of(n, seed="plain"):
    """n distinct-ish words in short sentences, no filler, no ask markers."""
    out = []
    i = 0
    while len(out) < n:
        out.append("{}{}".format(seed, i))
        i += 1
    sentences = []
    for start in range(0, n, 10):
        chunk = out[start:start + 10]
        sentences.append(" ".join(chunk) + ".")
    return " ".join(sentences)


def run_cli(args, stdin=None):
    return subprocess.run(
        [sys.executable, str(SCRIPT)] + args,
        input=stdin,
        capture_output=True,
    )


class LengthSignals(unittest.TestCase):
    def test_counts_words_pages_and_reading_time(self):
        result = measure.measure(words_of(1000))
        self.assertEqual(result["words"], 1000)
        self.assertAlmostEqual(result["pages"], 2.0, places=1)
        self.assertLessEqual(abs(result["reading_minutes"] - 1000 / 238), 1)

    def test_markdown_syntax_is_not_counted(self):
        text = (
            "# Title\n\n"
            "One two three.\n\n"
            "- four five six.\n"
            "* seven eight nine.\n\n"
            "```\nnot counted at all\n```\n"
        )
        result = measure.measure(text)
        # Title (1) + three sentences of three words; markers and the code block are ignored.
        self.assertEqual(result["words"], 10)
        self.assertEqual(result["sentences"], 3)

    def test_empty_input_returns_zeros_and_nulls(self):
        result = measure.measure("")
        self.assertEqual(result["words"], 0)
        self.assertEqual(result["sentences"], 0)
        self.assertEqual(result["repeated_sentence_share"], 0)
        self.assertIsNone(result["ask_position"])
        self.assertEqual(result["filler"]["found"], [])


class RepetitionSignals(unittest.TestCase):
    def test_repeated_sentence_is_detected_and_listed(self):
        repeated = "Customers want a single dashboard that shows every renewal date."
        text = " ".join([repeated, FILLER_WORDS, repeated, FILLER_WORDS, repeated])
        result = measure.measure(text)
        self.assertGreater(result["repeated_sentence_share"], 0)
        phrases = [p["phrase"] for p in result["repeated_phrases"]]
        self.assertTrue(
            any("single dashboard that shows every renewal date" in p for p in phrases),
            phrases,
        )

    def test_distinct_sentences_are_not_repetition(self):
        result = measure.measure(FILLER_WORDS)
        self.assertEqual(result["repeated_sentence_share"], 0)
        self.assertEqual(result["repeated_phrases"], [])


class FillerSignals(unittest.TestCase):
    def test_filler_phrases_are_found_and_rated(self):
        text = (
            "It's worth noting that churn fell. "
            "In today's landscape, buyers compare tools quickly. "
            + FILLER_WORDS
        )
        result = measure.measure(text)
        found = {f["phrase"] for f in result["filler"]["found"]}
        self.assertIn("it's worth noting", found)
        self.assertIn("in today's landscape", found)
        expected_rate = round(2 / result["words"] * 1000, 1)
        self.assertEqual(result["filler"]["per_1000_words"], expected_rate)

    def test_curly_apostrophes_still_match(self):
        result = measure.measure("It’s worth noting that churn fell.")
        found = {f["phrase"] for f in result["filler"]["found"]}
        self.assertIn("it's worth noting", found)


class AskPosition(unittest.TestCase):
    def test_ask_late_in_the_doc(self):
        before = words_of(700, seed="a")
        after = words_of(290, seed="b")
        text = before + " We recommend raising Pro to $49 in Q3. " + after
        result = measure.measure(text)
        self.assertIsNotNone(result["ask_position"])
        self.assertGreaterEqual(result["ask_position"], 0.65)
        self.assertLessEqual(result["ask_position"], 0.75)

    def test_no_ask_markers_gives_null(self):
        self.assertIsNone(measure.measure(FILLER_WORDS)["ask_position"])


class CommandLine(unittest.TestCase):
    def test_stdin_matches_file_input(self):
        text = FILLER_WORDS + " We recommend a pilot."
        tmp = ROOT / "tests" / "_tmp_measure_input.md"
        tmp.write_text(text, encoding="utf-8")
        try:
            from_file = run_cli([str(tmp)])
            from_stdin = run_cli([], stdin=text.encode("utf-8"))
        finally:
            tmp.unlink()
        self.assertEqual(from_file.returncode, 0, from_file.stderr)
        self.assertEqual(from_stdin.returncode, 0, from_stdin.stderr)
        self.assertEqual(json.loads(from_file.stdout), json.loads(from_stdin.stdout))

    def test_binary_input_fails_with_one_line_message(self):
        png = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00"
        result = run_cli([], stdin=png)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")
        self.assertEqual(len(result.stderr.decode().strip().splitlines()), 1)

    def test_missing_file_fails_cleanly(self):
        result = run_cli(["does-not-exist.md"])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(len(result.stderr.decode().strip().splitlines()), 1)


class Performance(unittest.TestCase):
    def test_sixty_page_doc_is_fast(self):
        text = (FILLER_WORDS + " ") * 600  # about 30,000 words
        start = time.perf_counter()
        result = measure.measure(text)
        elapsed = time.perf_counter() - start
        self.assertGreater(result["words"], 25000)
        self.assertLess(elapsed, 2.0)


if __name__ == "__main__":
    unittest.main()
