#!/usr/bin/python3
'''a function to check if object is instance of specific class'''


def is_same_class(obj, a_class):
    '''return true if is instance, false otherwise'''
    if type(obj) == a_class:
        return True
    else:
        return False
