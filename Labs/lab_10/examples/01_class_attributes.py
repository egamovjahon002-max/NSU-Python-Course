class Product:
    currency = "RUB"
    def __init__(self, name):
        self.name = name

first = Product("Notebook")
second = Product("Pen")
print(first.currency, second.currency)
first.currency = "EUR"
print(first.currency, second.currency)