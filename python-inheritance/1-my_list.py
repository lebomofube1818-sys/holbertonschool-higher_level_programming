#!/usr/bin/python3
"""
Module that defines the MyList class, which inherits from list.
Provides a method to print a sorted version of the list.
"""


class MyList(list):
    """
    Represents a list with a method to print a sorted copy.

    Inherits all behavior from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.

        Example:
            >>> my_list = MyList([3, 1, 2])
            >>> my_list.print_sorted()
            [1, 2, 3]
        """
        print(sorted(self))
