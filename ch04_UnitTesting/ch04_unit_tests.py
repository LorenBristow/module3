# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:03:58 2019

@author: loren
"""

import unittest
from is_prime import is_prime


class prime_test(unittest.TestCase):
    def test_prime_is_prime(self): #NB - test MUST begin with 'test' in test function name! Else will not be pulled into unit test run. 
        self.assertTrue(is_prime(2), msg = "prime numbers must return true")
    def test_even_is_not_prime(self):
        self.assertFalse(is_prime(4), msg = "4 is not prime")
    def test_0_is_not_prime(self):
        self.assertFalse(is_prime(0), msg = "prime nums must be greater than 0")
    def test_1_is_not_prime(self):
        self.assertFalse(is_prime(1), msg = "1 is not prime")
    def test_negative_is_not_prime(self):
        self.assertFalse(is_prime(-5), msg = "prime nums are only positive")

from is_prime import wordcount

class wordcount_test(unittest.TestCase):
    def test_wordcount(self):
        self.assertDictEqual({'foo': 2,'bar': 1}, wordcount('foo bar foo')) 
    def test_wordcount_type(self):
        self.assertIsInstance(wordcount('foo bar foo'), dict) 
        
if __name__ == '__main__':
    unittest.main()


   