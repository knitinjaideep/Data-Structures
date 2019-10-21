#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 06:12:36 2019

@author: nitinkotcherlakota
"""

#permutations

def permutations(nums):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    
#    if string == '':
#        return ''
#    for i,n in enumerate(string):
#        for p in permutations(string[:i] + string[i+1:]):
#            return n + p
#    
    return [[]] or [[n] + p 
            for i, n in enumerate(nums)
            for p in nums[:i] + nums[i+1:]]

print(permutations([1,2,3]))