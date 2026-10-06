"""Resolve fixture paths relative to the lab, not the terminal."""
from pathlib import Path
DATA = Path(__file__).resolve().parent.parent / "data"
for filename in ["number_valid.txt", "number_invalid.txt", "missing.txt"]:
    try:
        with open(DATA / filename, encoding="utf-8") as file:
            value = int(file.readline().strip())
    except FileNotFoundError:
        print(filename, "is missing")
    except ValueError:
        print(filename, "does not start with an integer")
    else:
        print(filename, value)
