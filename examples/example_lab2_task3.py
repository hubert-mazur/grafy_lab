#!/usr/bin/python3.7

# najwieksza wspolna skladowa na grafie

import tasks.lab2_task3 as t3
import tasks.dataReader as reader

graph = reader.readDataFromFile('testData_lab2_task3.json')
graph = graph.exportToAdjacencyList()

arr = t3.components(graph)
print(arr)
