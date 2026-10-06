"""Process a file without collecting all lines in a list."""
from pathlib import Path
path = Path(__file__).resolve().parent.parent / "data" / "names.txt"
with open(path, "r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        if name:
            print(name)
