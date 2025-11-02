def is_balanced(number):
    digits = list(map(int, str(number)))
    n = len(digits)

    if n <= 2:
        return True

    if n % 2 == 0:
        mid_start = n // 2 - 1
        mid_end = n // 2
        left = digits[:mid_start]
        right = digits[mid_end + 1:]
    else:
        mid = n // 2
        left = digits[:mid]
        right = digits[mid + 1:]

    return sum(left) == sum(right)