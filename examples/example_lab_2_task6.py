#!/usr/bin/python3.7


import tasks.dataReader as reader
import tasks.lab2_task6 as t6

G = reader.readDataFromFile("testData_lab2_task6.json")

nodeStack = []
visitedNodes = []
startNode = next(iter(G.nodeList))
nodeStack.append(int(startNode))
visitedNodes.append(int(startNode))

t6.hamiltonCycle(G, visitedNodes, nodeStack, startNode, startNode)
