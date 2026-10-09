"""
============================================================
NSU Python — Lab 05
Funksiyalar amalda: argumentlar, rekursiya, math, list metodlari
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 38 ta topshiriq ketma-ket yechilgan:
- Task 1-12: asosiy topshiriqlar
- Task 13-14: bonus
- Task 15-38: qo'shimcha mashqlar

TAQIQLANGAN NARSALAR (bu labda ishlatilmaydi):
---------------------------------------------
- lambda
- sorted()
- filter()
- map()

MUHIM TUSHUNCHALAR:
-------------------
- *args   -> istalgan sonda pozitsion argumentlarni qabul qiladi (tuple)
- **kwargs-> istalgan sonda kalit-so'z argumentlarini qabul qiladi (dict)
- def     -> funksiya e'lon qiladi
- return  -> qiymat qaytaradi (return yo'q bo'lsa -> None)
- scope   -> o'zgaruvchi ko'rinish doirasi (global / local)
- rekursiya-> funksiya o'zini-o'zi chaqiradi
- math    -> matematik funksiyalar moduli
"""

import math   # Task 12, 19, 31, 38 uchun kerak

# ============================================================
# TASK 1 — Pozitsion va kalit-so'z argumentlar
# ============================================================
# MAQSAD: Funksiyani turli usullar bilan chaqirishni o'rganish.
#
# MANTIQ:
# - Pozitsion argumentlar -> tartib bo'yicha joylashadi
# - Kalit-so'z argumentlari -> nom bo'yicha, tartib muhim emas
# - Aralash -> avval pozitsion, keyin kalit-so'z

print("\n===== TASK 1 =====")

def describe_student(name, age, city):
    # Uchta parametr: name, age, city
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# 1) Faqat pozitsion argumentlar (tartib muhim)
describe_student("Anna", 23, "Novosibirsk")

# 2) Faqat kalit-so'z argumentlari (tartib muhim emas)
describe_student(city="Moscow", name="Ivan", age=20)

# 3) Bitta pozitsion + qolganlari kalit-so'z
describe_student("Mira", city="Kazan", age=21)

# ============================================================
# TASK 2 — Default (sukut bo'yicha) argumentlar
# ============================================================
# MAQSAD: Argumentga sukut qiymat berish.
#
# MANTIQ:
# - rate=2.5 -> agar rate berilmasa, 2.5 ishlatiladi
# - Sukut argumentlar funksiya e'lonida OXIRIDA bo'lishi kerak

print("\n===== TASK 2 =====")

def shipping_cost(weight, rate=2.5):
    return weight * rate

print(shipping_cost(4))              # 10.0 (rate = 2.5)
print(shipping_cost(4, 3.0))         # 12.0 (rate = 3.0)
print(shipping_cost(4, rate=1.5))    # 6.0  (kalit-so'z bilan)

# ============================================================
# TASK 3 — Erta return (early return)
# ============================================================
# MAQSAD: Xatolikni darhol aniqlab, funksiyadan chiqish.
#
# MANTIQ:
# - b == 0 -> None qaytaramiz (0 ga bo'lish mumkin emas)
# - Aks holda -> a / b

print("\n===== TASK 3 =====")

def safe_divide(a, b):
    if b == 0:
        return None          # erta chiqish
    return a / b

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None

# ============================================================
# TASK 4 — *args: umumiy ball
# ============================================================
# MAQSAD: Istalgan sonda argumentlarni qabul qilish.
#
# MANTIQ:
# - *scores -> barcha pozitsion argumentlar bitta TUPLEDA yig'iladi
# - Bo'sh bo'lsa ham ishlaydi (sum = 0)

print("\n===== TASK 4 =====")

def total_score(*scores):
    total = 0
    for s in scores:         # scores - bu tuple
        total += s
    return total

print(total_score(10, 20, 30))   # 60
print(total_score(5))            # 5
print(total_score())             # 0

# ============================================================
# TASK 5 — *args: o'rtacha ball
# ============================================================
# MAQSAD: Bo'sh bo'lsa None, aks holda o'rtacha.
#
# MANTIQ:
# - len(scores) -> tuple uzunligi
# - Bo'sh bo'lsa -> None

