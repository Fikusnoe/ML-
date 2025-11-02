import pytest
from task4_basics import magic

def test_negative_numbers():
    assert magic(-1) == "Число должно быть положительным"
    assert magic(-5) == "Число должно быть положительным"

def test_single_digit_numbers():
    assert magic(0) == 0
    assert magic(1) == 0
    assert magic(5) == 0
    assert magic(9) == 0

def test_two_digit_numbers():
    assert magic(10) == 1
    assert magic(25) == 2
    assert magic(39) == 3
    assert magic(77) == 4
    assert magic(99) == 2

def test_three_digit_numbers():
    assert magic(100) == 1
    assert magic(123) == 1
    assert magic(256) == 2
    assert magic(999) == 4

def test_larger_numbers():
    assert magic(1234) == 2
    assert magic(6789) == 3
    assert magic(7777) == 4
    assert magic(9999) == 3