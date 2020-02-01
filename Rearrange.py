#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:15:29 2019

@author: nitinkotcherlakota
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    count = 0
    number_1 = ""
    number_2 = ""
    if len(input_list) == 0:
        return []
    if len(input_list) > 0 and len(input_list) <= 2:
        return input_list
    else:
        for i in range(9,-1,-1):
            if i in input_list:
                if count == 0:
                    number_1 += str(i)
                    count += 1
                elif count == 1:
                    number_2 += str(i)
                    count -= 1
            else:
                continue
    
    return [int(number_1), int(number_2)]
            


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case1 = [[],[]]
test_case2 = [[1],[1]]

test_function(test_case)
test_function(test_case1)
test_function(test_case2)