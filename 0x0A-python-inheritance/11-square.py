#!/usr/bin/python3
'''module for Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class square that inherits from Rectangle'''
    def __init__(self, size):
        '''initialize class'''
        Rectangle.integer_validator(self, 'size', size)
        self.__size = size
        
    def area(self):
        '''implementing area'''
        return self.__width * self.__height
    
    def __str__(self) -> str:
        return '[Square] {}/{}'.format(self.__width, self.__height)
