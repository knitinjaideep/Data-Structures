#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 06:11:26 2018

@author: nitinkotcherlakota
"""

class FindTreasure:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = FindTreasure(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = FindTreasure(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

node1 = FindTreasure('A')
node1.InsertData('D')
node1.InsertData('B')
node1.InsertData('C')
node1.PrintTree()

node2 = FindTreasure('B')
node3 = FindTreasure('E')
node4 = FindTreasure('F')
node5 = FindTreasure('G')
node6 = FindTreasure('H')
node7 = FindTreasure('I')
node8 = FindTreasure('J')
node9 = FindTreasure('K')
node10 = FindTreasure('L')
node11 = FindTreasure('M')
node12 = FindTreasure('N')
node13 = FindTreasure('O')
