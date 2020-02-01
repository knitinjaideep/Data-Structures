#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:28:50 2019

@author: nitinkotcherlakota
"""

#Finding the square root of an integer

    
def sqrt(number):
#    """
#    Calculate the floored square root of a number
#
#    Args:
#       number(int): Number to find the floored squared root
#    Returns:
#       int: Floored Square Root
#    """

    if number < 0:
        return "No real square root exists"
    if number == 0 or number == 1:
        return number
    start = 0
    end = number 
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number: 
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans
print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (7 == sqrt(49)) else "Fail")
print ("Pass" if  ("No real square root exists" == sqrt(-1)) else "Fail")
print ("Pass" if  (7 == sqrt(51)) else "Fail")
print ("Pass" if  (35 == sqrt(1247)) else "Fail")