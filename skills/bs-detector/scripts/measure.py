#!/usr/bin/env python3
"""Measure what a reader will feel in a document.

Prints one JSON object of countable signals: length, sentence load,
repetition, filler phrases, and how far in the ask first appears.
bs-detector cites these as evidence. They are never a verdict on their own.
Heuristics are tuned for English.

Usage: python3 measure.py [FILE]    reads stdin when FILE is omitted or "-"
Standard library only. Python 3.8+.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

WORDS_PER_PAGE = 500
WORDS_PER_MINUTE = 238
LONG_SENTENCE_WORDS = 30

# A sentence repeats an earlier one when most of its content 3-grams already appeared.
REPEAT_SHINGLE = 3
REPEAT_MIN_SHINGLES = 2
REPEAT_SEEN_SHARE = 0.6

# A phrase is "repeated" when a 4-gram run shows up this many times.
PHRASE_GRAM = 4
PHRASE_MIN_COUNT = 3
TOP_PHRASES = 5

FILLER_FILE = Path(__file__).with_name("filler-phrases.txt")

STOPWORDS = frozenset(
    "a an and are as at be been but by can do does for from had has have how i if in into is it "
    "its of on or our so than that the their them then there these they this those to was we "
    "were what when where which who why will with you your not no".split()
)

ASK_MARKERS = re.compile(
    r"\b(?:we|i)\s+(?:recommend|propose|suggest|request)\b"
    r"|\bour\s+recommendation\b"
    r"|\bthe\s+ask\b"
    r"|\bwe\s+(?:are\s+asking|need\s+(?:you|your|approval|a\s+decision))\b"
    r"|\bapprove\b"
    r"|\bwe\s+should\b",
    re.IGNORECASE,
)

WORD = re.compile(r"[^\W_]+(?:['\-][^\W_]+)*")
FENCE = re.compile(r"^\s{0,3}(```|~~~)")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
RULE = re.compile(r"^\s{0,3}(?:[-*_]\s*){3,}$")
LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
TAG = re.compile(r"<[^>]+>")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def _clean(line: str) -> str:
    line = LINK.sub(r"\1", line)
    line = TAG.sub(" ", line)
    line = line.replace("’", "'").replace("‘", "'")
    for mark in ("*", "`", "~", "|", ">"):
        line = line.replace(mark, " ")
    return line


def _segments(text: str):
    """Yield ("heading" | "block", text) in document order, with markdown syntax removed."""
    in_fence = False
    block = []
    for raw in text.splitlines():
        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not raw.strip() or RULE.match(raw):
            if block:
                yield "block", " ".join(block)
                block = []
            continue
        heading = HEADING.match(raw)
        if heading:
            if block:
                yield "block", " ".join(block)
                block = []
            yield "heading", _clean(heading.group(1))
            continue
        if LIST_ITEM.match(raw):
            if block:
                yield "block", " ".join(block)
                block = []
            raw = LIST_ITEM.sub("", raw, count=1)
        block.append(_clean(raw))
    if block:
        yield "block", " ".join(block)


def _words(text: str):
    return WORD.findall(text)


def load_filler_phrases(path: Path = FILLER_FILE):
    if not path.exists():
        return []
    phrases = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip().lower().replace("’", "'")
        if line and not line.startswith("#"):
            phrases.append(line)
    return phrases


def _repetition(sentence_tokens):
    seen = set()
    repeated = 0
    for tokens in sentence_tokens:
        content = [t for t in tokens if t not in STOPWORDS]
        shingles = [tuple(content[i:i + REPEAT_SHINGLE]) for i in range(len(content) - REPEAT_SHINGLE + 1)]
        if len(shingles) >= REPEAT_MIN_SHINGLES:
            if sum(1 for s in shingles if s in seen) / len(shingles) >= REPEAT_SEEN_SHARE:
                repeated += 1
        seen.update(shingles)
    return repeated


def _repeated_phrases(sentence_tokens):
    grams = Counter()
    for tokens in sentence_tokens:
        for i in range(len(tokens) - PHRASE_GRAM + 1):
            grams[tuple(tokens[i:i + PHRASE_GRAM])] += 1

    phrases = Counter()
    for tokens in sentence_tokens:
        run_start = None
        for i in range(len(tokens) - PHRASE_GRAM + 2):
            gram = tuple(tokens[i:i + PHRASE_GRAM])
            hot = (
                len(gram) == PHRASE_GRAM
                and grams[gram] >= PHRASE_MIN_COUNT
                and not all(t in STOPWORDS for t in gram)
            )
            if hot and run_start is None:
                run_start = i
            elif not hot and run_start is not None:
                phrases[" ".join(tokens[run_start:i - 1 + PHRASE_GRAM])] += 1
                run_start = None

    chosen = []
    for phrase, count in sorted(phrases.items(), key=lambda kv: (-kv[1], -len(kv[0]))):
        if count < PHRASE_MIN_COUNT or any(phrase in c["phrase"] for c in chosen):
            continue
        chosen.append({"phrase": phrase, "count": count})
        if len(chosen) == TOP_PHRASES:
            break
    return chosen


def _filler(text: str, total_words: int, phrases):
    lowered = text.lower()
    found = []
    for phrase in phrases:
        pattern = r"(?<![\w'])" + re.escape(phrase) + r"(?![\w'])"
        count = len(re.findall(pattern, lowered))
        if count:
            found.append({"phrase": phrase, "count": count})
    found.sort(key=lambda f: (-f["count"], f["phrase"]))
    hits = sum(f["count"] for f in found)
    rate = round(hits / total_words * 1000, 1) if total_words else 0.0
    return {"per_1000_words": rate, "found": found}


def measure(text: str, filler_phrases=None) -> dict:
    if filler_phrases is None:
        filler_phrases = load_filler_phrases()

    sentences = []
    total_words = 0
    ask_offset = None
    kept = []
    for kind, segment in _segments(text):
        kept.append(segment)
        if kind == "heading":
            total_words += len(_words(segment))
            continue
        for piece in SENTENCE_END.split(segment):
            words = _words(piece)
            if not words:
                continue
            if ask_offset is None and ASK_MARKERS.search(piece):
                ask_offset = total_words
            sentences.append(words)
            total_words += len(words)

    sentence_tokens = [[w.lower() for w in s] for s in sentences]
    n = len(sentences)
    return {
        "words": total_words,
        "pages": round(total_words / WORDS_PER_PAGE, 1),
        "reading_minutes": round(total_words / WORDS_PER_MINUTE, 1),
        "sentences": n,
        "avg_sentence_words": round(sum(len(s) for s in sentences) / n, 1) if n else 0.0,
        "long_sentence_share": round(sum(1 for s in sentences if len(s) > LONG_SENTENCE_WORDS) / n, 3) if n else 0.0,
        "repeated_sentence_share": round(_repetition(sentence_tokens) / n, 3) if n else 0.0,
        "repeated_phrases": _repeated_phrases(sentence_tokens),
        "filler": _filler(" ".join(kept), total_words, filler_phrases),
        "ask_position": round(ask_offset / total_words, 3) if ask_offset is not None and total_words else None,
    }


def _decode(data: bytes):
    if b"\x00" in data:
        return None
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("latin-1")


def main(argv=None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args and args[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    if len(args) > 1:
        print("measure.py: give one file, or none to read stdin", file=sys.stderr)
        return 2
    path = args[0] if args else "-"
    try:
        data = sys.stdin.buffer.read() if path == "-" else Path(path).read_bytes()
    except OSError as err:
        print("measure.py: can't read {}: {}".format(path, err.strerror or err), file=sys.stderr)
        return 2
    text = _decode(data)
    if text is None:
        print("measure.py: input is not text; extract the text first", file=sys.stderr)
        return 2
    print(json.dumps(measure(text), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
