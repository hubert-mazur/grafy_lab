#!/usr/bin/python3.7

def hamiltonCycle(G, visitedNodes, nodeStack, node, startNode):
    if len(visitedNodes) == len(G.nodeList):
        if nodeStack[-1] in G.nodeList[startNode]:
            nodeStack.append(int(startNode))
            visitedNodes.append(startNode)
            print('This graph has hamilton cycle: ')
            print(nodeStack)
            exit()
        else:
            visitedNodes.remove(nodeStack[-1])
            nodeStack.pop()
            return

    for i in G.nodeList[node]:
        if i not in visitedNodes:
            visitedNodes.append(i)
            nodeStack.append(i)
            hamiltonCycle(G, visitedNodes, nodeStack, str(i), startNode)
            if len(visitedNodes) != len(G.nodeList):
                visitedNodes.remove(nodeStack[-1])
                nodeStack.pop()

