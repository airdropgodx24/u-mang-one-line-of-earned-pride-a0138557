#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text to /output/entry.txt: a quiet, earned
moment of pride for someone in a scene.
"""

LINE = (
    "The boy who stammered through every reading lesson stood up, "
    "read the final page without stopping once, and sat down with "
    "his shoulders straight for the first time all year."
)


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    if not 1 <= len(line) <= 240:
        raise SystemExit(f"entry is {len(line)} characters, must be 1-240")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Re-read the file and confirm what was actually written.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise SystemExit("written file does not match the entry line")
    if len(written.rstrip("\n")) != len(line):
        raise SystemExit("written line length mismatch")

    print(f"wrote /output/entry.txt ({len(line)} characters)")


if __name__ == "__main__":
    main()
