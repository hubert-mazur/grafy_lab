#!/usr/bin/python3.7

import sys
sys.path.insert(0, '../../Lab_2/')
sys.path.insert(0,'../../modules/')

import dataReader
import task4

graph = dataReader.readDataFromFile('data/testTask4Data.json')
graph = graph.exportToAdjacencyList()

task4.eulerCycle(graph)