"""finally runs after a handled failure and after success."""
for denominator in [2, 0]:
    try:
        result = 12 / denominator
    except ZeroDivisionError:
        print("Zero divisor")
    else:
        print("Result:", result)
    finally:
        print("Calculation attempt finished")
