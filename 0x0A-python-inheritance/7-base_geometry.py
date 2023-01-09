#!/usr/bin/python3
'''class BaseGeometry that raise exception'''


class BaseGeometry:
    '''class that raise exception'''
    def area(self):
        '''public method that raise exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validate a parameter as integer
        Args:
        name (str): name of the parameter
        value (int): parameter to validate
        Raises:
        TypeError: if value is not integer
        ValueError: if value is less than or equal to 0
        '''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
