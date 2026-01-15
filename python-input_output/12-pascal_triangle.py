#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle
    of n rows.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list: List of lists of integers representing the triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # First element of the row
        # Generate middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element of the row
        triangle.append(row)

    return triangle
