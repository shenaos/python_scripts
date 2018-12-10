#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:43:52 2018

@author: labfluidos
"""

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = int(len(sorted_list)/2 - 1)
        index_2 = int(len(sorted_list)/2)
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print(median([4, 4, 5, 5]))