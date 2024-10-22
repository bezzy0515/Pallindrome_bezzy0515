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
