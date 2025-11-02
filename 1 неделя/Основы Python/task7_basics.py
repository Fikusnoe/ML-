def pyramid(number):
    if number <= 0:
        return "It is impossible"

    k = 0
    total = 0

    while total < number:
        k += 1
        total += k * k

        if total == number:
            return k

    return "It is impossible"