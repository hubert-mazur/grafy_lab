#!/usr/bin/python3.7

from utils.dijkstra import dijkstra


def lab3_task3(ret):
    numberOfNodes = len(ret[0].nodeList)
    distanceMatrix = [[] for _ in range(numberOfNodes)]

    for i in range(numberOfNodes):
        distanceMatrix[i].extend(*[dijkstra(ret[0], ret[1], i)[0].values()])

    return distanceMatrix
