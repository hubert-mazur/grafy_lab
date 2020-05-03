from random import random, randint

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
            if r <= p and all(False for v in gRep[v2] if v[0] == v1) and all(False for v in gRep[v1] if v[0] == v2):
                w = randint(-5, 10)
                gRep[v1].append((v2, "to", {'weight': w}))
                gRep[v2].append((v1, "from", {'weight': w}))
                gTup.append((v1, v2, {'weight': w}))
            r = random()
            if r <= p and all(False for v in gRep[v2] if v[0] == v1) and all(False for v in gRep[v1] if v[0] == v2):
                w = randint(-5, 10)
                gRep[v1].append((v2, "from", {'weight': w}))
                gRep[v2].append((v1, "to", {'weight': w}))
                gTup.append((v2, v1, {'weight': w}))
    return gRep, gTup