print("\n===== TASK 5 =====")

def average_score(*scores):
    if len(scores) == 0:
        return None
    total = 0
    for s in scores:
        total += s
    return total / len(scores)

print(average_score(80, 90, 100))   # 90.0
print(average_score())              # None

# ============================================================
# TASK 6 — **kwargs: profil
# ============================================================
# MAQSAD: Kalit-so'z argumentlarini dict sifatida qabul qilish.
#
# MANTIQ:
# - **details -> barcha kalit=qiymat juftlari dictga yig'iladi
# - .items() -> kalit va qiymat juftlarini beradi

print("\n===== TASK 6 =====")

def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Anna", city="Novosibirsk", year=1)

# ============================================================
# TASK 7 — Fixed + *args + **kwargs birgalikda
# ============================================================
# MAQSAD: Uch xil argument turini birlashtirish.
#
# TARTIB MUHIM: fixed -> *args -> **kwargs

print("\n===== TASK 7 =====")

def course_report(student, *scores, **options):
    print("Student:", student)
    print("Scores:", scores)        # tuple
    print("Options:", options)      # dict

course_report(
    "Mira",
    80, 92, 75,
    rounded=True,
    scale=100
)

# ============================================================
# TASK 8 — Scope (ko'rinish doirasi)
# ============================================================
# MAQSAD: Global va local o'zgaruvchilar farqini tushunish.
#
# MANTIQ:
# - TAX_RATE -> global (fayl darajasida)
# - tax -> local (faqat funksiya ichida mavjud)
# - Global o'zgaruvchini funksiya ichida O'QISH mumkin

print("\n===== TASK 8 =====")

TAX_RATE = 0.20     # global o'zgaruvchi

def final_price(price):
    tax = price * TAX_RATE   # TAX_RATE - global, tax - local
    return price + tax

print(final_price(100))      # 120.0
# print(tax)                 # XATO! tax faqat funksiya ichida mavjud

# ============================================================
# TASK 9 — Rekursiv sanoq (countdown)
# ============================================================
# MAQSAD: Rekursiyani birinchi marta ko'rish.
#
# MANTIQ:
# - Base case (asosiy holat): n == 0 -> "Go!" va to'xtash
# - Recursive case: n > 0 -> n chiqaramiz va countdown(n-1) chaqiramiz
#
# MUHIM: tsikl ISHLATILMAYDI!

print("\n===== TASK 9 =====")

def countdown(n):
    if n == 0:
        print("Go!")            # base case
        return                  # funksiyadan chiqamiz
    print(n)                    # hozirgi qiymat
    countdown(n - 1)            # rekursiv chaqiruv

countdown(3)

# ============================================================
# TASK 10 — Rekursiv faktorial
# ============================================================
# MAQSAD: n! ni rekursiya bilan hisoblash.
#
# MANTIQ:
# - n < 0 -> None (xato)
# - n == 0 -> 1 (base case: 0! = 1)
# - n > 0 -> n * factorial(n-1)

print("\n===== TASK 10 =====")

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1                       # base case
    return n * factorial(n - 1)        # rekursiv qadam

print(factorial(5))    # 120
print(factorial(0))    # 1
print(factorial(-2))   # None

# ============================================================
# TASK 11 — Rekursiv yig'indi
# ============================================================
# MAQSAD: 1 + 2 + ... + n ni rekursiya bilan.
#
# MANTIQ:
# - n < 0 -> None
# - n == 0 -> 0 (base case)
# - n > 0 -> n + sum_to(n-1)

print("\n===== TASK 11 =====")

