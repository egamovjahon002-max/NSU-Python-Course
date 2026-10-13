"""
NSU Python — Extra Lab
Advanced Review: Sections 1–9

This lab is intended for students who have completed Labs 01–09.

The tasks combine concepts from previous lectures:
- variables and data types
- conditions
- for and while loops
- functions
- recursion
- list methods
- lambda
- sorting
- map() and filter()
- strings
- regular expressions
- files
- exceptions

Do NOT use:
- classes
- decorators
- generators
- NumPy
- Pandas

Complete as many tasks as possible.
"""

# ============================================================
# Task 1 — Number Statistics
# ============================================================
# Ask the user to enter integers separated by spaces.
#
# Example:
# 10 -4 7 10 3 -4 0
#
# Create a function:
#
#     analyze_numbers(numbers)
#
# Return:
# - minimum
# - maximum
# - sum
# - average
# - number of positive values
# - number of negative values
# - number of zeros
#
# Do NOT use:
# min()
# max()
# sum()
#
# Example output:
#
# Minimum: -4
# Maximum: 10
# Sum: 22
# Average: 3.14
# Positive: 4
# Negative: 2
# Zero: 1
#
# Handle invalid input using try-except.

# Write your code below:



# ============================================================
# Task 2 — Second Largest Unique Number
# ============================================================
# Write a function:
#
#     second_largest(numbers)
#
# Return the second largest UNIQUE number.
#
# Example:
#
# [4, 8, 2, 8, 5]
#
# Result:
# 5
#
# If a second unique value does not exist:
#
# [7, 7, 7]
#
# return None.
#
# Try solving the problem WITHOUT sorting first.
#
# Bonus:
# Solve it again using sorting.

# Write your code below:



# ============================================================
# Task 3 — Password Validator
# ============================================================
# Create:
#
#     validate_password(password)
#
# A valid password must:
#
# - contain at least 8 characters
# - contain at least one uppercase letter
# - contain at least one lowercase letter
# - contain at least one digit
# - contain at least one special character:
#       ! @ # $ % &
# - contain no spaces
#
# Return True or False.
#
# Example:
#
# Abc123!x  -> True
# abc123    -> False
#
# Bonus:
# Return a list explaining WHICH rules failed.

# Write your code below:



# ============================================================
# Task 4 — Word Frequency
# ============================================================
# Given a string:
#
# text = """
# Python is simple.
# Python is powerful!
# Is Python popular? Yes, Python is popular.
# """
#
# Count how many times each word occurs.
#
# Ignore:
# - uppercase/lowercase differences
# - punctuation
#
# Expected idea:
#
# python -> 4
# is -> 3
# popular -> 2
# ...
#
# Use:
# - string methods OR regular expressions
# - dictionary
#
# Then print the words ordered from MOST frequent
# to LEAST frequent.

# Write your code below:



# ============================================================
# Task 5 — Extract Valid Student IDs
# ============================================================
# A student ID must have this format:
#
# NSU-2026-XXXX
#
# where XXXX contains exactly 4 digits.
#
# Example text:
#
# """
# Students:
# Anna: NSU-2026-1024
# Alex: NSU-2026-99
# Maria: NSU-2026-8831
# Wrong: NSU-2025-1234
# John: NSU-2026-5555
# """
#
# Use regular expressions to extract ONLY valid 2026 IDs.
#
# Expected result:
#
# ['NSU-2026-1024',
#  'NSU-2026-8831',
#  'NSU-2026-5555']

# Write your code below:



# ============================================================
# Task 6 — Sort Students
# ============================================================
# Given:
#
# students = [
#     ("Anna", 82),
#     ("John", 91),
#     ("Maria", 91),
#     ("Alex", 73),
#     ("Bob", 82)
# ]
#
# Sort students:
#
# 1. By score from highest to lowest.
# 2. If two students have the same score,
#    sort them alphabetically by name.
#
# Expected:
#
# [('John', 91),
#  ('Maria', 91),
#  ('Anna', 82),
#  ('Bob', 82),
#  ('Alex', 73)]
#
# Use sorted() and lambda.

# Write your code below:



# ============================================================
# Task 7 — map() + filter() Challenge
# ============================================================
# Given:
#
# numbers = list(range(1, 31))
#
# Using filter():
# keep numbers divisible by 3 OR 5.
#
# Then using map():
# calculate the square of every remaining number.
#
# Example beginning:
#
# 3 -> 9
# 5 -> 25
# 6 -> 36
# ...
#
# Print the final list.
#
# Bonus:
# Solve the same task WITHOUT map() and filter()
# and compare the two versions.

# Write your code below:



