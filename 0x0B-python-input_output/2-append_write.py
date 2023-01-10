#!/usr/bin/python3
'''module to append text to file'''


def append_write(filename='', text=''):
    '''
    function to append text to file
    Args:
    filename: filename
    text: text to append with
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
