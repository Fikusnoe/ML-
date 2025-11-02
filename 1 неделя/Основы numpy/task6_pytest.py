import pytest
import numpy as np
from task6_numpy import draw_rectangle, draw_ellipse

def test_draw_rectangle_basic():
    result = draw_rectangle(4, 3, 10, 10, [255, 0, 0], [0, 0, 0])
    assert result.shape == (10, 10, 3)
    assert result.dtype == np.uint8

def test_draw_ellipse():
    result = draw_ellipse(2, 2, 10, 10, [255, 0, 0], [0, 0, 0])
    assert result.shape == (10, 10, 3)
    assert result.dtype == np.uint8

def test_different_colors():
    rect_result = draw_rectangle(2, 2, 4, 4, [255, 0, 0], [0, 255, 0])
    ellipse_result = draw_ellipse(2, 2, 4, 4, [0, 0, 255], [255, 255, 0])
    assert rect_result[1, 1, 0] == 255
    assert ellipse_result[2, 2, 2] == 255