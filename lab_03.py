"""
NSU Python — Lab 03

"""
print("Task 1 — Positive, negative, or zero")
#bu yerda butun son (integer) kiritishimiz kerak ekan.
number = int(input("Enter an integer: "))

if number > 0: #agar butun son 0 dan katta bo'lsa "Positive" bo'ladi.
    print("Positive")
elif number < 0: #agar birinchi shart bajarilmasa, u holda 0 dan kichikligi tekshiriladi.
    print("Negative")
else:
    print("Zero") #agar ikki shart ham bajarilmasa, natija nol bo'ladi.

print()


print("Task 2 — Age category")
#foydalanuvchidan yoshini so'raymiz.
age = int(input("Enter your age: "))

if age < 13: #agar 13 yoshdan kichik bo'lsa.
    print("Child") 
elif age <= 17: #agar 13 va 17 yosh oralig'ida bo'lsa.
    print("Teenager")
elif age <= 64: #agar 18 va 64 yosh oralig'ida bo'lsa.
    print("Adult")
else: #65 dan katta bo'lsa.
    print("Senior")

print()


print("Task 3 — Grade classifier")
#foydalanuvchidan ballni so'raymiz.
score = int(input("Enter your score: "))
#Avval ball 0 va 100 oralig'ida ekanini tekshiramiz.
if score < 0 or score > 100:
    print("Invalid scores")
else:
    if score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
    else:
        print("Fail")

print()


print("Task 4 — Access decision")
#Foydalanuvchidan yoshini va chiptasi bor yoki yo'qligini so'raymiz.
age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18 and ticket == "yes":
    print("Access granted")
elif age >= 18 and ticket == "no":
    print("Ticket required")
else:
    print("Must be 18 or older")

print()


print("Task 5 — Even numbers with range()")
#30 gacha bo'lgan juft sonlar.
for number in range(2 , 31, 2):
    print(number)
#range kodi:(start) birinchi 2 qaysi sondan boshlanishi.(stop) qaysi songacha bo'lishi.(step) har safar qanchaga oshib borishi.
print()


print("Task 6 — Sum of multiples of 3")
#3 ga karrali bo'lgan sonlarni hisoblash.
total = 0 #akkamulyatorni noldan boshlaymiz
#3 dan 99 gacha bo'lgan 3 ga karrali sonlar.
for number in range(3, 100, 3):
    total += number #har bir sonni akkamulyatorga qo'shamiz.

print(total)

print()


print("Task 7 — Count number categories")
#berilgan sonlar orasida nechta musbat, nechta manfiy va nechta nol borligini topish kerak.
number = [4, -2, 0, 7, -5, 9, 0, -1, 8]
#hisoblash uchun o'zgaruvchi kiritamiz. 
positive_count = 0
negative_count = 0
zero_count = 0

for number in number:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)

print()


print("Task 8 — Count vowels")
#Foydalanuvchidan so'z yoki qiaqa matn kiritish talab qilinadi. Keyin matndagi unli harflarni topish kerak.
text = input("Enter a word or short text: ")
#unlilarni hisoblash uchun hisoblagich kiritamiz.
vowel_count = 0
#mmatnni har bir harfni tekshiramiz.
for char in text:
    if char.lower() in "aeiou": #matnni kichik harf qilib, tekshiramiz.
        vowel_count += 1

print(vowel_count)

print()


print("Task 9 — Student results")
#kimlar o'tagan kimlar yiqilganini topish kerak.
scores = [85, 42, 67, 91, 58, 73, 100, 39]
#hisoblagichlar va yig'indilar uchun o'zgaruvchi kitamiz.
passed_count = 0
failed_count = 0
total_count = 0
#tekshiramiz.
for score in scores:
    total_score += score  #yig'indiga qo'shamiz.
    if score >= 60: #o'tgan yoki yiqilganligi tekshiramiz.
        passed_count += 1
    else:
        failed_count += 1
#o'rtacha ballni hisoblaymiz.
average = total_score / len(scores)   

print("Passed:", passed_count)
print("Failed:", failed_count)
print("Average: {average:.2f}")

print()


print("Task 10 — Search and stop")
#Foydalanuvchidan ism so'rash kerak va berilgan ismlar orasidan tekshirish kerak.
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]
#ism so'rash.
target = input("Enter a name: ")
#topilganligini tekshirish uchun boolean o'zgaruvchi.
found = False
#Ro'yxatdagi har bir ismni tekshiradi.
for name in names:
    if name == target:
        print("Found") 
        found = True
        break #qidruvni to'xtatamiz.
if not found:  #agar qidruv(sikl) tugagach ham topilmasa.
    print("Not found")

print()


print("Task 11 — Skip invalid scores")
#to'g'ri (valid)(0 dan 100 gacha) baholarni ajratib olish.
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]
#To'g'ri baholar uchun bo'sh ro'yxat.
valid_scores =[]
#yig'indi uchun akkumulyator
total = 0
#tekshiruv
for score in raw_scores:
    if score < 0 or score > 100:
        continue
#to'g'ri baholarni ro'xatga qoshamiz va yig'indiga qo'shamiz.
valid_scores.append(score)
total += score
#o'tahca qiymatni hisoblaymiz.
average = total / len(valid_scores)

print("Valid scores:", valid_scores)
print("Average:", average)

print()


print("Task 12 — Dictionary iteration")
#nechta o'qtuvchi o'tganini chiqarish.
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}
#o'tganlar sonini sanash uchun hisoblagich.
passed_count = 0

