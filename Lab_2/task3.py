#!/usr/bin/python3.7

def components(G):
    nr = 0
    comp = []
    for i in G.nodeList:
        comp.append(-1)
    
    for i in G.nodeList:
        if comp[int(i) - 1] == -1:
            nr += 1
            comp[int(i) - 1] = nr
            components_R(nr, i, G, comp)
    return comp

def components_R(nr, v, G, comp):
    for i in G.nodeList[v]:
        if comp[i-1] == -1:
            comp[i-1] = nr
            components_R(nr, str(i), G, comp)
    
