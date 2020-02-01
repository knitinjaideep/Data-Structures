#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 05:50:45 2019

@author: nitinkotcherlakota
"""

#LRU Cache
#from collections import deque
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def addToFront(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        new_node.next = self.head
        self.head = new_node
        return 
    def removeNode(self,value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        if self.tail.value == value:
            self.tail = self.tail.prev
            
        node = self.head
        while node.next:
            if node.next.value == value:
                returned_node = node.next
                node.next = node.next.next
                return returned_node
            node = node.next
    def moveToFront(self,node):
        self.removeNode(node)
        self.addToFront(node)
    def removeTail(self,node):
        return
    def printList(self):
        if self.head is None:
            return None
        node = self.head
        while node:
            print(node.value)
            node = node.next

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.capacityCount = 0
        self.cache = DoublyLL()
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache_dict:
            self.cache.moveToFront(key)
            return self.cache_dict[key]
        else:
            return
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacityCount >= self.capacity:
            self.cache.removeTail()
        self.cache.addToFront(key)
        self.cache_dict[key] = value
        self.capacityCount += 1
    def printCache(self):
        self.cache.printList()
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.printCache()
print(our_cache.cache_dict)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(9))
our_cache.set(5, 5) 
#our_cache.set(6, 6)
print(our_cache.cache)
print(our_cache.cache_dict)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.cache_dict)