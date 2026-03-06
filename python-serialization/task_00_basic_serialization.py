#!/usr/bin/python3
"""
Module for basic JSON serialization and deserialization.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file where the JSON data will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
