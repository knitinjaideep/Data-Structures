#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:02:39 2019

@author: nitinkotcherlakota
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):

    head1 = llist_2.head
    temp_list = LinkedList()
    temp_list = copy(llist_1,temp_list)    
    while head1:
        temp_list.append(head1.value)
        head1 = head1.next
    union_list = LinkedList()
    union_list = removeDuplicates(temp_list)
    if union_list.head is None:
        return "Both lists are empty"
    return union_list

def copy(llist,temp_list):
    head1 = llist.head
    while head1:
        temp_list.append(head1.value)
        head1 = head1.next
    return temp_list

def removeDuplicates(llist):
    l = []
    new_llist = LinkedList()
    llhead = llist.head
    while llhead:
        if llhead.value not in l:
            l.append(llhead.value)
            new_llist.append(llhead)
        llhead = llhead.next
    return new_llist

def intersection(llist_1, llist_2):
   
    intersection_list = LinkedList()
    new_list = set()
    head1 = llist_1.head
    while head1:
        head2 = llist_2.head
        while head2:
            if head1.value == head2.value:
                new_list.add(head1.value)
            head2 = head2.next
        head1 = head1.next
    for num in new_list:
        intersection_list.append(num)
    if intersection_list.head is None:
        return "No common elements"
    return intersection_list


# Test case 1
print("\n----------------Test Case 1----------------\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,4,9,6,1,11,21,4]

for i in element_1:
    linked_list_1.append(i)
print("----")
for i in element_2:
    linked_list_2.append(i)

print ("Union of 2 lists is: ",union(linked_list_1,linked_list_2))
print ("Intersection of 2 lists is: ",intersection(linked_list_1,linked_list_2))

# Test case 2
print("\n----------------Test Case 2----------------\n")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("Union of 2 lists is: ",union(linked_list_3,linked_list_4))
print ("Intersection of 2 lists is: ",intersection(linked_list_3,linked_list_4))

# Test case 3
print("\n----------------Test Case 3----------------\n")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,3,3,3,3]
element_2 = [4,3,3,3,2]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ("Union of 2 lists is: ",union(linked_list_5,linked_list_6))
print ("Intersection of 2 lists is: ",intersection(linked_list_5,linked_list_6))

# Edge case 1
print("\n----------------Edge Case 1----------------\n")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [4,3,3,3,2]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print ("Union of 2 lists is: ",union(linked_list_7,linked_list_8))
print ("Intersection of 2 lists is: ",intersection(linked_list_7,linked_list_8))

# Edge case 2
print("\n----------------Edge Case 2----------------\n")
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [4,3,3,3,2]
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print ("Union of 2 lists is: ",union(linked_list_9,linked_list_10))
print ("Intersection of 2 lists is: ",intersection(linked_list_9,linked_list_10))

# Edge case 3
print("\n----------------Edge Case 3----------------\n")
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print ("Union of 2 lists is: ",union(linked_list_9,linked_list_10))
print ("Intersection of 2 lists is: ",intersection(linked_list_9,linked_list_10))