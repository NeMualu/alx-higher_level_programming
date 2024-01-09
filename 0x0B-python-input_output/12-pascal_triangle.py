#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Create Pascal's Triangle of size n.

    Returns a nested list of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) < n:
        last_row = pascal[-1]
        next_row = [1]
        for j in range(len(last_row) - 1):
            next_row.append(last_row[j] + last_row[j + 1])
        next_row.append(1)
        pascal.append(next_row)
    return pascal

