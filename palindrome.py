"""
Validates strings as palindromes.
"""

def is_palindrome(input_value):
    if not isinstance(input_value, str):        # Make sure input is a string
        raise ValueError()
    else:
        if all(char.isspace() for char in input_value):
            ip = False
            return ip