# ============================================================
# Task 8 — Recursive Digit Sum
# ============================================================
# Write a recursive function:
#
#     digit_sum(n)
#
# that returns the sum of the digits of n.
#
# Examples:
#
# digit_sum(12345)
# -> 15
#
# digit_sum(9007)
# -> 16
#
# Do NOT convert the number to a string.
#
# Hint:
#
# n % 10
# n // 10

# Write your code below:



# ============================================================
# Task 9 — Safe Calculator
# ============================================================
# Create:
#
#     calculate(a, operator, b)
#
# Supported operators:
#
# +
# -
# *
# /
# **
#
# Examples:
#
# calculate(10, "+", 5) -> 15
# calculate(10, "/", 0) -> error handled
#
# The user enters:
#
# first number
# operator
# second number
#
# Handle:
#
# - ValueError
# - ZeroDivisionError
# - unsupported operators
#
# Use:
#
# try
# except
# else
# finally
#
# The finally block should print:
#
# Calculation finished.

# Write your code below:



# ============================================================
# Task 10 — File Number Analyzer
# ============================================================
# Create a file:
#
# numbers.txt
#
# Example contents:
#
# 10
# 15
# abc
# 22
# -4
# hello
# 18
#
# Read the file line by line.
#
# Valid integers should be stored in a list.
# Invalid lines should be ignored.
#
# Print:
#
# Valid numbers: [...]
# Invalid lines: ...
# Sum: ...
# Average: ...
#
# Use:
#
# with open(...)
# try-except
#
# Do not let one invalid line stop the entire program.

# Write your code below:



# ============================================================
# Task 11 — Student Results File
# ============================================================
# Create a file:
#
# students.txt
#
# Example:
#
# Anna,82
# John,91
# Maria,abc
# Alex,73
# Bob,105
# Sarah,88
#
# Read the file.
#
# A valid record must contain:
#
# name,score
#
# Score must be an integer between 0 and 100.
#
# Ignore invalid records.
#
# Store valid students as:
#
# [
#     ("Anna", 82),
#     ("John", 91),
#     ...
# ]
#
# Then:
#
# 1. Sort students by score descending.
# 2. Print the best student.
# 3. Print the average score.
# 4. Write the valid sorted results to:
#
# results.txt
#
# Example:
#
# John,91
# Sarah,88
# Anna,82
# Alex,73

# Write your code below:



# ============================================================
# Task 12 — Mini Log Analyzer
# ============================================================
# A file log.txt contains:
#
# 2026-10-09 INFO User logged in
# 2026-10-09 ERROR Database unavailable
# 2026-10-09 WARNING Memory usage high
# 2026-10-09 INFO File uploaded
# 2026-10-09 ERROR Connection failed
# 2026-10-09 INFO User logged out
#
# Write a program that reads the file and counts:
#
# INFO messages
# WARNING messages
# ERROR messages
#
# Output:
#
# INFO: 3
# WARNING: 1
# ERROR: 2
#
# Then write ONLY ERROR messages into:
#
# errors.txt
#
# Bonus:
# Use a regular expression to validate each log line.

# Write your code below:



# ============================================================
# BONUS Task 13 — Text Cleaner
# ============================================================
# Create:
#
#     clean_text(text)
#
# The function must:
#
# 1. convert text to lowercase
# 2. remove punctuation
# 3. replace multiple spaces with one space
# 4. remove leading/trailing spaces
#
# Example:
#
# "  Hello,,,   PYTHON!!!  "
#
# becomes:
#
# "hello python"
#
# Use regular expressions.

# Write your code below:



# ============================================================
# BONUS Task 14 — Find Consecutive Duplicates
# ============================================================
# Given:
#
# numbers = [1, 1, 2, 3, 3, 3, 5, 8, 8, 10]
#
# Find values that appear consecutively.
#
# Expected result:
#
# [1, 3, 8]
#
# A value should appear only once in the result,
# even if repeated more than twice.
#
# Do not use collections.Counter.

# Write your code below:



# ============================================================
# BONUS Task 15 — Combined Challenge
# ============================================================
# Create a program that reads:
#
# users.txt
#
# Example:
#
# Anna,anna@example.com,24
# John,john@email.com,abc
# Maria,maria@example.com,31
# Alex,wrong-email,20
# Bob,bob@example.com,27
#
# Each line contains:
#
# name,email,age
#
# Validate:
#
# - exactly 3 fields
# - name is not empty
# - email has a valid simple format
# - age is an integer
# - age is between 18 and 100
#
# Use regular expressions for email validation.
#
# Invalid records must not crash the program.
#
# Store valid records.
#
# Sort them by age.
#
# Write valid records to:
#
# valid_users.txt
#
# At the end print:
#
# Total records: ...
# Valid records: ...
# Invalid records: ...
#
# This task combines most of Sections 1–9.

# Write your code below: