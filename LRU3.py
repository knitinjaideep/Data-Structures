#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 08:16:23 2019

@author: nitinkotcherlakota
"""

class Node(object):
    def __init__(self,key=None,value= None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache:
    def __init__(self,cache_capacity):
        self.cache_dict = dict()
        self.cache_capacity = cache_capacity
        self.itemsInCache = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
 
    def get(self,key):
        if self.cache_capacity == 0:
            return "Cache Capacity is 0, please increase the cache capacity to use it"
        if key not in self.cache_dict:
            return -1
        if key in self.cache_dict:
            node = self.cache_dict[key]
            self.removeFromCache(node)
            self.addToFront(node)
            return node.value
        
  
    def set(self,key,value):
        if self.cache_capacity == 0:
            return "Cache Capacity is 0, please increase the cache capacity to use it"
        if key in self.cache_dict:
            if self.cache_dict[key].value != value:
                self.cache_dict[key].value = value
            self.removeFromCache(self.cache_dict[key])
            self.addToFront(self.cache_dict[key])
        if key not in self.cache_dict:
            new_node = Node(key,value)
            self.addToFront(new_node)
            self.cache_dict[key] = new_node
            self.itemsInCache += 1
        if self.itemsInCache > self.cache_capacity:
            tail = self.tail
            self.removeFromCache(tail)
            del self.cache_dict[tail.key]
            tail.prev = self.tail
            
    def removeFromCache(self,node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev  
        if node.prev is not None and node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            
    def addToFront(self,node):
        node.next  = self.head
        node.prev = None
        
        self.head.prev = node
        self.head = node
        if self.tail.value == 0:
            self.tail = self.head.next    

#Test Case 1
print("Test Case 1")
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(1, 7);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))# returns 7
print(our_cache.get(2))# returns 2
print(our_cache.get(9))# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("-----------------------")
#Test Case 2
print("Test Case 2")
our_cache1 = LRU_Cache(3)
our_cache1.set(1, 1);
our_cache1.set(1, 7);
our_cache1.set(2, 2);
our_cache1.set(3, 3);
our_cache1.set(4, 4);

print(our_cache1.get(1))# returns -1
print(our_cache1.get(2))# returns 2
print(our_cache1.get(9))# returns -1 because 9 is not present in the cache

our_cache1.set(5, 5)
our_cache1.set(6, 6)

print(our_cache1.get(4))# returns -1 because the cache reached it's capacity 

print("-----------------------")
#Test Case 3
print("Test Case 3")
our_cache1 = LRU_Cache(7)
our_cache1.set(1, 1);
our_cache1.set(1, 7);
our_cache1.set(2, 2);
our_cache1.set(3, 3);
our_cache1.set(4, 4);

print(our_cache1.get(1))# returns 7
print(our_cache1.get(2))# returns 2
print(our_cache1.get(9))# returns -1 because 9 is not present in the cache

our_cache1.set(5, 5)
our_cache1.set(6, 6)
print(our_cache1.get(4))# returns 4 because the cache reached it's capacity 

print("-----------------------")
#Edge Case 1
print("Edge Case 1")
our_cache1 = LRU_Cache(0)
our_cache1.set(1, 1);
our_cache1.set(1, 7);
our_cache1.set(2, 2);
our_cache1.set(3, 3);
our_cache1.set(4, 4);
print(our_cache1.get(1))# Cache Capacity is 0, please increase the cache capacity to use it
