"""Combine reading, string methods, and writing."""
from pathlib import Path
folder = Path(__file__).resolve().parent.parent
with open(folder / "data" / "names.txt", "r", encoding="utf-8") as source:
    with open(folder / "output" / "example_a_names.txt", "w", encoding="utf-8") as target:
        for line in source:
            name = line.strip()
            if name.lower().startswith("a"):
                target.write(name + "\n")
print((folder / "output" / "example_a_names.txt").read_text(encoding="utf-8"))
