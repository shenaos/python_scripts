# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:09:28 2018

@author: sebastian
"""


def anti_vowel(text):

    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    vector_a = []
    pattern = ""
    vector_t = []
    for i in text:
        vector_a.append(i)
    print(vector_a)
    for i in vector_a:
        for j in vowels:
            if i == j:
                break
        else:
            vector_t.append(i)           
        
    
    vector_t = pattern.join(vector_t)        
    print(vector_t)
    return vector_t
    #for a, b in zip(vowels, vector_a):
        
        
    
    
    
#    for a, b in zip(list_a, list_b):
 
anti_vowel("Hey You!")   