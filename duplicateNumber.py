#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 04:34:16 2019

@author: nitinkotcherlakota
"""

#duplicate number in an array
arr = [0,0,1]

def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    d = {}
    for i in range(0,len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        elif d[arr[i]] in d:
            return arr[i]
print(duplicate_number(arr))