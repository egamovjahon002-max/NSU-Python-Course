# NSU Python — Lab 10

## Object-Oriented Programming

Matches Lecture 10 and continues Lab 09. There are **12 main tasks** and
**2 optional bonuses**. The course minimum is **at least 10 main tasks**;
aim to complete all 12. Follow the instructor's announced deadline.

### Topics

- Tasks 1–3: class attributes, instance attributes, and independent lists.
- Tasks 4–5: encapsulation, validation, and returning copies.
- Tasks 6–9: inheritance, `super()`, overriding, and extending methods.
- Tasks 10–12: polymorphism, duck typing, and composition.
- Bonuses: a further subclass and saving a roster to a text file.

### Dependencies

Complete Task 6 before Tasks 7 and 8. Task 9 needs Task 7. Tasks 10 and 12
use the classes from Tasks 6–9. Task 13 extends Task 9. Task 14 uses Task 12.
If selecting ten tasks, include any prerequisite classes needed by your
selected tasks. Use the specified distinct class names to avoid overwriting
earlier definitions. Each task states the assumptions on its inputs.

### Running

Python 3.10 or newer. No packages need installation.

- Windows: `python tasks.py` or `py tasks.py`.
- macOS/Linux: `python3 tasks.py`.

Write your code under each task. All uncommented top-level code runs in
order. Define prerequisite classes before their uses. Keep `output/` next
to `tasks.py`; the supplied OUTPUT path works even when the terminal has a
different working directory. Run file tasks normally so `__file__` exists.

Eight independent demonstration scripts are in `examples/`. For example,
run `python examples/01_class_attributes.py` (or use `python3`). These
illustrate techniques rather than providing the task answer key.

### Working rules

Use `self` for instance state. Validate before mutation. Use public methods
in demonstrations when the task asks for an encapsulated interface.
A leading underscore is a convention, not enforced privacy. Keep per-object
lists in `__init__`. A polymorphic loop should call the common method without
branching on the concrete type. Use `with` and UTF-8 for file output.

### Submission

Submit your completed `tasks.py` in the usual course repository. List your
completed task numbers in its README. If you do bonus Task 14, also submit
`output/roster.txt`. Instructor solutions are distributed separately.
