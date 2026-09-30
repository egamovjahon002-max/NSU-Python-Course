"""Test for None before reading a match object."""
import re
for text in ["Room 204", "Room A"]:
    result = re.search(r"[0-9]+", text)
    if result is not None:
        print(result.group(), result.span())
    else:
        print("No number")
