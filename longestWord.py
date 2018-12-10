#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:40:18 2018

@author: labfluidos
"""

def longestWord(sen):
    
    word_a = []
    new_word = ""
    win = 0
    equal  = 0
    for i in sen:
        
        if i.isalpha() == True:
            word_a.append(i)
            new_word += i
        elif i == " ":
            new_word += " "
            word_a.append(" ")        
    print(word_a)
    print(new_word)
    
    new_word = new_word.split(" ")
    print(new_word)
    
    for i in range(0, len(new_word)):
        for j in new_word:
            if len(j) > len(new_word[i]):
                win = j
    
    for i in new_word:
        if len(i) == len(win):
            win = i
            break
    
        
    print(win)
    
    
    #print(new_word)
            
    
    
    
longestWord("I love dogs")