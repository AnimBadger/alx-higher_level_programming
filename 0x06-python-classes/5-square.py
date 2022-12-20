#!/usr/bin/python3
'''class Square to define square'''


class Square:
    '''class Square to define square'''

    def __init__(self, size=0):
        '''Initialize Square

        Args:
             size (int): size of Square
        '''

        self.size = size

    @property
    def size(self):
        '''int: private size

        Returns:
            private size
        '''

        return self.__size

    @size.setter
    def size(self, value):
        '''Sets value into size

        Args:
            value (int): size of the square
        '''

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  # : size of the square

    def area(self):
        '''returns the area.

        Returns:
            area
        '''

        return self.__size ** 2

    def my_print(self):
        '''Print out square with character #'''

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
