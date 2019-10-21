#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 05:58:25 2019

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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Approach1: where I used logical operators. 
"""

dialed_phone = [call[0] for call in calls]
received_phone = [call[1] for call in calls]
sent_text = [text[0] for text in texts]
received_text = [text[1] for text in texts]

print "These numbers could be telemarketers: \n{0}".format("\n".join(sorted(list(((set(dialed_phone) - set(received_phone)) - set(sent_text)) - set(received_text)))))

"""
Time Complexity: O(n^4)
"""