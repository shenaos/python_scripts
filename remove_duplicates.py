#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:27:46 2018

@author: labfluidos
"""

def remove_duplicates(x):
    vector = []
    vector_a = []
    for i in x:
        vector.append(i)
    
    for i in range(0,len(x)):
        for j in vector_a:
            if len(vector_a) == 0:
                vector_a.append(x[i])
                break
            if x[i] == j:
                break
        else:
            vector_a.append(x[i])
            
    print(vector_a)
    return vector_a
remove_duplicates([1,1,0,1,2,1,1,1,2, 2])            
        
        