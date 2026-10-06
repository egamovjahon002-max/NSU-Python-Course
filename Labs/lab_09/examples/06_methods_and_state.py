"""A method can update the object on which it is called."""
class Lamp:
    def __init__(self):
        self.is_on = False

    def switch_on(self):
        self.is_on = True

lamp = Lamp()
print(lamp.is_on)
lamp.switch_on()
print(lamp.is_on)
