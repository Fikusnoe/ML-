import pytest
from task6_basics import prime_factors

def test_number_one():
    assert prime_factors(1) == "(1)"

def test_prime_numbers():
    assert prime_factors(2) == "(2)"
    assert prime_factors(3) == "(3)"
    assert prime_factors(5) == "(5)"
    assert prime_factors(7) == "(7)"
    assert prime_factors(11) == "(11)"

def test_numbers_with_single_prime():
    assert prime_factors(4) == "(2**2)"
    assert prime_factors(8) == "(2**3)"
    assert prime_factors(9) == "(3**2)"
    assert prime_factors(16) == "(2**4)"
    assert prime_factors(25) == "(5**2)"

def test_numbers_with_multiple_primes():
    assert prime_factors(6) == "(2)(3)"
    assert prime_factors(15) == "(3)(5)"
    assert prime_factors(18) == "(2)(3**2)"
    assert prime_factors(30) == "(2)(3)(5)"
    assert prime_factors(1024) == "(2**10)"
    assert prime_factors(2310) == "(2)(3)(5)(7)(11)"

