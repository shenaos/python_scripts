#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:09:43 2018

@author: labfluidos
"""

def median(x):
    x = sorted(x)
    pos1 = 0
    pos2 = 0
    mediana = 0
    if len(x) % 2 == 0:
        
        pos1 = x[int((len(x)/2))]
        pos2 = x[int((len(x)/2)-1)]
        
        mediana =  (pos1 + pos2)/2
            
    elif len(x) % 2 != 0:
        
        mediana =  x[int(((len(x)-1)/2))]
    
    print(mediana)
    
    return  round(mediana)
median([4, 5, 5, 4])
