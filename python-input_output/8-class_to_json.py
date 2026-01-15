#!/usr/bin/python3
"""Module that converts a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary representation of the object.
    """
    return obj.__dict__
