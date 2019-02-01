# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:00:27 2019

@author: loren
"""
#### TASK 1 - PRIME NUMBERS to FAIL & TASK 2 - to PASS  ####
def is_prime(number):
    '''Return True if number is a prime number'''
    if number <= 1:
        return False
    elif number > 1:#to prevent div by 0 error 
        for each in range(2,number):
            if number % each == 0 and number != each:
                print("false")
                return False
        return True
    else:
        print("weird")

def print_next_prime(number): ##something still wrong here. 
    '''If number is prime, provide next prime number'''
    next_number = number
    while is_prime(number) == True: 
        next_number += 1
        if is_prime(next_number) == True:
            print("After {}, the next prime number is {}".format(number, next_number))
            return number

### TASK 4 - Count Words ###

def wordcount(text):
    wordcount_dictionary = {}
    words = text.split()
    for word in words:
        if word in wordcount_dictionary:
            wordcount_dictionary[word] = wordcount_dictionary[word] + 1
        else:
            wordcount_dictionary[word] = 1
    return wordcount_dictionary

       

wordcount('foo bar foo') 