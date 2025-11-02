def prime_factors(n):
    if n == 1:
        return "(1)"

    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    result = ""
    for prime in sorted(factors.keys()):
        power = factors[prime]
        if power == 1:
            result += f"({prime})"
        else:
            result += f"({prime}**{power})"
    return result
