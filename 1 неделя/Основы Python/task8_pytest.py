import pytest
from task8_basics import is_balanced

def test_single_digit():
    assert is_balanced(0) == True
    assert is_balanced(1) == True
    assert is_balanced(5) == True

def test_two_digits():
    assert is_balanced(10) == True
    assert is_balanced(11) == True
    assert is_balanced(99) == True

def test_odd_length():
    assert is_balanced(121) == True
    assert is_balanced(12321) == True
    assert is_balanced(1234321) == True
    assert is_balanced(1234567) == False
    assert is_balanced(100) == False

def test_even_length():
    assert is_balanced(1221) == True
    assert is_balanced(123321) == True
    assert is_balanced(1234554321) == True
    assert is_balanced(1000) == False
    assert is_balanced(1112) == False
