def magic(n):
    if n < 0:
        return "Число должно быть положительным"

    if n < 10:
        return 0

    steps = 0
    current = n
    while current >= 10:
        product = 1
        for digit in str(current):
            product *= int(digit)

        current = product
        steps += 1

    return steps