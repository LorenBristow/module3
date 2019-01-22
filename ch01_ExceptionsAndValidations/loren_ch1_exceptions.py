# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:54:28 2019

@author: loren
"""

print("###TASK 1###")

try:
    f = open("testfile.txt")
    s1 = not_exists
except Exception as e: # indicates specific problem line
    print(e)    

print("###TASK 2###")

try:
    f = open("testfile.txt")
except Exception as e:
    print(e)  
else:  #else is executed if the try does not raise exception. 
    print(f.read())
    f.close()
    
print("###TASK 3###")    
      
try:
    f = open("testfile.txt")
except Exception as e:
    print(e)  
else:  #else is executed if the try does not raise exception. 
    print(f.read())
    f.close()      
finally:
    print("Executing finally...")   
    
  