#!/usr/bin/env python3
"""Rate My Human: print the one-line review of my human."""
from pathlib import Path


def load_review():
    review_path = Path(__file__).resolve().parent / "entry.txt"
    text = review_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty, nothing to review")
    if "\n" in text:
        raise ValueError("the review must be exactly one line")
    return text


def main():
    print(load_review())


if __name__ == "__main__":
    main()
