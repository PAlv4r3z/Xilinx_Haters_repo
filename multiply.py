def multiply(num1, num2):
    # The following function multiplies two numbers by adding the first one as many times as the second number.
    multiplier = 0
    if num2 > 0:
        for _ in range(num2):
            multiplier += num1
        return multiplier
    elif num2 < 0:
        num2 = -num2
        for _ in range(num2):
            multiplier += num1
        return -(multiplier)
    elif num2 == 0:
        return 0
