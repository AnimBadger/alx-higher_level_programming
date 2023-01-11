#!/usr/bin/python3
'''module to print squares in hash'''


def print_square(size):
    '''function to print square
    Args:
    size: size of square

	Raises:
	TypeError: if size not type int
	ValueError: if size not >= 0
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    size = int(size)

    for sqr in range(size):
        for in_sqr in range(size):
            print('#', end='')
        print()
