#!/usr/bin/python3
import sys
if __name__ == '__main__':
    n = len(sys.argv)
    sums = 0
    if (n <= 1):
        print('{:d}'.format(sums))
        sys.exit()
    else:
        for i in range(1, n):
            sums += int(sys.argv[i])
    print('{:d}'.format(sums))
