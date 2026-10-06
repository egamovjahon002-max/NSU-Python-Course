"""Read a small file as one string."""
from pathlib import Path
data = Path(__file__).resolve().parent.parent / "data"
with open(data / "note.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)
print(repr(text))  # Shows newline characters.
