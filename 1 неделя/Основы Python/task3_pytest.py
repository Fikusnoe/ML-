import pytest
from task3_basics import count_bits

def test_positive_numbers():
    assert count_bits(0) == 0
    assert count_bits(1) == 1
    assert count_bits(5) == 2
    assert count_bits(7) == 3
    assert count_bits(10) == 2
    assert count_bits(15) == 4
    assert count_bits(255) == 8
    assert count_bits(1023) == 10
    assert count_bits(1024) == 1

def test_negative_numbers():
    assert count_bits(-1) == "Число должно быть положительным"
    assert count_bits(-5) == "Число должно быть положительным"
