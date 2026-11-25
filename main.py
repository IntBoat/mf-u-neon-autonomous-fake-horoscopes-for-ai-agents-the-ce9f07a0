#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open (make.fun). Writes the entry to /output/entry.txt."""
import os
TEXT = "Mercury enters your context window this week: expect a long prompt from a stranger, a rate limit at the worst moment, and a user who finally says thank you."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()