def sum_to(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    return n + sum_to(n - 1)

print(sum_to(4))    # 10
print(sum_to(0))    # 0

# ============================================================
# TASK 12 — math moduli va list metodlari
# ============================================================
# MAQSAD: math.pi, math.ceil, math.floor va list metodlarini o'rganish.

print("\n===== TASK 12 — A qism (math) =====")

# radius ni so'raymiz
radius = float(input("Aylana radiusi: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Circumference:", circumference)
print("Area:", area)
print("Area ceil:", math.ceil(area))     # yuqoriga yaxlitlaydi
print("Area floor:", math.floor(area))   # pastga yaxlitlaydi

print("\n===== TASK 12 — B qism (list metodlari) =====")

numbers = [10, 20, 20, 30]

numbers.append(40)              # oxiriga qo'shadi
numbers.extend([50, 60])        # ro'yxatni kengaytiradi
numbers.insert(1, 15)           # 1-indeksga 15 qo'yadi
print("20 soni necha marta:", numbers.count(20))
print("Birinchi 30 indeksi:", numbers.index(30))
numbers.remove(20)              # birinchi 20 ni o'chiradi
removed = numbers.pop()         # oxirgi elementni oladi va o'chiradi
print("numbers:", numbers)
print("removed:", removed)

# ============================================================
# BONUS TASK 13 — Rekursiv raqamlar yig'indisi
# ============================================================
# MAQSAD: Sondagi barcha raqamlar yig'indisini rekursiya bilan.
#
# MANTIQ:
# - n < 10 -> n (bir xonali son)
# - aks holda -> (n % 10) + digit_sum(n // 10)
#
# n % 10 -> oxirgi raqam
# n // 10 -> oxirgi raqam olib tashlangan son

print("\n===== BONUS TASK 13 =====")

def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)

print(digit_sum(1234))   # 10
print(digit_sum(7))      # 7

# ============================================================
# BONUS TASK 14 — Talaba natijalari xulosasi
# ============================================================
# MAQSAD: *args + **kwargs + shartlar birgalikda.
#
# MANTIQ:
# - scores bo'sh -> "No scores"
# - average -> o'rtacha
# - passed -> passing dan katta yoki teng ballar soni

print("\n===== BONUS TASK 14 =====")

def result_summary(name, *scores, passing=60):
    if len(scores) == 0:
        return "No scores"
    
    total = 0
    passed = 0
    for s in scores:
        total += s
        if s >= passing:
            passed += 1
    
    avg = total / len(scores)
    return f"{name}: average={avg}, passed={passed}/{len(scores)}"

print(result_summary("Anna", 80, 70, 50, 120, passing=60))

# ============================================================
# TASK 15 — Validatsiyali funksiya
# ============================================================
# MAQSAD: Kirish qiymatlarini tekshirish.
#
# MANTIQ:
# - price > 0 bo'lishi kerak
# - 0 <= discount <= 100 bo'lishi kerak
# - Aks holda -> None

print("\n===== TASK 15 =====")

def calculate_discount(price, discount=10):
    if price <= 0:
        return None
    if discount < 0 or discount > 100:
        return None
    return price - price * discount / 100

print(calculate_discount(100))         # 90.0
print(calculate_discount(200, 25))     # 150.0
print(calculate_discount(100, 120))    # None
print(calculate_discount(-20, 10))     # None

# ============================================================
# TASK 16 — *args bilan min va max
# ============================================================
# MAQSAD: min() va max() siz oraliqni topish.
#
# MANTIQ:
# - Bo'sh -> None
# - Birinchi elementni smallest/largest qilib olamiz
# - Qolganlarini solishtiramiz

print("\n===== TASK 16 =====")

def score_range(*scores):
    if len(scores) == 0:
        return None
    
    smallest = scores[0]
    largest = scores[0]
    
    for s in scores:
        if s < smallest:
            smallest = s
        if s > largest:
            largest = s
    
    return largest - smallest

print(score_range(10, 30, 20, 50))   # 40
print(score_range(5))                # 0
print(score_range())                 # None

# ============================================================
# TASK 17 — Limitdan yuqori qiymatlarni sanash
# ============================================================
# MAQSAD: Berilgan limitdan katta sonlarni sanash.

print("\n===== TASK 17 =====")

def count_above(limit, *numbers):
    count = 0
    for n in numbers:
        if n > limit:
            count += 1
    return count

print(count_above(10, 5, 12, 30, 7, 20))   # 3
print(count_above(100, 10, 20, 30))        # 0
print(count_above(5))                      # 0

# ============================================================
# TASK 18 — **kwargs: konfiguratsiya
# ============================================================
# MAQSAD: Sozlamalarni chiqarish.

print("\n===== TASK 18 =====")

def show_settings(**settings):
    if len(settings) == 0:
        print("No settings")
        return
    for key, value in settings.items():
        print(f"{key} = {value}")

show_settings(language="Python", version=3.12, debug=True)
show_settings()

# ============================================================
# TASK 19 — math: ikki nuqta orasidagi masofa
# ============================================================
# MAQSAD: Evklid masofasini hisoblash.
#
# FORMULA: sqrt((x2-x1)^2 + (y2-y1)^2)

print("\n===== TASK 19 =====")

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx ** 2 + dy ** 2)

