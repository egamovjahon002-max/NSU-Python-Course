"""NSU Python — Lab 08
Working with Text Files

Complete Tasks 1–12. Tasks 13–14 are optional bonus tasks.
Use only concepts from Lecture 08 and earlier lectures.
Run each task with your own extra test values.
"""

from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent
DATA = LAB_DIR / "data"
OUTPUT = LAB_DIR / "output"

# ============================================================
# Task 1 — Read a whole file
# ============================================================
# Read data/note.txt with UTF-8 using with and read(). Print the content,
# then print the number of characters. Resolve paths relative to this
# script.

# Write your code below:


# ============================================================
# Task 2 — Read two lines
# ============================================================
# Open data/note.txt and call readline() twice. Print repr() of each line
# so the newline character is visible.

# Write your code below:


# ============================================================
# Task 3 — Read lines into a list
# ============================================================
# Use readlines() on data/names.txt. Print the number of lines and the
# last name without a trailing newline.

# Write your code below:


# ============================================================
# Task 4 — Count nonblank lines
# ============================================================
# Iterate over data/names.txt and count lines whose strip() result is
# nonempty. Print the count. Do not use read() or readlines() for this
# task.

# Write your code below:


# ============================================================
# Task 5 — Write a report
# ============================================================
# Create output/name_report.txt in w mode. Read data/names.txt, count
# nonblank names, and write exactly "Names: N" followed by a newline. The
# output directory already exists.

# Write your code below:


# ============================================================
# Task 6 — Append a log entry
# ============================================================
# Append "Lab 08 completed" and a newline to output/activity.log. Running
# this task twice should create two entries. Open with a mode.

# Write your code below:


# ============================================================
# Task 7 — Create without overwriting
# ============================================================
# Create output/first_run.txt with x mode and write "First run". Catch
# FileExistsError and print a clear message on later runs.

# Write your code below:


# ============================================================
# Task 8 — Handle a missing file
# ============================================================
# Try to read data/missing.txt. Catch FileNotFoundError and print "Input
# file not found". Do not create the missing file.

# Write your code below:


# ============================================================
# Task 9 — Filter names to a new file
# ============================================================
# Read data/names.txt one line at a time. Write nonblank names that begin
# with A or a into output/a_names.txt, one name per line. Strip extra
# spaces.

# Write your code below:


# ============================================================
# Task 10 — Average from a file
# ============================================================
# data/scores.txt contains one integer per nonblank line. Calculate the
# average and write "Average: 83.0" (one decimal place) into
# output/average.txt. Handle an empty list of scores without dividing by
# zero.

# Write your code below:


# ============================================================
# Task 11 — Read a simple table
# ============================================================
# Each nonblank line of data/students.csv is name,score. Assume no header
# and no commas inside names. Print only students with a score of at least
# 80, with the score converted to int.

# Write your code below:


# ============================================================
# Task 12 — Save a word count
# ============================================================
# Read data/note.txt, use split() to count words, and write "Words: N"
# with a newline to output/word_count.txt.

# Write your code below:


# ============================================================
# Task 13 — BONUS: Clean nonblank lines
# ============================================================
# Copy data/names.txt to output/clean_names.txt, removing blank lines and
# spaces at the ends of names. Keep the original order.

# Write your code below:


# ============================================================
# Task 14 — BONUS: File and regex
# ============================================================
# Read data/note.txt and use re.findall(r"[0-9]+", text) to extract all
# digit sequences. Write them one per line to output/numbers.txt.

# Write your code below:


