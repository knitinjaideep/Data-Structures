#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:29:33 2019

@author: nitinkotcherlakota

USING PANDAS MODULE
"""

import psycopg2 as p
import urllib
import csv
import pandas as pd
from datetime import datetime
from datetime import date
conn = p.connect("dbname = postgres user=nitinkotcherlakota password=abc123")
cur = conn.cursor()

# =============================================================================
# Functions
# =============================================================================
def getdfinfo(dfname):
    print '__________________\nTop 5 in dataframe\n___________________\n\n'
    print dfname.head()
    print '__________________\nData Frame Information\n___________________\n\n'
    print dfname.info()
    print '__________________\nDataframe column names\n___________________'
    print list(dfname.columns)

# =============================================================================
#Use urllib and pull in the data
response = urllib.urlopen('https://dq-content.s3.amazonaws.com/251/storm_data.csv')
#Store in reader
reader = csv.reader(response)
next(reader)
for line in reader:
    if line[1] > '1990': 
        line[4] = str(datetime.strptime(line[4][0:2] + line[4][2:4],'%H%M').strftime('%H:%M:%S'))
        new_list.append(line)
        hur_date = (datetime.strptime(line[1]+' '+line[2]+' '+line[3]+' '+line[4],'%Y %m %d %H:%M:%S').strftime('%Y-%m-%d, %H:%M:%S'))
        new_list = [line[0]]
        new_list.append(hur_date)
        new_list.append(line[5])
        new_list.append(line[6])
        new_list.append(line[7])
#cur.execute('Drop table storms')
#cur.execute("""CREATE TABLE Storms(
#         FID int PRIMARY KEY,
#         Date Date,
#         BTID int,
#         Name Text,
#         Lat Decimal(3,1),
#         Long Decimal(4,1),
#         Wind_KTS int,
#         Pressure int,
#         Cat Varchar(2),
#         Basin text,
#         shape_length decimal(7,6))
#            """)
for line in new_list:
    cur.copy_from(line,'storms',sep = ",")


#for line in new_list:
#    new_list1 = [line[0]]
#    new_list1.append(hur_date[0])
#    new_list1.append(line[5:])
conn.commit()
#Store in a dataframe
#df = pd.read_csv(response)
##Will get dataframe information
##getdfinfo(df)
##looking at the data we can first fix the AD_TIME column 
#df['AD_TIME'] = [datetime.strptime(a[0:2]+':'+a[2:4], '%H:%M').time() for a in df['AD_TIME']]
#print df['AD_TIME'].head()
#we can merge YEAR,MONTH,DAY,AD_TIME and convert it into a datetime








