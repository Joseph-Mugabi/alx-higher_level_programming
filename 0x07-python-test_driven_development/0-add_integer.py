#!/usr/bin/python3
"""
module 0-add integer

he 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Return a + b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
