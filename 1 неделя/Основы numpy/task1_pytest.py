import pytest
import numpy as np
from task1_numpy import sum_prod

def test_empty_arrays():
    result = sum_prod([], [])
    assert np.array_equal(result, np.array([]))

def test_single_element():
    result = sum_prod([[2]], [3])
    assert np.array_equal(result, np.array([6]))

def test_row_vector():
    result = sum_prod([[1, 2]], [3, 4])
    assert np.array_equal(result, np.array([11]))

def test_column_vector():
    result = sum_prod([[1], [2]], [3])
    assert np.array_equal(result, np.array([3, 6]))

def test_matrix_vector():
    X = [[1, 2], [3, 4]]
    V = [5, 6]
    result = sum_prod(X, V)
    expected = np.array([17, 39])
    assert np.array_equal(result, expected)

def test_larger_matrix():
    X = [[1, 2, 3], [4, 5, 6]]
    V = [7, 8, 9]
    result = sum_prod(X, V)
    expected = np.array([50, 122])
    assert np.array_equal(result, expected)

def test_3x3_matrix():
    X = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    V = [2, 3, 4]
    result = sum_prod(X, V)
    expected = np.array([2, 3, 4])
    assert np.array_equal(result, expected)