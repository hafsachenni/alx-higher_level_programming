#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda h: list(map(lambda k: k**2, h)), matrix))
