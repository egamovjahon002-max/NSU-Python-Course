print("Task 1 — Built-in Functions")

values = [12, 7, 19, 5, 14]


count = len(values)
smallest = min(values)
largest = max(values)
total = sum(values)
mean = total / count

print(f"Number of values: {count}")
print(f"Smallest value: {smallest}")
print(f"Largest value: {largest}")
print(f"Total: {total}")
print(f"Mean: {mean}")

print()



print("Task 2 — Absolute Value and Rounding")

temperature_change = -7.438
measurement = 19.87654

print(f"Absolute value: {abs(temperature_change)}")

print(f"1 decimal place: {round(measurement, 1)}")
print(f"2 decimal places: {round(measurement, 2)}")
print(f"3 decimal places: {round(measurement, 3)}")

print()



print("Task 3 — Assignment and Augmented Assignment")

balance = 1000.0


balance += 250
balance -= 120
balance *= 1.05

print(f"Final balance: {balance:.2f}")

print()



print("Task 4 — Operator Precedence")

expression_1 = 2 + 3 * 4
expression_2 = (2 + 3) * 4
expression_3 = 20 / 5 + 3
expression_4 = 20 / (5 + 3)
expression_5 = 2 ** 3 ** 2

print(f"2 + 3 * 4 = {expression_1}")
print(f"(2 + 3) * 4 = {expression_2}")
print(f"20 / 5 + 3 = {expression_3}")
print(f"20 / (5 + 3) = {expression_4}")
print(f"2 ** 3 ** 2 = {expression_5}")

print()


print("Task 5 — Time Conversion")

total_seconds = int(input("Enter a number of seconds: "))

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"{total_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")

print()



print("Task 6 — Type Conversion")

value = 17.95


integer_value = int(value)

print(f"Integer_value: {integer_value}")


float_value = float(integer_value)

print(f"Float_value: {float_value}")


text_value = str(integer_value)

print(f"Value as text: {text_value}")
print(f"Type: {type(text_value)}")

print()



print("Task 7 — Basic String Operations")

first_name = input("First name: ")
last_name = input("Last name: ")


full_name = first_name + " " + last_name

print(f"Full name: {full_name}")
print(f"Number of characters: {len(full_name)}")
print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")
print(f"First three characters: {full_name[:3]}")

print(full_name * 3)

print()



print("Task 8 — Useful print() Options")

language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"

print(language, course, university, sep=" | ")
print("Python", end=" ")
print("Programming")

print()



print("Task 9 — Collections")

student_name = "Anna"
student_age = 22
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"

student = {
    "name": student_name,
    "age": student_age,
    "skills": student_skills,
    "university": student_university
}

print(f"Student's name: {student['name']}")
print(f"Student's university: {student['university']}")
print(f"First skill: {student['skills']}")
print(f"Number of skills: {len(student['skills'])}")

print()



print("Task 10 — Mutable and Immutable Objects")

numbers = [10, 20, 30]
same_numbers = numbers

numbers[0] = 99

print(f"numbers: {numbers}")
print(f"same_numbers: {same_numbers}")

text = "Python"
same_text = text
new_text = text + "Course"

print(f"text: {text}")
print(f"same_text; {same_text}")
print(f"new_text: {new_text}")

print()



print("Task 11 — Small Statistics Report")

scores = [78, 92, 85, 69, 88]


score_count = len(scores)
minimum_score = min(scores)
maximum_score = max(scores)
total_score = sum(scores)
mean_score = total_score / score_count

print(f"Number of scores: {score_count}")
print(f"Minimum: {minimum_score}")
print(f"Maximum: {maximum_score}")
print(f"Mean: {mean_score:.2f}")

print()



print("Task 12 — PEP 8 Cleanup")


price = 1250
quantity = 3
discount_percent = 10
subtotal = price * quantity
discount_amount = (discount_percent / 100) * subtotal
final_price = subtotal - discount_amount

print(f"Final: {final_price}")

print()

student_name = input("Student name: ")
score1 = float(input("Score 1: "))
score2 = float(input("Score 2: "))
score3 = float(input("Score 3: "))

