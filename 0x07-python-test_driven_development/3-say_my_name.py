#!/usr/bin/python3
'''module to print name in a format'''


def say_my_name(first_name, last_name=''):
    '''function to print name
    Args:
    first_name: first name
    last_name: optional parameter

    Raises:
    TypeError: if name is not a string
    '''
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
