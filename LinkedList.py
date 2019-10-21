#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 08:35:12 2018

@author: nitinkotcherlakota
"""
########################################  
#Node class
########################################  
class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None
########################################  
#Create a Singly Linked List
########################################  
class SLL:
    def __init__(self):
        self.headval = None
########################################  
#Printing the linked list
########################################  
    def printval(self):
        thisval = self.headval
        while thisval is not None:
            print(thisval.dataval)
            thisval = thisval.nextval
########################################  
#Inserting at the beginning of the list
########################################  
    def AtBeginning(self,Newdata):
        Newnode = Node(Newdata)
        Newnode.nextval = self.headval
        self.headval= Newnode
########################################  
#Inserting in the middle of the list
########################################  
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print( 'The mentioned node is absent')
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
######################################## 
#Inserting at the end of the list 
########################################  
    def AtEnd(self,Newdata):
        NewNode = Node(Newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode
        
######################################## 
#Swapping 2 nodes 
########################################  
    def swap(self,data1,data2):
        if data1 == data2:
            return
        
        prev_1 = None
        curr_1 = self.headval
        #loop until you find data1
        while curr_1 and curr_1.dataval != data1:
            prev_1 = curr_1
            curr_1 = curr_1.nextval
        prev_2 = None
        curr_2 = self.headval
        #loop until you find data2
        while curr_2 and curr_2.dataval != data2:
            prev_2 = curr_2
            curr_2 = curr_2.nextval
        
        if prev_1:
            prev_1.nextval = curr_2
        else:
            self.headval = curr_2
        if prev_2:
            prev_2.nextval = curr_1
        else:
            self.headval = curr_1
        #Swapping in python
        curr_1.nextval, curr_2.nextval = curr_2.nextval, curr_1.nextval
    
########################################     
#Function to Remove Node
########################################  
    def RemoveNode(self, Removekey):
        Head = self.headval
        if (Head is not None):
            if (Head.dataval == Removekey):
                self.headval = Head.nextval
                Head = None
                return
        while (Head is not None):
            if Head.dataval == Removekey:
                break
            prev = Head
            Head = Head.nextval
        if (Head == None):
            return
        prev.nextval = Head.nextval
        Head = None
 
########################################     
#Function to append a new node
########################################         
    def AppendNode(self,data):
        new_node = Node(data)
        if self.headval is None:
            self.headval = new_node
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = new_node
 
########################################     
#Function to find length of the linked list
######################################## 
    def llength(self):
        last = self.headval
        count = 0
        if self.headval is None:
            print(0)
        while last:
            count += 1
            last = last.nextval
        print (str(count) + '\n')
        
    
linkedlist = SLL()
ll2 = SLL()
ll2.headval = Node(2)
ll2.AppendNode(4)
linkedlist.headval = Node(1)
linkedlist.AppendNode(3)
linkedlist.AppendNode(ll2)
linkedlist.printval()
#list = SLL()
#list.headval = Node('Mon')
#e2 = Node('Tue')
#e3 = Node('Wed')
#
#list.headval.nextval = e2
#e2.nextval = e3
#
#list.AtBeginning('Sun')
#list.AtEnd('Fri')
#list.Inbetween(e3,'Thurs')
#list.RemoveNode('Sun')
#list.AppendNode('Sat')
#list.llength()
#list.printval()