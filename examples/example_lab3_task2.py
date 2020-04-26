#!/usr/bin/python3.7

from tasks.lab3_task2 import lab3_task2

numberOfNodes = 8
numberOfEdges = 19
startNode = 0

shortestPaths = lab3_task2(numberOfNodes, numberOfEdges)[2]
print(f'shortest_paths:  {shortestPaths}')
