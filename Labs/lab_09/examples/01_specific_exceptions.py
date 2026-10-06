"""Run each conversion in its own try block."""
for text in ["15", "not a number"]:
    try:
        value = int(text)
    except ValueError:
        print("Cannot convert:", text)
    else:
        print("Converted value:", value)
