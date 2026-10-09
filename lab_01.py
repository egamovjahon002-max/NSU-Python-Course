 
print("Task 1 — Personal Information")

name = input("Enter your name:  ")
age = int(input("Enter your age:  "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")

print()

print("Task 2 — Rectangle")

width = float(input("Enter width: "))
height = float(input("Enter height: "))

area = width * height
perimeter = 2 * (width + height)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

print()


print("Task 3 — Temperature Converter")

celsius = float(input("Enter celsius temperatura: "))
fahrenheit = celsius * 9 / 5 +  32

print(f"{celsius}C = {fahrenheit}F")

print()


print("Task 4 — Purchase Calculator")

quantity = int(input("Enter quantity: "))
price = float(input("Enter price for one: "))

total_price = quantity * price
discounted = total_price * 0.10
discounted_price = total_price - discounted

print(f"Total price: {total_price}")
print(f"Discounted price: {discounted_price}")

print()


print("Task 5 — Arithmetic Operators")

a = 17
b = 5

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

print()



print("Task 6 — Data Types")

integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
taxt_value = "Python"
boolean_value = True

print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(taxt_value))
print(type(boolean_value))


print()



print("Task 7 — Comparisons and Boolean Logic")


age = 22
is_master_student = True

print(age >= 18)
print(age < 30)
print(age == 22)
print(age != 25)

print(age >= 18 and is_master_student)
print(age < 18 or is_master_student)
print(not is_master_student)

print()



print("Task 8 — Python Collections")

programming_languages = input("Enter programming languages: ")
numbers = int(input("Enter numbers: "))
cities = input("Enter cities: ")
student_name= input("Enter student name: ")
student_age= int(input("Enter student age: "))
university_name=  input("Enter university name: ")


print(f"Programming Languages: {programming_languages} ")
print(f"Numbers: {numbers} ")
print(f"Cities: {cities} ")
print(f"Student name: {student_name} ")
print(f"Student age: {student_age} ")
print(f"University name: {university_name} ")

print("Type of programming_languages:", type(programming_languages))
print("Type of numbers:", type(numbers))
print("Type of cities:", type(cities))
print("Type of student_name:", type(student_name))
print("Type of student_age:", type(student_age))
print("Type of university_name:", type(university_name))


print()



print("Task 9 — Indexing and Slicing")


numbers = [0, 1, 2, 3, 4, 5, 6, 7]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[::2])


word = "Python"

print(word[0])
print(word[-1])
print(word[0:3])

print()



print("Task 10 — Dictionaries and Membership")

student = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}
print(student["name"])
print(student["age"])
print("age" in student)
print("email" in student)



numbers = [10, 20, 30, 40]

print("20" in numbers)
print("50" in numbers)
print("23" in numbers)

print()



print("Task 11 — Formatted Output")

radius = float(input("Enter the radius of a circle: "))

area = 3.14159 * radius ** 2

print(f"Radius: {radius}")
print(f"Area: {area:.2f}")

print()



print("Task 12 — Trip Cost Calculator")

distance = float(input("Enter distance in kilometers: "))
fuel_consumption = float(input("Enter fuel consumption (liters per 100 km): "))
fuel_price = float(input("Enter fuel price per liter: "))

liters_needed = distance / 100 * fuel_consumption
trip_cost = liters_needed * fuel_price


print(f"Distance: {distance} km")
print(f"Fuel required: {liters_needed:.2f} liters")
print(f"Trip cost: {trip_cost:.2f}")

print()
