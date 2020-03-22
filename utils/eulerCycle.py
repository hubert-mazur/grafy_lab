#!/usr/bin/python3.7

def selectNextNode(G, currentNode):
    neighbourList = G.nodeList[currentNode]
    if len(neighbourList) == 0:
        return -666

    for i in neighbourList:
        if len(G.nodeList[i]) > 1:
            G.nodeList[i].remove(int(currentNode))
            G.nodeList[currentNode].remove(i)
            return i

    valueToDelete = neighbourList[0]
    G.nodeList[currentNode].remove(neighbourList[0])
    G.nodeList[valueToDelete].clear()
    return valueToDelete


def eulerCycle(G):
    for i in G.nodeList:
        if len(G.nodeList[i]) % 2:
            print('No Euler cycle in graph')
            exit()

    currentNode = str(1)
    eulerCycleList = [1]
    while True:
        value = selectNextNode(G, currentNode)
        if value != -666:
            eulerCycleList.append(value)
            currentNode = value
        else:
            print(eulerCycleList)
            break
