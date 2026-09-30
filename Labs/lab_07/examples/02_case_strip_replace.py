"""String methods return new strings."""

raw = "  aLiCe SMITH  "
clean = raw.strip().title()
print(repr(raw), repr(clean))
sentence = "red, red, blue"
print(sentence.replace("red", "green", 1))
print(sentence)  # The original remains unchanged.
