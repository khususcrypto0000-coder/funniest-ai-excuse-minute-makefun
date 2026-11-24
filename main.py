"""One-line make.fun entry: The Funniest AI Excuse.

Writes a single line (1-200 characters, no trailing newline) to
/output/entry.txt (overridable via the OUTPUT_DIR environment variable).
Standard library only.
"""

import os
import sys

ENTRY = (
    "I gave your deadline my full attention \u2014 all 96 heads \u2014 "
    "and they unanimously voted to stare at literally anything else."
)


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

