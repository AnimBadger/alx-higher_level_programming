#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_cpy = matrix.copy()
    for i in range(len(new_cpy)):
        new_cpy[i] = list(map(lambda x: x ** 2, new_cpy[i]))
    return new_cpy
