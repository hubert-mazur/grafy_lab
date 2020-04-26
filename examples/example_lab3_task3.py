#!/usr/bin/python3.7

from tasks.lab3_task3 import lab3_task3

numberOfNodes = 8
numberOfEdges = 19

matrix = lab3_task3(numberOfNodes, numberOfEdges)

for i in matrix:
    for j in i:
        print(j, end=' ')
    print('')