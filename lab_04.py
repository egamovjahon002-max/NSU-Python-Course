"""
============================================================
NSU Python — Lab 04
while tsikllar, tiplash, identifikatsiya va funksiyalar
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 30 ta topshiriq (1-13 asosiy, 14-15 bonus, 16-30 qo'shimcha)
ketma-ket yechilgan. Har bir topshiriq oldidan uning maqsadi va
mantiqi haqida batafsil izoh yozilgan.

QANDAY ISHLATISH?
-----------------
1. Faylni saqlang (masalan: lab04.py)
2. Terminalda: python lab04.py
3. Har bir topshiriq ketma-ket ishlaydi (ba'zilari input so'raydi)

MUHIM TUSHUNCHALAR (boshlovchilar uchun):
-----------------------------------------
- input()    -> foydalanuvchidan ma'lumot oladi (har doim MATN/str qaytaradi)
- int()      -> matnni butun songa aylantiradi
- float()    -> matnni o'nlik songa aylantiradi
- print()    -> ekranga chiqaradi
- while      -> shart True bo'lguncha takrorlaydi
- for        -> ketma-ketlik bo'ylab yuradi (masalan, ro'yxat)
- break      -> tsiklni darhol to'xtatadi
- continue   -> joriy qadamni o'tkazib yuboradi
- return     -> funksiyadan qiymat qaytaradi
- def        -> funksiya e'lon qiladi
"""

# ============================================================
# TASK 1 — while bilan sanoq (Countdown)
# ============================================================
# MAQSAD: Foydalanuvchi kiritgan sondan 1 gacha sanash,
#         keyin "Go!" chiqarish.
#
# MANTIQ:
# 1. Foydalanuvchidan musbat son so'raymiz
# 2. n > 0 bo'lguncha tsiklni aylantiramiz
# 3. Har qadamda n ni chiqaramiz va 1 ga kamaytiramiz
# 4. n = 0 bo'lganda tsikl tugaydi va "Go!" chiqadi

print("\n===== TASK 1 =====")

n = int(input("Musbat son kiriting: "))
# input() matn qaytaradi -> int() uni butun songa aylantiradi

while n > 0:
    # while sharti: n > 0 bo'lsa, tsikl tanasi ishlaydi
    print(n)          # hozirgi n qiymatini ekranga chiqaramiz
    n = n - 1         # n ni 1 ga kamaytiramiz
                      # MUHIM: bu qator bo'lmasa -> cheksiz tsikl!

print("Go!")          # tsikl tugagach bajariladi

# ============================================================
# TASK 2 — Nolga yetguncha takrorlash
# ============================================================
# MAQSAD: Foydalanuvchi 0 kiritguncha sonlarni qabul qilish,
#         har bir nolga teng bo'lmagan sonni sanash va yig'indisini
#         hisoblash.
#
# MANTIQ:
# - while True -> cheksiz tsikl (faqat break bilan to'xtaydi)
# - 0 kiritilsa -> break
# - Aks holda -> count va total ni yangilaymiz

print("\n===== TASK 2 =====")

count = 0     # nechta son kiritilganini sanaymiz
total = 0     # yig'indini saqlaymiz

while True:
    # while True -> shart har doim True, faqat break bilan chiqamiz
    num = int(input("Son kiriting (0 = to'xtatish): "))
    
    if num == 0:
        break     # 0 kiritilsa, tsikldan chiqamiz
    
    count += 1    # count = count + 1 bilan bir xil (qisqa yozuv)
    total += num  # total = total + num bilan bir xil

print("Count:", count)
print("Sum:", total)

# ============================================================
# TASK 3 — while True bilan to'g'ri kiritishni tekshirish
# ============================================================
# MAQSAD: Foydalanuvchi 1 dan 10 gacha son kiritguncha so'rash.
#
# MANTIQ:
# - while True -> cheksiz so'rash
# - Noto'g'ri qiymat -> "Invalid value" chiqarib, davom etamiz
# - To'g'ri qiymat -> "Accepted" chiqarib, break

print("\n===== TASK 3 =====")

while True:
    num = int(input("1 dan 10 gacha son kiriting: "))
    
    if num < 1 or num > 10:
        # "or" -> ikkita shartdan BIRI True bo'lsa, umumiy True
        print("Invalid value")
        # continue shart emas, chunki tsikl avtomatik davom etadi
    else:
        print("Accepted")
        break     # to'g'ri qiymat -> tsikldan chiqamiz

