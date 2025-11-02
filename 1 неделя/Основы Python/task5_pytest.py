import pytest
from task5_basics import mse

def test_different_length():
    assert mse([1, 2], [1]) == "Векторы должны быть одинаковой длины"
    assert mse([1], [1, 2, 3]) == "Векторы должны быть одинаковой длины"
    assert mse([], [1]) == "Векторы должны быть одинаковой длины"

def test_empty_vectors():
    assert mse([], []) == 0

def test_single_element():
    assert mse([1], [1]) == 0
    assert mse([2], [1]) == 1

def test_positive_numbers():
    assert mse([1, 2, 3], [1, 2, 3]) == 0
    assert mse([2, 3, 4], [1, 2, 3]) == 1
    assert mse([1, 1, 1], [2, 2, 2]) == 1

def test_negative_numbers():
    assert mse([-1, -2, -3], [-1, -2, -3]) == 0
    assert mse([0, -1, -2], [1, 0, -1]) == 1

