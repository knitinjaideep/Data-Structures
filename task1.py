#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 06:50:12 2019

@author: nitinkotcherlakota
"""

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('/Users/nitinkotcherlakota/Downloads/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/nitinkotcherlakota/Downloads/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Time complexity is O(4n)
"""
total_numbers = set()
for text, call in zip(texts,calls):
    for i in range(0,2):
        total_numbers.add(text[i])
        total_numbers.add(call[i])
        
print "There are {0} different telephone numbers in the records.".format(len(total_numbers))