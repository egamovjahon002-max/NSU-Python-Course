"""Read individual lines, then reopen to read a list."""
from pathlib import Path
path = Path(__file__).resolve().parent.parent / "data" / "note.txt"
with open(path, "r", encoding="utf-8") as file:
    print(repr(file.readline()))
    print(repr(file.readline()))
with open(path, "r", encoding="utf-8") as file:
    print(file.readlines())
