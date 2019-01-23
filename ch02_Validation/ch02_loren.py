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
#

###TASK 2###

choice = 0
while True:
    try:
        while choice < 1 or choice > 3:
            choice = int(input("What is your choice - 1, 2 or 3? "))
            #break
    except ValueError:
        choice = int(input("Please type a number in digits. "))
    else:
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


##extra exception example from Mabel###
#try:
#    with open('test.txt', 'r') as f:
#        f_text = f.read()
#        if f.name == 'test.txt':
#            # it's better to raise specific errors than generic
#            raise OSError('that is the wrong file!')
#except Exception as e:
#    print(e)
#else:
#    print(f_text)
#finally:
#    print('this is the end!')
