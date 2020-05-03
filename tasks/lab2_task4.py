#!/usr/bin/python3.8

import random

from tasks.lab2_task1 import degree_seq
from tasks.lab2_task1 import create_adjacency_list as aList
from utils.eulerCycle import eulerCycle
from utils.representation import AdjacencyList


def generateEulerGraph(n=10):
    # n = random.randint(3, 30)
    samples = [i for i in range(2, n, 2)]
    verticeDegrees = [random.choice(samples) for i in range(1, n + 1)]
    print(verticeDegrees)
    adList = []

    while not degree_seq(verticeDegrees, n):
        verticeDegrees = [random.choice(samples) for i in range(1, n + 1)]

    adList = aList(verticeDegrees)
    print(adList)
    print(len(adList))
    adjacencyList = {i: [] for i in range(n)}
    for i, j in adList:
        adjacencyList[i].append(j)
        adjacencyList[j].append(i)

    graph = AdjacencyList({'list': adjacencyList, 'position': {}, 'colors': {}})
    eulerCycle(graph)

