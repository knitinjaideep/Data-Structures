#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:03:02 2019

@author: nitinkotcherlakota
"""
A=[3,1,2,4]
n, mod = len(A), 10**9 + 7
left, right, s1, s2 = [0] * n, [0] * n, [], []
for i in range(n):
    count = 1
    print "This is in the for loop:",s1,left
    while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
    left[i] = count
    s1.append([A[i], count])
    print "This is after the for loop",s1,left
    print "---------"