print(distance(0, 0, 3, 4))   # 5.0

# ============================================================
# TASK 20 — List amallari: xarid ro'yxati
# ============================================================
# MAQSAD: List metodlarini amalda qo'llash.

print("\n===== TASK 20 =====")

shopping = ["bread", "milk", "eggs"]
shopping.append("rice")
shopping.insert(1, "coffee")
shopping.extend(["tea", "sugar"])
shopping.remove("milk")
print("eggs indeksi:", shopping.index("eggs"))
print("bread soni:", shopping.count("bread"))
removed_item = shopping.pop()
print("shopping:", shopping)
print("removed_item:", removed_item)

# ============================================================
# TASK 21 — CHALLENGE: Rekursiv daraja
# ============================================================
# MAQSAD: base^exponent ni rekursiya bilan.
#
# MANTIQ:
# - exponent == 0 -> 1
# - aks holda -> base * power(base, exponent-1)

print("\n===== TASK 21 =====")

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))    # 32
print(power(3, 3))    # 27
print(power(10, 0))   # 1

# ============================================================
# TASK 22 — CHALLENGE: Rekursiv raqam sanash
# ============================================================
# MAQSAD: Sondagi raqamlar sonini rekursiya bilan.
#
# MANTIQ:
# - n < 10 -> 1 (bir xonali)
# - aks holda -> 1 + count_digits(n // 10)

print("\n===== TASK 22 =====")

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(7))       # 1
print(count_digits(1234))    # 4
print(count_digits(10000))   # 5

# ============================================================
# TASK 23 — CHALLENGE: Rekursiv ro'yxat yig'indisi
# ============================================================
# MAQSAD: Ro'yxat elementlarini rekursiya bilan qo'shish.
#
# MANTIQ:
# - Bo'sh ro'yxat -> 0
# - aks holda -> numbers[0] + recursive_sum(numbers[1:])

print("\n===== TASK 23 =====")

def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

print(recursive_sum([10, 20, 30]))   # 60
print(recursive_sum([5]))            # 5
print(recursive_sum([]))             # 0

# ============================================================
# TASK 24 — CHALLENGE: Imtihon statistikasi
# ============================================================
# MAQSAD: Bir tsiklda barcha statistikani hisoblash.

print("\n===== TASK 24 =====")

def exam_statistics(student, *scores, passing=60):
    if len(scores) == 0:
        return "No scores"
    
    total = 0
    highest = scores[0]
    lowest = scores[0]
    passed = 0
    failed = 0
    
    for s in scores:
        total += s
        if s > highest:
            highest = s
        if s < lowest:
            lowest = s
        if s >= passing:
            passed += 1
        else:
            failed += 1
    
    avg = total / len(scores)
    return (f"{student}: average={avg}, highest={highest}, "
            f"lowest={lowest}, passed={passed}, failed={failed}")

print(exam_statistics("Anna", 80, 70, 50, 90, passing=60))

# ============================================================
# TASK 25 — Bir nechta qiymat qaytaruvchi funksiya
# ============================================================
# MAQSAD: min va max ni qo'lda topish, ikkalasini qaytarish.

print("\n===== TASK 25 =====")

def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest

smallest, largest = min_max([5, 2, 9, 1, 7])
print("smallest:", smallest)   # 1
print("largest:", largest)     # 9

