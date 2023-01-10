#!/usr/bin/python3
import json
'''Module to covert to Json'''


def to_json_string(my_obj):
    '''function to convert to json
    Args:
    my_obj: object to convert to json
    '''
    return json.dumps(my_obj)
