#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda a: a * a), elm)) for elm in matrix]