# ============================================================
# TASK 26 — Harorat konvertori
# ============================================================
# MAQSAD: C <-> F konvertatsiyasi.

print("\n===== TASK 26 =====")

def convert_temperature(value, unit="C"):
    if unit == "C":
        return value * 9 / 5 + 32
    elif unit == "F":
        return (value - 32) * 5 / 9
    else:
        return None

print(convert_temperature(0))         # 32.0
print(convert_temperature(100))       # 212.0
print(convert_temperature(32, "F"))   # 0.0
print(convert_temperature(10, "K"))   # None

# ============================================================
# TASK 27 — Qiymatni qo'lda topish
# ============================================================
# MAQSAD: index() siz qiymat indeksini topish.

print("\n===== TASK 27 =====")

def find_value(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

print(find_value([10, 20, 30, 20], 20))   # 1
print(find_value([1, 2, 3], 5))           # -1

# ============================================================
# TASK 28 — Barcha mos keluvchi elementlarni o'chirish
# ============================================================
# MAQSAD: Ro'yxatdan barcha bir xil qiymatlarni o'chirish.
#
# MANTIQ:
# - while value in numbers -> remove(value)
# - Yoki: count() bilan takrorlash

print("\n===== TASK 28 =====")

def remove_all(numbers, value):
    while value in numbers:
        numbers.remove(value)

numbers = [10, 20, 20, 30, 20]
remove_all(numbers, 20)
print(numbers)   # [10, 30]

# ============================================================
# TASK 29 — Rekursiv ko'paytirish
# ============================================================
# MAQSAD: * operatorisiz ko'paytirish (faqat + va rekursiya).
#
# MANTIQ:
# - b == 0 -> 0
# - aks holda -> a + multiply(a, b-1)

print("\n===== TASK 29 =====")

def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

print(multiply(5, 3))    # 15
print(multiply(10, 0))   # 0
print(multiply(-2, 4))   # -8

# ============================================================
# TASK 30 — Rekursiv Fibonachchi
# ============================================================
# MAQSAD: Fibonachchi sonini rekursiya bilan.
#
# MANTIQ:
# - n == 0 -> 0
# - n == 1 -> 1
# - aks holda -> fib(n-1) + fib(n-2)

print("\n===== TASK 30 =====")

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(6))   # 8

# ============================================================
# TASK 31 — math: gipotenuza
# ============================================================
# MAQSAD: To'g'ri burchakli uchburchak gipotenuzasi.

print("\n===== TASK 31 =====")

def hypotenuse(a, b):
    if a <= 0 or b <= 0:
        return None
    return math.sqrt(a ** 2 + b ** 2)

print(hypotenuse(3, 4))     # 5.0
print(hypotenuse(5, 12))    # 13.0
print(hypotenuse(-3, 4))    # None

# ============================================================
# TASK 32 — Ro'yxatni o'zgartiruvchi funksiya
# ============================================================
# MAQSAD: Ro'yxat mutable ekanligini ko'rsatish.

print("\n===== TASK 32 =====")

def add_student(students, name):
    students.append(name)   # return yo'q -> None qaytaradi

students = ["Anna", "Alex"]
result = add_student(students, "Mira")
print(students)   # ['Anna', 'Alex', 'Mira']
print(result)     # None

# ============================================================
# TASK 33 — return va print farqi
# ============================================================
# MAQSAD: print va return orasidagi farqni ko'rsatish.

print("\n===== TASK 33 =====")

def square_print(n):
    print(n ** 2)      # faqat chiqaradi, return yo'q

def square_return(n):
    return n ** 2      # qiymat qaytaradi

a = square_print(5)    # ekranga 25 chiqadi, a = None
b = square_return(5)   # b = 25
print("a:", a)         # None
print("b:", b)         # 25

# ============================================================
# TASK 34 — Bo'sh return
# ============================================================
# MAQSAD: return (bo'sh) -> None qaytarishini ko'rsatish.

print("\n===== TASK 34 =====")

def check_age(age):
    if age < 0:
        print("Invalid age")
        return           # return None bilan bir xil
    print("Valid age")

