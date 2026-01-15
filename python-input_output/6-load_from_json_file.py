#!/usr/bin/python3
"""Module that loads an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file

    Returns:
        The Python object represented by the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
