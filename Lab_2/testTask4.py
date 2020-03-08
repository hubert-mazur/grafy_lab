#!/usr/bin/python3.7

import sys
sys.path.insert(0, '../Lab_1/')

import dataReader
import task4

graph = dataReader.readDataFromFile('testData1.json')
graph = graph.exportToAdjacencyList()

task4.eulerCycle(graph)