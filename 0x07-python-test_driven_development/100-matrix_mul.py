#!/usr/bin/python3
"""
Defines a function for matrix multiplication.
"""


def matrix_mul(matrix_a, matrix_b):
    """Multiply two matrices.

    Args:
        matrix_a (list of lists of ints/floats): The first matrix.
        matrix_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If either matrix_a or matrix_b is not a list of lists of ints/floats.
        TypeError: If either matrix_a or matrix_b is empty.
        TypeError: If either matrix_a or matrix_b has different-sized rows.
        ValueError: If matrix_a and matrix_b cannot be multiplied.

    Returns:
        list of lists of ints/floats: A new matrix representing the multiplication of matrix_a by matrix_b.
    """

    if not matrix_a or not matrix_a[0]:
        raise ValueError("matrix_a can't be empty")
    if not matrix_b or not matrix_b[0]:
        raise ValueError("matrix_b can't be empty")

    if not isinstance(matrix_a, list):
        raise TypeError("matrix_a must be a list")
    if not isinstance(matrix_b, list):
        raise TypeError("matrix_b must be a list")

    if not all(isinstance(row, list) for row in matrix_a):
        raise TypeError("matrix_a must be a list of lists")
    if not all(isinstance(row, list) for row in matrix_b):
        raise TypeError("matrix_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in matrix_a for num in row]):
        raise TypeError("matrix_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in matrix_b for num in row]):
        raise TypeError("matrix_b should contain only integers or floats")

    if not all(len(row) == len(matrix_a[0]) for row in matrix_a):
        raise TypeError("each row of matrix_a must be of the same size")
    if not all(len(row) == len(matrix_b[0]) for row in matrix_b):
        raise TypeError("each row of matrix_b must be of the same size")

    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("matrix_a and matrix_b can't be multiplied")

    transposed_b = [[matrix_b[j][i] for j in range(len(matrix_b))] for i in range(len(matrix_b[0]))]

    result_matrix = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in transposed_b] for row_a in matrix_a]

    return result_matrix