for name, score in student_scores.items():
    if score >= 60:
        print(f"{name}: Pass")
        passed_count += 1
    else:
        print(f"{name}: Fail")

print(f"Passed: {passed_count}")


print("Task 13 — FizzBuzz")
#1 dan 30 gacha bo'lgan sonlarni orasidan 3 ga va 5 ga bo'linadiganni va ikkalasiga ham bo'linadiganni topish.
for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print()


print("Task 14 — Limited login attempts")
#3 ta urinishda kodni kiritish kerak.
correct_pin = "4821" #to'g'ri pin kod.
#3 ta urinish beramiz.
for attempt in range(3):
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access granted")
        break
else:
    print("Access denied") 

print()


print("Task 15 — Largest of three numbers")
#Foydalanuvchidan 3 ta butun son kiritishini so'rab va ularni eng kattasini topish. max() dan foydalanmasdan.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
#eng kattasini topamiz.
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)

print()


print("Task 16 — Number statistics")
#berilgan ro'yxatdagi sonlar bo'yicha for dan foydalanib musbat, manfiy, nollar, musbatlar yig'indisi va manfiylar yig'indisini topish.
numbers = [12, -4, 7, 0, 15, -9, 8, -2, 0, 21]
#hisoblagichlar va yig'indi akkumulyatorlarini 0 dan boshlab yozamiz.
positive_count = 0
negative_count = 0
zero_count = 0
positive_sum = 0
negative_sum = 0

for nomber in numbers:
    if number > 0:
        positive_count += 1
        positive_sum += number
    elif number < 0:
        negative_count += 1
        negative_sum += number
    else:
        zero_count += 1

print("Positive:", positive_count)
print("Negative:", negative_count)
print("zero:", zero_count)
print("Positive sum:", positive_sum)
print("Negative sum:", negative_sum)

print()


print("Task 17 — Highest and lowest score")
#berilgan baholar ro'yxatidan eng katta(max()dan foydalanmasdan) va eng kichigini(min()dan foydalanmasdan)(va yana sorted siz ham)
# qiymatlarini (highest = scores[0] va lowest = scores[0] bilan boshlab) topish kerak.
scores = [71, 85, 42, 96, 58, 83, 67, 91]
#boshlang'ich qiymatlar sifatida ro'yxatni birinchi elementini olamiz.
highest = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print("Highest:", highest)
print("Lowest:", lowest)

print()


print("Task 18 — Temperature analysis")
#berilgan temperatura ro'yhatini toifalarga ajratish kerak.
temperatures = [12, 18, 25, 31, 7, 22, 35, 16, 29, 4]
cold_count = 0
mild_count = 0
warm_count = 0
hot_count = 0

for temp in temperatures:
    if temp < 10:
        print(f"{temp}: Cold")
    elif temp <= 19:
        print(f"{temp}: Mild")
        mild_count += 1
    elif temp <= 29:
        print(f"{temp}: Warm")
        warm_count += 1
    else:
        print(f"{temp}: Hot")
        hot_count += 1

print("Cold:", cold_count)
print("Mild:", mild_count)
print("Warm:", warm_count)
print("Hot:", hot_count)

print()


print("Task 19 — Running balance")
#berilgan tranzaksiyalar ro'yxatidagi musbat va manfiy sonlarni topish.
transactions = [500, -120, -80, 250, -700, 300, -200]
balance = 1000

deposits_count = 0
withdrawals_count = 0

for transaction in transactions:
    balance += transaction
    if transaction > 0:
        deposits_count += 1
    else:
        withdrawals_count += 1

print(f"Transaction: {transaction}")
print(f"Balance: {balance}")

print("\nFinal balace:",  balance)
print(f"Deposits: {deposits_count} ta")
print(f"Withdrawals: {withdrawals_count} ta")

print()


print("Task 20 — Find first number divisible by 7 and 11")
#1 dan 500 gacha bo'lgan sonlar orasidan 7 ga ham 11 ga bo'linadigan 1-soni topish kerak.
for number in range(1, 500):
    if number % 7 == 0 and number % 11 == 0:
        print(number) 
        break

print()


print("Task 21 — Limited number guessing")
#Foydalanuvchiga maxfiy sonni 5 ta urinishda topa olmasa unga maslahat berilishi kerak.
secret_number = 37

for attempt in range(5):
    guess = int(input("Enter secret number: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")
        break

else:
    print("Out of attempts")

print()


print("Task 22 — Count increases")
#berilgan ro'yxatda har bir son o'zidan oldin turgan sondan katta bo'lgan holatlar sonni sanash.
values = [10, 14, 13, 18, 22, 20, 25, 25, 30]
#ortirishlar sonnini hisoblash uchun hisoblagich.
increases_count = 0

for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        increases_count += 1

print(f"Increases: {increases_count}")

print()



print("Task 23 — Prime number check")
#foydalanuvchidan 1 dan katta butun son kiritish kerak so'rash va tub son yoki tub son emaslidini aniqlash kerak.
number = int(input("Enter an integer greater than 1: "))

is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")

print()


print("Task 24 — Multiplication table")
#1 dan 5 gacha ko'paytirish jadvalini chiqarish kerak.
for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end=' ')

print()


print("Task 25 — Second largest value")
#ro'yxatdan ikkinchi eng katta va takrorlanmaydigan sonni topish kerak.
numbers = [12, 7, 19, 3, 19, 14, 8]

largest = -1
second_largest = -1

for num in number:
    if num > largest:
        second_largest = largest
        largest = num 
    elif num > second_largest and num != largest:
        second_largest = num 

print(f"Second largest: {second_largest}")

print()