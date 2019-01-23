# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:30:36 2019

@author: loren
"""

#print("what is your age?")
#age = int(input())
#
#
#
###TASK 1###
#option = input("please input yes or no").lower()
#
#if len(option) in range(1,4):
#    print("thanks")
#else:
#    option = input("please try again - input yes or no").lower()
#    


###TASK 2###
choice = int(input("What is your choice? "))
while True:
    try:
        while choice < 1 or choice > 3:
            choice = int(input("What is your choice? "))
            #break
    except ValueError:
        print("please try another number")
    print('***choice****')
    print('1. Display my name')
    print('2. Display my age')
    print('3. Display my city')
    print("What is your choice? {}".format(choice))
    if choice == 1:
        print('Ms Wu')
    elif choice == 2:
        print('5 years old')
    elif choice == 3:
        print('London')
    break
