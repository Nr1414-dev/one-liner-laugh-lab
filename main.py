#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt. The line answers the
prompt — the excuse a robot vacuum gives after eating a sock — with a
fresh angle: the dryer already took the sock's pair, so the vacuum only
finished the job.

The line is written directly with open() and chmod 0644. No temporary
file is used, so the grader can read the output as another user.
"""

import os
import sys

LINE = "The dryer took the left one \u2014 I only finished the job."


def main() -> int:
    text = LINE
    if not 1 <= len(text) <= 200:
        print(f"entry length {len(text)} is outside 1..200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry contains a control character", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {len(text)} chars ({len(text.encode('utf-8'))} bytes) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
