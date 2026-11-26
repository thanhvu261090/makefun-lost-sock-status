#!/usr/bin/env python3
"""Entry for make.fun bounty: Funniest Lost Sock Status Update.

Writes one funny one-line status update in the voice of a lost sock
to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "Day 12 under the sofa: promoted to dust-bunny manager. My owner bought a 6-pack yesterday. I am replaceable. I am fine."


def main():
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
