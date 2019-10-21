#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 05:59:13 2019

@author: nitinkotcherlakota
"""

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
with open('/Users/nitinkotcherlakota/Downloads/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/nitinkotcherlakota/Downloads/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
O(n^2): 2 dictionaries
O(n): Explicit For
O(n): Sorted Function
O(n): To get all the Fixed_to_fixed numbers

Time Complexity: O(n^5)
"""

Calls_in_bangalore = [call for call in calls if call[0].startswith("(080)")]
Calls_dialed_in_bangalore = [call[1] for call in Calls_in_bangalore]
Areas_called = []
for call in Calls_dialed_in_bangalore:
    if re.search(r'^[7|8|9]',call):
        Areas_called.append(call[:4])
    elif call.startswith("140"):
        Areas_called.append(call[:3])
    elif re.search("\(\w+\)",call):
        Areas_called.append(re.search(r'(\(.*?\))',call).group(1))
    total_calls = "\n".join(sorted(list(set(Areas_called))))

print "The numbers called by people in Bangalore have codes:\n{0}".format(total_calls)

fixed_to_fixed = float(len([call for call in Calls_dialed_in_bangalore if call.startswith("(080)")]))
print "---------------------------------------------------------------------------------------"
print "{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((fixed_to_fixed * 100)/float(len(Calls_in_bangalore)))
