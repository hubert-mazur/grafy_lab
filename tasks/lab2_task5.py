from random import randint

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
    k = randint(0, n-1)
    while (n*k)%2 != 0:
        n = randint(minn, maxn)
        k = randint(0, n-1)
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
            if v1 not in gRep[v2] and v2 not in gRep[v1] and node_edge[v1] > 0 and node_edge[v2] > 0:
                fill_graph_and_reduce_k(v1, v2, gRep, gTup, node_edge)
        if sum(node_edge) == 0:
            break
        iterN = iterN + 1
        if iterN >= 1000:
            return False, False
    return gRep, gTup

def fill_graph_and_reduce_k(v1, v2, gRep, gTup, node_edge):
    gRep[v1].append(v2)
    gRep[v2].append(v1)
    gTup.append((v1, v2))
    node_edge[v1] = node_edge[v1] - 1
    node_edge[v2] = node_edge[v2] - 1
