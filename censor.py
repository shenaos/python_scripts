# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:06:21 2018

@author: sebastian
"""

def censor(text, word):
    vector=[]
    pattern = " "
    vector = text.split(" ")
    print(vector)    
    for i in range(0,len(vector)):  
        if vector[i] == word:
            vector[i] = len(word)*'*'        
    
    vector = pattern.join(vector)
    print(vector)
    return vector
    
    
    

censor("hola hola hola", "hola")
    