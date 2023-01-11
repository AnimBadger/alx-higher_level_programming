#!/usr/bin/python3
'''Unittest for max_integer([..])'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''class for tests'''
    
    def test_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)
        
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        
    def test_repeated_numbers(self):
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)
    
    def test_float_numbers(self):
        self.assertEqual(max_integer([21.5, 20.5, 6.7, 100.0]), 100.0)
        