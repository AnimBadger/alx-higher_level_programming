#!/usr/bin/python3
import json
'''module to save file using JSON representation'''


def save_to_json(my_obj, filename):
    with open('filename', 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
