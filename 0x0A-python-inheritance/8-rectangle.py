#!/usr/bin/python3
'''module subclass Rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


'''class Rectangle that inherits from BaseGeometry'''


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
