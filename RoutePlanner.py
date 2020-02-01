#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:06:58 2020

@author: nitinkotcherlakota
"""

import math
from queue import PriorityQueue

def generatePath(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path

def shortest_path(M, start, goal):
    
    pathQueue = PriorityQueue()
    pathQueue.put(start, 0)
    
    prev = {start: None}
    score = {start: 0}

    while not pathQueue.empty():
        curr = pathQueue.get()

        if curr == goal:
            generatePath(prev, start, goal)
        
        for node in M.roads[curr]:
            #Implementing the math formila Sqrt((X2 - X1)**2) + (Y2 - Y1) ** 2))
            updateScore = score[curr] + heuristicMeasure(M.intersections[curr], M.intersections[node])
            
            if node not in score or updateScore < score[node]:
                score[node] = updateScore
                totalScore = updateScore + heuristicMeasure(M.intersections[curr], M.intersections[node])
                pathQueue.put(node, totalScore)
                prev[node] = curr

    return generatePath(prev, start, goal)


#returning distance from start to goal
def heuristicMeasure(start, goal):
    return math.sqrt(((goal[0] - start[0]) ** 2) + ((goal[1] - start[1]) ** 2))

