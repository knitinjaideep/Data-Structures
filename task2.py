#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 06:03:12 2019

@author: nitinkotcherlakota
"""

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('/Users/nitinkotcherlakota/Downloads/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/nitinkotcherlakota/Downloads/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dialed_calls = {call[0]: int(call[3]) for call in calls}
received_calls = {call[1]: int(call[3]) for call in calls}
total_time = {}
for (key,value),(key1,value1) in zip(dialed_calls.items(),received_calls.items()):
    if key in received_calls.keys():
        dialed_calls[key] = value + received_calls[key]
    if key1 not in dialed_calls.keys():
        total_time[key1] = value1
dialed_calls.update(total_time)

total_dials = max(dialed_calls, key = lambda key:dialed_calls[key])
print "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(total_dials,dialed_calls[total_dials])

"""
O(n^2): for 2 dictionaries
O(n): Explicit For loop
max: is usually O(n)
Time complexity = O(n^3 + n)= O(n^3) 
"""