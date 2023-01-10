#!/usr/bin/python3
'''module to return dictionary with JSON structure'''


def class_to_json(obj):
    '''function to return dictionary of obj'''
    
    result = {}
    if hasattr(obj, '__dict__'):
        result = obj.__dict__.copy()
    return result
