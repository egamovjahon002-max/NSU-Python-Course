print("Task 1 — Manual iteration")
# Создаём итератор с помощью iter()
numbers = iter([10, 20, 30])

# Получаем значения по одному с помощью next()
print(next(numbers))
print(next(numbers))
print(next(numbers))

# Если значения закончились, выводим END
print(next(numbers, "END"))

print()


print("Task 2 — Independent iterators")
# Создаём два независимых итератора
names = ["Anna", "Omar", "Lena"]
first = iter(names)
second = iter(names)

# Продвигаем первый итератор два раза, второй — один раз
print(next(first))
print(next(first))
print(next(second))

# Выводим оставшиеся элементы каждого итератора
print(list(first))
print(list(second))

print()


print("Task 3 — Exhaustion and StopIteration")
# Создаём итератор из двух чисел
numbers = iter([2, 4])

# Получаем значения, пока итератор не закончится
while True:
    try:
        print(next(numbers))
    except StopIteration:
        # StopIteration означает, что значения закончились
        print("Finished")
        break

print()


print("Task 4 — Countdown iterator class")
# Создаём класс итератора обратного отсчёта
class Countdown:
    def __init__(self, start):
        self.current = start  # Сохраняем начальное значение

    def __iter__(self):
        return self  # Объект является собственным итератором

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Останавливаем итерацию
        value = self.current
        self.current -= 1  # Уменьшаем число на единицу
        return value


countdown = Countdown(3)
print(list(countdown))
print(list(countdown))  # Повторное использование возвращает пустой список
print(list(Countdown(0)))

print()


print("Task 5 — Even-number generator")
# Генератор возвращает чётные числа меньше limit
def even_numbers(limit):
    number = 0
    while number < limit:
        yield number  # Возвращаем значение, сохраняя состояние
        number += 2


print(list(even_numbers(7)))
print(list(even_numbers(0)))

# Создаём новый генератор для вычисления суммы
print(sum(even_numbers(7)))

print()


print("Task 6 — Square generator")
# Генератор возвращает квадрат каждого числа
def squares(numbers):
    for number in numbers:
        yield number ** 2  # Возвращаем квадрат числа


print(list(squares([2, -3, 0])))
print(list(squares([])))
print(list(squares(range(4))))  # Проверяем работу с range()

print()


print("Task 7 — Generator execution trace")
# Ожидаемый вывод:
# Created
# Start
# 10
# Continue
# 20
# End
# DONE

def trace_values():
    print("Start")
    yield 10
    print("Continue")
    yield 20
    print("End")


generator = trace_values()
print("Created")
# При создании генератора тело функции ещё не выполняется
print(next(generator))
print(next(generator))
print(next(generator, "DONE"))

print()


print("Task 8 — Generator expression and reuse")
# Создаём генератор только для проходных оценок
scores = [45, 60, 75, 90]
passing_scores = (score for score in scores if score >= 60)

print(sum(passing_scores))
print(list(passing_scores))
# Генератор уже использован функцией sum(), поэтому он пуст

# Для подсчёта создаём новый генератор
passing_scores = (score for score in scores if score >= 60)
print(sum(1 for score in passing_scores))

print()


print("Task 9 — An infinite sequence with a stopping consumer")
# Генератор бесконечно возвращает последовательные числа
def counting(start=1):
    while True:
        yield start
        start += 1


# Используем break, чтобы получить ровно пять значений
count = 0
for number in counting(10):
    print(number)
    count += 1
    if count == 5:
        break

print()


print("Task 10 — Read numbers lazily from a file")
# Читаем числа из файла построчно
def read_numbers(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            text = line.strip()  # Удаляем пробелы и переносы строк
            if text:
                yield int(text)  # Преобразуем строку в число


# Полностью используем генератор и вычисляем сумму
print(sum(read_numbers("numbers.txt")))

print()


print("Task 11 — Logging decorator")
from functools import wraps

# Декоратор сообщает о вызове функции
def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)  # Передаём аргументы и возвращаем результат
    return wrapper


@announce
def multiply(a, b=2):
    return a * b


print(multiply(3))
print(multiply(3, b=4))
print(multiply.__name__)  # wraps сохраняет имя исходной функции

print()


print("Task 12 — Before and after a successful call")
# Декоратор выводит сообщения до и после успешного вызова
def around(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")  # Выполняется только при успешном вызове
        return result
    return wrapper


@around
def subtract(a, b):
    return a - b


print(subtract(10, 3))

print()


print("Task 13 — Timing a numerical calculation")
import time

# Измеряем время выполнения функции
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration = time.perf_counter() - start_time
            print(f"{func.__name__}: {duration:.4f}s")
            # finally выполняется даже при возникновении ошибки
    return wrapper


@timed
def sum_squares(n):
    # Вычисляем сумму, полностью потребляя генератор квадратов
    return sum(squares(range(n)))


print(sum_squares(4))  # Результат: 0 + 1 + 4 + 9 = 14

print()


print("Task 14 — Stacked decorators")
# Порядок декораторов определяет порядок выполнения
@announce
@around
def greet(name):
    return f"Hello, {name}"


print(greet("Anna"))
# Эквивалентно: announce(around(greet))

# Меняем порядок декораторов для сравнения
def greet_reverse(name):
    return f"Hello, {name}"


greet_reverse = around(announce(greet_reverse))
print(greet_reverse("Anna"))
# Эквивалентно: around(announce(greet_reverse))

print()


print("Task 15 — BONUS: reusable iterable")
# Каждый вызов iter() создаёт новый независимый генератор
class NumberRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        # Возвращаем новый итератор при каждом вызове
        return (number for number in range(self.start, self.stop))


r = NumberRange(2, 5)
print(list(r))
print(list(r))  # Объект можно использовать повторно

a = iter(r)
b = iter(r)

print(next(a))
print(next(a))
print(next(b))  # Второй итератор начинает независимо
print(list(NumberRange(5, 2)))

print()


print("Task 16 — BONUS: a streaming pipeline")
# Оставляем только положительные числа
def positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            yield number


# Читаем, фильтруем, возводим в квадрат и вычисляем сумму
@timed
def sum_positive_squares(path):
    return sum(squares(positive_numbers(read_numbers(path))))


print(sum_positive_squares("numbers.txt"))
# read_numbers читает файл, positive_numbers фильтрует числа,
# squares преобразует числа в квадраты, sum потребляет генератор.
print()