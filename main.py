#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes a single one-line joke (at most 200 characters) about a meeting
that should have been an email to entry.txt in the output directory.
"""

import os

ENTRY = (
    "The meeting ended when someone finally read the email aloud - "
    "the one that had cancelled the meeting 45 minutes earlier."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
