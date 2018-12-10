#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:25:24 2018

@author: labfluidos
"""

def product(x):
    total = 1
    for i in x:    
        total = total*i
    
    print(total)
    return total

product([4, 5, 5])