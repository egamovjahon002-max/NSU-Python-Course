"""Create mutable instance data inside __init__."""
class ShoppingList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

first = ShoppingList()
second = ShoppingList()
first.add("milk")
print(first.items)
print(second.items)
