#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:53:28 2018

@author: labfluidos
"""

def check_bit4(input):
    
    mask = 0b01000
    
    check = mask & input
    
    if check >= 8:
        return "on"
    else:
        
        return "off"


def flip_bit(number, n):
    mask = 0b0000000001
    result = 0
    result  = number ^ (mask << (n-1))
    return result


print(flip_bit())

"""
a = 0b11101110
mask = 0b11111111
resul  =  mask ^ a
print(bin(resul))
"""