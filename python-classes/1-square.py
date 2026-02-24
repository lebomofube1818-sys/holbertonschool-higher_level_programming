#!/usr/bin/python3
"""Module 1-square: Defines a Square class with a private size attribute."""


class Square:
    """Represents a square defined by a private instance attribute 'size'."""

    def __init__(self, size):
        """Initialize a Square with a private attribute size.

        Args:
            size (int): The size of the square (no type/value checks for now).
        """
        self.__size = size
