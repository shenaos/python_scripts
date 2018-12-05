# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:09:29 2018

@author: sebastian
"""

def is_prime(x):
    
    if x == 1 or x == 0 or x < 0:
        return False   	
    for i in range(2, x):
        
        if x % i == 0:
            print("It's not prime")
            return False            
            break
        #return False
    else:
    #return True
        return True
        print("It's prime")
        
