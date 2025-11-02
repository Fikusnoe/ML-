import pytest
from task2_basics import has_unique_chars

def test_empty_and_single_char():
    assert has_unique_chars("") == True
    assert has_unique_chars("a") == True
    assert has_unique_chars("1") == True
    assert has_unique_chars("!") == True

def test_unique_strings():
    assert has_unique_chars("abc") == True
    assert has_unique_chars("123") == True
    assert has_unique_chars("a1b2") == True

def test_duplicate_strings():
    assert has_unique_chars("hello") == False
    assert has_unique_chars("112233") == False
    assert has_unique_chars("abcac") == False
    assert has_unique_chars("test") == False
    assert has_unique_chars("aa") == False