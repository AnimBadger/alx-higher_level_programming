#!/usr/bin/python3
'''module to create object from JSON'''
import json


def load_from_json_file(filename):
    '''function to create object from JSON'''
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
