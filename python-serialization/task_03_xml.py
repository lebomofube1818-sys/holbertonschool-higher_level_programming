#!/usr/bin/python3
"""
Module for serializing and deserializing dictionaries using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML file to write to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: The reconstructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for child in root:
        result[child.tag] = child.text

    return result
