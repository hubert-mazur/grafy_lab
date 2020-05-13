import math
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy
import collections

def BSF(G, s, t, P_s): 
    D_s = [ float("Inf") for i in range (len(G))]
    D_s[s] = 0 
    Q = []
    Q.append(s)

    while Q: 
        v = Q.pop(0)
        neighbors = G.neighbors(v)

        for u in neighbors: 
            if D_s[u] == float("Inf"):
                 D_s[u] = D_s[v] + 1 
                 P_s[u] = v
                 Q.append(u)
                
    return True if P_s.get(t) else False


def FordFulkerson(G, s, t):  
    P_s = {}
    C_f = [list(e) for e in G.edges.data('weight')]
    C_f_zeros = [list(e) for e in G.edges.data('weight')]
    G_r = [list(e) for e in G.edges]
    P = []
    max_flow_value = 0 
    
    Gf = deepcopy(G)

    while BSF(Gf, s, t, P_s):
        res = {}
        last, v = t, t
    
        while v != 0 and v != None:
            v = P_s.get(last)
            if v is not None:
                res[last] = v
                last = v

        min_capacity = min([e[2] for v,k in res.items() for e in C_f if e[0] == k and e[1] == v])
        print("min capacity ", min_capacity)
        max_flow_value += min_capacity

        for v, k in res.items(): 
            print(k, v)
            if [k, v] in G_r: 

                for e in C_f: 
                    if e[0] == k and e[1] == v: 
                        e[2] = e[2] - min_capacity
                        if e[2] == 0: 
                            C_f.remove(e)
                        break

                for e in C_f_zeros: 
                    if e[0] == k and e[1] == v: 
                        e[2] = e[2] - min_capacity
                        break

                Gf.clear()
                Gf.add_weighted_edges_from(C_f)
                
            else: 
                for e in C_f_zeros: 
                    if e[0] == k and e[1] == v: 
                        e[2] = e[2] + min_capacity
                        if e not in C_f: 
                            C_f.append(e)
                        break

                Gf.clear()
                Gf.add_weighted_edges_from(C_f)

        P_s = {}
    flow_C_f_zeros = [e[2] for e in C_f_zeros]
    return max_flow_value, flow_C_f_zeros



def print_graph(G, flow):
    radius = 8
    nodes = len(G)
    alpha = 2 * math.pi / nodes

    x_0, y_0 = 20, 20
    positions = {}

    for i in range(nodes):
        positions.update(
            {(i): (x_0 + radius * math.cos(i * alpha), y_0 + radius * math.sin(i * alpha))})   
    
    labels = nx.get_edge_attributes(G, 'weight')
    order_labels = collections.OrderedDict(sorted(labels.items()))
    
    i = 0
    for k in order_labels:
            order_labels[k] = str(order_labels[k]-flow[i])+"/"+str(order_labels[k])
            i+=1

    nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=order_labels, font_color='green')
    nx.draw(G, pos=positions)
    plt.show()