scores = [score1, score2, score3]
minimum = min(scores)
maximum = max(scores)
mean = sum(scores) / len(scores)

print()
print(f"Student: {student_name}")
print(f"Scores: {scores}")
print(f"Minimum: {minimum:.2f}")
print(f"Maximum: {maximum:.2f}")
print(f"Mean: {mean:.2f}")

print()


print("Task 13 — Multiple Assignment")

x = 10
y = 20
z = 30

print(f"x = {x}, y = {y}, z = {z}")

a = 5
b = 10

a, b = b, a

print()


print("Task 14 — String Methods")

text = "  Python Programming Course  "

print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("Course", "Lab"))

cleaned_text = text.strip()

print(cleaned_text.startswith("Python"))
print(cleaned_text.endswith("Course"))

print()


print("Task 15 — Boolean Expressions")
#Здесь нужно просто вывести результат сравнений. Python автоматически выведет True или False.
#Даны переменные:
age = 22
score = 85
is_master_student = True

print(age >= 18)
print(score >= 60)
print(score >= 60 and is_master_student)
print(score < 60 or age < 18)
print(not is_master_student)

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))

print()


print("Task 16 — Membership")
#bu vazifada biror element boshqa bir to'plam (ro'yxat, matn, lug'at) ichida bor yoki yo'qligi tekshiramiz.
numbers = [10, 20, 30] #o'zgaruvchilar 
text = "Python Programming"
student = {
    "name": "Anna",
    "age": 22,
}

print(20 in numbers)
print(50 not in numbers)
print("Python" in text)
print("Java" not in text)
print("age" in student)
print("email" in student)

print()


print("Task 17 — Time Decomposition")
#bu vazifada foydalanuvchi kiritgan umumiy sekundlarni soat, minut va sekundlarga ajratish kerak. 
total_seconds = 0

total_seconds = int(input("Enter duration in seconds: "))
#input foydalanuvchidan matn ko'rinishidagi ma'lumot so'raydi.int esa o'sha o'zgaruvchini songa aylantiradi va total_seconds o'zgaruvchiga saqlaydi.
hours = 0
remaining_seconds = 0 #berilgan o'zgaruvchini soatlarga bo'lgandan keyingi qoldiq uchun o'zgaruvchi.
minutes = 0
seconds = 0

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600 #umumiy sekundlardan soatlarni ajratib tashlagandan keyin qolgan sekundlarni topadi.
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60 #qolgan sekunlardan minutlarni ajratib tashlangandan keyin oxirgi sekunlarni topadi.

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")

print()


print("Task 18 — Order Invoice")
#bu vazifada siz do'kondan 3 xil mahsulot sotib olinganda chek chiqaradigan dastur yozishingiz kerak.
#Vazifada if, for/while va funksiyalardan foydanmaslik kerak 
price_1 = 0.0 #bitta mahsulotni narxi.
quantity_1 = 0 #mahsulotni soni.

price_2 = 0.0
quantity_2 = 0

price_3 = 0.0
quantity_3 = 0
#Mahsulotni narxini so'rash
price_1 = float(input("Enter price for product 1: "))
quantity_1 = int(input("Enter quantity for product 1: "))

price_2 = float(input("Enter price for product 2: "))
quantity_2 = int(input("Enter quantity for product 2: "))

price_3 = float(input("Enter price for product 3: "))
quantity_3 = int(input("Enter quantity for product 3: "))
#Keyingi hisob-kitob uchun yangi o'zgaruvchi kiritamiz. 
product_1_total = 0.0
product_2_total = 0.0
product_3_total = 0.0

subtotal = 0.0
tax = 0.0
final_total = 0.0
#umumiy narxni hisoblash.
product_1_total = price_1 * quantity_1
product_2_total = price_2 * quantity_2
product_3_total = price_3 * quantity_3

subtotal = product_1_total + product_2_total + product_3_total
tax = subtotal * 0.05 #soliqni hisoblash.
final_total = subtotal + tax

