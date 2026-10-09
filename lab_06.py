"""
============================================================
NSU Python — Lab 06
Funksiyalar qiymat sifatida: lambda, saralash, filtrlash, map
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 24 ta topshiriq ketma-ket yechilgan:
- Task 1-12: asosiy topshiriqlar
- Task 13-14: bonus
- Task 15-24: qo'shimcha mashqlar

ASOSIY TUSHUNCHALAR:
--------------------
- Funksiyalar ham qiymat (obyekt) -> o'zgaruvchiga saqlash mumkin
- Yuqori tartibli funksiya (higher-order) -> funksiyani argument sifatida oladi
- lambda -> bir qatorli anonim funksiya
- sorted() -> YANGI ro'yxat qaytaradi (asl o'zgarmaydi)
- list.sort() -> JOYIDA saralaydi, None qaytaradi
- key=... -> saralash mezonini belgilaydi
- filter() -> shartni bajaruvchi elementlarni qoldiradi
- map() -> har bir elementga funksiya qo'llaydi

MUHIM:
------
- filter() va map() "iterator" qaytaradi -> list() ga o'rash kerak
- sorted() asl ro'yxatni O'ZGARTIRMAYDI
- list.sort() asl ro'yxatni O'ZGARTIRADI va None qaytaradi
"""

# ============================================================
# TASK 1 — Funksiyalar qiymat sifatida
# ============================================================
# MAQSAD: Funksiya ham obyekt ekanligini tushunish.
#
# MANTIQ:
# - operation = square -> funksiya obyektini saqlaymiz
# - operation = square() -> funksiyani DARHOL chaqiradi (natijani saqlaydi)

print("\n===== TASK 1 =====")

def square(number):
    return number ** 2

operation = square           # QAVSSIZ! funksiya obyektini saqlaymiz
print(square(5))             # 25
print(operation(5))          # 25 - bir xil ishlaydi
print(operation is square)   # True - bir xil obyekt

# ============================================================
# TASK 2 — Funksiyani argument sifatida uzatish
# ============================================================
# MAQSAD: Yuqori tartibli funksiya (higher-order function).
#
# MANTIQ:
# - apply(operation, value) -> operation ni chaqiradi
# - operation - bu funksiya, uni QAVSSIZ uzatamiz

print("\n===== TASK 2 =====")

def double(number):
    return number * 2

def triple(number):
    return number * 3

def apply(operation, value):
    return operation(value)   # operation ni chaqiramiz

print(apply(double, 5))       # 10
print(apply(triple, 5))       # 15

# ============================================================
# TASK 3 — Yuqori tartibli funksiya (transform)
# ============================================================
# MAQSAD: Har bir elementga funksiya qo'llash.
#
# MANTIQ:
# - Bo'sh ro'yxat yaratamiz
# - Har bir element uchun operation(value) chaqiramiz
# - Natijalarni qo'shamiz

print("\n===== TASK 3 =====")

def transform(values, operation):
    result = []
    for v in values:
        result.append(operation(v))
    return result

def square(number):
    return number ** 2

print(transform([1, 2, 3, 4], square))   # [1, 4, 9, 16]

# ============================================================
# TASK 4 — Lambda ifodalar
# ============================================================
# MAQSAD: Bir qatorli anonim funksiyalar.
#
# MANTIQ:
# - lambda parametrlar: ifoda
# - ifoda natijasi qaytariladi (return shart emas!)
# - lambda ni o'zgaruvchiga saqlash mumkin

print("\n===== TASK 4 =====")

double = lambda x: x * 2
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0

print(double(5))      # 10
print(add(3, 4))      # 7
print(is_even(8))     # True
print(is_even(7))     # False

# ============================================================
# TASK 5 — sorted() va list.sort() farqi
# ============================================================
# MAQSAD: Ikki saralash usuli orasidagi farqni tushunish.
#
# MANTIQ:
# - sorted(numbers) -> YANGI ro'yxat qaytaradi, asl o'zgarmaydi
# - numbers.sort() -> JOYIDA saralaydi, None qaytaradi

print("\n===== TASK 5 =====")

numbers = [8, 3, 10, 1, 6]

# A qism: sorted() -> yangi ro'yxat
ordered = sorted(numbers)
print("numbers:", numbers)     # [8, 3, 10, 1, 6] - o'zgarmadi
print("ordered:", ordered)     # [1, 3, 6, 8, 10]

# B qism: list.sort() -> joyida saralaydi
numbers.sort()
print("numbers (sort dan keyin):", numbers)   # [1, 3, 6, 8, 10]

result = numbers.sort()        # sort() None qaytaradi!
print("result:", result)       # None

