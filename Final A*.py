#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:33:44 2020

@author: nitinkotcherlakota
"""

#References Used:
#https://en.wikipedia.org/wiki/A*_search_algorithm
#https://www.educative.io/edpresso/what-is-the-python-priority-queue

import math
from queue import PriorityQueue

def Path(parent, start, goal):
    cur = goal
    path = [cur]
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    path.reverse()
    return path

#Implementing the math formula Sqrt((X2 - X1)**2) + (Y2 - Y1) ** 2))
def heuristic_cost_estimate(start, goal):
    return math.sqrt(((goal[0] - start[0]) ** 2) + ((goal[1] - start[1]) ** 2))

def shortest_path(M, start, goal):
    
    PQueue = PriorityQueue()
    PQueue.put(start, 0)
    score = {start: 0}
    parent = {start: None}
    
    while not PQueue.empty():
        cur = PQueue.get()

        if cur == goal:
            Path(parent, start, goal)
        
        for node in M.roads[cur]:
            
            updateScore = score[cur] + heuristic_cost_estimate(M.intersections[cur], M.intersections[node])
            if node not in score or updateScore < score[node]:
                score[node] = updateScore
                totalScore = updateScore + heuristic_cost_estimate(M.intersections[cur], M.intersections[node])
                PQueue.put(node, totalScore)
                parent[node] = cur

    return Path(parent, start, goal)