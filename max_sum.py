#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 06:14:59 2019

@author: nitinkotcherlakota
"""

#sum of nums
nums = [-2,-1]
l = 0
m = len(nums) - 1
maxs = -2**31
if len(nums) <= 1:
    print nums[l]
while l < m:
    maxs = max(maxs,sum(nums[l:m+1]),nums[l],nums[m])
    if nums[l] < nums[m]:
        l += 1
    else:
        m -= 1
print maxs