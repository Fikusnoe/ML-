import pytest
import numpy as np
from task5_numpy import chess

def test_2x2_matrix():
    result = chess(2, 2, 0, 1)
    expected = np.array([[0, 1], [1, 0]])
    assert np.array_equal(result, expected)

def test_3x3_matrix():
    result = chess(3, 3, 'A', 'B')
    expected = np.array([['A', 'B', 'A'],
                         ['B', 'A', 'B'],
                         ['A', 'B', 'A']])
    assert np.array_equal(result, expected)

def test_different_values():
    result = chess(2, 3, 100, 200)
    expected = np.array([[100, 200, 100],
                         [200, 100, 200]])
    assert np.array_equal(result, expected)

def test_rectangular_matrix():
    result = chess(3, 4, 1, 0)
    expected = np.array([[1, 0, 1, 0],
                         [0, 1, 0, 1],
                         [1, 0, 1, 0]])
    assert np.array_equal(result, expected)

def test_string_values():
    result = chess(2, 2, 'black', 'white')
    expected = np.array([['black', 'white'],
                         ['white', 'black']])
    assert np.array_equal(result, expected)

def test_float_values():
    result = chess(2, 2, 1.5, 2.5)
    expected = np.array([[1.5, 2.5],
                         [2.5, 1.5]])
    assert np.array_equal(result, expected)

def test_boolean_values():
    result = chess(2, 2, True, False)
    expected = np.array([[True, False],
                         [False, True]])
    assert np.array_equal(result, expected)