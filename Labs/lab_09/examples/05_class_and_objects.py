"""Two instances can have different attribute values."""
class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def describe(self):
        return f"{self.name}, {self.country}"

first = City("Novosibirsk", "Russia")
second = City("Algiers", "Algeria")
print(first.describe())
print(second.describe())
