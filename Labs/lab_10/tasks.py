"""NSU Python — Lab 10
Object-Oriented Programming

Main tasks: 1–12. Course minimum: at least 10 main tasks.
Aim to complete all 12. Tasks 13–14 are optional bonuses.
Use Lecture 10 and earlier concepts. No external packages are needed.
Tasks 7–10 and 12–14 reuse classes defined in earlier tasks.
"""
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent
OUTPUT = LAB_DIR / "output"


# ============================================================
# Task 1 — Instance and class attributes
# ============================================================
# Create Student with class attribute university = "NSU".
# __init__(name) must store name as an instance attribute.
# Create Anna and Omar. Print each name and university.
# Then set Student.university = "NSU Updated" and print both universities.
# Expected universities after the change: NSU Updated, NSU Updated.
# Do not assign self.university inside __init__.

# Write your code below:


# ============================================================
# Task 2 — Shadow a class attribute
# ============================================================
# Create Device with class attribute category = "General" and an instance
# attribute name set in __init__. Create a = Device("Laptop") and
# b = Device("Printer"). Set a.category = "Personal" and then
# Device.category = "Shared".
# Print a.category, b.category, and Device.category on separate lines.
# Expected: Personal, Shared, Shared.
# Add a comment explaining why a differs from b.

# Write your code below:


# ============================================================
# Task 3 — Fix shared mutable state
# ============================================================
# The following design accidentally shares one list:
# class Team:
#     members = []
#     def __init__(self, name):
#         self.name = name
#     def add_member(self, name):
#         self.members.append(name)
# Fix Team so each instance has its own members list.
# Create Alpha and Beta. Add Anna to Alpha only.
# Print both lists and whether they are the same object.
# Expected: ['Anna'], [], False (one result per line).

# Write your code below:


# ============================================================
# Task 4 — Encapsulation and validation
# ============================================================
# Create PositiveCounter with self._value = 0 in __init__.
# add(amount) accepts a positive integer and increases _value.
# Reject zero and negative integers with ValueError("Amount must be positive")
# before changing state. get_value() returns the current value.
# Assume arguments are integers. Use only these public methods in the demo.
# Add 3 and 2, then attempt to add 0 inside try/except.
# Print the value before and after the rejected update: both must be 5.
# Add a comment: the leading underscore is a convention, not enforced privacy.

# Write your code below:


# ============================================================
# Task 5 — Return a copy of internal data
# ============================================================
# Create ScoreBook with self._scores = [] inside __init__.
# add_score(score) accepts integer scores from 0 to 100 inclusive.
# Otherwise raise ValueError("Score must be between 0 and 100").
# get_scores() must return a COPY of the internal list.
# Add 80. Store snapshot = book.get_scores(), then append 100 to snapshot.
# Print snapshot and book.get_scores(). Expected: [80, 100] and [80].
# Create a second ScoreBook and verify its scores remain empty.

# Write your code below:


# ============================================================
# Task 6 — Inherit a method
# ============================================================
# Create Person with __init__(name) and describe(), returning
# "Person: NAME". Create Visitor(Person) with an empty body using pass.
# Create Visitor("Omar") and print its description: Person: Omar.
# Also print isinstance(visitor, Visitor), isinstance(visitor, Person),
# and issubclass(Visitor, Person). All three must be True.
# Do not redefine __init__ or describe inside Visitor.

# Write your code below:


# ============================================================
# Task 7 — Initialize a subclass with super
# ============================================================
# Using Person from Task 6, create StudentPerson(Person).
# __init__(name, program) must call super().__init__(name), then store program.
# Create StudentPerson("Anna", "AI"). Print name, program, and describe().
# Expected: Anna, AI, Person: Anna (one result per line).
# Do not duplicate the assignment to self.name in the subclass.

# Write your code below:


# ============================================================
# Task 8 — Override a method
# ============================================================
# Using Person, create Teacher(Person). Its __init__(name, subject) calls
# the parent initializer and stores subject.
# Override describe() to return "Teacher: NAME, subject: SUBJECT".
# Print Teacher("Mira", "Python").describe().
# Expected: Teacher: Mira, subject: Python.
# Then print Person("Omar").describe(): Person: Omar.
# The Person implementation must remain unchanged.

# Write your code below:


# ============================================================
# Task 9 — Extend an inherited method
# ============================================================
# Create DetailedStudent(StudentPerson).
# Inherit __init__ unchanged. Override describe() by calling
# super().describe(), then appending ", program: PROGRAM".
# For DetailedStudent("Anna", "AI"), the result must be:
# Person: Anna, program: AI.
# Return a string; do not print inside describe().

# Write your code below:


# ============================================================
# Task 10 — Polymorphic descriptions
# ============================================================
# Create a list containing Person("Omar"), Teacher("Mira", "Python"),
# and DetailedStudent("Anna", "AI") from Tasks 6–9.
# Use ONE for loop to call describe() and print each result.
# Expected:
# Person: Omar
# Teacher: Mira, subject: Python
# Person: Anna, program: AI
# Do not use type(), isinstance(), or if/elif to choose a description.

# Write your code below:


# ============================================================
# Task 11 — Duck typing with shapes
# ============================================================
# Create unrelated Rectangle and Square classes (no custom common parent).
# Rectangle(width, height).area() returns width * height.
# Square(side).area() returns side * side. Assume positive numeric dimensions.
# Define total_area(shapes), which sums shape.area() in a loop and returns it.
# For [Rectangle(3, 4), Square(5)], print 37.
# For an empty list, print 0. Do not branch on the shape's type.

# Write your code below:


# ============================================================
# Task 12 — Composition: a course roster
# ============================================================
# Create Course with title and an independent self.students list.
# enroll(person) appends the supplied object. Assume it supports describe().
# roster() returns a list of the enrolled objects' describe() results.
# Enroll Teacher("Mira", "Python") and DetailedStudent("Anna", "AI").
# Print each roster string in enrollment order:
# Teacher: Mira, subject: Python
# Person: Anna, program: AI
# Create a second course and verify its roster() returns [].
# Course contains objects; it must not inherit from Person or StudentPerson.

# Write your code below:


# ============================================================
# Task 13 — BONUS: a further subclass
# ============================================================
# Create ResearchStudent(DetailedStudent) with __init__(name, program, thesis).
# Call super().__init__(name, program), then store thesis.
# Override describe() by extending super().describe() with ", thesis: THESIS".
# ResearchStudent("Anna", "AI", "XAI").describe() must return:
# Person: Anna, program: AI, thesis: XAI.
# Enroll this object in Course from Task 12. Its roster must use the new
# description without changes to Course.

# Write your code below:


# ============================================================
# Task 14 — BONUS: save the roster
# ============================================================
# Define save_roster(course, path). Use course.roster() and write one
# returned description per line using with, mode "w", and UTF-8.
# Use the Course from Task 12. Save to OUTPUT / "roster.txt".
# At the call site, catch OSError and print "Cannot save roster" on failure.
# Print "Roster saved" only on success. Do not catch unrelated exceptions.
# The supplied output/ directory already exists. Do not create other folders.
# Also test OUTPUT / "missing_folder" / "roster.txt"; it should fail while
# missing_folder does not exist. Do not create that folder.
# Repeated successful runs should replace roster.txt, not append duplicates.

# Write your code below:
