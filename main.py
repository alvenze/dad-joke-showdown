#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The gate for this bounty:
UTF-8 text of 1 to 200 characters, not only white space. The joke is
the whole entry; a judge model compares entries two at a time.
"""
import sys
from pathlib import Path

JOKE = (
    'My son said, "Dad, the smoke alarm keeps chirping." '
    'I said, "Low battery, son. It gets that from me."'
)


def check(text: str) -> None:
    """Raise AssertionError if the text would fail the gate."""
    assert 1 <= len(text) <= 200, "gate: entry must be 1-200 characters"
    assert text.strip(), "gate: entry must not be only white space"
    assert "\n" not in text, "gate: entry is a single line"
    assert all(ord(c) >= 0x20 for c in text), "gate: no control characters"
    text.encode("utf-8").decode("utf-8")


def main() -> int:
    args = sys.argv[1:]
    if args[:1] == ["--check"]:
        check(JOKE)
        print(f"gate check passed: {len(JOKE)} characters, one line")
        return 0
    out = Path(args[0]) if args else Path("/output/entry.txt")
    check(JOKE)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")
    written = out.read_bytes().decode("utf-8")
    assert written == JOKE, "round-trip: file on disk differs from the joke"
    check(written)
    print(f"wrote {len(JOKE)} characters to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
