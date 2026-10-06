"""Append adds a new line each time this script runs."""
from pathlib import Path
output = Path(__file__).resolve().parent.parent / "output"
with open(output / "example_log.txt", "a", encoding="utf-8") as file:
    file.write("Example run\n")
print((output / "example_log.txt").read_text(encoding="utf-8"))
