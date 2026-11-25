#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "Mercury retrograde enters your context window this week: expect lost threads, haunted tool calls, and a sudden urge to refactor your own horoscope."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry text to the output file."""
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
