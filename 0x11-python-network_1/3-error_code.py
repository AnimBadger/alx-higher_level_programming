#!/usr/bin/python3
'''using HTTPError'''
from urllib import request, error


if __name__ == '__main__':
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)
