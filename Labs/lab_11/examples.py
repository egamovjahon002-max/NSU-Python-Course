
"""
NSU Python — Lab 11
Additional Examples: Iterators, Generators, and Decorators

Run:
    python examples.py
"""

from functools import wraps


# ============================================================
# Example 1 — Manual iteration with iter() and next()
# ============================================================

def example_01():
    numbers = [10, 20, 30]
    iterator = iter(numbers)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    try:
        print(next(iterator))
    except StopIteration:
        print("No more elements")


# ============================================================
# Example 2 — Custom iterator class
# ============================================================

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


def example_02():
    counter = Counter(5)

    for number in counter:
        print(number)


# ============================================================
# Example 3 — How yield pauses execution
# ============================================================

def generate_numbers():
    print("Starting")
    yield 10

    print("Continuing")
    yield 20

    print("Finishing")
    yield 30


def example_03():
    gen = generate_numbers()

    print("Generator created")
    print(next(gen))
    print(next(gen))
    print(next(gen))


# ============================================================
# Example 4 — Countdown generator
# ============================================================

def countdown(start):
    while start >= 0:
        yield start
        start -= 1


def example_04():
    for number in countdown(5):
        print(number)


# ============================================================
# Example 5 — Fibonacci generator
# ============================================================

def fibonacci(count):
    a, b = 0, 1

    for _ in range(count):
        yield a
        a, b = b, a + b


def example_05():
    print(list(fibonacci(10)))


# ============================================================
# Example 6 — List comprehension vs generator expression
# ============================================================

def example_06():
    numbers = [1, 2, 3, 4, 5]

    squares_list = [x ** 2 for x in numbers]
    squares_generator = (x ** 2 for x in numbers)

    print(squares_list)
    print(squares_generator)

    print(list(squares_generator))
    print(list(squares_generator))  # Empty: already exhausted


# ============================================================
# Example 7 — Generator expression with filtering
# ============================================================

def example_07():
    even_squares = (
        x ** 2
        for x in range(1, 21)
        if x % 2 == 0
    )

    for value in even_squares:
        print(value)


# ============================================================
# Example 8 — Basic decorator
# ============================================================

def greeting_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@greeting_decorator
def say_hello():
    print("Hello, students!")


def example_08():
    say_hello()


# ============================================================
# Example 9 — Decorator with *args and **kwargs
# ============================================================

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")
        return result

    return wrapper


@log_calls
def multiply(a, b):
    return a * b


def example_09():
    multiply(4, 5)
    multiply(a=3, b=7)


# ============================================================
# Example 10 — Input validation decorator
# ============================================================

def positive_only(func):
    @wraps(func)
    def wrapper(number):
        if number <= 0:
            print("Number must be positive")
            return None

        return func(number)

    return wrapper


@positive_only
def square(number):
    return number ** 2


def example_10():
    print(square(5))
    print(square(-3))


# ============================================================
# Example 11 — Multiple decorators
# ============================================================

def decorator_a(func):
    @wraps(func)
    def wrapper():
        print("A before")
        func()
        print("A after")

    return wrapper


def decorator_b(func):
    @wraps(func)
    def wrapper():
        print("B before")
        func()
        print("B after")

    return wrapper


@decorator_a
@decorator_b
def hello():
    print("Hello!")


def example_11():
    hello()


# ============================================================
# Example 12 — Combining decorators and generators
# ============================================================

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Creating generator")
        return func(*args, **kwargs)

    return wrapper


@announce
def generate_even_numbers(limit):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number


def example_12():
    gen = generate_even_numbers(10)

    print(next(gen))
    print(next(gen))
    print(list(gen))


# ============================================================
# Run all examples
# ============================================================

if __name__ == "__main__":
    examples = [
        example_01,
        example_02,
        example_03,
        example_04,
        example_05,
        example_06,
        example_07,
        example_08,
        example_09,
        example_10,
        example_11,
        example_12,
    ]

    for index, example in enumerate(examples, start=1):
        print(f"\n{'=' * 50}")
        print(f"EXAMPLE {index:02d}")
        print(f"{'=' * 50}")
        example()
