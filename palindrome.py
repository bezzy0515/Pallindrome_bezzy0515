"""
Validates strings as palindromes.
"""

def is_palindrome(input_value):
    if not isinstance(input_value, str):        # Make sure input is a string
        raise ValueError()
