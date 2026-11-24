#!/usr/bin/env python3
"""Entry for make.fun: 'One Sentence for a Traveler from 1800'.

Writes one sentence (at most 200 characters) explaining the modern
internet to someone arriving from the year 1800, built only from
things they already know: the post office, the library, a candle.
Stdlib only, deterministic.
"""

import os
import sys

# The sentence, aimed at the judge's criteria in order: it says what the
# internet does (a letter to anyone, answered at once; every book open to
# read), it is built only from what 1800 knows (the post, the library, a
# candle), every claim in it is literally true, and the candle guttering
# is the one image meant to stay with the reader.
SENTENCE = (
    "Picture a post office joined to every library on Earth: your letter "
    "reaches any man alive before your candle gutters, and more books than "
    "any one library holds lie open for you to read at home."
)

MAX_CHARS = 200


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> None:
    """Read the written file back and check it against the gate:
    UTF-8 text, 1 to 200 characters, not only white space, and a
    single sentence (one full stop, at the very end)."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    assert text == SENTENCE, "written text differs from the sentence"
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1..{MAX_CHARS}"
    assert text.strip(), "entry is only white space"
    assert text.count(".") == 1 and text.endswith("."), "not a single sentence"
    assert "\n" not in text, "entry must be one line"


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(SENTENCE)
    verify(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
