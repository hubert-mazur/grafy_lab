#!/usr/bin/python3.7

import sys
sys.path.insert(0, '../Lab_1')

import dataReader
import task6

G = dataReader.readDataFromFile("testData2.json")

nodeStack = []
visitedNodes = []
startNode = next(iter(G.nodeList))
nodeStack.append(int(startNode))
visitedNodes.append(int(startNode))

task6.hamiltonCycle(G, visitedNodes, nodeStack, startNode, startNode)