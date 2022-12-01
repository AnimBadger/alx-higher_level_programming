#!/usr/bin/python3
import sys
if __name__ == '__main__':
    n = len(sys.argv)
    if n <= 1:
        print('{:d} arguments.'.format(0))
    elif (n == 2):
        print('{:d} arguement:'.format(n - 1))
        for i in range(1, n):
            print('{:d}: {:s}'.format(i, sys.argv[i]))
    else:
        print('{:d} arguments:'.format(n - 1))
        for i in range(1, n):
            print('{:d}: {:s}'.format(i, sys.argv[i]))
