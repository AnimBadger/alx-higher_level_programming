#!/usr/bin/python3
'''class to print list in ascending order'''


class MyList(list):
    '''Inherits from list'''
    def print_sorted(self):
        '''print a inherited list in ascending order'''
        return sorted(self)
