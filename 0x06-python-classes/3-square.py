#!/usr/bin/python3
'''class Square to define square'''


class Square:
    '''class Square to define square'''

    def __init__(self, size=0):
        '''Initialize Square

        Args:
            size (int): size of Square
        '''

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''returns the area.

        Returns:
            area
        '''

        return self.__size ** 2
