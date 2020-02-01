#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 07:02:18 2020

@author: nitinkotcherlakota
"""

def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    temp_departure = []
    i = 0
    while i < len(arrival):
        if i == 0:
            temp_departure.append(departure[i])
        else:
            for j in range(len(temp_departure),0,-1):    
                if arrival[i] > min(temp_departure):
                    temp_departure[j-1] = departure[i]
                    break
                else:
                    temp_departure.append(departure[i])
                    break
        i += 1
        
    return len(temp_departure)

def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
        
arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]
test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)