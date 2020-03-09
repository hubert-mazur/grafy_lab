#!/usr/bin/python3.7

import sys
sys.path.insert(0,'../../modules/')
sys.path.insert(0,'../../Lab_1')

import dataReader
from task2 import drawNodesOnCircle

G = dataReader.readDataFromFile("data/testTask2Data.json")
G.exportToAdjacencyList()

drawNodesOnCircle(G)