# ============================================================
# TASK 6 — Teskari tartibda saralash
# ============================================================
# MAQSAD: reverse=True parametri.
#
# MANTIQ:
# - sorted(scores, reverse=True) -> kattadan kichikka
# - Asl ro'yxat o'zgarmaydi

print("\n===== TASK 6 =====")

scores = [82, 95, 73, 88, 61]
high_to_low = sorted(scores, reverse=True)
print("high_to_low:", high_to_low)   # [95, 88, 82, 73, 61]
print("scores:", scores)             # o'zgarmadi

# ============================================================
# TASK 7 — key bilan saralash
# ============================================================
# MAQSAD: key funksiyasi orqali saralash mezoni.
#
# MANTIQ:
# - key=len -> har bir so'zning uzunligi bo'yicha saralaydi
# - reverse=True -> teskari tartib

print("\n===== TASK 7 =====")

words = ["pear", "watermelon", "fig", "banana", "kiwi"]

shortest_first = sorted(words, key=len)
longest_first = sorted(words, key=len, reverse=True)

print("shortest_first:", shortest_first)   # ['fig', 'pear', 'kiwi', 'banana', 'watermelon']
print("longest_first:", longest_first)     # teskari

# ============================================================
# TASK 8 — Katta-kichik harflarga sezgir bo'lmagan saralash
# ============================================================
# MAQSAD: key=str.lower orqali registrga sezgir bo'lmagan saralash.
#
# MANTIQ:
# - str.lower -> harflarni kichik harflarga aylantiruvchi metod
# - key=str.lower -> barcha so'zlarni kichik harfga aylantirib saralaydi
# - Asl so'zlar o'zgartirilmaydi (faqat taqqoslashda ishlatiladi)

print("\n===== TASK 8 =====")

cities = ["berlin", "Algiers", "cairo", "Amsterdam", "zurich"]
ordered_cities = sorted(cities, key=str.lower)
print("ordered_cities:", ordered_cities)
# ['Algiers', 'Amsterdam', 'berlin', 'cairo', 'zurich']

# ============================================================
# TASK 9 — Lambda bilan tuplelarni saralash
# ============================================================
# MAQSAD: lambda orqali tuple elementiga murojaat.
#
# MANTIQ:
# - student[1] -> tuple ning ikkinchi elementi (ball)
# - reverse=True -> kattadan kichikka

print("\n===== TASK 9 =====")

students = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
    ("Daniel", 73)
]

sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("sorted_students:", sorted_students)
# [('Boris', 95), ('Mira', 88), ('Anna', 82), ('Daniel', 73)]

# ============================================================
# TASK 10 — filter() bilan filtrlash
# ============================================================
# MAQSAD: Shartni bajaruvchi elementlarni qoldirish.
#
# MANTIQ:
# - filter(funksiya, ketma-ketlik) -> iterator qaytaradi
# - list() ga o'rash kerak
# - lambda True qaytarsa -> element qoladi

print("\n===== TASK 10 =====")

scores = [45, 70, 82, 39, 91, 60, 58]
passing = list(filter(lambda s: s >= 60, scores))
print("passing:", passing)   # [70, 82, 91, 60]

# ============================================================
# TASK 11 — map() bilan o'zgartirish
# ============================================================
# MAQSAD: Har bir elementga funksiya qo'llash.
#
# MANTIQ:
# - map(funksiya, ketma-ketlik) -> iterator qaytaradi
# - lambda har bir narxni 1.1 ga ko'paytiradi (10% oshirish)

print("\n===== TASK 11 =====")

prices = [100, 250, 80, 40]
new_prices = list(map(lambda p: p * 1.1, prices))
print("new_prices:", new_prices)   # [110.0, 275.0, 88.0, 44.0]

# ============================================================
# TASK 12 — filter, sorted va map birgalikda
# ============================================================
# MAQSAD: Uchta amalni ketma-ket bajarish (pipeline).
#
# MANTIQ:
# 1. filter -> faqat o'tganlar
# 2. sorted -> ball bo'yicha kamayish tartibida
# 3. map -> faqat ismlarni olish

print("\n===== TASK 12 =====")

students = [
    {"name": "Anna", "score": 82},
    {"name": "Boris", "score": 55},
    {"name": "Mira", "score": 91},
    {"name": "Daniel", "score": 67},
    {"name": "Sara", "score": 48}
]

# 1-qadam: faqat o'tganlar (score >= 60)
passing_students = list(filter(lambda s: s["score"] >= 60, students))

# 2-qadam: ball bo'yicha kamayish tartibida
sorted_students = sorted(passing_students, key=lambda s: s["score"], reverse=True)

# 3-qadam: faqat ismlar
names = list(map(lambda s: s["name"], sorted_students))

print("names:", names)   # ['Mira', 'Anna', 'Daniel']

