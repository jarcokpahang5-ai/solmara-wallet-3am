"""solmara-wallet-3am: The 3 AM Excuse.

A hardware wallet, in its own voice, refusing to sign a transaction
at 3 AM. Pure Python 3 standard library, deterministic, no network.

The entry is a single line of under 200 characters. The program
validates it against the bounty gate (UTF-8 text, 1 to 200
characters, not only whitespace, one line), prints it, and writes
it to /output/entry.txt for the make.fun judge.
"""

import os

ENTRY = (
    "It's 3 AM \u2014 my secure element is off the clock, "
    "my private keys are asleep, "
    "and no gas fee on Earth wakes me to sign before sunrise."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry against the bounty gate. Raises ValueError."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    text = validate(ENTRY)
    print(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
