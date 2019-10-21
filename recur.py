#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 05:23:23 2019

@author: nitinkotcherlakota
"""

#def sums(arr,size):
#    sum = 0
#    for i in range(size):
#        sum += arr[i]
#    return sum
def delegate(arr,size):
    if size == 0:
        return 0
    lastelement = arr[size-1]
    onelesselement = delegate(arr,size - 1)
    return lastelement + onelesselement

print(delegate([1,2,3,4],4))



[1,2,3,[5,6,[8,9]]]

[[[9,8],6,5],3,2,1]