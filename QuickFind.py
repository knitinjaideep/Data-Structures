#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 07:53:55 2018

@author: nitinkotcherlakota
"""

class QuickFindUF(object):
    id = []
    
    def __init__(self,n,arr = None):
        if arr == None:
            self.id = self._constuct_array(n)
        else:
            self.id = arr

    def _constuct_array(self, n):
        temp_arr = []
        for e in range(n):
            temp_arr.append(e)
        return temp_arr

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for e in range(len(self.id)):
            if self.id[e] == pid:
                self.id[e] = qid
q = QuickFindUF(10)
q.union(4,3)
print q.connected(4,3)
