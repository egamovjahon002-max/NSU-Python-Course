print("Task 1 - Class and Instance Attributes")
# Создаём класс Student
class Student:
    university = "NSU"  # Общий атрибут класса

    def __init__(self, name):
        self.name = name  # Сохраняем имя студента

    def describe(self):
        # Выводим имя и название университета
        print(f"{self.name} studies at {self.university}")


student1 = Student("Anna")  # Создаём первого студента
student2 = Student("Ivan")  # Создаём второго студента

student1.describe()
student2.describe()

Student.university = "New University"  # Меняем атрибут класса

student1.describe()
student2.describe()

print()


print("Task 2 - Class Attributes")
# Атрибут экземпляра может перекрывать атрибут класса
class Device:
    status = "Shared"  # Атрибут класса

    def __init__(self):
        self.status = "Personal"  # Атрибут экземпляра


device1 = Device()
device2 = Device()

print(device1.status)  # Выводим атрибут первого объекта
print(device2.status)  # Выводим атрибут второго объекта
print(Device.status)   # Выводим атрибут самого класса

print()


print("Task 3 - Mutable Class Attributes")
# Создаём отдельный список для каждого объекта
class Team:
    def __init__(self):
        self.members = []  # Индивидуальный список участников

    def add_member(self, name):
        self.members.append(name)  # Добавляем участника в список


team1 = Team()
team2 = Team()

team1.add_member("Anna")  # Добавляем участника только в первую команду

print(team1.members)
print(team2.members)
print(team1.members is team2.members)  # Проверяем, один ли это объект

print()


print("Task 4 - Property Validation")
# Проверяем, что добавляемое значение положительное
class PositiveCounter:
    def __init__(self):
        self._value = 0  # Начальное значение счётчика

    def add(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")  # Вызываем ошибку
        self._value += amount  # Увеличиваем значение счётчика

    def get_value(self):
        return self._value  # Возвращаем текущее значение


counter = PositiveCounter()
counter.add(3)
counter.add(2)

print(counter.get_value())  # Выводим значение до ошибочного действия

try:
    counter.add(0)  # Ноль нельзя добавить
except ValueError:
    pass  # Обрабатываем ошибку без дополнительного вывода

print(counter.get_value())  # Проверяем, что значение не изменилось

print()


print("Task 5 - Encapsulation and Copies")
# Возвращаем копию списка, чтобы защитить исходные данные
class ScoreBook:
    def __init__(self):
        self._scores = []  # Внутренний список оценок

    def add_score(self, score):
        self._scores.append(score)  # Добавляем оценку

    def get_scores(self):
        return self._scores.copy()  # Возвращаем копию списка


book = ScoreBook()
book.add_score(80)
book.add_score(100)

scores = book.get_scores()
print(scores)

scores.clear()  # Очищаем только полученную копию

print(book.get_scores())  # Исходный список остаётся без изменений
print(scores)

print()


print("Task 6 - Inheritance")
# Класс Visitor наследует класс Person
class Person:
    def __init__(self, name):
        self.name = name  # Сохраняем имя человека

    def introduce(self):
        print(f"My name is {self.name}")  # Представляем человека


class Visitor(Person):
    pass  # Используем методы родительского класса


visitor = Visitor("Anna")
visitor.introduce()

print()


print("Task 7 - Using super()")
# Используем super() для вызова конструктора родительского класса
class StudentPerson(Person):
    def __init__(self, name, university):
        super().__init__(name)  # Инициализируем имя из класса Person
        self.university = university  # Сохраняем название университета

    def describe(self):
        print(f"{self.name} studies at {self.university}")


student = StudentPerson("Ivan", "NSU")
student.introduce()
student.describe()

print()


print("Task 8 - Method Overriding")
# Переопределяем метод introduce()
class Teacher(Person):
    def introduce(self):
        # Создаём собственный вариант представления
        print(f"I am a teacher. My name is {self.name}")


teacher = Teacher("Maria")
teacher.introduce()

print()


print("Task 9 - Extending an Inherited Method")
# Расширяем метод родительского класса
class DetailedStudent(StudentPerson):
    def introduce(self):
        super().introduce()  # Вызываем родительский метод
        print(f"My university is {self.university}")  # Добавляем информацию


detailed_student = DetailedStudent("Alex", "NSU")
detailed_student.introduce()

print()


print("Task 10 - Polymorphism")
# Разные классы вычисляют площадь с помощью метода area()
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Площадь прямоугольника


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  # Площадь квадрата


def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()  # Вызываем area() у каждой фигуры
    return total  # Возвращаем общую площадь


rectangle = Rectangle(4, 5)
square = Square(3)

print(rectangle.area())
print(square.area())
print(total_area([rectangle, square]))

print()


print("Task 11 - Duck Typing")
# Функция может работать с любым объектом, имеющим метод area()
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Сохраняем радиус круга

    def area(self):
        return 3.14 * self.radius ** 2  # Вычисляем площадь круга


circle = Circle(2)

print(circle.area())
print(total_area([rectangle, square, circle]))  # Суммируем площади фигур

print()


print("Task 12 - Composition")
# Класс Course содержит список студентов
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []  # Список студентов курса

    def enroll(self, student):
        self.students.append(student)  # Записываем студента на курс

    def roster(self):
        return [student.describe() for student in self.students]


class CourseStudent:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name  # Возвращаем имя студента


course = Course("Python")
course_student = CourseStudent("Anna")

course.enroll(course_student)
print(course.roster())

print()


print("Task 13 - Extending a Class")
# Добавляем тему исследования к классу студента
class ResearchStudent(StudentPerson):
    def __init__(self, name, university, research_topic):
        super().__init__(name, university)  # Инициализируем родительские атрибуты
        self.research_topic = research_topic  # Сохраняем тему исследования

    def describe(self):
        print(
            f"{self.name} studies at {self.university}. "
            f"Research topic: {self.research_topic}"
        )


research_student = ResearchStudent("Alex", "NSU", "Mathematics")
research_student.describe()

course.enroll(research_student)  # Добавляем студента в список курса
print(course.roster())

print()
