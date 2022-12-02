#!/usr/bin/python3
import sys
if __name__ == '__main__':
    n = len(sys.argv) - 1
    if n < 1:
        print('{:d} arguments.'.format(n))
    elif (n == 1):
        print('{:d} argument:'.format(n))
        for i in range(1, n + 1):
            print('{:d}: {}'.format(i, sys.argv[i]))
    else:
        print('{:d} arguments:'.format(n))
        for i in range(1, n + 1):
            print('{:d}: {}'.format(i, sys.argv[i]))
