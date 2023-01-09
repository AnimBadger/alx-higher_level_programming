#!/usr/bin/python3
'''class BaseGeometry that raise exception'''


class BaseGeometry:
    '''empty class that raise exception'''
    def area(self):
        '''public method that raise exception'''
        raise Exception('area() is not implemented')
