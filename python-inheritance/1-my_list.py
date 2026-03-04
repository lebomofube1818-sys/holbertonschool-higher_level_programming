#!/usr/bin/python3
"""This module defines a class that inherits from list and
provides a method to print the list in sorted order."""


class MyList(list):
    """This class inherits from list and adds a method to
    print the elements in ascending sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        The original list remains unchanged.
        """
        print(sorted(self))
