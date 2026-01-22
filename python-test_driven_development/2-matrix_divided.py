#!/usr/bin/python3
"""
This module contains a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    matrix must be a list of lists of integers/floats.
    Each row must be of the same size.
    div must be a number (int/float) and cannot be 0.
    All results are rounded to 2 decimal places.
    """
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix type
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(all(isinstance(x, (int, float)) for x in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row sizes
    row_length = len(matrix[0]) if matrix else 0
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Divide elements
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
