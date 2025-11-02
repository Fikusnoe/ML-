import pytest
import numpy as np
from task2_numpy import binarize

def test_empty_matrix():
    result = binarize([])
    expected = np.array([])
    assert np.array_equal(result, expected)

def test_single_element():
    result = binarize([[0.3]])
    expected = np.array([[0]])
    assert np.array_equal(result, expected)

    result = binarize([[0.7]])
    expected = np.array([[1]])
    assert np.array_equal(result, expected)

def test_default_threshold():
    M = [[0.4, 0.6], [0.5, 0.5]]
    result = binarize(M)
    expected = np.array([[0, 1], [0, 0]])
    assert np.array_equal(result, expected)

def test_custom_threshold():
    M = [[0.3, 0.7], [0.4, 0.6]]
    result = binarize(M, threshold=0.5)
    expected = np.array([[0, 1], [0, 1]])
    assert np.array_equal(result, expected)

    result = binarize(M, threshold=0.3)
    expected = np.array([[0, 1], [1, 1]])
    assert np.array_equal(result, expected)

def test_mixed_values():
    M = [[0.1, 0.5, 0.9], [0.2, 0.6, 0.4]]
    result = binarize(M, threshold=0.5)
    expected = np.array([[0, 0, 1], [0, 1, 0]])
    assert np.array_equal(result, expected)

def test_different_thresholds():
    M = [[0.2, 0.5, 0.8]]

    result1 = binarize(M, threshold=0.1)
    expected1 = np.array([[1, 1, 1]])
    assert np.array_equal(result1, expected1)

    result2 = binarize(M, threshold=0.5)
    expected2 = np.array([[0, 0, 1]])
    assert np.array_equal(result2, expected2)

    result3 = binarize(M, threshold=0.9)
    expected3 = np.array([[0, 0, 0]])
    assert np.array_equal(result3, expected3)