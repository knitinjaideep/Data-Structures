#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:55:13 2018

@author: nitinkotcherlakota
"""

class Queue:
    def __init__(self):
        self.queue = []
    def add(self,data):
        if self.queue is not None:
            self.queue.insert(0,data)
        else:
            return False
    def remove(self):
        if self.queue is not None:
            self.queue.pop()
    def printqueue(self):
        print ','.join([x for x in self.queue])
q = Queue()
q.add('1')
q.add('2')
q.printqueue()