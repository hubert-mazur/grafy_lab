from random import randint, random

def rand_graph_edge_number(n, l):
    '''
    Method for creating random graph with n nodes and l edges

    :param n: number of node
    :param l: number of edges

    :retun: returns list of list for representation and list of tuple for networkx graph creation
    '''
    if l >= ((n*(n-1))/2):
        print("Max number of edges ((n*(n-1))/2)-1")
        return False
    gRep = [[] for _ in range(n)]
    pair = []
    gTup = []
    m = 0
    while m <= l:
        v1, v2 = randint(0, n-1), randint(0, n-1)
        while v1 == v2:
            v2 = randint(0, n-1)
        if (v1, v2) not in pair and (v2, v1) not in pair:
            pair.append((v1, v2))
            if v1 not in gRep[v2] and v2 not in gRep[v1]:
                gRep[v1].append(v2)
                gRep[v2].append(v1)
                gTup.append((v1, v2))
                m = m + 1
    return gRep, gTup

def rand_graph_edge_probability(n, p):
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
            if r <= p:
                gRep[v1].append(v2)
                gRep[v2].append(v1)
                gTup.append((v1, v2))
    return gRep, gTup
