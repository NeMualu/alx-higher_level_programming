#!/usr/bin/python3
"""
Defines a function for integer addition.
"""


def add_integer(x, y=98):
    """Return the integer addition of x and y.

    Float arguments are typecasted to integers before addition is performed.

    Raises:
        TypeError: If either x or y is a non-integer and non-float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an integer or float")
    if not isinstance(y, (int, float)):
        raise TypeError("y must be an integer or float")
    
    return int(x) + int(y)

