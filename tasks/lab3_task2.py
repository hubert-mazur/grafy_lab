#!/usr/bin/python3.7

from utils.dijkstra import dijkstra
from tasks.lab3_task1 import random_weighted_graph as rwg
from utils.representation import AdjacencyList


def lab3_task2(numberOfNodes, numberOfEdges):
    ret = rwg(numberOfNodes, numberOfEdges)[1]

    dictOfEdges = {(i, j): z['weight'] for i, j, z in ret}

    adjList = {i: [] for i in range(numberOfNodes)}

    for i, j in dictOfEdges.keys():
        adjList[i].append(j)
        adjList[j].append(i)

    Graph = AdjacencyList({'list': adjList, 'position': {}, 'colors': {}})

    return Graph, dictOfEdges, dijkstra(Graph, dictOfEdges, 0)[0]
