#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 06:05:31 2019

@author: nitinkotcherlakota
"""

#Sort the array in single traversal

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """           
    start = 0
    end = len(input_list) - 1
    counter = 0
    if len(input_list) == 0:
        return []
    while start <= end:
        if input_list[start] == 0:
            input_list[start] = input_list[counter]
            input_list[counter] = 0
            start += 1
            counter += 1
        elif input_list[start] == 2:
            last = input_list[end]
            input_list[end] = 2
            input_list[start] = last
            end -= 1
        else:
            start += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print(sorted_array)
        print(sorted(test_case))
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 1, 1, 1, 2])
test_function([0, 0, 0, 0])
test_function([])