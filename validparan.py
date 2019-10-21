#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:38:39 2019

@author: nitinkotcherlakota
"""

#Daily interview pro
"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
"""
def validPar(s):

    left_chars = []
    lookup = { '(':')', '[':']', '{':'}'}
    
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()]!= c:
            return False
    return not left_chars

print(validPar('({[)]'))

#Input: "((()))"
#Output: True
#
#Input: "[()]{}"
#Output: True
#
#Input: "({[)]"
#Output: False