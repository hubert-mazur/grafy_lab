#!/usr/bin/python3.7

from utils.dijkstra import dijkstra
from tasks.lab3_task2 import lab3_task2


def lab3_task3(numberOfNodes, numberOfEdges):
    ret = lab3_task2(numberOfNodes, numberOfEdges)

    distanceMatrix = [[] for i in range(numberOfNodes)]

    for i in range(numberOfNodes):
        distanceMatrix[i].extend(*[dijkstra(ret[0], ret[1], i)[0].values()])

    return distanceMatrix
