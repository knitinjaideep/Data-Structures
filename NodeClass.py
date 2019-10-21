#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 07:47:34 2018

@author: nitinkotcherlakota
"""

class Node:
    def __init__(self,dataval):
        self.dataval= dataval
        self.nextval = None
        
e1 = Node('Mon')
e2 = Node('Wed')
e3 = Node('Tue')

e1.nextval = e3
e3.nextval = e2

thisval = e1

while thisval:
    print thisval.dataval,
    thisval = thisval.nextval