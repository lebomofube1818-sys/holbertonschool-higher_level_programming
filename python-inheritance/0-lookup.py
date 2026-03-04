#!/usr/bin/python3
"""This module defines a function that returns the list of
available attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    This function takes any object and returns the list of names
    representing its attributes and methods.
    """
    return dir(obj)
