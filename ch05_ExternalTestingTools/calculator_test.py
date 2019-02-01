# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:36:55 2019

@author: loren
"""

import unittest
from calculator import calculator

class calculator_tests(unittest.TestCase):
    #calc = calculator()
    
    def test_add_works(self):
        result = calculator().add(self,2,2)
        self.assertEqual(4, result)
    def test_add_works_with_neg_input(self):
        result = calculator().add(self,-4,2)
        self.assertEqual(-2, result)
    def test_string_input_rejected(self):
        self.assertRaises(ValueError, calculator().add,'two', 'two' )
if __name__ == '__main__':
    unittest.main()