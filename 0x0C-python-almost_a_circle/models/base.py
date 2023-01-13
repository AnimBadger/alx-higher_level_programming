#!/usr/bin/python3
import json
'''Base class module'''


class Base:
    '''declaration of class'''
    __nb_objects = 0
    def __init__(self, id=None):
        '''constructor of class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''static method that returns Json format'''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)