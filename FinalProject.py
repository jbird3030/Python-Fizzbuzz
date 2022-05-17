#!/usr/bin/env pthon 3
#Final Project
#Author: Jason McGee
#5/9/2021
#Application that allows the user to know which numbers in a range
#are evenly divisible by 3, 5, or both

#Functions to determine if numbers are divisible by 3, 5, or both
def divisible_by_3(n):
    return n % 3 == 0

def divisible_by_5(n):
    return n % 5 == 0

def divisible_by_3_and_5(n):
    return divisible_by_3(n) and divisible_by_5(n)


#User inputs starting and ending values
low = int(input('Please enter a starting value: '))
max = int(input('Please enter an ending value: '))  


#Creates a range between the users values, incrementing by 1s
#Then passes values back to functions
for low_number in range (low,max+1,1):
        
    if divisible_by_3_and_5(low_number):
        print (low_number, ' -- Both')        
    elif divisible_by_3(low_number):
        print (low_number, ' -- 3')       
    elif divisible_by_5(low_number):
        print (low_number, ' -- 5')        
    else: 
        print (low_number) 
       
           


