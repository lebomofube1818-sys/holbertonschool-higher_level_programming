#!/usr/bin/python3
"""
Module that defines a function is_same_class.

The function returns True if the object is exactly an instance of the
specified class, otherwise it returns False.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.

    Example:
        >>> is_same_class(10, int)
        True
        >>> is_same_class(10, float)
        False
    """
    return type(obj) is a_class
