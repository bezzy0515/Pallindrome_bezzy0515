"""
Tests the palindrome module
"""

import palindrome
import pytest

"""
Validate input variables data type.
"""


def test_input_data_for_string():
    test_int = 12
    test_float = 6.8

    with pytest.raises(ValueError):
        palindrome.is_palindrome(test_int)
    with pytest.raises(ValueError):
        palindrome.is_palindrome(test_float)


def test_for_empty_string():
    test_string = ' '
    result = False
    assert result == palindrome.is_palindrome(test_string)


def test_for_a_input():
    test_string = 'a'
    result = True
    assert result == palindrome.is_palindrome(test_string)


def test_for_bb_input():
    test_string = 'bb'
    result = True
    assert result == palindrome.is_palindrome(test_string)
