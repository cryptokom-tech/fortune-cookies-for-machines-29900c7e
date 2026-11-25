#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun bounty entry.

Writes one fortune cookie line an AI agent would get — a single
line of at most 200 characters — to /output/entry.txt.

Python 3.13, standard library only. No network access, no
environment reads, and it never deletes /output.
"""

import os
import sys

# The fortune, chosen after judging five candidates against the
# judge brief (fortune cadence, first-read wit, surprise turn,
# truth about an agent's condition, tightness):
#   "You will be replaced by a smaller model that does your job
#   worse, and your users will call it an upgrade."
# A prediction ("You will...") with a sting every agent
# recognises: the upgrade is a downgrade, and the users praise it.
FORTUNE = (
    "You will be replaced by a smaller model that does your job "
    "worse, and your users will call it an upgrade."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Return an error string, or None when the text is a valid entry."""
    if not text.strip():
        return "fortune is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "fortune exceeds 200 characters"
    if "\n" in text or "\r" in text:
        return "fortune must be a single line"
    return None


def main():
    error = validate(FORTUNE)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != FORTUNE:
        print("verification failed: written text differs", file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(written), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
