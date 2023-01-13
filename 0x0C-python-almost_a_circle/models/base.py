#!/usr/bin/python3
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
