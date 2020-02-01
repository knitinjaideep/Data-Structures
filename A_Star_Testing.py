#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:11:44 2020

@author: nitinkotcherlakota
"""

from Queue import PriorityQueue

class State:
    def __init__(self,value,parent,start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = []
            self.start = start
            self.goal = goal
    
    def GetDist(self):
        pass
    def CreateChildren(self):

class State_String(State):
    def __init__(self,value,parent,start = 0, goal = 0):
        super(State_String,self).__init__(value,parent,start,goal)
        self.dist = self.GetDist()
    
    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist
    def 