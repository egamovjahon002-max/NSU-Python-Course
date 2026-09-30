"""Extract digit sequences with a raw regex string."""
import re
text = "Room B-204 and room C-17"
print(re.findall(r"[0-9]+", text))
print(re.findall(r"\w+", text))
print(re.findall(r"\s", "A B\tC"))
