# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Creating a Binary Tree
"""

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:    
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def FindVal(self,val):
        if val < self.data:
            if self.val is None:
                return str(self.val) + 'Not Found'
            return self.left.FindVal(val)
        elif val > self.data:
            if self.val is None:
                return str(self.val) + 'Not Found'
            return self.right.FindVal(val)
        else:
            return str(self.val) + 'Found'
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data,)
        if self.right:
            self.right.PrintTree()
            
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()