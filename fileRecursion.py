#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:13:25 2019

@author: nitinkotcherlakota
"""

def threeNumberSum(array, targetSum):
	final_array = []
	for i in range(len(array)-2):
		a = array[i]
		for j in range(i+1,len(array)-1):
			b = array[j]
			for k in (i+2,len(array)):
				c = array[k]
				if a+b+c == targetSum:
					final_array.append(sorted[a,b,c])
    if len(final_array) == 0:
        return []
    else:
        final_array

array = [1,2,3,4,5,6]
targetSum = 10