#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Returns the addition of two integers.

    a and b must be integers or floats.
    Floats are casted to integers before addition.
    Raises TypeError for invalid inputs or non-finite floats.
    """
    # Check type
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for float NaN or infinity
    if isinstance(a, float):
        if a != a or a in (float('inf'), float('-inf')):
            raise TypeError("a must be an integer")
    if isinstance(b, float):
        if b != b or b in (float('inf'), float('-inf')):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