# ============================================================
# TASK 4 — while tsiklida continue
# ============================================================
# MAQSAD: 1 dan 20 gacha sonlarni chiqarish, lekin 3 ga
#         bo'linadiganlarini o'tkazib yuborish.
#
# MANTIQ:
# - continue -> tsiklning qolgan qismini o'tkazib yuboradi
# - MUHIM: i ni continue dan OLDIN oshirish kerak, aks holda
#   cheksiz tsikl bo'ladi!

print("\n===== TASK 4 =====")

i = 1
while i <= 20:
    i = i + 1               # AVVAL oshiramiz (continue uchun muhim)
    
    if i % 3 == 0:
        # % -> qoldiqni topadi. 6 % 3 = 0, 7 % 3 = 1
        continue            # 3 ga bo'linsa, keyingi qadamga o'tamiz
    
    print(i)

# ============================================================
# TASK 5 — for...else bilan qidirish
# ============================================================
# MAQSAD: Ro'yxatdagi birinchi toq sonni topish.
#         Topilmasa -> "All values are even"
#
# MANTIQ:
# - for...else: else bloki FAQAT tsikl break siz tugaganda ishlaydi
# - Agar toq son topilsa -> break -> else ishlamaydi

print("\n===== TASK 5 =====")

numbers = [4, 8, 12, 16, 21, 24]

for num in numbers:
    if num % 2 != 0:        # != -> teng emas. Toq sonmi?
        print("First odd number:", num)
        break               # topdik -> to'xtaymiz
else:
    # Bu blok faqat tsikl break bilan to'xtamaganda ishlaydi
    print("All values are even")

# ============================================================
# TASK 6 — Ichma-ich tsikllar bilan ko'paytirish jadvali
# ============================================================
# MAQSAD: 5x5 ko'paytirish jadvalini chiqarish.
#
# MANTIQ:
# - Tashqi tsikl -> qatorlar (i = 1..5)
# - Ichki tsikl -> ustunlar (j = 1..5)
# - print(i*j, end=" ") -> bir qatorda chiqaradi
# - print() -> qatorni tugatadi

print("\n===== TASK 6 =====")

for i in range(1, 6):        # range(1, 6) -> 1, 2, 3, 4, 5
    for j in range(1, 6):
        print(i * j, end=" ")  # end=" " -> yangi qatorga o'tmaslik
    print()                   # qator tugadi -> yangi qator

# ============================================================
# TASK 7 — Dinamik tiplash
# ============================================================
# MAQSAD: Bitta o'zgaruvchi turli xil tiplarni saqlashi mumkinligini
#         ko'rsatish.
#
# MANTIQ:
# - Python dinamik tipli: o'zgaruvchi tipi ish paytida o'zgaradi
# - type() -> qiymatning turini qaytaradi

print("\n===== TASK 7 =====")

value = 42
print(value, type(value))    # 42 <class 'int'>

value = 3.14
print(value, type(value))    # 3.14 <class 'float'>

value = "Python"
print(value, type(value))    # Python <class 'str'>

value = [1, 2, 3]
print(value, type(value))    # [1, 2, 3] <class 'list'>

# ============================================================
# TASK 8 — Tenglik, identifikatsiya va havolalar
# ============================================================
# MAQSAD: == va is farqini tushunish.
#
# MANTIQ:
# - a == b -> QIYMATLARNI solishtiradi
# - a is b -> XOTIRADAGI MANZILNI solishtiradi
# - c = a -> yangi ro'yxat yaratmaydi, faqat havola nusxalanadi

print("\n===== TASK 8 =====")

a = [10, 20]
b = [10, 20]     # boshqa ro'yxat (boshqa obyekt, bir xil qiymat)
c = a            # bir xil obyektga havola

print("a == b:", a == b)     # True (qiymatlar teng)
print("a is b:", a is b)     # False (turli obyektlar)
print("a == c:", a == c)     # True (qiymatlar teng)
print("a is c:", a is c)     # True (bir xil obyekt)

print("id(a):", id(a))       # har xil ID
print("id(b):", id(b))       # a dan farqli
print("id(c):", id(c))       # a bilan bir xil

