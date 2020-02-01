#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 06:19:23 2019

@author: nitinkotcherlakota
"""

import random
def get_min_max(ints):
    mini = float("inf") 
    maxi = -float("inf")
    if len(ints) == 0:
        return None
    for i in ints:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    
    return (mini,maxi)

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
l1 = [i for i in range(-100,300)]
random.shuffle(l1)
l2 = [i for i in range(0,0)]
print ("Pass" if (None == get_min_max(l2)) else "Fail")
print ("Pass" if ((-100,299) == get_min_max(l1)) else "Fail")
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")