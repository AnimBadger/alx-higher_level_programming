#!/usr/bin/python3
'''empty class Rectangle'''


class Rectangle:
    '''class Rectangle'''
    def __init__(self, width=0, height=0):
        '''Instantiate with optional width and height'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width'''
        return self.__width

    @property
    def height(self):
        '''height'''
        return self.__height

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError('width must be integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise ValueError('height must be integer')
        if value < 0:
            raise ValueError('height ,ust be >= 0')
        self.__height = value
