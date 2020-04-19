#!/usr/bin/python3.7

import tasks.dataReader as dataReader
import tasks.lab1_task2 as t2

nodeList = dataReader.readDataFromFile("./dataTask2.json")
G = nodeList.exportToAdjacencyList()
t2.drawNodesOnCircle(G)
