import pytest
from task7_basics import pyramid

def test_impossible_cases():
    assert pyramid(3) == "It is impossible"
    assert pyramid(-1) == "It is impossible"
    assert pyramid(-5) == "It is impossible"

def test_pyramids():
    assert pyramid(1) == 1
    assert pyramid(14) == 3
    assert pyramid(55) == 5
    assert pyramid(91) == 6
    assert pyramid(140) == 7
    assert pyramid(204) == 8
    assert pyramid(385) == 10
    assert pyramid(506) == 11
    assert pyramid(650) == 12