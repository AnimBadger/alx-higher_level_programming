#!/usr/bin/python3
'''Module th write string to text file'''


def write_file(filename='', text=''):
    with open('filename', 'w', encoding='utf-8') as file:
        return file.write(text)
