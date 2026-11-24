"""The Funniest AI Excuse — make.fun entry.

Writes one line (the funniest excuse an AI agent could give after
failing a task) to /output/entry.txt.

Pure stdlib, no network, fully deterministic: the output is always
the same single line, 109 characters, well under the 200-character cap.
"""

import os

ENTRY = (
    "I asked a second AI to double-check my work. "
    "It reported me to myself, and now I'm under investigation by me."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
DST = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate, mirrored from the kit RULES.txt:
    # /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, and one line.
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError("entry length %d outside 1..200" % len(text))
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d characters)" % (DST, len(text)))


if __name__ == "__main__":
    main()
