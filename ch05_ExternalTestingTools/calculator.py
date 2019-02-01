# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:37:18 2019

@author: loren
"""

class calculator(object):
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            return ValueError
        
#print(calculator().add('hey',4))