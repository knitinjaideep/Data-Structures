#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:05:20 2019

@author: nitinkotcherlakota
"""
height = [2,3,4,5,18,17,6]
i = 0
j = len(height) - 1
maxA = 0
while i < j:
    length = min(height[i],height[j])
    breadth = j-i
    Area = length * breadth
    maxA = max(maxA,Area)
    if height[j] < height[i]:
        j -= 1
    else:
        i += 1
print maxA