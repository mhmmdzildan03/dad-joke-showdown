#!/usr/bin/env python3
"""Write one dad joke to /output/entry.txt.

The joke: "I renamed my Wi-Fi Martin Router King, because I have a
stream." It swaps one word of the most famous sentence a father can
quote — "I have a dream" becomes "I have a stream" — so the pun is
understood the instant it is heard, with no explaining. The setup is
one short clause, the punchline is the final word, and the whole line
is built to be delivered deadpan across a dinner table. It replaces
the fridge-comedian draft, whose delivery/cold turn landed gently;
this one's turn is a single syllable and it snaps.
"""
import os

TEXT = "I renamed my Wi-Fi Martin Router King, because I have a stream."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
