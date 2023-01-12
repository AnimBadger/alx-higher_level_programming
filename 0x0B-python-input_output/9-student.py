#!/usr/bin/python3
'''module that define class Student'''


class Student:
    '''class to create instance of student'''
    
    def __init__(self, first_name, last_name, age):
        '''initialization'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        '''method to return directory description'''
        return self.__dict__.copy()
