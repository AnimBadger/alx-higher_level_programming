#!/usr/bin/python3
'''module to save file using JSON representation'''
import json


def save_to_json_file(my_obj, filename):
    '''
    function to save file using JSON
    Args:
    my_obj: object
    filename: name of file
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
