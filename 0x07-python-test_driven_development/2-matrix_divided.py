#!/usr/bin/python3
'''module to divide matrix'''


def matrix_divided(matrix, div):
    '''function to divide matrix'''

    err_type = 'matrix must be a matrix (list of lists) of integers/floats'
    error_msg_size = 'Each row of the matrix must have \
        the same size'

    if not isinstance(div, int) or not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not matrix or not isinstance(matrix, list):
        raise TypeError(err_type)

    len_e = 0

    for items in matrix:
        if not items or not isinstance(items, list):
            raise TypeError(err_type)

        if len_e != 0 and len(items) != len_e:
            raise TypeError(error_msg_size)

        for in_item in items:
            if not type(in_item) in (int, float):
                raise TypeError(err_type)

        len_e = len(items)

    r = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return r
