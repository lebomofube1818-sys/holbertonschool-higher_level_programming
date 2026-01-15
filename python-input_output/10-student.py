#!/usr/bin/python3
"""Module that defines a Student class and JSON serialization method."""


class Student:
    """Student class with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in this list are returned.
        Otherwise, all attributes are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__.copy()
        if isinstance(attrs, list):
            filtered_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    # Split the assignment to satisfy PEP8 79 chars limit
                    filtered_dict[attr] = self.__dict__.get(
                        attr
                    )
            return filtered_dict
        return self.__dict__.copy()
