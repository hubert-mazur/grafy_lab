from random import randint, random

def random_weighted_graph(n, l):
    '''
    Method for creating random graph with n nodes and l edges with weights between 1 and 10

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
    while m < l:
        v1, v2 = randint(0, n-1), randint(0, n-1)
        while v1 == v2:
            v2 = randint(0, n-1)
        if (v1, v2) not in pair and (v2, v1) not in pair:
            pair.append((v1, v2))
            if all(False for v in gRep[v2] if v[0] == v1) and all(False for v in gRep[v1] if v[0] == v2):
                w = randint(1, 10)
                gRep[v1].append((v2, {'weight': w}))
                gRep[v2].append((v1, {'weight': w}))
                gTup.append((v1, v2, {'weight': w}))
                m = m + 1
    return gRep, gTup

def rand_weigted_graph_edge_probability(n, p):
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
    pair = []
    for v1 in range(n):
        for v2 in range(n):
            if v1 == v2:
                continue
            r = random()
            if r <= p and (v1, v2) not in pair and (v2, v1) not in pair:
                w = randint(1, 10)
                gRep[v1].append((v2, {'weight': w}))
                gRep[v2].append((v1, {'weight': w}))
                gTup.append((v1, v2, {'weight': w}))
                pair.append((v1, v2))
    return gRep, gTup

def random_k_regular_graph():
    '''
        Method for creating random k-regular graph
        with number of vertices(n) in range of 2 to 20
        and degree 0 < k < (n-1)

        :retun: returns list of list for representation and list of tuple for networkx graph creation
    '''
    maxn = 20
    minn = 2
    n = randint(minn, maxn)
    k = randint(1, n-1)
    while (n*k)%2 != 0:
        n = randint(minn, maxn)
        k = randint(1, n-1)
    gRep = [[] for _ in range(n)]
    gTup = []
    pair = []
    if k == 0:
        return gRep, gTup
    node_edge = [k for _ in range(n)]
    print("n=", n, "k=", k)
    iterN = 0
    while True:
        v1, v2 = randint(0, n-1), randint(0, n-1)
        while v1 == v2:
            v2 = randint(0, n-1)
        if sum(node_edge) == 4 and max(node_edge) == 2 and min(node_edge) == 1:
            v1 = node_edge.index(max(node_edge))
            v2 = node_edge.index(1)
            fill_graph_and_reduce_k(v1, v2, gRep, gTup, node_edge)
            v1 = node_edge.index(1)
            v2 = node_edge.index(1, v1)
            fill_graph_and_reduce_k(v1, v2, gRep, gTup, node_edge)
        if (v1, v2) not in pair and (v2, v1) not in pair:
            pair.append((v1, v2))
            if all(False for v in gRep[v2] if v[0] == v1) and all(False for v in gRep[v1] if v[0] == v2) and node_edge[v1] > 0 and node_edge[v2] > 0:
                fill_graph_and_reduce_k(v1, v2, gRep, gTup, node_edge)
        if sum(node_edge) == 0:
            break
        iterN = iterN + 1
        if iterN >= 1000:
            return False, False
    return gRep, gTup

def fill_graph_and_reduce_k(v1, v2, gRep, gTup, node_edge):
    w = randint(1, 10)
    gRep[v1].append((v2, {'weight': w}))
    gRep[v2].append((v1, {'weight': w}))
    gTup.append((v1, v2, {'weight': w}))
    node_edge[v1] = node_edge[v1] - 1
    node_edge[v2] = node_edge[v2] - 1
