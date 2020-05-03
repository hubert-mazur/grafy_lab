#!/usr/bin/python3.7

def components(G):
    nr = 0  # numer spojnej skladowej
    comp = []
    for i in G.nodeList:
        comp.append(-1)  # wszystkie wierzcholki sa nieodwiedzone

    for i in G.nodeList:
        if comp[i - 1] == -1:
            nr += 1
            comp[i - 1] = nr  # nalezy do spojnej skadowej nr
            components_R(nr, i, G, comp)  # dalsze przeszukiwanie w glab
    return comp


def components_R(nr, v, G, comp):
    for i in G.nodeList[v]:
        if comp[i - 1] == -1:
            comp[i - 1] = nr
            components_R(nr, i, G, comp)