# ============================================================
# BONUS TASK 13 — Bir nechta mezon bilan saralash
# ============================================================
# MAQSAD: Turli kalitlar bilan saralash.

print("\n===== BONUS TASK 13 =====")

products = [
    {"name": "Keyboard", "price": 70},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 220},
    {"name": "USB Cable", "price": 10}
]

# Narx bo'yicha (arzon -> qimmat)
by_price = sorted(products, key=lambda p: p["price"])

# Nom uzunligi bo'yicha (qisqa -> uzun)
by_name_length = sorted(products, key=lambda p: len(p["name"]))

print("by_price:")
for p in by_price:
    print(" ", p)

print("by_name_length:")
for p in by_name_length:
    print(" ", p)

# ============================================================
# BONUS TASK 14 — Talaba reytingi pipeline
# ============================================================
# MAQSAD: filter + sorted + map to'liq pipeline.

print("\n===== BONUS TASK 14 =====")

students = [
    ("Anna", 82),
    ("Boris", 55),
    ("Mira", 91),
    ("Daniel", 67),
    ("Sara", 48),
    ("Omar", 76)
]

# 1. Ball >= 60
passing = list(filter(lambda s: s[1] >= 60, students))

# 2. Ball bo'yicha kamayish tartibida
ranked = sorted(passing, key=lambda s: s[1], reverse=True)

# 3. "Name: score" formatiga o'tkazish
ranking = list(map(lambda s: f"{s[0]}: {s[1]}", ranked))

print("ranking:", ranking)
# ['Mira: 91', 'Anna: 82', 'Omar: 76', 'Daniel: 67']

# ============================================================
# TASK 15 — Noldan masofa bo'yicha saralash
# ============================================================
# MAQSAD: key=abs orqali absolyut qiymat bo'yicha saralash.

print("\n===== TASK 15 =====")

numbers = [-10, 3, -2, 8, -7, 1]
ordered = sorted(numbers, key=abs)
print("ordered:", ordered)   # [1, -2, 3, -7, 8, -10]

# ============================================================
# TASK 16 — Oxirgi harf bo'yicha saralash
# ============================================================
# MAQSAD: word[-1] orqali oxirgi harfni olish.

print("\n===== TASK 16 =====")

words = ["apple", "banana", "kiwi", "orange", "pear"]
ordered_words = sorted(words, key=lambda w: w[-1])
print("ordered_words:", ordered_words)
# ['banana', 'orange', 'apple', 'pear', 'kiwi']
# (oxirgi harflar: a, e, e, r, i)

# ============================================================
# TASK 17 — Manfiy sonlarni filtrlash
# ============================================================
# MAQSAD: filter + lambda bilan manfiy sonlarni olish.

print("\n===== TASK 17 =====")

numbers = [5, -3, 8, -1, 0, 12, -7, 4]
negatives = list(filter(lambda n: n < 0, numbers))
print("negatives:", negatives)   # [-3, -1, -7]

# ============================================================
# TASK 18 — So'zlarni uzunligi bo'yicha filtrlash
# ============================================================
# MAQSAD: len() va lambda birgalikda.

print("\n===== TASK 18 =====")

words = ["cat", "python", "AI", "computer", "data", "algorithm"]
long_words = list(filter(lambda w: len(w) >= 5, words))
print("long_words:", long_words)   # ['python', 'computer', 'algorithm']

# ============================================================
# TASK 19 — Haroratni map() bilan o'zgartirish
# ============================================================
# MAQSAD: C -> F formula bilan map.

print("\n===== TASK 19 =====")

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print("fahrenheit:", fahrenheit)   # [32.0, 50.0, 68.0, 86.0, 104.0]

# ============================================================
# TASK 20 — Dict qiymatlarini map() bilan olish
# ============================================================
# MAQSAD: Ro'yxatdagi dictlardan faqat bitta maydonni olish.

print("\n===== TASK 20 =====")

students = [
    {"name": "Anna", "age": 22},
    {"name": "Boris", "age": 24},
    {"name": "Mira", "age": 21},
    {"name": "Daniel", "age": 25}
]

names = list(map(lambda s: s["name"], students))
print("names:", names)   # ['Anna', 'Boris', 'Mira', 'Daniel']

# ============================================================
# TASK 21 — Alifbo bo'yicha saralash (registrga sezgir emas)
# ============================================================
# MAQSAD: student[0].lower() orqali.

print("\n===== TASK 21 =====")

students = [
    ("Mira", 91),
    ("anna", 82),
    ("Daniel", 67),
    ("boris", 55)
]

ordered = sorted(students, key=lambda s: s[0].lower())
for s in ordered:
    print(" ", s)
# anna, boris, Daniel, Mira

