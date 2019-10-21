#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:26:32 2019

@author: nitinkotcherlakota
"""

#Stack: Linked-List implementation 
class LinkedList:
    def __init__(self):
        self.head = None
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
    def isEmpty(self):
        return self.head == None
    def push(self,newdata):
        olddata = self.head
        self.head = Node(newdata)
        self.head.next = olddata
    def pop(self):
        item = self.head
        self.head = self.head.next
        return item
    def printlist(self,node):
        while (node is not None):
            print(node.data)
            node = node.next
            
l = LinkedList()
l.push(5)
l.push(6)
l.printlist(l.head)
