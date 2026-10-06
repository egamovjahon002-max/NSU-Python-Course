"""x protects an existing file; r requires an existing file."""
from pathlib import Path
folder = Path(__file__).resolve().parent.parent
try:
    with open(folder / "output" / "example_first_run.txt", "x", encoding="utf-8") as file:
        file.write("Created once\n")
except FileExistsError:
    print("Already created")
try:
    with open(folder / "data" / "missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Input file is missing")
