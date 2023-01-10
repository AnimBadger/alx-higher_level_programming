#!/usr/bin/python3
'''module to return object by JSON string'''
import json


def from_json_string(my_str):
    '''
    function to return json string
    Args:
    my_str: string to convert
    '''
    return json.loads(my_str)
