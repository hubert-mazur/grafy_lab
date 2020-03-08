import random
from math import fabs

"""
Method for creating random graph with n nodes and l edges
@param n number of node
@param l number of edges
@retun returns list of list for representation and list of tuple for
    networkx graph creation
"""
def Gl(n, l):
    if l >= ((n*(n-1))/2):
        print("Max number of edges ((n*(n-1))/2)-1")
        return False
    gRep = [[] for _ in range(n)]
    pair = []
    gTup = []
    m = 0
    while m <= l:
        v1, v2 = random.randint(0, n-1),  random.randint(0, n-1)
        while v1 == v2:
            v2 = random.randint(0, n-1)
        if (v1, v2) not in pair and (v2, v1) not in pair:
            pair.append((v1, v2))
            if v1 not in gRep[v2] and v2 not in gRep[v1]:
                gRep[v1].append(v2)
                gRep[v2].append(v1)
                gTup.append((v1, v2))
                m = m + 1
    return gRep, gTup

"""
Method for creating random graph with n nodes and number of edges depending
on probability
@param n number of node
@param p probability of creating an edge
@retun returns list of list for representation and list of tuple for
    networkx graph creation
"""
def Gp(n, p):
    gRep = [[] for _ in range(n)]
    pair = []
    gTup = []
    while True:
        v1 = random.randint(0, n-1)
        v2 = random.randint(0, n-1)
        while v1 == v2:
            v2 = random.randint(0, n-1)
        if (v1, v2) not in pair and (v2, v1) not in pair:
            pair.append((v1, v2))
            r = random.random()
            if r <= p and v1 not in gRep[v2] and v2 not in gRep[v1]:
                gRep[v1].append(v2)
                gRep[v2].append(v1)
                gTup.append((v1, v2))
        if len(pair) == n*(n-1)/2:
            break
    return gRep, gTup
        