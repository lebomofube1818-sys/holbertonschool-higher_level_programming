#!/usr/bin/python3
"""Module 3-square:
Defines a Square class with a private size attribute and an area method.
"""


class Square:
    """Represents a square with a private size attribute
    and area calculation.
    """

    def __init__(self, size=0):
        """Initialize a Square with validated size.

        Args:
            size (int, optional): The size of the square.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size
