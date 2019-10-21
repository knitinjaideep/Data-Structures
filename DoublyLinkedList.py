#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 08:29:18 2018

@author: nitinkotcherlakota
"""

#doubly Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def push(self,data):
        NewData = Node(data)
        NewData.next = self.head
        if self.head is not None:
            self.head.prev = NewData
        self.head = NewData
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next
    def gethead(self):
        print '\n'
        print self.head.data
    def getTail(self):
        curr = self.head
        temp = curr.prev 
        while curr is not None:
            temp = curr
            curr = curr.next
        while temp is not None:
            temp = temp.prev
            print temp.data
        
d = DLL()
d.push('Mon')
d.push('Tue')
d.push('Wed')
d.listprint(d.head)
d.gethead()
d.getTail()
#d.reverse()
#d.listprint(d.head)

