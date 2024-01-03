#!/usr/bin/python3
"""Defines a function for dividing all elements in a matrix."""

def matrix_divided(matrix, divisor):
    """Performs division on each element in a matrix.

    Args:
        matrix (list): A list of lists containing integers or floats.
        divisor (int/float): The number by which to divide matrix elements.

    Raises:
        TypeError: If elements in the matrix are not numbers.
        TypeError: If rows in the matrix have varying lengths.
        TypeError: If divisor is not a number.
        ZeroDivisionError: If divisor is zero.

    Returns:
        list: A new matrix with each element divided by the divisor.
    """
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(element, (int, float)) for element in [item for sublist in matrix for item in sublist])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must be of the same size")

    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / divisor, 2) for element in row] for row in matrix]

