import pytest
import numpy as np
from task3_numpy import get_unique_rows, get_unique_columns

def test_not_2d_matrix():
    assert get_unique_rows(np.array(1)) == "Матрица должна быть двумерной"
    assert get_unique_rows(np.array([1, 2, 3])) == "Матрица должна быть двумерной"
    assert get_unique_columns(np.array(1)) == "Матрица должна быть двумерной"
    assert get_unique_columns(np.array([1, 2, 3])) == "Матрица должна быть двумерной"

def test_empty_matrix():
    matrix = np.array([]).reshape(0, 0)
    result_rows = get_unique_rows(matrix)
    result_cols = get_unique_columns(matrix)
    assert result_rows == []
    assert result_cols == []

def test_single_element():
    matrix = np.array([[5]])
    result_rows = get_unique_rows(matrix)
    result_cols = get_unique_columns(matrix)
    expected = [np.array([5])]
    assert len(result_rows) == 1
    assert np.array_equal(result_rows[0], expected[0])
    assert len(result_cols) == 1
    assert np.array_equal(result_cols[0], expected[0])

def test_unique_rows():
    matrix = np.array([[1, 2, 3],
                       [4, 4, 4],
                       [1, 2, 1]])
    result = get_unique_rows(matrix)
    expected = [np.array([1, 2, 3]),
                np.array([4]),
                np.array([1, 2])]
    assert len(result) == 3
    for i in range(3):
        assert np.array_equal(result[i], expected[i])

def test_unique_columns():
    matrix = np.array([[1, 4, 1],
                       [2, 4, 2],
                       [3, 4, 1]])
    result = get_unique_columns(matrix)
    expected = [np.array([1, 2, 3]),
                np.array([4]),
                np.array([1, 2])]
    assert len(result) == 3
    for i in range(3):
        assert np.array_equal(result[i], expected[i])

def test_all_unique():
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6]])
    result_rows = get_unique_rows(matrix)
    result_cols = get_unique_columns(matrix)
    expected_rows = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    expected_cols = [np.array([1, 4]), np.array([2, 5]), np.array([3, 6])]

    for i in range(2):
        assert np.array_equal(result_rows[i], expected_rows[i])
    for i in range(3):
        assert np.array_equal(result_cols[i], expected_cols[i])

def test_all_same():
    matrix = np.array([[1, 1, 1],
                       [1, 1, 1]])
    result_rows = get_unique_rows(matrix)
    result_cols = get_unique_columns(matrix)
    expected = [np.array([1])]

    assert len(result_rows) == 2
    assert np.array_equal(result_rows[0], expected[0])
    assert np.array_equal(result_rows[1], expected[0])

    assert len(result_cols) == 3
    for i in range(3):
        assert np.array_equal(result_cols[i], expected[0])
