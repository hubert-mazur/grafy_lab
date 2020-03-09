#!/usr/bin/python3.7

# najwieksza wspolna skladowa na grafie

import sys
sys.path.insert(0, '../../modules/')
sys.path.insert(0,'../../Lab_2/')
import dataReader
import task3


graph = dataReader.readDataFromFile('data/testTask3Data.json')
graph = graph.exportToAdjacencyList()

arr = task3.components(graph)
print(arr)