print(f"Product 1: {product_1_total:.2f}")
print(f"Product 2: {product_2_total:.2f}")
print(f"Product 3: {product_3_total:.2f}")
print("-" * 20) #bu yerda 20 mata - cha chiqadi.
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {final_total:.2f}")

print()


print("Task 19 — Coordinate Analysis")
#ikkita nuqta orasidagi masofani hisoblash.
x1 = 0.0
y1 = 0.0
x2 = 0.0
y2 = 0.0
#foydalanuvchidan o'zgaruvchilarga son kiritishini so'raymiz.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
#ikkita tuple(o'zgarmas ro'yxat)yaratish.
point_1 = (x1, y1)
point_2 = (x2, y2)

delta_x = x2 - x1 #koordinatalar farqi.
delta_y = y2 - y1
distance_squared =delta_x ** 2 + delta_y ** 2 
distance = distance_squared ** 0.5 #ikkita nuqta orasidagi masofa.

print(f"Point 1: {point_1}") 
print(f"Point 2: {point_2}")
print(f"Distance: {distance:.2f}")

print()


print("Task 20 — Complex Numbers")


z1 = 3 + 4j
z2 = 2 - 1j
#bu yerda sonlarni va ularning turlarini (type) ekranga chiqaramiz.
print(z1)
print(z2)
print(type(z1))
#kompleks sonlar ustida ammallar bajaramiz.
print(z1 - z2)
print(z1 + z2)
print(z1 * z2)
print(z1 / z2)
#kompleks sonning tarkibiy qismlarini olish uchun .real va .imag xossalaridan foydalanamiz.
print(z1.real)
print(z1.imag)

print()


print("Task 21 — Student Data Record")
#bu vazifada siz foydalanuvchidan ma'lumotlarni qabul qilib, ularni list va dictionary saqlashimiz, so'ngra statistik hisob-kitoblarni bajarishimiz so'ralgan.
student_name = ""
student_age = 0
university = ""

score_1 = 0.0
score_2 = 0.0
score_3 = 0.0

scores = []
student = {}
#foydalnuvchidan ism, yosh, unversitetini va 3 ta bahosini so'raymiz.
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
university = input("Enter university: ")

score_1 = int(input("Enter first score: "))
score_2 = int(input("Enter second score: "))
score_3 = int(input("Enter third score: "))
#baholarni bitta list ichiga joylashtiramiz.
scores = [score_1, score_2, score_3]
#talaba ma'lumotlarini dictionaryga saqlash.
student = {
    "name": student_name,
    "age": student_age,
    "university": university,
    "scores": scores
}
#statistkani hisoblash.
score_count = len(scores) #baholar sonini hisoblaydi.
minimum_score = min(scores) #eng kichik bahoni topadi.
maximum_score = max(scores) #eng katta bahoni topadi.
mean_score = sum(scores) / len(scores) #o'rtacha bahoni hisoblaydi.
#natijani chiqarish.
print("\n--- Student Report ---")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"University: {student['university']}")
print(f"Scores: {student['scores']}")
print(f"Number of scores: {score_count}")
print(f"Minimum score: {minimum_score:.1f}")
print(f"Maximum score: {maximum_score:.1f}")
print(f"Mean score: {mean_score:.1f}")

print()


print("Task 22 — Debug the Program")
#bu yerda xato yozilgan kodni topib to'g'rilash kerak.
score_1 = int(input("Score 1: ")) 
#bu yerda son kiritish kerak harf emas, shuning uchun int kodidan foydalanamiz.
score_2 = int(input("Score 2: ")) 
#bu yerda o'zgaruvchi nomlari nomuvofiq(PEP 8 qoidasi buzilgan).Ya'ni score1 -> score_1.
score_3 = int(input("Score 3: "))

total = score_1 + score_2 + score_3
average = total / 3

print(f"Average: {average:.2f}") 
#bu yerda ; emas : bo'lishi kerak. Va yana + dan ham noto'g'ri foydalanilgan.
#bu yer f(formatted string literal) so'zlarni bir-biriga bog'laydi.
#print("Average:" + str(average))

print()