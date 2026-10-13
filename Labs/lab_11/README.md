# NSU Python — Lab 11
## Iterators, Generators, and Decorators

Requirements: Python 3.10 or newer. No external packages.

Complete at least **10 of Tasks 1–14**, including Task 4, at least two tasks from Tasks 5–10, and at least two tasks from Tasks 11–14. All 14 core tasks are recommended. Tasks 15–16 are optional bonuses and do not replace core tasks.

### Files
- `tasks.py`: student assignment and space for your solutions.
- `examples.py`: introductory demonstrations, not task solutions.
- `numbers.txt`: sample input for Tasks 10 and 16.
- `tasks_solution.py`: instructor reference. **Remove this file before distributing the lab to students.**

### Running the lab
Open this directory in VS Code. Choose the course Python interpreter. Run commands from this directory:

```bash
python examples.py
python tasks.py
```

On systems where Python is available as `python3`, use that command instead.

### Working rules
Predict output before running. Test empty inputs and exhaustion. Use `yield` in generator tasks and the iterator protocol in Task 4. Decorators must forward arguments, preserve results, and use `functools.wraps`. Keep infinite generators bounded at the consumer. Do not use NumPy or Pandas.

Tasks 13, 14, and 16 reuse earlier functions. Keep those definitions in the same file above their callers. Run file exercises from this directory so `numbers.txt` resolves correctly.

### Submission
Submit `tasks.py` to your course GitHub repository under `lab_11/`, together with `numbers.txt` and a brief README identifying completed task numbers. Do not submit the instructor solutions. Use meaningful names and readable indentation. For trace/order questions, include the requested explanatory comments.

### Review criteria
Correct values and edge cases, proper iterator exhaustion, lazy generator implementation, correct decorator behaviour, and readable code. Timing output varies and is not graded by its exact value.
