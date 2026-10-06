"""A function reports invalid data to its caller."""
def square_root_input(number):
    if number < 0:
        raise ValueError("Number must be nonnegative")
    return number ** 0.5

for number in [9, -4]:
    try:
        print(square_root_input(number))
    except ValueError as error:
        print(error)
