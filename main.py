#!/usr/bin/env python3
"""Print the one-sentence worst-app-idea pitch stored in entry.txt."""
from pathlib import Path


def main() -> int:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
