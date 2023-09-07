#!/usr/bin/python3
"""divides matrix"""


def matrix_divided(matrix, div):
    """
    Check if matrix is made up of  integers/floats
    """
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """check for empty matrix"""
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """ Check  row  size"""
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """ Check if div is a number"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """Check if div is not equal to zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
