#!/usr/bin/python3
'''Module that contains a function that reads from a file'''


def read_file(filename=''):
    '''function that reads from file
    Args:
    filename: filename
    Raises
    Exception: when file cannot be open
    '''
    with open('filename', 'r', encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end='')
