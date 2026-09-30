"""Validate the complete shape of a simple student code."""
import re
pattern = r"[A-Z]{2}-[0-9]{4}"
for code in ["NS-2047", "N-2047", "xNS-2047"]:
    print(code, re.fullmatch(pattern, code) is not None)
