def count_bits(n):
    if n < 0:
        return "Число должно быть положительным"
    return bin(n).count('1')