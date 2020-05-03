from random import randint

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
    while m <= l:
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
