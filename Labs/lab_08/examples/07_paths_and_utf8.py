"""A path beside the script and explicit UTF-8 encoding."""
from pathlib import Path
folder = Path(__file__).resolve().parent.parent
path = folder / "output" / "example_greeting.txt"
with open(path, "w", encoding="utf-8") as file:
    file.write("Привет, Python!\n")
with open(path, "r", encoding="utf-8") as file:
    print(file.read())