c.append(30)                 # c ga 30 qo'shamiz
print("a:", a)               # [10, 20, 30] - a ham o'zgardi!
print("b:", b)               # [10, 20] - b o'zgarmadi
print("c:", c)               # [10, 20, 30]

# TUSHUNTIRISH:
# c = a -> c va a bir xil ro'yxatga "ishora" qiladi.
# c ni o'zgartirsak -> a ham o'zgaradi (chunki ular bir xil obyekt).
# b mustaqil ro'yxat, shuning uchun o'zgarmadi.

# ============================================================
# TASK 9 — Funksiya: is_even
# ============================================================
# MAQSAD: Son juft yoki toq ekanligini aniqlovchi funksiya.
#
# MANTIQ:
# - Juft son -> 2 ga bo'linadi (qoldiq 0)
# - return -> True yoki False qaytaradi
# - Funksiya ICHIDA print BO'LMASLIGI kerak!

print("\n===== TASK 9 =====")

def is_even(number):
    # % 2 == 0 bo'lsa -> juft son
    return number % 2 == 0   # True yoki False qaytaradi

print(is_even(4))            # True
print(is_even(7))            # False
print(is_even(0))            # True (0 ham juft son)

# ============================================================
# TASK 10 — Funksiya: calculate_discount
# ============================================================
# MAQSAD: Chegirmadan keyingi narxni hisoblash.
#
# FORMULA: final = price - price * percent / 100
#
# MANTIQ:
# - price va percent parametr sifatida qabul qilinadi
# - Natija return bilan qaytariladi

print("\n===== TASK 10 =====")

def calculate_discount(price, percent):
    final_price = price - price * percent / 100
    return final_price

print(calculate_discount(1000, 15))   # 850.0
print(calculate_discount(250, 20))    # 200.0

# ============================================================
# TASK 11 — return va print farqi
# ============================================================
# MAQSAD: return va print orasidagi farqni ko'rsatish.
#
# MUHIM:
# - print -> ekranga chiqaradi, lekin qiymat QAYTARMAYDI (None)
# - return -> qiymatni qaytaradi, keyinchalik ishlatish mumkin

print("\n===== TASK 11 =====")

def rectangle_area(width, height):
    return width * height   # print emas, return!

result = rectangle_area(5, 4)   # natijani saqlaymiz
print("Area:", result)          # 20
print("Double:", result * 2)    # 40 - qayta ishlatish mumkin!

# Agar print ishlatilganda edi:
# def rectangle_area_bad(w, h):
#     print(w * h)
#
# x = rectangle_area_bad(5, 4)  # ekranga 20 chiqadi
# print(x * 2)                   # XATO! None * 2 ishlamaydi

# ============================================================
# TASK 12 — Bir nechta qiymat qaytaruvchi funksiya
# ============================================================
# MAQSAD: Ro'yxatdagi eng kichik va eng katta qiymatni topish.
#
# MANTIQ:
# - Boshlang'ich qiymat sifatida birinchi elementni olamiz
# - Har bir elementni solishtiramiz
# - min() va max() ishlatilmaydi!

print("\n===== TASK 12 =====")

def min_max(numbers):
    smallest = numbers[0]   # birinchi elementni boshlang'ich qiymat qilamiz
    largest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num  # yangi minimum topildi
        if num > largest:
            largest = num   # yangi maksimum topildi
    
    return smallest, largest   # ikkita qiymat qaytaramiz (tuple)

values = [7, 2, 9, -1, 5, 12, 3]
smallest, largest = min_max(values)   # unpacking
print("Smallest:", smallest)          # -1
print("Largest:", largest)            # 12

# ============================================================
# TASK 13 — Integratsiyalashgan: o'rtacha hisoblash
# ============================================================
# MAQSAD: Funksiya + while + shart + return + is None
#
# MANTIQ:
# - average(total, count) funksiyasi
# - count == 0 -> None qaytaradi (0 ga bo'lish mumkin emas)
# - Foydalanuvchidan count >= 0 bo'lguncha so'raymiz
# - Natijani 2 xona aniqlikda chiqaramiz

print("\n===== TASK 13 =====")

def average(total, count):
    if count == 0:
        return None             # 0 ga bo'lish mumkin emas
    return total / count

