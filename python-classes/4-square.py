#!/usr/bin/python3
"""Module 4-square:
Defines a Square class with a private size attribute, property getter and
setter, and an area method.
"""


class Square:
    """Represents a square with a private size attribute and area calculation.
    The size attribute is accessed and updated via property methods.
    """

    def __init__(self, size=0):
        """Initialize a Square with a validated size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """Retrieve the current size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size
