#!/usr/bin/python3
"""a function that divides all elemnts of a matrix
matrix must be a list of lists of ints and floats otherwise
raise typeerror, each row of matrix must be of the same size
div must be a number otherwise raise typeerror
div cant be equal to 0 otherwise raise zerodivision error
All elements of the matrix should be divided by div"""


def matrix_divided(matrix, div):
    """division of the numbers while raising the
    errors mentioned upwards and returning
    a new matrix"""
    for el in range(len(matrix)):
        if not isinstance(matrix[el], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
                raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = round((num / div), 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
