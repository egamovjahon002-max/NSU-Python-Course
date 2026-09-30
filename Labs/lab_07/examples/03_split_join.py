"""Split words and join them with a chosen separator."""

text = "  Python  files  are useful  "
words = text.split()
print(words)
print(",".join(words))
row = "Ada,82,NSU"
print(" - ".join(row.split(",")))
