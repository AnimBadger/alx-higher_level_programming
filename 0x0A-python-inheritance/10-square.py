#!/usr/bin/python3
'''module for Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class square that inherits from Rectangle'''
    def __init__(self, size):
        '''initialize class'''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''implementing area'''
        return self.__width * self.__height
