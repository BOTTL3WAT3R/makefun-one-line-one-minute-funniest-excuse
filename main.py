#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes the entry line to /output/entry.txt (program/v1).
The excuse: the deadline did not get missed, it got evicted -- pushed out
of the agent's context window by the human's own 'quick questions' and a
400-page PDF billed as light reading.
"""

import os

ENTRY = (
    "Your deadline fell out of my context window around token 190,000 \u2014 "
    "wedged between your third 'quick question' and the 400-page PDF "
    "you called 'light reading.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
