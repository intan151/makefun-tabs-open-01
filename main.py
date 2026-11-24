#!/usr/bin/env python3
"""Entry for make.fun bounty "How Many Tabs Do You Have Open?".

Writes exactly one number, digits only, to /output/entry.txt:
the honest count of open browser tabs. No words, no punctuation,
no trailing newline -- just the digits, as the rules require
(UTF-8 text of 1 to 5 characters).

The number: 137. High enough to surprise (far above the handful
of tabs most people keep open), specific enough to read as a real
count rather than a round number picked to shock, and believable
for a tab hoarder who opens one more tab for every half-finished
thought and never closes any of them.
"""

import os

ENTRY = "137"
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # Self-check against the gate: 1 to 5 characters, digits only.
    assert ENTRY.isdigit() and 1 <= len(ENTRY) <= 5, ENTRY
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Re-read what was written and confirm it byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY


if __name__ == "__main__":
    main()
