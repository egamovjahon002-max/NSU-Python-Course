class Animal:
    def speak(self):
        return "A sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

for animal in [Cat(), Dog()]:
    print(animal.speak())
