#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 08:49:48 2018

@author: nitinkotcherlakota
"""

#Quick Find - Union

class QuickFindU:
    def __init__(self,n,arr = None):
        if arr == None:
            self.id = self._constructArr(n)
        else:
            self.id = arr
    def _constructArr(self,n):
        temp_arr = []
        for i in range(n):
            temp_arr.append(i)
        return temp_arr
    def root(self,p):
        while(self.p != self.id[p]):
            self.p = self.id[p]
        return self.p
    def connected(self,p,q):
        return self.root(p) == self.root(q)
    def union(self,p,q):
        i = self.root(p)
        j = self.root(q)
        id[i] = j
        
a = QuickFindU(10)
a.union(3,4)
a.root(3)
print a.connected(3,4)
    