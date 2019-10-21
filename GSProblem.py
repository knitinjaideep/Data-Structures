#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 08:19:22 2018

@author: nitinkotcherlakota
"""

d = {}
x = [['john', 60],
 ['b', 80],
 ['john', 95],
 ['b', 45],
 ['b', 55]]
for i in range(5):
    if x[i][0] in d:
        d[x[i][0]][0] = x[i][1] + d[x[i][0]][0]
        d[x[i][0]][1] += 1
    else:
        d[x[i][0]] = [x[i][1],1]
for i in d:
        d[i] = (d[i][0]/d[i][1])
print max(d, key = d.get),d[max(d, key=d.get)]