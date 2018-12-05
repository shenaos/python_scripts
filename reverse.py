# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:25:36 2018

@author: sebastian
"""
"""
a = ["a","b","c","d"]


for i in range(len(a)-1,-1,-1):
     print(a[i])   
"""
    

def reverse(text):
    vector = []
    ab_vect = []
    pattern =""
    for i in text:
        vector.append(i)
    print(vector)
    for i in range(len(vector)-1,-1,-1):   
        
        ab_vect.append(vector[i])
    
    print(pattern.join(ab_vect))        
    return pattern.join(ab_vect)
            
reverse("abcd")
