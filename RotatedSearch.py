#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:39:10 2019

@author: nitinkotcherlakota
"""



def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    
    if arr[mid_index] == target:
        return mid_index
    index_right_side = binary_search_func(arr, start_index, mid_index - 1, target)
    index_left_side = binary_search_func(arr, mid_index + 1, end_index, target)
    return max(index_left_side, index_right_side)



def rotated_array_search(input_list: list, number: int) -> int:
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array): Input array to search
       number (int): target to search
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    return binary_search_func(input_list, 0, len(input_list) - 1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
#edge cases
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 1])
test_function([[1, 2, 3, 4, 5, 6], 4])