# count ni 0 dan katta yoki teng bo'lguncha so'raymiz
while True:
    count = int(input("Nechta son? "))
    if count >= 0:
        break

total = float(input("Yig'indi: "))

result = average(total, count)

if result is None:              # None ni "is" bilan tekshiramiz
    print("Cannot calculate average")
else:
    print(f"Average: {result:.2f}")   # :.2f -> 2 xona aniqlik

# ============================================================
# BONUS TASK 14 — Sonni topish o'yini
# ============================================================
# MAQSAD: Foydalanuvchi yashirin sonni topguncha so'rash.
#
# MANTIQ:
# - while True -> to'g'ri topilguncha davom etadi
# - Kichik -> "Too low"
# - Katta -> "Too high"
# - Teng -> "Correct" + break

print("\n===== BONUS TASK 14 =====")

secret_number = 37
attempts = 0

while True:
    guess = int(input("Sonni toping: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")
        break

print("Attempts:", attempts)

# ============================================================
# BONUS TASK 15 — Funksiya asosida son statistikasi
# ============================================================
# MAQSAD: Musbat, manfiy va nol sonlarni sanash.
#
# MANTIQ:
# - Uchta hisoblagich: positive, negative, zeros
# - Bir tsiklda barcha holatlarni tekshiramiz
# - Uchta qiymat qaytaramiz

print("\n===== BONUS TASK 15 =====")

def number_statistics(numbers):
    positive = 0
    negative = 0
    zeros = 0
    
    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zeros += 1
    
    return positive, negative, zeros

data = [3, -1, 0, 8, -5, 0, 2, -9]
pos, neg, zer = number_statistics(data)
print("Positive:", pos)     # 3
print("Negative:", neg)     # 3
print("Zero:", zer)         # 2

# ============================================================
# TASK 16 — while bilan juft sonlar yig'indisi
# ============================================================
# MAQSAD: 1 dan n gacha bo'lgan juft sonlar yig'indisi.
#
# MANTIQ:
# - i = 2 dan boshlaymiz (birinchi juft son)
# - Har qadamda i ni 2 ga oshiramiz
# - i > n bo'lganda to'xtaymiz

print("\n===== TASK 16 =====")

n = int(input("Musbat son kiriting: "))
i = 2
even_sum = 0

while i <= n:
    even_sum += i
    i += 2              # 2 qadam -> faqat juft sonlar

print("Even sum:", even_sum)

# ============================================================
# TASK 17 — 7 ga bo'linadigan birinchi son
# ============================================================
# MAQSAD: Ro'yxatdagi 7 ga bo'linadigan birinchi sonni topish.
#
# MANTIQ:
# - for...else -> break ishlamasa, else ishlaydi

print("\n===== TASK 17 =====")

numbers = [11, 17, 25, 28, 35, 41]

for num in numbers:
    if num % 7 == 0:
        print("Found:", num)
        break
else:
    print("Not found")

# ============================================================
# TASK 18 — while True bilan oddiy menyu
# ============================================================
# MAQSAD: 3 variantli menyu yaratish.
#
# MANTIQ:
# - while True -> menyu doimiy ko'rinadi
# - 1, 2, 3 -> tegishli amallar
# - 3 -> break (chiqish)
# - Boshqa -> "Invalid option"

print("\n===== TASK 18 =====")

while True:
    print("\n1 - Say hello")
    print("2 - Show a number")
    print("3 - Exit")
    
    choice = input("Tanlang: ")
    
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        num = input("Son kiriting: ")
        print("Siz kiritgan son:", num)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option")

# ============================================================
# TASK 19 — Musbat qiymatlarni sanash
# ============================================================
# MAQSAD: Ro'yxatdagi musbat, manfiy va nollarni sanash.
#
# MANTIQ: Task 15 bilan bir xil, faqat funksiyasiz.

print("\n===== TASK 19 =====")

numbers = [5, -2, 0, 8, -4, 11, 0, -1, 7]

positive = 0
negative = 0
zeros = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zeros)

# ============================================================
# TASK 20 — Raqamlar sonini aniqlash
# ============================================================
# MAQSAD: Butun sonda nechta raqam borligini aniqlash.
#
# MANTIQ:
# - Har safar n ni 10 ga butun bo'lamiz (oxirgi raqamni olib tashlaymiz)
# - 58372 // 10 = 5837
# - n = 0 bo'lganda to'xtaymiz
#
# MUHIM: str() ishlatilmaydi!