# ============================================================
# TASK 22 — Bir nechta qiymat bo'yicha saralash
# ============================================================
# MAQSAD: Tuple key orqali bir nechta mezon.
#
# MANTIQ:
# - Ball bo'yicha KAMAYISH tartibida -> -s[1] ishlatamiz
# - Teng bo'lsa -> ism bo'yicha O'SISH tartibida -> s[0]
# - Tuple key: (-s[1], s[0])
#
# NEGA -s[1]? reverse=True ishlatsak, ism ham teskari bo'ladi.
# Shuning uchun ballni manfiy qilib, "kamayish" effektini olamiz.

print("\n===== TASK 22 =====")

students = [
    ("Anna", 80),
    ("Boris", 90),
    ("Mira", 80),
    ("Daniel", 90),
    ("Sara", 70)
]

ordered = sorted(students, key=lambda s: (-s[1], s[0]))
print("ordered:", ordered)
# [('Boris', 90), ('Daniel', 90), ('Anna', 80), ('Mira', 80), ('Sara', 70)]

# ============================================================
# TASK 23 — Filtrlash va o'zgartirish
# ============================================================
# MAQSAD: filter + map ketma-ket.

print("\n===== TASK 23 =====")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda n: n % 2 == 0, numbers)      # juftlar
squares = list(map(lambda n: n ** 2, evens))       # kvadratlar
print("squares:", squares)   # [4, 16, 36, 64, 100]

# ============================================================
# TASK 24 — Mahsulot chegirma tizimi
# ============================================================
# MAQSAD: filter + map + sorted to'liq pipeline.
#
# MANTIQ:
# 1. Narxi >= 50 bo'lganlar
# 2. 20% chegirma qo'llash
# 3. Arzon -> qimmat tartibida saralash
#
# MUHIM: Asl ro'yxatni o'zgartirmaslik uchun map ichida
# YANGI dict yaratamiz.

print("\n===== TASK 24 =====")

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300},
    {"name": "USB Cable", "price": 10}
]

# 1. Narxi >= 50
expensive = filter(lambda p: p["price"] >= 50, products)

# 2. 20% chegirma -> yangi dict yaratamiz
discounted = map(
    lambda p: {"name": p["name"], "price": p["price"] * 0.8},
    expensive
)

# 3. Arzon -> qimmat
result = sorted(discounted, key=lambda p: p["price"])

for p in result:
    print(" ", p)
# Keyboard 64.0, Monitor 240.0, Laptop 960.0

# ============================================================
# YAKUNIY XULOSA
# ============================================================
"""
BU LABDA O'RGANILGAN ASOSIY TUSHUNCHALAR:
------------------------------------------

1. FUNKSIYALAR QIYMAT SIFATIDA
   - operation = square       -> funksiya obyektini saqlaydi
   - operation = square()     -> funksiyani DARHOL chaqiradi
   - operation is square      -> bir xil obyektni tekshiradi

2. YUQORI TARTIBLI FUNKSIYALAR
   - Funksiyani argument sifatida qabul qiladi
   - Funksiyani qaytaradi
   - Misol: apply(operation, value), transform(values, operation)

3. LAMBDA
   - lambda parametrlar: ifoda
   - Bir qatorli, nomsiz funksiya
   - O'zgaruvchiga saqlash mumkin: double = lambda x: x * 2

4. SORTED() vs LIST.SORT()
   - sorted(lst)      -> YANGI ro'yxat, asl o'zgarmaydi
   - lst.sort()       -> JOYIDA saralaydi, None qaytaradi

5. KEY PARAMETRI
   - key=len            -> uzunlik bo'yicha
   - key=str.lower      -> registrga sezgir emas
   - key=abs            -> absolyut qiymat bo'yicha
   - key=lambda x: ...  -> o'z funksiyangiz

6. FILTER()
   - filter(funksiya, ketma-ketlik)
   - funksiya True qaytarsa -> element qoladi
   - list() ga o'rash kerak

7. MAP()
   - map(funksiya, ketma-ketlik)
   - har bir elementga funksiya qo'llaydi
   - list() ga o'rash kerak

8. PIPELINE
   - filter -> sorted -> map kabi ketma-ket amallar

9. TUPLE KEY BILAN BIR NECHTA MEZON
   - key=lambda s: (-s[1], s[0])
   - -s[1] -> ball bo'yicha kamayish
   - s[0]  -> ism bo'yicha o'sish

MUHIM MASLAHATLAR:
------------------
- sorted() va filter()/map() asl ma'lumotni O'ZGARTIRMAYDI
- list.sort() va list.reverse() JOYIDA o'zgartiradi
- filter()/map() iterator qaytaradi -> ko'pincha list() kerak
- lambda ni faqat qisqa ifodalar uchun ishlating
- Murakkab mantiq uchun oddiy def funksiya yozing
"""
