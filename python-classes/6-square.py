#!/usr/bin/python3
"""Module 6-square:
Defines a Square class with size, position, area, and my_print methods.
"""


class Square:
    """Represents a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the current position of the square.

        Returns:
            tuple: The current position as (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): The new position (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character # to stdout.

        Position is considered using horizontal and vertical offsets.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
