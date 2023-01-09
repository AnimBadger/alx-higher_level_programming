#!/usr/bin/python3
'''Module to check if class is a subclass'''


def is_kind_of_class(obj, a_class):
    '''return true if object is instance of the object, false if otherwise'''
    return isinstance(obj, a_class)
