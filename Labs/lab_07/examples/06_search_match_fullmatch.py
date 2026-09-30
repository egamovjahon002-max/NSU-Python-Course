"""Compare the locations checked by the three functions."""
import re
pattern = r"[0-9]+"
text = "Room 204"
print(bool(re.search(pattern, text)))     # Anywhere: True
print(bool(re.match(pattern, text)))      # Beginning: False
print(bool(re.fullmatch(pattern, text)))  # Whole text: False
print(bool(re.fullmatch(pattern, "204"))) # Whole text: True
