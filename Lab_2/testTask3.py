#!/usr/bin/python3.7

# najwieksza wspolna skladowa na grafie

import sys
sys.path.insert(0, '../Lab_1/')

import dataReader
import task3

graph = dataReader.readDataFromFile('testData1.json')
graph = graph.exportToAdjacencyList()

arr = task3.components(graph)
print(arr)