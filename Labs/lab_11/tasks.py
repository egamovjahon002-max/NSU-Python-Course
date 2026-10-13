"""
NSU Python — Lab 11
Iterators, Generators, and Decorators

Tasks 1–14 are core practice. Tasks 15–16 are optional bonus tasks.
Complete at least 10 core tasks, including Task 4, at least two tasks
from Tasks 5–10, and at least two tasks from Tasks 11–14.
Use only Lecture 11 and earlier course concepts. Python 3.10+.
Place your code below each task. Keep function/class names as specified.
Do not use NumPy or Pandas in this lab.
"""


# ========================================================================
# Task 1 — Manual iteration
# ========================================================================
# Create an iterator over [10, 20, 30] using iter().
# Print each value using next(), without a loop.
# Then print next(iterator, "END").
# Expected output: 10, 20, 30, END on separate lines.

# Write your code below:



# ========================================================================
# Task 2 — Independent iterators
# ========================================================================
# Create two iterators over ["Anna", "Omar", "Lena"].
# Advance the first iterator twice and the second once.
# Print each returned name and both remaining sequences using list().
# Expected names: Anna, Omar, Anna.
# Remaining sequences: ["Lena"] and ["Omar", "Lena"].

# Write your code below:



# ========================================================================
# Task 3 — Exhaustion and StopIteration
# ========================================================================
# Create an iterator over [2, 4].
# Use a while loop, next(), and try-except to print all its values.
# Catch only StopIteration and print "Finished" before leaving the loop.
# Do not use a for loop for this task.
# Expected output: 2, 4, Finished on separate lines.

# Write your code below:



# ========================================================================
# Task 4 — Countdown iterator class
# ========================================================================
# Define class Countdown(start). Accept an integer start.
# Implement __iter__() returning self and __next__().
# Yield values from start down to 1. Raise StopIteration at the end.
# For start <= 0, the iterator must be empty.
# Do not use yield in this class.
# Examples: list(Countdown(3)) == [3, 2, 1]; list(Countdown(0)) == [].
# Verify that consuming the same object again returns an empty list.

# Write your code below:



# ========================================================================
# Task 5 — Even-number generator
# ========================================================================
# Define even_numbers(limit), accepting an integer limit.
# Use yield to produce even integers from 0 up to limit, exclusive.
# For limit <= 0, yield no values.
# Examples: list(even_numbers(7)) == [0, 2, 4, 6];
# list(even_numbers(0)) == [].
# Calculate sum(even_numbers(7)) using a fresh generator. Expected: 12.

# Write your code below:



# ========================================================================
# Task 6 — Square generator
# ========================================================================
# Define squares(numbers), where numbers is an iterable of numbers.
# Yield the square of each input, preserving its order.
# Do not build a result list inside the function.
# Examples: list(squares([2, -3, 0])) == [4, 9, 0];
# list(squares([])) == [].
# Test with both a list and range(4).

# Write your code below:



# ========================================================================
# Task 7 — Generator execution trace
# ========================================================================
# Define trace_values() that prints "Start", yields 10,
# prints "Continue", yields 20, then prints "End".
# Create the generator and print "Created".
# Call print(next(generator)) twice, then print(next(generator, "DONE")).
# Before running, write the expected output as a comment.
# Explain in one comment why "Start" is not printed during creation.

# Write your code below:



# ========================================================================
# Task 8 — Generator expression and reuse
# ========================================================================
# Given scores = [45, 60, 75, 90], create a generator expression
# that supplies only scores >= 60.
# Print sum(generator), then list(generator).
# Expected: 225 and []. Explain why the list is empty.
# Create a fresh generator expression to calculate the count of passing scores.
# Expected count: 3. Do not use a list comprehension.

# Write your code below:



# ========================================================================
# Task 9 — An infinite sequence with a stopping consumer
# ========================================================================
# Define counting(start=1), accepting an integer start.
# Use yield and while True to generate successive integers indefinitely.
# Using a for loop and break, print exactly five values from counting(10).
# Expected values: 10, 11, 12, 13, 14.
# Do not convert this generator to a list.

# Write your code below:



# ========================================================================
# Task 10 — Read numbers lazily from a file
# ========================================================================
# Define read_numbers(path) as a generator function.
# Open the file with with and encoding="utf-8" inside the generator.
# Strip each line, skip blank lines, and yield int(text).
# Use the supplied numbers.txt. Its sum must be 50.
# If a non-blank line is invalid, let ValueError propagate.
# Do not read the entire file with read() or readlines().
# Fully consume the generator with sum() for this exercise.

# Write your code below:



# ========================================================================
# Task 11 — Logging decorator
# ========================================================================
# Define announce(func) using functools.wraps.
# Its wrapper must print "Running <function name>" before the call.
# Forward *args and **kwargs and return the original result.
# Decorate multiply(a, b=2), which returns a * b.
# Test multiply(3) and multiply(3, b=4). Expected results: 6 and 12.
# Check that multiply.__name__ is still "multiply".

# Write your code below:



# ========================================================================
# Task 12 — Before and after a successful call
# ========================================================================
# Define around(func) using functools.wraps.
# Print "Before" before calling func and "After" after a successful call.
# Forward all arguments and preserve the return value.
# Decorate subtract(a, b). print(subtract(10, 3)) must print:
# Before
# After
# 7
# Do not catch exceptions. If func raises, "After" must not print.

# Write your code below:



# ========================================================================
# Task 13 — Timing a numerical calculation
# ========================================================================
# Define timed(func) using wraps and time.perf_counter.
# Print "<function name>: <duration>s" with four decimal places.
# Use try-finally so timing prints even if func raises.
# Preserve the original result and allow exceptions to propagate.
# Decorate sum_squares(n), which consumes squares(range(n)) from Task 6.
# Check sum_squares(4) returns 14. Exact timing values will vary.
# Time the consumer, rather than the creation of a generator.

# Write your code below:



# ========================================================================
# Task 14 — Stacked decorators
# ========================================================================
# Use announce from Task 11 and around from Task 12.
# Apply @announce above @around to greet(name), returning "Hello, <name>".
# Call print(greet("Anna")). Expected output:
# Running greet
# Before
# After
# Hello, Anna
# Reverse the decorator order and record the new output.
# Explain the equivalent nested calls in one comment.

# Write your code below:



# ========================================================================
# Task 15 — BONUS: reusable iterable
# ========================================================================
# Create NumberRange(start, stop), where stop is exclusive.
# Its __iter__ method must return a NEW iterator on each call.
# You may return a generator from a separate helper function.
# Test r = NumberRange(2, 5): list(r) must be [2, 3, 4] twice.
# Then create a = iter(r), b = iter(r) and show independent positions.
# For stop <= start, the iterable must be empty.

# Write your code below:



# ========================================================================
# Task 16 — BONUS: a streaming pipeline
# ========================================================================
# Define positive_numbers(numbers) yielding only values > 0.
# Compose read_numbers(), positive_numbers(), and squares().
# Use supplied numbers.txt and calculate the sum without intermediate lists.
# Expected result: 1125.
# Wrap the consumer in @timed and preserve its result.
# Describe which function reads, filters, transforms, and consumes the data.

# Write your code below:


