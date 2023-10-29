#!/usr/bin/python3
def matrix_divided(matrix, div):
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