print("\n===== TASK 20 =====")

n = int(input("Musbat son kiriting: "))
digits = 0

while n > 0:
    n = n // 10         # oxirgi raqamni olib tashlaymiz
    digits += 1

print("Digits:", digits)

# ============================================================
# TASK 21 — Funksiya: absolute_value
# ============================================================
# MAQSAD: Sonning absolyut qiymatini qaytarish.
#
# MANTIQ:
# - Manfiy bo'lsa -> ishorasini o'zgartiramiz (-number)
# - Musbat yoki 0 -> o'zgarishsiz
#
# MUHIM: abs() ishlatilmaydi!

print("\n===== TASK 21 =====")

def absolute_value(number):
    if number < 0:
        return -number
    return number

print(absolute_value(10))    # 10
print(absolute_value(-7))    # 7
print(absolute_value(0))     # 0

# ============================================================
# TASK 22 — Funksiya: largest_of_three
# ============================================================
# MAQSAD: Uchta sondan eng kattasini topish.
#
# MANTIQ:
# - a ni "hozirgi eng katta" deb belgilaymiz
# - b va c ni solishtiramiz
#
# MUHIM: max() ishlatilmaydi!

print("\n===== TASK 22 =====")

def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(largest_of_three(4, 9, 2))      # 9
print(largest_of_three(10, 3, 10))    # 10
print(largest_of_three(-1, -5, -3))   # -1

# ============================================================
# TASK 23 — Qiymat va uning pozitsiyasini topish
# ============================================================
# MAQSAD: Ro'yxatdan sonni topish va pozitsiyasini (1 dan) chiqarish.
#
# MANTIQ:
# - for i in range(len(numbers)) -> indekslar bo'ylab
# - numbers[i] == target -> topildi
# - i + 1 -> 1 dan boshlanadigan pozitsiya
#
# MUHIM: index() va in ishlatilmaydi!

print("\n===== TASK 23 =====")

numbers = [12, 7, 19, 4, 7, 25]
target = int(input("Qidirilayotgan son: "))

position = 0     # 0 = topilmadi

for i in range(len(numbers)):
    if numbers[i] == target:
        position = i + 1
        break

if position > 0:
    print("Found at position:", position)
else:
    print("Not found")

# ============================================================
# TASK 24 — Parol urinishlari
# ============================================================
# MAQSAD: 3 marta parol kiritish imkoniyati.
#
# MANTIQ:
# - while attempts < max_attempts
# - To'g'ri parol -> break
# - 3 marta noto'g'ri -> while...else ishlaydi

print("\n===== TASK 24 =====")

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Parolni kiriting: ")
    attempts += 1
    
    if password == correct_password:
        print("Access granted")
        break
else:
    # Bu blok faqat tsikl break siz tugaganda ishlaydi
    print("Access denied")

# ============================================================
# TASK 25 — Funksiya: count_even
# ============================================================
# MAQSAD: Ro'yxatdagi juft sonlarni sanash.
#
# MANTIQ:
# - count = 0
# - Har bir juft son uchun count += 1
# - Natijani return qilamiz

print("\n===== TASK 25 =====")

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

values = [4, 7, 10, 13, 16, 19, 20]
print(count_even(values))    # 4

# ============================================================
# TASK 26 — Teskari sanoq namunasi
# ============================================================
# MAQSAD: Quyidagi naqshni chiqarish (n = 5 uchun):
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
#
# MANTIQ:
# - Tashqi tsikl -> qator raqami (1..n)
# - Ichki tsikl -> i dan 1 gacha kamayadi
# - range(i, 0, -1) -> i, i-1, ..., 1

print("\n===== TASK 26 =====")

n = int(input("n kiriting: "))

for i in range(1, n + 1):
    for j in range(i, 0, -1):    # i dan 1 gacha (0 kirmaydi)
        print(j, end=" ")
    print()

# ============================================================
# TASK 27 — Funksiya: classify_number
# ============================================================
# MAQSAD: Sonni turkumlash.
#
# MANTIQ:
# - Avval nolni tekshiramiz
# - Keyin ishorani (musbat/manfiy)
# - Keyin juft/toqligini

print("\n===== TASK 27 =====")

