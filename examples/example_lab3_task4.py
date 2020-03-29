#!/usr/bin/python3.7

from tasks.lab3_task4 import graphCenter
from tasks.lab3_task3 import lab3_task3

numberOFNodes = 8
numberfOfEdges = 19

matrix = lab3_task3(numberOFNodes, numberfOfEdges)
task4Result = graphCenter(matrix)

print(f'graph center: {task4Result[0]}, minimax: {task4Result[1]}')
