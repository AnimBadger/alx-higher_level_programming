#!/usr/bin/python3
'''class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        '''get/set size of square'''
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    