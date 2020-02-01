#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 08:25:49 2019

@author: nitinkotcherlakota
"""
#Two Number Sum
def twoNumberSum(arr, targetSum):
    # Write your code here.
	for i in range(len(arr)-1):
		first_num = arr[i]
		n = binary_search(arr,targetSum - first_num)
		if n == True:
			return sorted([first_num, targetSum - first_num])
		else:
			continue
	if n == False:
		return []
def binary_search(arr, target):
    arr = sorted(arr)
    return binary_search_func(arr, 0, len(arr) - 1, target)

def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    
    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return binary_search_func(arr, start_index, mid_index - 1, target)
    else:
        return binary_search_func(arr, mid_index + 1, end_index, target)

print(twoNumberSum([4,6],10))
