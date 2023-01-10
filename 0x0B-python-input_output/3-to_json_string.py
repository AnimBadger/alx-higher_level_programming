#!/usr/bin/python3
'''Module to covert to Json'''
import json


def to_json_string(my_obj):
    '''function to convert to json
    Args:
    my_obj: object to convert to json
    '''
    return json.dumps(my_obj)
