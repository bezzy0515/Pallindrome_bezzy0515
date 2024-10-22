"""
Validates strings as palindromes.
"""

from collections import deque


def is_palindrome(input_value):
    if not isinstance(input_value, str):        # Make sure input is a string
        raise ValueError()
    else:
        if all(char.isspace() for char in input_value):
            ip = False
            return ip
        else:
            char_deque = deque(input_value.casefold())

            if len(char_deque) == 1:
                if input_value == 'a':
                    ip = True
                    return ip
