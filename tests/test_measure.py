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
    def test_counts_words_and_pages(self):
        result = measure.measure(words_of(1000))
        self.assertEqual(result["words"], 1000)
        self.assertEqual(result["pages"], 2.0)

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


class SentenceLoad(unittest.TestCase):
    def test_average_and_long_share_are_exact(self):
        thirty = " ".join("w{}".format(i) for i in range(30)) + "."
        thirty_one = " ".join("x{}".format(i) for i in range(31)) + "."
        result = measure.measure(thirty + " " + thirty_one)
        self.assertEqual(result["avg_sentence_words"], 30.5)
        self.assertEqual(result["long_sentence_share"], 0.5)

    def test_reading_minutes_is_exact(self):
        self.assertEqual(measure.measure(words_of(1000))["reading_minutes"], round(1000 / 238, 1))


class FillerOverlap(unittest.TestCase):
    def test_nested_phrases_count_once(self):
        result = measure.measure("We need to delve into the churn data before Friday.")
        self.assertEqual(result["filler"]["found"], [{"phrase": "delve into", "count": 1}])

    def test_overlapping_phrases_count_once(self):
        result = measure.measure("Teams harness the power of shared dashboards every day.")
        total = sum(f["count"] for f in result["filler"]["found"])
        self.assertEqual(total, 1, result["filler"]["found"])


class AskMarkers(unittest.TestCase):
    def test_each_marker_is_detected(self):
        for sentence in (
            "We recommend a pilot.",
            "I propose a pilot.",
            "Our recommendation is a pilot.",
            "Ask: approve the pilot budget.",
            "Recommendation: run the pilot.",
            "Please approve the pilot budget.",
            "We need a decision by Friday.",
            "We should run the pilot.",
        ):
            with self.subTest(sentence=sentence):
                self.assertIsNotNone(measure.measure(sentence)["ask_position"])

    def test_negations_and_background_are_not_asks(self):
        for sentence in (
            "We should not change the pricing page.",
            "The board approved the budget last year.",
            "Do not approve of shortcuts in the plan.",
        ):
            with self.subTest(sentence=sentence):
                self.assertIsNone(measure.measure(sentence)["ask_position"])

    def test_ask_in_a_heading_is_found(self):
        text = words_of(100, seed="a") + "\n\n## The ask\n\nFund the pilot at $10,000 this quarter.\n"
        position = measure.measure(text)["ask_position"]
        self.assertIsNotNone(position)
        self.assertAlmostEqual(position, 100 / 110, places=2)


class MarkdownEdges(unittest.TestCase):
    def test_table_rows_are_separate_sentences(self):
        text = (
            "| Plan | Requests per minute | Burst |\n"
            "|---|---|---|\n"
            "| Free | 60 | 5 |\n"
            "| Team | 600 | 20 |\n"
        )
        result = measure.measure(text)
        self.assertEqual(result["sentences"], 3)
        self.assertEqual(result["long_sentence_share"], 0)

    def test_unclosed_fence_keeps_the_rest_of_the_doc(self):
        text = "Intro text here.\n\n```\nThis fence never closes. Words still count.\n"
        self.assertEqual(measure.measure(text)["words"], 10)

    def test_yaml_frontmatter_is_skipped(self):
        text = "---\ntitle: Pricing review\nowner: Dana\n---\n\nOne two three.\n"
        result = measure.measure(text)
        self.assertEqual(result["words"], 3)
        self.assertEqual(result["sentences"], 1)

    def test_long_line_of_brackets_is_fast(self):
        start = time.perf_counter()
        measure.measure("[" * 30000 + "\n" + "<" * 30000)
        self.assertLess(time.perf_counter() - start, 2.0)


class Decoding(unittest.TestCase):
    def test_bom_utf8_matches_plain(self):
        text = "Plain words in a short sentence."
        plain = run_cli([], stdin=text.encode("utf-8"))
        bom = run_cli([], stdin=b"\xef\xbb\xbf" + text.encode("utf-8"))
        self.assertEqual(json.loads(plain.stdout), json.loads(bom.stdout))

    def test_utf16_is_text(self):
        result = run_cli([], stdin="Plain words in a short sentence.".encode("utf-16"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["words"], 6)

    def test_cp1252_is_text(self):
        result = run_cli([], stdin="Café “quoted” words.".encode("cp1252"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["words"], 3)

    def test_help_and_bad_arguments(self):
        help_run = run_cli(["--help"])
        self.assertEqual(help_run.returncode, 0)
        self.assertIn(b"Usage", help_run.stdout)
        self.assertNotEqual(run_cli(["a.md", "b.md"]).returncode, 0)


class Performance(unittest.TestCase):
    def test_sixty_page_doc_is_fast(self):
        text = (FILLER_WORDS + " ") * 600  # about 30,000 words
        start = time.perf_counter()
        result = measure.measure(text)
        elapsed = time.perf_counter() - start
        self.assertGreater(result["words"], 25000)
        # Generous so a slow shared CI runner doesn't flake; locally this takes well under a second.
        self.assertLess(elapsed, 5.0)


if __name__ == "__main__":
    unittest.main()
