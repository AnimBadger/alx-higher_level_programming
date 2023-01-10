#!/usr/bin/python3
import json
'''module to return object by JSON string'''


def from_json_string(my_str):
    return json.loads(my_str)
