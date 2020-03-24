from random import random

def rand_digraph_edge_probability(n, p):
    '''
    Method for creating random graph with n nodes and number of edges depending
    on probability
    :param n: number of node
    :param p: probability of creating an edge
    :retun: returns list of list for representation and list of tuple for
        networkx graph creation
    '''
    gRep = [[] for _ in range(n)]
    gTup = []
    for v1 in range(n):
        for v2 in range(n):
            if v1 == v2:
                continue
            r = random()
            if r <= p and (v2, "to") not in gRep[v1] and (v1, "from") not in gRep[v2]:
                gRep[v1].append((v2, "to"))
                gRep[v2].append((v1, "from"))
                gTup.append((v1, v2))
            r = random()
            if r <= p and (v2, "from") not in gRep[v1] and (v1, "to") not in gRep[v2]:
                gRep[v1].append((v2, "from"))
                gRep[v2].append((v1, "to"))
                gTup.append((v2, v1))
    return gRep, gTup
