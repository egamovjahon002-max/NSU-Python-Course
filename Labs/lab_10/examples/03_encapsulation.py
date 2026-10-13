class Thermostat:
    def __init__(self):
        self._temperature = 20
    def set_temperature(self, value):
        if not 10 <= value <= 30:
            raise ValueError("Temperature must be 10–30")
        self._temperature = value
    def get_temperature(self):
        return self._temperature

unit = Thermostat()
for value in [24, 50]:
    try:
        unit.set_temperature(value)
    except ValueError as error:
        print(error)
    print(unit.get_temperature())
