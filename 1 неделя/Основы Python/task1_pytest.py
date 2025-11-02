import pytest
from task1_basics import count_vowels

def test_empty_and_no_vowels():
    assert count_vowels("") == 0
    assert count_vowels("bcdfg") == 0
    assert count_vowels("12356") == 0

def test_common_words():
    assert count_vowels("aabb") == 2
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("mageblood") == 4

def test_with_special():
    assert count_vowels("hello world") == 3
    assert count_vowels("a e i o u") == 5
    assert count_vowels("hello!") == 2
    assert count_vowels("  test  ") == 1
