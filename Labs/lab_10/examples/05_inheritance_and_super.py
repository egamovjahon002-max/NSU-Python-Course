class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bicycle(Vehicle):
    def __init__(self, brand, gears):
        super().__init__(brand)
        self.gears = gears

bike = Bicycle("Example", 6)
print(bike.brand, bike.gears)
print(isinstance(bike, Vehicle))
