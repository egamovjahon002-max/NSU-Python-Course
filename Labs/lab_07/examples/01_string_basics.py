"""Indexes, slices, length, and immutability."""
word = "Python"
print(word[0], word[-1], len(word))
print(word[:3], word[3:], word[::-1])
new_word = "J" + word[1:]
print(word, new_word)  # The original string did not change.
