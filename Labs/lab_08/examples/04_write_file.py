"""Writing with w creates or replaces an output file."""
from pathlib import Path
output = Path(__file__).resolve().parent.parent / "output"
with open(output / "example_report.txt", "w", encoding="utf-8") as file:
    file.write("Names: 5\n")
    print("Ready", file=file)
print((output / "example_report.txt").read_text(encoding="utf-8"))
