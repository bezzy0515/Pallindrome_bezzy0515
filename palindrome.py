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
            if len(char_deque) == 2:
                if char_deque[0] == char_deque[-1]:
                    ip = True
                    return ip
            else:
                while len(char_deque) > 1:
                    first = char_deque[0]
                    last = char_deque[-1]

                    if first != last:
                        ip = False
                        return ip
                    else:
                        char_deque.pop()
                        char_deque.popleft()

                ip = True
                return ip
