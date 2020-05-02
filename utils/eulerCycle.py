#!/usr/bin/python3.7

from tasks.lab2_task3 import components
import copy


def selectNextNode(G, currentNode, no_s_connected):
    if len(G.nodeList[currentNode]) == 0:
        return -666

    neighbourList = copy.deepcopy(G.nodeList[currentNode])
    # print(neighbourList)
    for i in neighbourList:
        G.nodeList[i].remove(int(currentNode))
        G.nodeList[currentNode].remove(i)
        if max(components(G)) > no_s_connected and neighbourList.index(i) != len(neighbourList) - 1:
            G.nodeList[i].append(currentNode)
            G.nodeList[currentNode].append(i)
        else:
            return i

    # valueToDelete = neighbourList[0]
    # G.nodeList[currentNode].remove(neighbourList[0])
    # G.nodeList[valueToDelete].clear()
    # return valueToDelete


def eulerCycle(G):
    for i in G.nodeList:
        if len(G.nodeList[i]) % 2:
            print('No Euler cycle in graph')
            exit()

    currentNode = 1
    eulerCycleList = [1]
    no_s_connected = max(components(G))
    while True:
        value = selectNextNode(G, currentNode, no_s_connected)
        no_s_connected = max(components(G))
        if value != -666:
            eulerCycleList.append(value)
            currentNode = value
        else:
            print("Cykl Eulera:\n")
            print(eulerCycleList)
            # print(len(eulerCycleList))
            break
