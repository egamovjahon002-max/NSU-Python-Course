class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Basket:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def total(self):
        amount = 0
        for item in self.items:
            amount += item.price
        return amount

basket = Basket()
basket.add(Item("Notebook", 100))
basket.add(Item("Pen", 40))
print(basket.total())
