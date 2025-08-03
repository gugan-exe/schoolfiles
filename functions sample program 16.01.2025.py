# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:07:43 2025

@author: SSS Family
"""

def donkey(x,y):
    x=int(input("Enter your first number: "))
    y=int(input("Enter your second number: "))
    result=x+y
    return result,x,y
    
def multiplication(x,y):
    x=int(input("Enter your first number: "))
    y=int(input("Enter your second number: "))
    result=x*y
    return result

sum,x,y=donkey("x","y")
print(x,y,sum)
mul=multiplication("x","y")
print(mul)
print(sum*mul)
