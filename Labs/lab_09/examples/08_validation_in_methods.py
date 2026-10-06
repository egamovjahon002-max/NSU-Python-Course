"""Validate before changing the object's state."""
class Thermostat:
    def __init__(self):
        self.temperature = 20

    def set_temperature(self, value):
        if not 10 <= value <= 30:
            raise ValueError("Temperature must be between 10 and 30")
        self.temperature = value

thermostat = Thermostat()
for value in [24, 50]:
    try:
        thermostat.set_temperature(value)
    except ValueError as error:
        print(error)
    print("Current:", thermostat.temperature)
