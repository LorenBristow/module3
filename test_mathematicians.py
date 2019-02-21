# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:55:54 2019

@author: loren
"""

from mathematicians import simple_get
raw_html = simple_get('https://headmasters.com/')
print(len(raw_html))
