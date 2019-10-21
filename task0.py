"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from datetime import datetime
with open('/Users/nitinkotcherlakota/Downloads/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open('/Users/nitinkotcherlakota/Downloads/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""



"""
I have used 
<incoming number> as <sending telephone number>,
<receiving telephone number> as <answering number>,
and reduced the datetime stamp to time. for example, 30-09-2016 23:57:15 to 23:57:15.
Note: If the question requires me to print the entire timestanp,please ignore the use of datetime library.
"""
"""""""""""""""""""""""
Time Complexity: Worst time complexity is O(1). since no matter what amount of data is present,
I will always consider the first value in list "texts" and last value in list "calls".
"""""""""""""""""""""""
#I used strptime only because the print state says "at time <time>."
print "First record of texts, {0} texts {1} at time {2}".format(texts[0][0],texts[0][1],datetime.strptime(texts[0][2], '%d-%m-%Y %H:%M:%S').time())
print "First record of calls, {0} calls {1} at time {2} lasting {3} seconds".format(calls[-1][0],calls[-1][1],datetime.strptime(calls[-1][2], '%d-%m-%Y %H:%M:%S').time(),calls[-1][3])
