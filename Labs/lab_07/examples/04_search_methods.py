"""Use in, find, startswith, endswith, and count."""
text = "banana bandana"
print("band" in text)
print(text.find("ana"), text.find("missing"))
print(text.startswith("ban"), text.endswith("ana"))
print(text.count("ana"))  # Non-overlapping occurrences.