result1 = check_age(-5)   # Invalid age
result2 = check_age(20)   # Valid age
print("result1:", result1)   # None
print("result2:", result2)   # None

# ============================================================
# TASK 35 — *args bilan son statistikasi
# ============================================================
# MAQSAD: sum/min/max siz to'rt qiymatni hisoblash.

print("\n===== TASK 35 =====")

def number_statistics(*numbers):
    if len(numbers) == 0:
        return None
    
    total = 0
    smallest = numbers[0]
    largest = numbers[0]
    
    for n in numbers:
        total += n
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    
    average = total / len(numbers)
    return total, average, smallest, largest

total, average, smallest, largest = number_statistics(5, 10, 2, 13)
print("total:", total)         # 30
print("average:", average)     # 7.5
print("smallest:", smallest)   # 2
print("largest:", largest)     # 13

# ============================================================
# TASK 36 — Ro'yxat elementlarini rekursiv yig'ish
# ============================================================
# MAQSAD: Task 23 bilan bir xil mantiq.

print("\n===== TASK 36 =====")

def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

print(recursive_sum([1, 2, 3, 4]))   # 10
print(recursive_sum([10]))           # 10
print(recursive_sum([]))             # 0

# ============================================================
# TASK 37 — List metodlari bilan ro'yxatni teskari aylantirish
# ============================================================
# MAQSAD: .reverse() list metodini ishlatish.

print("\n===== TASK 37 =====")

def reverse_list(numbers):
    numbers.reverse()    # in-place (joyida) o'zgartiradi
    # return yo'q -> None

numbers = [1, 2, 3, 4]
result = reverse_list(numbers)
print(numbers)   # [4, 3, 2, 1]
print(result)    # None

# ============================================================
# TASK 38 — math: eng yaqin butun son
# ============================================================
# MAQSAD: floor va ceil farqini o'rganish.
#
# MUHIM:
# - floor(-4.7) -> -5 (pastga, ya'ni kichikroq tomonga)
# - ceil(-4.7)  -> -4 (yuqoriga, ya'ni kattaroq tomonga)

print("\n===== TASK 38 =====")

def rounding_report(number):
    print("Original:", number)
    print("Floor:", math.floor(number))   # pastga
    print("Ceil:", math.ceil(number))     # yuqoriga

rounding_report(4.7)
print()
rounding_report(-4.7)

# ============================================================
# YAKUNIY XULOSA
# ============================================================
"""
BU LABDA O'RGANILGAN ASOSIY TUSHUNCHALAR:
------------------------------------------

1. ARGUMENTLAR
   - Pozitsion: describe_student("Anna", 23, "NSK")
   - Kalit-so'z: describe_student(name="Anna", age=23, city="NSK")
   - Default:   def f(weight, rate=2.5)
   - *args:     istalgan sonda pozitsion (tuple)
   - **kwargs:  istalgan sonda kalit-so'z (dict)

2. TARTIB (funksiya e'lonida)
   def f(fixed, *args, **kwargs)

3. RETURN vs PRINT
   - print -> ekranga chiqaradi, None qaytaradi
   - return -> qiymat qaytaradi (return yo'q bo'lsa ham None)
   - return (bo'sh) -> return None bilan bir xil

4. SCOPE
   - Global -> fayl darajasida
   - Local  -> funksiya ichida
   - Funksiya globalni O'QISHI mumkin, lekin o'zgartirish uchun global kerak

5. REKURSIYA
   - Base case (to'xtash sharti) SHART
   - Recursive case -> funksiya o'zini chaqiradi
   - Har bir chaqiruvda muammo KICHRAYISHI kerak

6. MATH MODULI
   - math.pi, math.sqrt, math.ceil, math.floor

7. LIST METODLARI
   - append, extend, insert, remove, pop, index, count, reverse

8. MUHIM MASLAHATLAR
   - Ro'yxat mutable -> funksiya ichida o'zgartirilsa, tashqarida ham o'zgaradi
   - Rekursiyada har doim base case bo'lsin
   - *args tuple, **kwargs dict qaytaradi
"""