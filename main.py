#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's final text message to /output/entry.txt.
One line, plain text, at most 200 characters (competition gate).
Standard library only; fully deterministic.
"""

import os

# The entry: the battery's last text. It waited all day at 1%, the charger
# finally shows up acting like a hero, and the battery can't even finish
# its parting burn -- the message itself dies mid-word, which is the joke.
ENTRY = (
    "i waited all day at 1% while you were lost under the couch, "
    "and NOW you show up acting like the hero. "
    "fyi, the power bank treats me bett\u2014"
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