def classify_number(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        if number % 2 == 0:
            return "Positive even"
        else:
            return "Positive odd"
    else:
        if number % 2 == 0:
            return "Negative even"
        else:
            return "Negative odd"

print(classify_number(8))     # Positive even
print(classify_number(-3))    # Negative odd
print(classify_number(0))     # Zero

# ============================================================
# TASK 28 — 100 gacha yig'indi
# ============================================================
# MAQSAD: Yig'indi 100 dan oshguncha sonlar kiritish.
#
# MANTIQ:
# - total < 100 bo'lguncha tsikl ishlaydi
# - Har bir son qo'shiladi va count oshadi

print("\n===== TASK 28 =====")

total = 0
count = 0

while total < 100:
    num = int(input("Son kiriting: "))
    total += num
    count += 1

print("Total:", total)
print("Numbers entered:", count)

# ============================================================
# BONUS TASK 29 — Tub son tekshiruvi
# ============================================================
# MAQSAD: Son tub yoki tub emasligini aniqlash.
#
# MANTIQ:
# - 1 va undan kichik -> tub emas
# - 2 dan sqrt(number) gacha bo'luvchi qidiramiz
# - Bo'luvchi topilsa -> tub emas
# - Topilmasa -> tub
#
# NEGA sqrt? Agar n = a*b bo'lsa, a yoki b dan biri
# sqrt(n) dan kichik yoki teng bo'ladi. Shuning uchun
# faqat sqrt(n) gacha tekshirish yetarli.

print("\n===== BONUS TASK 29 =====")

def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        # ** 0.5 -> kvadrat ildiz
        if number % i == 0:
            return False    # bo'luvchi topildi
    
    return True

print(is_prime(2))     # True
print(is_prime(7))     # True
print(is_prime(8))     # False
print(is_prime(1))     # False

# ============================================================
# BONUS TASK 30 — Mini kalkulyator
# ============================================================
# MAQSAD: Asosiy arifmetik amallarni bajaruvchi kalkulyator.
#
# MANTIQ:
# - calculate(a, b, operation) funksiyasi
# - 0 ga bo'lish -> None
# - while True -> foydalanuvchi "no" kiritguncha davom etadi

print("\n===== BONUS TASK 30 =====")

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return None     # 0 ga bo'lish mumkin emas
        return a / b
    else:
        return None         # noma'lum amal

while True:
    a = float(input("Birinchi son: "))
    b = float(input("Ikkinchi son: "))
    op = input("Amal (+, -, *, /): ")
    
    result = calculate(a, b, op)
    
    if result is None:
        print("Xatolik: noto'g'ri amal yoki 0 ga bo'lish")
    else:
        print("Natija:", result)
    
    again = input("Continue? yes/no: ")
    if again == "no":
        break

# ============================================================
# YAKUNIY XULOSA
# ============================================================
"""
BU LABDA O'RGANILGAN ASOSIY TUSHUNCHALAR:
------------------------------------------

1. WHILE TSIKLI
   - Shart True bo'lguncha takrorlaydi
   - while True + break -> noaniq takrorlash uchun

2. BREAK VA CONTINUE
   - break -> tsiklni darhol to'xtatadi
   - continue -> joriy qadamni o'tkazib yuboradi

3. FOR...ELSE
   - else bloki faqat break ISHLAMAGANDA ishlaydi

4. FUNKSIYALAR
   - def -> funksiya e'lon qiladi
   - return -> qiymat qaytaradi
   - print vs return -> print faqat chiqaradi, return qaytaradi

5. TENGLIK VA IDENTIFIKATSIYA
   - == -> qiymatni solishtiradi
   - is -> xotiradagi manzilni solishtiradi
   - id() -> obyektning manzilini ko'rsatadi

6. DINAMIK TIPLASH
   - Bitta o'zgaruvchi turli tiplarni saqlashi mumkin

7. ICHMA-ICH TSIKLLAR
   - Tashqi tsikl -> qatorlar
   - Ichki tsikl -> ustunlar

8. FOYDALI MASLAHATLAR
   - input() har doim str qaytaradi -> int()/float() kerak
   - 0 ga bo'lishdan oldin tekshiring
   - None ni "is None" bilan tekshiring
   - while tsiklida o'zgaruvchini o'zgartirishni unutmang!
"""