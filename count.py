# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:28:28 2018

@author: sebastian
"""


def count(sequence, item):


    total = 0    
    for i in sequence:
        if i == item:
            total += 1
    
    print(total)
    return total
    

count([1, 2, 1, 1], 1)