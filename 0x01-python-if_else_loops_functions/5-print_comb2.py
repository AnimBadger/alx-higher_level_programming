#!/usr/bin/python3
for i in range(10):
    for j in range(9):
        print('{:d}{:d}'.format(i, j), end=', ')
print(f'{i}{j + 1}')
