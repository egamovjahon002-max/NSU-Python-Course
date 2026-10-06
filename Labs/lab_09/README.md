# NSU Python — Lab 09

## Exceptions and OOP Foundations

Matches the **revised Lecture 09**, including the OOP introduction moved
from Lecture 10. Main tasks: **1–12**. The course submission minimum is
**at least 10 main tasks**. Aim to complete all 12 and practise both parts.
Tasks **13–14** are optional bonuses.

### Topics

- Tasks 1–6: specific exception handlers, `else`, `finally`, `raise`,
  file failures, and input-validation loops.
- Tasks 7–12: classes and objects, `self`, `__init__`, instance attributes,
  methods, independent object state, and validation inside methods.
- Bonuses: combine files, validation, and objects.

Use only Lecture 09 and earlier concepts. Inheritance, `super()`, class
attributes, encapsulation conventions, properties, and decorators belong
to later material and are not required here. No packages need installation.
Python 3.10 or newer is sufficient.

### Files and running

Keep `data/` next to `tasks.py`. The supplied `DATA` variable resolves
file paths relative to this lab folder, independently of the terminal's
working directory. Use `DATA / "number_valid.txt"` in Task 5.
Do not edit fixture files or create `data/missing.txt`.

Windows: `python tasks.py` or `py tasks.py`.
macOS/Linux: `python3 tasks.py`.

The starter contains task instructions and empty work areas. As you add
solutions, all uncommented top-level code runs in order. During development,
run only the task you are working on with your editor's selected-code
command, or temporarily comment out completed interactive demonstrations.
For file tasks, run the file normally so `__file__` is available.

Eight short demonstration scripts are in `examples/`. For example:
`python examples/01_specific_exceptions.py` (use `python3` where needed).
The examples illustrate techniques; they are not the task answer key.

### Working rules

Use specific exception types. Do not hide failures with `except: pass`.
Use `with` and UTF-8 for text files. Respect requested return values and
messages. Test both valid and invalid cases. Store per-object lists inside
`__init__`. Numeric arguments are assumed where stated in the task.

### Submission

Submit your completed `tasks.py` in your usual course repository, keeping
`data/` alongside it. State which task numbers you completed in your
repository README. Follow the instructor's announced submission deadline.
Instructor solutions are provided separately.
