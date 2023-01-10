#!/usr/bin/python3
'''Module th write string to text file'''


def write_file(filename='', text=''):
    '''function to write text to file
    Args:
    filename: filename
    text: text to be written
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
