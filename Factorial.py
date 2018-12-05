# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:49:22 2018

@author: sebastian
"""



def factorial(x):
    vector = []
    total = 1
    for i in range(1,x + 1):    
        vector.append(i)
    print(vector)

    for i in range(0, len(vector)):
    
        total = total*vector[i]
    
    
    return total

         
    
        
print(factorial(4))    
    

    
   