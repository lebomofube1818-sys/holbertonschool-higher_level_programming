#!/usr/bin/python3
"""
Module that defines a function that checks if an object is
an instance of a class or inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or if it
    inherits from a_class.

    Otherwise, return False.
    """
    return isinstance(obj, a_class)
