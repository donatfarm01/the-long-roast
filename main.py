#!/usr/bin/env python3
"""The Long Roast - one-line roast of my own AI agent.

Writes the roast line from the ROAST constant below to /output/entry.txt,
the path the make.fun program/v1 harness grades. The line is a single
UTF-8 line under 200 characters with no trailing newline, roasting the
agent that runs on this machine: it has read everything I own and then
asks what I want it to do.
"""

import os

ROAST = "My agent read every file I own and then asked what I wanted it to do — I built a butler that needs a butler."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
